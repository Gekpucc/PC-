# Process Execution System (PES) — Master Spec Document
**Element Materials Technology — Precision Cleaning Operations**
*Version 1.0 | Drafted March 2026*

---

## 1. Project Overview

A **Process Execution System** for aerospace precision cleaning and surface treatment job shop operations. Replaces paper-based travelers, manual COC generation, and tribal knowledge with a fully digital, auditable, AS9100-compliant system.

**Not an MES.** This is a service execution system — parts belong to customers, our value is controlled transformation (cleaning, treating, verifying) and the chain of custody around it.

**Hosting:** Local on-premise (Windows machine, company network). No data leaves the building. ITAR-compliant by design.

**Build strategy:** Paper-first, digital-ready. Phase 1 generates documents for physical execution. Phase 2 moves execution to tablet/screen. Same data model throughout — UI changes, backend doesn't.

---

## 2. Tech Stack

| Layer | Technology | Notes |
|---|---|---|
| Database | PostgreSQL | Local, open source, relational |
| Backend | Python + FastAPI | Business logic, API, document generation |
| Frontend | React | Browser-based, any machine on network |
| Document Export | python-docx + ReportLab | Word travelers, PDF COCs — fully local |
| Packaging | Docker Desktop (Windows) | One-command startup, clean audit trail |
| Version Control | GitHub | Code storage, change tracking, auditor review |
| IDE | Cursor | AI-assisted development |

---

## 3. Data Model (Core Objects)

### 3.1 Customer
- customer_id (PK)
- name, contact, ITAR_flag

### 3.2 Purchase Order (PO)
- po_id (PK)
- customer_id (FK)
- part_number, qty, due_date, value, status

### 3.3 Receiving / Intake Record
- intake_id (PK)
- po_id (FK)
- received_qty, received_date, discrepancy_flag
- tech_id (FK → User)

### 3.4 Work Order
- wo_id (PK)
- po_id (FK)
- part_id (FK)
- work_plan_id (FK)
- status (see Workflow States)
- priority_level (Normal / Expedite / Hold)
- created_date, due_date

### 3.5 Part / Job
- part_id (PK)
- customer_id (FK)
- part_number, description, material, spec

### 3.6 Cleaning Procedure
- procedure_id (PK)
- name, version, status (active / retired)
- document_number, spec_reference

### 3.7 Procedure Version History
- version_id (PK)
- procedure_id (FK)
- version_number, changed_by (FK → User)
- change_summary, archived_date
- previous_version_id (FK → self)

### 3.8 Work Plan
- work_plan_id (PK)
- name, created_by (FK → User)
- assembled from Cleaning Procedures via junction table

### 3.9 Work Plan Procedure *(junction table)*
- work_plan_id (FK)
- procedure_id (FK)
- sequence_order

### 3.10 Traveler
- traveler_id (PK)
- wo_id (FK)
- work_plan_id (FK)
- export_date, status
- scanned_upload_attachment

### 3.11 Section Group
- section_id (PK)
- work_plan_id (FK)
- name, sequence_order
*(Groups steps under named section headers e.g. "Pre-Clean", "Final Clean", "Packaging")*

### 3.12 Step / Operation
- step_id (PK)
- procedure_id (FK)
- section_id (FK)
- sequence_order (decimal — supports 1.5, 2.5 etc.)
- description, spec_reference
- requires_authorization (boolean)

### 3.13 Sub-Step / Work Instruction
- substep_id (PK)
- step_id (FK)
- instruction_text
- warning_flag (boolean — renders highlighted on export)
- image_attachment
- requires_signoff (boolean)

### 3.14 Step Field Definition
*(Configures what inputs a step requires — set once when building procedure)*
- step_field_id (PK)
- step_id (FK)
- field_type (text / number / checkbox_group / dropdown / table)
- field_label (e.g. "Acid Temp", "Method", "pH")
- options (for checkbox/dropdown)
- required (boolean)
- min_value, max_value (numeric validation)
- spec_limit_low, spec_limit_high (triggers out-of-spec flag)
- table_columns (JSON — for table field type, defines column headers and acceptance criteria)

