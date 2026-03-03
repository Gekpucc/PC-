import { NavLink, Outlet, useNavigate } from 'react-router-dom'
import { useAuth } from '@/context/AuthContext'
import type { UserRole } from '@/api/types'
import {
  LayoutDashboard,
  PackageOpen,
  ListOrdered,
  ClipboardList,
  Wrench,
  FlaskConical,
  ShieldCheck,
  FileText,
  Users,
  LogOut,
  ChevronRight,
} from 'lucide-react'
import { cn } from '@/lib/utils'

interface NavItem {
  label: string
  to: string
  icon: React.ReactNode
  roles?: UserRole[]
}

const NAV_ITEMS: NavItem[] = [
  {
    label: 'Dashboard',
    to: '/',
    icon: <LayoutDashboard size={18} />,
  },
  {
    label: 'Intake / Receiving',
    to: '/intake',
    icon: <PackageOpen size={18} />,
    roles: ['Admin', 'Ops Manager', 'Shipping & Receiving'],
  },
  {
    label: 'Queue',
    to: '/queue',
    icon: <ListOrdered size={18} />,
    roles: ['Admin', 'Ops Manager', 'Technician', 'QA Internal'],
  },
  {
    label: 'Work Orders',
    to: '/work-orders',
    icon: <ClipboardList size={18} />,
    roles: ['Admin', 'Ops Manager', 'Technician', 'QA Internal', 'Quality Source'],
  },
  {
    label: 'Equipment & Lab',
    to: '/equipment',
    icon: <FlaskConical size={18} />,
    roles: ['Admin', 'Ops Manager', 'QA Internal', 'Technician'],
  },
  {
    label: 'Quality',
    to: '/quality',
    icon: <ShieldCheck size={18} />,
    roles: ['Admin', 'Ops Manager', 'QA Internal'],
  },
  {
    label: 'COC & Documents',
    to: '/documents',
    icon: <FileText size={18} />,
    roles: ['Admin', 'Ops Manager', 'QA Internal', 'Shipping & Receiving'],
  },
  {
    label: 'Admin',
    to: '/admin',
    icon: <Wrench size={18} />,
    roles: ['Admin'],
  },
  {
    label: 'Users',
    to: '/users',
    icon: <Users size={18} />,
    roles: ['Admin'],
  },
]

function roleBadgeColor(role: UserRole): string {
  const map: Partial<Record<UserRole, string>> = {
    Admin: 'bg-purple-100 text-purple-800',
    'Ops Manager': 'bg-blue-100 text-blue-800',
    'QA Internal': 'bg-green-100 text-green-800',
    'Sales Manager': 'bg-amber-100 text-amber-800',
    Technician: 'bg-gray-100 text-gray-700',
    'Shipping & Receiving': 'bg-cyan-100 text-cyan-800',
    'Quality Source': 'bg-indigo-100 text-indigo-800',
  }
  return map[role] ?? 'bg-gray-100 text-gray-700'
}

export default function AppShell() {
  const { user, logout } = useAuth()
  const navigate = useNavigate()

  function handleLogout() {
    logout()
    navigate('/login')
  }

  const visibleItems = NAV_ITEMS.filter(
    (item) => !item.roles || (user && item.roles.includes(user.role))
  )

  return (
    <div className="flex h-screen bg-gray-50 overflow-hidden">
      {/* ─── Sidebar ──────────────────────────────────────────────── */}
      <aside className="w-60 flex flex-col bg-white border-r border-gray-200 shrink-0">
        {/* Brand */}
        <div className="h-14 flex items-center px-4 border-b border-gray-200">
          <div className="w-7 h-7 rounded-lg bg-blue-600 flex items-center justify-center mr-2.5">
            <ShieldCheck size={14} className="text-white" />
          </div>
          <span className="font-bold text-sm text-gray-900 leading-tight">
            PES
          </span>
        </div>

        {/* Nav */}
        <nav className="flex-1 overflow-y-auto py-3 px-2 space-y-0.5">
          {visibleItems.map((item) => (
            <NavLink
              key={item.to}
              to={item.to}
              end={item.to === '/'}
              className={({ isActive }) =>
                cn(
                  'flex items-center gap-2.5 px-3 py-2 rounded-lg text-sm font-medium transition-colors',
                  isActive
                    ? 'bg-blue-50 text-blue-700'
                    : 'text-gray-600 hover:bg-gray-100 hover:text-gray-900'
                )
              }
            >
              {({ isActive }) => (
                <>
                  <span className={isActive ? 'text-blue-600' : 'text-gray-400'}>
                    {item.icon}
                  </span>
                  <span className="flex-1">{item.label}</span>
                  {isActive && <ChevronRight size={14} className="text-blue-400" />}
                </>
              )}
            </NavLink>
          ))}
        </nav>

        {/* User info + logout */}
        {user && (
          <div className="border-t border-gray-200 p-3">
            <div className="flex items-center gap-2 mb-2 px-1">
              <div className="w-8 h-8 rounded-full bg-blue-600 flex items-center justify-center text-white text-xs font-bold shrink-0">
                {user.name.charAt(0)}
              </div>
              <div className="min-w-0">
                <p className="text-sm font-medium text-gray-900 truncate">{user.name}</p>
                <span
                  className={cn(
                    'inline-block text-xs px-1.5 py-0.5 rounded-full font-medium',
                    roleBadgeColor(user.role)
                  )}
                >
                  {user.role}
                </span>
              </div>
            </div>
            <button
              onClick={handleLogout}
              className="flex w-full items-center gap-2 px-3 py-1.5 text-sm text-gray-500 hover:text-red-600 hover:bg-red-50 rounded-lg transition-colors"
            >
              <LogOut size={15} />
              Sign out
            </button>
          </div>
        )}
      </aside>

      {/* ─── Main content ─────────────────────────────────────────── */}
      <main className="flex-1 flex flex-col overflow-hidden">
        <div className="flex-1 overflow-y-auto p-6">
          <Outlet />
        </div>
      </main>
    </div>
  )
}
