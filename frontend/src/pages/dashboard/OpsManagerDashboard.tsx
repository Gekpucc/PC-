import { useEffect, useState } from 'react'
import { workOrdersApi } from '@/api/client'
import type { WorkOrder } from '@/api/types'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { ListOrdered, AlertTriangle, PauseCircle, CheckCircle2 } from 'lucide-react'

export default function OpsManagerDashboard() {
  const [workOrders, setWorkOrders] = useState<WorkOrder[]>([])

  useEffect(() => {
    workOrdersApi.list().then(setWorkOrders).catch(() => {})
  }, [])

  const expedite = workOrders.filter((wo) => wo.priority_level === 'Expedite')
  const onHold = workOrders.filter((wo) => wo.priority_level === 'Hold')
  const active = workOrders.filter((wo) => wo.priority_level === 'Normal')

  const statCards = [
    {
      label: 'Active Jobs',
      value: active.length,
      icon: <ListOrdered size={20} className="text-blue-500" />,
      color: 'text-blue-700',
    },
    {
      label: 'Expedite',
      value: expedite.length,
      icon: <AlertTriangle size={20} className="text-amber-500" />,
      color: 'text-amber-700',
    },
    {
      label: 'On Hold',
      value: onHold.length,
      icon: <PauseCircle size={20} className="text-red-500" />,
      color: 'text-red-700',
    },
    {
      label: 'Total WOs',
      value: workOrders.length,
      icon: <CheckCircle2 size={20} className="text-green-500" />,
      color: 'text-green-700',
    },
  ]

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-gray-900">Operations Dashboard</h1>
        <p className="text-sm text-gray-500 mt-1">Full queue · expedite flags · holds · daily status</p>
      </div>

      {/* Stat cards */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        {statCards.map((s) => (
          <Card key={s.label}>
            <CardContent className="pt-4 pb-4">
              <div className="flex items-center gap-3">
                {s.icon}
                <div>
                  <p className="text-xs text-gray-500">{s.label}</p>
                  <p className={`text-2xl font-bold ${s.color}`}>{s.value}</p>
                </div>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>

      {/* Queue preview */}
      <Card>
        <CardHeader>
          <CardTitle>Work Order Queue</CardTitle>
        </CardHeader>
        <CardContent>
          {workOrders.length === 0 ? (
            <p className="text-sm text-gray-400 text-center py-8">No work orders yet</p>
          ) : (
            <div className="overflow-x-auto">
              <table className="w-full text-sm">
                <thead>
                  <tr className="border-b border-gray-200">
                    <th className="text-left py-2 px-3 text-gray-500 font-medium">WO #</th>
                    <th className="text-left py-2 px-3 text-gray-500 font-medium">Status</th>
                    <th className="text-left py-2 px-3 text-gray-500 font-medium">Priority</th>
                    <th className="text-left py-2 px-3 text-gray-500 font-medium">Due</th>
                  </tr>
                </thead>
                <tbody>
                  {workOrders.slice(0, 10).map((wo) => (
                    <tr key={wo.wo_id} className="border-b border-gray-100 hover:bg-gray-50">
                      <td className="py-2 px-3 font-mono font-medium">WO-{wo.wo_id}</td>
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
                      <td className="py-2 px-3 text-gray-500">{wo.due_date ?? '—'}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  )
}