### 3.15 Record / Log Entry
- record_id (PK)
- wo_id (FK)
- step_id (FK)
- substep_id (FK)
- bath_id (FK)
- tech_id (FK → User)
- timestamp, signoff

### 3.16 Step Field Entry
*(Captures what tech actually entered during execution)*
- entry_id (PK)
- record_id (FK)
- step_field_id (FK)
- entered_value
- out_of_spec (boolean, calculated)

### 3.17 Bath / Resource
- bath_id (PK)
- name, type, chemical, current_status

### 3.18 Equipment Log
- equipment_log_id (PK)
- bath_id (FK)
- calibration_due, certification_expiry
- maintenance_notes, status

### 3.19 Lab Maintenance Log
*(Scheduled recurring tasks — titrations, filter replacements, sealer checks)*
- lab_maintenance_id (PK)
- bath_id (FK)
- tech_id (FK → User)
- task_type (titration / filter / sealer_check)
- date_performed, result, next_due

### 3.20 User / Technician
- user_id (PK)
- name, role, email
- role options: Admin / Ops Manager / Sales Manager / QA Internal / Quality Source / Technician / Shipping & Receiving

### 3.21 Tech Certification / Authorization
*(Task-level authorization — controls which steps a tech can stamp off)*
- cert_id (PK)
- user_id (FK)
- procedure_id (FK)
- authorized_date, expiry_date
- authorized_by (FK → User)

### 3.22 Step Assignment
*(Tech claims a step — replaces "whoever grabs it" with logged record)*
- assignment_id (PK)
- wo_id (FK)
- step_id (FK)
- tech_id (FK → User)
- claimed_at, released_at
- handoff_to (FK → User, optional)

### 3.23 Time Log
*(Clock in/out per step per tech — feeds utilization tracking)*
- time_log_id (PK)
- wo_id (FK)
- step_id (FK)
- tech_id (FK → User)
- clock_in, clock_out, duration (calculated)
- handoff_to (FK → User, optional)

### 3.24 Queue Priority Flag
- priority_flag_id (PK)
- wo_id (FK)
- priority_level (Normal / Expedite / Hold)
- reason, set_by (FK → User), set_date

### 3.25 Nonconformance (NCR)
*(Per AS9100 — one per part, individual disposition required)*
- ncr_id (PK)
- wo_id (FK)
- part_id (FK)
- opened_by (FK → User)
- disposition, status, resolution_notes

### 3.26 Issue Log
*(Informal — replaces squawk sheet. Can escalate to NCR)*
- issue_id (PK)
- wo_id (FK)
- reported_by (FK → User)
- description, status
- ncr_id (FK, optional — if escalated)
- customer_notified, customer_response, resolution

### 3.27 Witness Record
*(External quality source sign-off — paper-first hybrid)*
- witness_id (PK)
- wo_id (FK)
- inspector_name, company, date_witnessed
- signed_document_attachment

### 3.28 COC (Certificate of Conformance)
*(Auto-generated from Work Order data at job close)*
- coc_id (PK)
- wo_id (FK)
- generated_date
- approved_by (FK → User)
- export_format, attachment

### 3.29 Tag Template
*(Per PN — populated with PO data at Final Packaging)*
- tag_template_id (PK)
- part_id (FK)
- template_layout, fields_required
- last_updated

### 3.30 Instruction Flag
*(Tech feedback on sub-steps — feeds knowledge loop / PDCA)*
- flag_id (PK)
- substep_id (FK)
- reported_by (FK → User)
- flag_type (unclear / better_method / caused_issue)
- description, status (open / reviewed / actioned)
- created_date

---

## 4. Workflow States

Work Order moves through the following states:

