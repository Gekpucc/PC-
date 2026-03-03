export type UserRole =
  | 'Admin'
  | 'Ops Manager'
  | 'Sales Manager'
  | 'QA Internal'
  | 'Quality Source'
  | 'Technician'
  | 'Shipping & Receiving'

export interface User {
  user_id: number
  name: string
  role: UserRole
  email: string | null
  username: string | null
}

export interface TokenResponse {
  access_token: string
  token_type: string
  user: User
}

export interface WorkOrder {
  wo_id: number
  po_id: number
  part_id: number
  work_plan_id: number
  status: string
  priority_level: 'Normal' | 'Expedite' | 'Hold'
  created_date: string
  due_date: string | null
}

export interface IntakeRecord {
  intake_id: number
  po_id: number
  received_qty: number
  received_date: string
  discrepancy_flag: boolean
  tech_id: number
}

export interface Nonconformance {
  ncr_id: number
  wo_id: number
  part_id: number
  opened_by: number
  disposition: string | null
  status: 'open' | 'in_disposition' | 'closed'
  resolution_notes: string | null
}

export interface IssueLog {
  issue_id: number
  wo_id: number
  reported_by: number
  description: string
  status: 'open' | 'in_progress' | 'closed'
  ncr_id: number | null
  customer_notified: boolean
  customer_response: string | null
  resolution: string | null
}
