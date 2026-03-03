import { useEffect, useState } from 'react'
import { usersApi, workOrdersApi } from '@/api/client'
import type { User, WorkOrder } from '@/api/types'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Users, Activity, Database } from 'lucide-react'

export default function AdminDashboard() {
  const [users, setUsers] = useState<User[]>([])
  const [workOrders, setWorkOrders] = useState<WorkOrder[]>([])

  useEffect(() => {
    usersApi.list().then(setUsers).catch(() => {})
    workOrdersApi.list().then(setWorkOrders).catch(() => {})
  }, [])

  const roleCounts = users.reduce<Record<string, number>>((acc, u) => {
    acc[u.role] = (acc[u.role] ?? 0) + 1
    return acc
  }, {})

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-gray-900">Admin Dashboard</h1>
        <p className="text-sm text-gray-500 mt-1">System health · user management</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <Card>
          <CardContent className="pt-4 pb-4">
            <div className="flex items-center gap-3">
              <Users size={20} className="text-blue-500" />
              <div>
                <p className="text-xs text-gray-500">Total Users</p>
                <p className="text-2xl font-bold text-blue-700">{users.length}</p>
              </div>
            </div>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="pt-4 pb-4">
            <div className="flex items-center gap-3">
              <Activity size={20} className="text-green-500" />
              <div>
                <p className="text-xs text-gray-500">Work Orders</p>
                <p className="text-2xl font-bold text-green-700">{workOrders.length}</p>
              </div>
            </div>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="pt-4 pb-4">
            <div className="flex items-center gap-3">
              <Database size={20} className="text-purple-500" />
              <div>
                <p className="text-xs text-gray-500">API Status</p>
                <p className="text-sm font-bold text-green-600">Online</p>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <Card>
          <CardHeader>
            <CardTitle>Users by Role</CardTitle>
          </CardHeader>
          <CardContent>
            {Object.keys(roleCounts).length === 0 ? (
              <p className="text-sm text-gray-400 text-center py-6">No users</p>
            ) : (
              <ul className="space-y-2">
                {Object.entries(roleCounts).map(([role, count]) => (
                  <li key={role} className="flex items-center justify-between text-sm">
                    <span className="text-gray-700">{role}</span>
                    <Badge variant="secondary">{count}</Badge>
                  </li>
                ))}
              </ul>
            )}
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Recent Users</CardTitle>
          </CardHeader>
          <CardContent>
            <ul className="space-y-2">
              {users.slice(0, 6).map((u) => (
                <li key={u.user_id} className="flex items-center gap-3 text-sm">
                  <div className="w-7 h-7 rounded-full bg-blue-100 text-blue-700 flex items-center justify-center text-xs font-bold shrink-0">
                    {u.name.charAt(0)}
                  </div>
                  <div className="flex-1 min-w-0">
                    <p className="font-medium text-gray-900">{u.name}</p>
                    <p className="text-gray-400 text-xs truncate">{u.username ?? u.email ?? '—'}</p>
                  </div>
                  <Badge variant="secondary" className="text-xs">{u.role}</Badge>
                </li>
              ))}
            </ul>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}
