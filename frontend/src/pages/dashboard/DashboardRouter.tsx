import { useAuth } from '@/context/AuthContext'
import OpsManagerDashboard from './OpsManagerDashboard'
import TechDashboard from './TechDashboard'
import QADashboard from './QADashboard'
import SalesDashboard from './SalesDashboard'
import AdminDashboard from './AdminDashboard'
import ShippingDashboard from './ShippingDashboard'

export default function DashboardRouter() {
  const { user } = useAuth()

  if (!user) return null

  switch (user.role) {
    case 'Admin':
      return <AdminDashboard />
    case 'Ops Manager':
      return <OpsManagerDashboard />
    case 'QA Internal':
      return <QADashboard />
    case 'Sales Manager':
      return <SalesDashboard />
    case 'Technician':
      return <TechDashboard />
    case 'Quality Source':
      return <TechDashboard /> // limited view — same shell, scoped later
    case 'Shipping & Receiving':
      return <ShippingDashboard />
    default:
      return <OpsManagerDashboard />
  }
}