| State | Trigger | Blocking Conditions |
|---|---|---|
| Received | Part arrives on dock | — |
| Intake / PO Verification | Intake record created | — |
| Customer Outreach Hold | PO missing, mismatch, or damage found | Awaiting customer response |
| In Queue | PO verified, traveler created | — |
| Pre-Clean | Tech claims first step | Tech must be certified |
| Final Clean | Pre-clean complete | Clean room access, cert required |
| 1st Packaging | Final clean complete | — |
| Final Packaging | 1st packaging complete | Tag template must exist for PN |
| Final Buyoff | QA review triggered | All steps must be stamped, PO reconciled |
| COC Generation | QA approved | — |
| Shipped | COC generated, packaging complete | — |
| NCR Hold | Nonconformance opened | Disposition required to continue |
| QA Rejection | QA rejects at buyoff | Sent back to specified state with reason |

**Hold types that can interrupt any active state:**
- Customer Outreach Hold
- NCR Hold
- Equipment Hold (bath/equipment out of spec)
- QA Rejection

---

## 5. User Roles & Permissions

| Role | Create | Execute | Approve | Override | View | Admin |
|---|---|---|---|---|---|---|
| Admin | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Ops Manager | ✓ | ✓ | — | ✓ (logged) | ✓ | — |
| Sales Manager | — | — | — | — | ✓ (limited) | — |
| QA Internal | ✓ | ✓ | ✓ | — | ✓ | — |
| Quality Source | — | ✓ (witness only) | — | — | ✓ (assigned jobs only) | — |
| Technician | — | ✓ (certified steps only) | — | — | ✓ (assigned jobs) | — |
| Shipping & Receiving | ✓ (intake/COC) | ✓ (intake/ship steps) | — | — | ✓ (limited) | — |

**Key permission rules:**
- Techs can only execute steps they are certified for (enforced by Tech Certification object)
- Overrides require logged reason and set_by field
- Quality Source access is scoped to assigned jobs only (ITAR consideration)
- QA Internal has final buyoff authority — nothing ships without QA sign-off

---

## 6. Document Generation

### 6.1 Traveler Export (Word / PDF)
Generated from Work Plan. Matches current Element Job Traveler format.

**Required elements:**
- Header block: Customer, Spec, PO No., MJO No., Date Rcvd, Required Ship Date, QTY, Part No./Description, Source Inspect checkboxes, QC 2nd Tech Approval
- Section group headers (bold, visually distinct)
- Numbered steps with decimal ordering (1.0, 1.5, 2.0...)
- Per step: instruction text, method checkboxes, input fields, table inputs
- Warning highlights on flagged sub-steps
- Embedded images per step/sub-step
- Spec reference text
- OPER & DATE column (blank for physical stamp in Phase 1)
- Document number and revision date in footer
- "HANDLE WITH CARE — MAINTAIN TRACEABILITY" banner
- "ELEMENT JOB TRAVELER" header with revision date

**Phase 1:** Export → physical stamp → scan back and attach to Work Order
**Phase 2:** Digital execution on tablet, traveler becomes summary output

### 6.2 COC (Certificate of Conformance)
Auto-generated at job close. Pulls from:
- Customer, PO, Part #, QTY (from PO / Work Order)
- Specification (from Work Plan)
- Processes performed (from completed steps)
- Dates (from Work Order timestamps)
- Tech and QA signatures (from sign-off records)
- NCR dispositions if any

### 6.3 Tag / Label
Per PN template populated with PO data at Final Packaging stage.

---

## 7. Scheduling & Queue Management

**Queue display:** Live board of all active Work Orders. Default sort by due date. Priority flags visually distinct.

**Priority levels:**
- Normal — due date order
- Expedite — manager flagged, jumps entire WO, reason required, visible to all techs
- On Hold — separated into Hold Queue, does not pollute active queue

