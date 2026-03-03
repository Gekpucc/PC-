import { useEffect, useState } from 'react'
import { qualityApi } from '@/api/client'
import type { Nonconformance, IssueLog } from '@/api/types'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { ShieldAlert, AlertCircle, CheckSquare } from 'lucide-react'

export default function QADashboard() {
  const [ncrs, setNcrs] = useState<Nonconformance[]>([])
  const [issues, setIssues] = useState<IssueLog[]>([])

  useEffect(() => {
    qualityApi.ncrs().then(setNcrs).catch(() => {})
    qualityApi.issues().then(setIssues).catch(() => {})
  }, [])

  const openNcrs = ncrs.filter((n) => n.status !== 'closed')
  const openIssues = issues.filter((i) => i.status !== 'closed')

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-gray-900">QA Dashboard</h1>
        <p className="text-sm text-gray-500 mt-1">Pending buyoff · open NCRs · open issues</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <Card>
          <CardContent className="pt-4 pb-4">
            <div className="flex items-center gap-3">
              <CheckSquare size={20} className="text-blue-500" />
              <div>
                <p className="text-xs text-gray-500">Pending Buyoff</p>
                <p className="text-2xl font-bold text-blue-700">0</p>
              </div>
            </div>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="pt-4 pb-4">
            <div className="flex items-center gap-3">
              <ShieldAlert size={20} className="text-red-500" />
              <div>
                <p className="text-xs text-gray-500">Open NCRs</p>
                <p className="text-2xl font-bold text-red-700">{openNcrs.length}</p>
              </div>
            </div>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="pt-4 pb-4">
            <div className="flex items-center gap-3">
              <AlertCircle size={20} className="text-amber-500" />
              <div>
                <p className="text-xs text-gray-500">Open Issues</p>
                <p className="text-2xl font-bold text-amber-700">{openIssues.length}</p>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <Card>
          <CardHeader>
            <CardTitle>Open NCRs</CardTitle>
          </CardHeader>
          <CardContent>
            {openNcrs.length === 0 ? (
              <p className="text-sm text-gray-400 text-center py-6">No open NCRs</p>
            ) : (
              <ul className="space-y-2">
                {openNcrs.map((n) => (
                  <li key={n.ncr_id} className="flex items-center justify-between text-sm py-1.5 border-b border-gray-100">
                    <span className="font-mono">NCR-{n.ncr_id}</span>
                    <Badge variant={n.status === 'open' ? 'destructive' : 'warning'}>
                      {n.status}
                    </Badge>
                  </li>
                ))}
              </ul>
            )}
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Open Issues</CardTitle>
          </CardHeader>
          <CardContent>
            {openIssues.length === 0 ? (
              <p className="text-sm text-gray-400 text-center py-6">No open issues</p>
            ) : (
              <ul className="space-y-2">
                {openIssues.map((i) => (
                  <li key={i.issue_id} className="text-sm py-1.5 border-b border-gray-100">
                    <div className="flex items-center justify-between">
                      <span className="font-medium truncate max-w-[200px]">{i.description}</span>
                      <Badge variant="warning">{i.status}</Badge>
                    </div>
                  </li>
                ))}
              </ul>
            )}
          </CardContent>
        </Card>
      </div>
    </div>
  )
}
