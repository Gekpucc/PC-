import { useEffect, useState } from 'react'
import { workOrdersApi } from '@/api/client'
import type { WorkOrder } from '@/api/types'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { BarChart2, CalendarClock } from 'lucide-react'

export default function SalesDashboard() {
  const [workOrders, setWorkOrders] = useState<WorkOrder[]>([])

  useEffect(() => {
    workOrdersApi.list().then(setWorkOrders).catch(() => {})
  }, [])

  const today = new Date().toISOString().split('T')[0]
  const upcoming = workOrders
    .filter((wo) => wo.due_date && wo.due_date >= today)
    .sort((a, b) => (a.due_date! < b.due_date! ? -1 : 1))
    .slice(0, 10)

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-gray-900">Sales Dashboard</h1>
        <p className="text-sm text-gray-500 mt-1">Job status by customer · upcoming due dates</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <Card>
          <CardContent className="pt-4 pb-4">
            <div className="flex items-center gap-3">
              <BarChart2 size={20} className="text-blue-500" />
              <div>
                <p className="text-xs text-gray-500">Total Jobs</p>
                <p className="text-2xl font-bold text-blue-700">{workOrders.length}</p>
              </div>
            </div>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="pt-4 pb-4">
            <div className="flex items-center gap-3">
              <CalendarClock size={20} className="text-amber-500" />
              <div>
                <p className="text-xs text-gray-500">Due This Week</p>
                <p className="text-2xl font-bold text-amber-700">
                  {
                    workOrders.filter((wo) => {
                      if (!wo.due_date) return false
                      const diff =
                        (new Date(wo.due_date).getTime() - Date.now()) / 86400000
                      return diff >= 0 && diff <= 7
                    }).length
                  }
                </p>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Upcoming Due Dates</CardTitle>
        </CardHeader>
        <CardContent>
          {upcoming.length === 0 ? (
            <p className="text-sm text-gray-400 text-center py-8">No upcoming jobs</p>
          ) : (
            <table className="w-full text-sm">
              <thead>
                <tr className="border-b border-gray-200">
                  <th className="text-left py-2 px-3 text-gray-500 font-medium">WO #</th>
                  <th className="text-left py-2 px-3 text-gray-500 font-medium">Status</th>
                  <th className="text-left py-2 px-3 text-gray-500 font-medium">Priority</th>
                  <th className="text-left py-2 px-3 text-gray-500 font-medium">Due Date</th>
                </tr>
              </thead>
              <tbody>
                {upcoming.map((wo) => (
                  <tr key={wo.wo_id} className="border-b border-gray-100 hover:bg-gray-50">
                    <td className="py-2 px-3 font-mono">WO-{wo.wo_id}</td>
                    <td className="py-2 px-3">{wo.status}</td>
                    <td className="py-2 px-3">
                      <Badge
                        variant={
                          wo.priority_level === 'Expedite'
                            ? 'warning'
                            : wo.priority_level === 'Hold'
                            ? 'destructive'
                            : 'secondary'
                        }
                      >
                        {wo.priority_level}
                      </Badge>
                    </td>
                    <td className="py-2 px-3 text-gray-600">{wo.due_date}</td>
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
