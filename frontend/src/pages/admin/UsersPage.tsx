import { useEffect, useState } from 'react'
import { usersApi } from '@/api/client'
import type { User } from '@/api/types'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'

export default function UsersPage() {
  const [users, setUsers] = useState<User[]>([])

  useEffect(() => {
    usersApi.list().then(setUsers).catch(() => {})
  }, [])

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-gray-900">User Management</h1>
      <Card>
        <CardHeader>
          <CardTitle>All Users ({users.length})</CardTitle>
        </CardHeader>
        <CardContent>
          {users.length === 0 ? (
            <p className="text-sm text-gray-400 text-center py-8">No users</p>
          ) : (
            <table className="w-full text-sm">
              <thead>
                <tr className="border-b border-gray-200">
                  <th className="text-left py-2 px-3 text-gray-500 font-medium">Name</th>
                  <th className="text-left py-2 px-3 text-gray-500 font-medium">Username</th>
                  <th className="text-left py-2 px-3 text-gray-500 font-medium">Role</th>
                  <th className="text-left py-2 px-3 text-gray-500 font-medium">Email</th>
                </tr>
              </thead>
              <tbody>
                {users.map((u) => (
                  <tr key={u.user_id} className="border-b border-gray-100 hover:bg-gray-50">
                    <td className="py-2 px-3 font-medium text-gray-900">{u.name}</td>
                    <td className="py-2 px-3 font-mono text-gray-600">{u.username ?? '—'}</td>
                    <td className="py-2 px-3">
                      <Badge variant="secondary">{u.role}</Badge>
                    </td>
                    <td className="py-2 px-3 text-gray-500">{u.email ?? '—'}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </CardContent>
      </Card>
    </div>
  )
}
