import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { PackageOpen, Truck } from 'lucide-react'

export default function ShippingDashboard() {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-gray-900">Shipping & Receiving</h1>
        <p className="text-sm text-gray-500 mt-1">Intake records · outbound shipments</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <Card>
          <CardContent className="pt-4 pb-4">
            <div className="flex items-center gap-3">
              <PackageOpen size={20} className="text-blue-500" />
              <div>
                <p className="text-xs text-gray-500">Pending Intake</p>
                <p className="text-2xl font-bold text-blue-700">0</p>
              </div>
            </div>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="pt-4 pb-4">
            <div className="flex items-center gap-3">
              <Truck size={20} className="text-green-500" />
              <div>
                <p className="text-xs text-gray-500">Ready to Ship</p>
                <p className="text-2xl font-bold text-green-700">0</p>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Recent Intake Records</CardTitle>
        </CardHeader>
        <CardContent>
          <p className="text-sm text-gray-400 text-center py-8">No intake records</p>
        </CardContent>
      </Card>
    </div>
  )
}
