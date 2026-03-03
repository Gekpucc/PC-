import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'

export default function AdminPage() {
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-gray-900">Admin</h1>
      <Card>
        <CardHeader><CardTitle>System Settings</CardTitle></CardHeader>
        <CardContent>
          <p className="text-sm text-gray-400 text-center py-8">Admin module — coming in Phase 2.</p>
        </CardContent>
      </Card>
    </div>
  )
}
