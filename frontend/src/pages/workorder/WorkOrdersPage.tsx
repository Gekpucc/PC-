import { useEffect, useState } from 'react'
import { workOrdersApi } from '@/api/client'
import type { WorkOrder } from '@/api/types'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'

export default function WorkOrdersPage() {
  const [workOrders, setWorkOrders] = useState<WorkOrder[]>([])

  useEffect(() => {
    workOrdersApi.list().then(setWorkOrders).catch(() => {})
  }, [])

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-gray-900">Work Orders</h1>
      <Card>
        <CardHeader>
          <CardTitle>All Work Orders ({workOrders.length})</CardTitle>
        </CardHeader>
        <CardContent>
          {workOrders.length === 0 ? (
            <p className="text-sm text-gray-400 text-center py-8">No work orders</p>
          ) : (
            <table className="w-full text-sm">
              <thead>
                <tr className="border-b border-gray-200">
                  <th className="text-left py-2 px-3 text-gray-500 font-medium">WO #</th>
                  <th className="text-left py-2 px-3 text-gray-500 font-medium">Status</th>
                  <th className="text-left py-2 px-3 text-gray-500 font-medium">Priority</th>
                  <th className="text-left py-2 px-3 text-gray-500 font-medium">Created</th>
                  <th className="text-left py-2 px-3 text-gray-500 font-medium">Due</th>
                </tr>
              </thead>
              <tbody>
                {workOrders.map((wo) => (
                  <tr key={wo.wo_id} className="border-b border-gray-100 hover:bg-gray-50 cursor-pointer">
                    <td className="py-2 px-3 font-mono font-medium text-blue-600">WO-{wo.wo_id}</td>
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
                    <td className="py-2 px-3 text-gray-500">{wo.created_date}</td>
                    <td className="py-2 px-3 text-gray-500">{wo.due_date ?? '—'}</td>
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
