import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { AuthProvider, useAuth } from '@/context/AuthContext'
import AppShell from '@/components/layout/AppShell'
import LoginPage from '@/pages/auth/LoginPage'
import DashboardRouter from '@/pages/dashboard/DashboardRouter'
import QueuePage from '@/pages/queue/QueuePage'
import IntakePage from '@/pages/intake/IntakePage'
import WorkOrdersPage from '@/pages/workorder/WorkOrdersPage'
import EquipmentPage from '@/pages/equipment/EquipmentPage'
import QualityPage from '@/pages/quality/QualityPage'
import AdminPage from '@/pages/admin/AdminPage'
import UsersPage from '@/pages/admin/UsersPage'

function RequireAuth({ children }: { children: React.ReactNode }) {
  const { user } = useAuth()
  if (!user) return <Navigate to="/login" replace />
  return <>{children}</>
}

function AppRoutes() {
  const { user } = useAuth()
  return (
    <Routes>
      <Route
        path="/login"
        element={user ? <Navigate to="/" replace /> : <LoginPage />}
      />
      <Route
        element={
          <RequireAuth>
            <AppShell />
          </RequireAuth>
        }
      >
        <Route index element={<DashboardRouter />} />
        <Route path="intake" element={<IntakePage />} />
        <Route path="queue" element={<QueuePage />} />
        <Route path="work-orders" element={<WorkOrdersPage />} />
        <Route path="equipment" element={<EquipmentPage />} />
        <Route path="quality" element={<QualityPage />} />
        <Route path="documents" element={<div className="p-4 text-gray-500">COC & Documents — coming soon</div>} />
        <Route path="admin" element={<AdminPage />} />
        <Route path="users" element={<UsersPage />} />
      </Route>
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  )
}

export default function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
        <AppRoutes />
      </AuthProvider>
    </BrowserRouter>
  )
}
