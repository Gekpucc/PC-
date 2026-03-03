import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { useAuth } from '@/context/AuthContext'
import { ClipboardList, Clock, Zap } from 'lucide-react'

export default function TechDashboard() {
  const { user } = useAuth()

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-gray-900">Welcome, {user?.name}</h1>
        <p className="text-sm text-gray-500 mt-1">My jobs · clocked-in step · next available</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <Card>
          <CardHeader className="pb-2">
            <CardTitle className="text-sm text-gray-500 font-medium flex items-center gap-2">
              <Clock size={16} className="text-blue-500" />
              Clocked In
            </CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-2xl font-bold text-gray-400">—</p>
            <p className="text-xs text-gray-400 mt-1">Not clocked in</p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="pb-2">
            <CardTitle className="text-sm text-gray-500 font-medium flex items-center gap-2">
              <ClipboardList size={16} className="text-green-500" />
              My Assigned Jobs
            </CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-2xl font-bold text-gray-400">0</p>
            <p className="text-xs text-gray-400 mt-1">No jobs assigned</p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="pb-2">
            <CardTitle className="text-sm text-gray-500 font-medium flex items-center gap-2">
              <Zap size={16} className="text-amber-500" />
              Next Available
            </CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-2xl font-bold text-gray-400">—</p>
            <p className="text-xs text-gray-400 mt-1">Queue is empty</p>
          </CardContent>
        </Card>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>My Jobs</CardTitle>
        </CardHeader>
        <CardContent>
          <p className="text-sm text-gray-400 text-center py-8">
            No jobs assigned to you yet. Check the queue for available work.
          </p>
        </CardContent>
      </Card>
    </div>
  )
}