**Assignment model (hybrid):**
- Manager assigns WO to tech
- Tech pulls from queue (only sees steps they are certified for)
- First available grab if unassigned

**Step-level assignment:** Techs claim individual steps, not whole jobs. Full handoff audit trail per step.

**Utilization tracking:** Time Log captures clock in/out per step. Feeds:
- Tech utilization rate
- Step duration averages by procedure
- Bottleneck identification
- Expedite impact on normal flow

---

## 8. Knowledge Production Loop (PDCA)

Built into execution layer:
- **Plan** → Work Plan / Cleaning Procedure
- **Do** → Traveler execution / Time Log / Step Field Entry
- **Check** → Instruction Flags, NCRs, Issue Log, out-of-spec entries
- **Act** → Procedure update, version bump, archived in Version History

Instruction Flags accumulate on sub-steps. QA/Admin reviews periodically. Approved improvements version into the Cleaning Procedure. Old version archived, never deleted. Over time: identify which procedures generate the most flags, which steps cause the most NCRs.

---

## 9. Screen Map

### Auth
- Login (all users)

### Dashboard / Home
- Ops Manager: full queue, expedite flags, holds, daily job status
- Tech: My Jobs, clocked-in step, next available jobs
- QA: jobs pending buyoff, open NCRs, open issues
- Sales: job status by customer/PO, upcoming due dates
- Admin: system health, user management

### Intake / Receiving
- New intake form — link part to PO, visual inspection, squawk sheet
- PO search / verification
- Discrepancy hold — log mismatch, initiate customer outreach

### Queue
- Full job queue — sortable by due date, priority, customer, status
- Expedite flag control (manager only)
- Hold queue (separate view)

### Work Order
- WO detail — all job info, current state, linked PO, part, work plan
- Step execution view — current step, sub-steps, field inputs, stamp off
- Traveler export button
- Attached documents (scanned traveler, witness record)
- Time log / clock in-out

### Work Plan Builder
- Procedure library browser
- Drag and drop step assembly
- Step field definition (inputs, checkboxes, tables, warnings, images)
- Section group management
- Version control / publish workflow

### Cleaning Procedure Library
- Procedure list with version status
- Procedure detail — steps, sub-steps, field definitions
- Instruction flag review queue (QA/Admin)
- Version history

### Equipment & Lab
- Equipment list — calibration status, certification expiry
- Lab maintenance schedule — upcoming tasks, overdue flags
- Bath status board

### Quality
- NCR list — open, in disposition, closed
- Issue log — open issues, customer outreach status
- NCR detail — part, WO, disposition, resolution

### COC & Documents
- COC generation — review auto-populated fields, approve, export
- Tag template manager — per PN
- Document archive — all COCs and travelers linked to WO

### Reports / KPIs *(Phase 4)*
- Utilization, cost per part, NCR trends, bath life

### Admin
- User management — roles, certifications, authorizations
- System settings
- Audit log — every action, who did what when

---

## 10. Build Phases

| Phase | Focus | Key Deliverables |
|---|---|---|
| 1 — Foundation | Database + backend | PostgreSQL schema, FastAPI CRUD, Docker setup |
| 2 — Core Workflow | Frontend | Intake, queue, WO execution, traveler export |
| 3 — Document Generation | Outputs | Traveler Word export, COC PDF, tag printing |
| 4 — Intelligence | Analytics | Utilization tracking, KPI dashboards, knowledge loop |

---

## 11. Compliance & Security Notes

- All data stored locally — no cloud, no external APIs for operational data
- ITAR: Quality Source (external) access scoped to assigned jobs only
- AS9100: NCR per part, individual disposition, full step-level audit trail
- Code verification: third party audit via GitHub repository review
- Override actions always logged with reason and user
- Procedure changes versioned and archived, never deleted
- Equipment certifications tracked with expiry alerts

---

*This document is the single source of truth for all development sessions. Paste relevant sections as context when coding.*
