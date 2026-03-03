import axios from 'axios'
import type { TokenResponse, User, WorkOrder, IntakeRecord, Nonconformance, IssueLog } from './types'

const api = axios.create({
  baseURL: '/api',
  headers: { 'Content-Type': 'application/json' },
})

// Attach JWT from localStorage on every request
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('pes_token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

// Redirect to login on 401
api.interceptors.response.use(
  (res) => res,
  (err) => {
    if (err.response?.status === 401) {
      localStorage.removeItem('pes_token')
      localStorage.removeItem('pes_user')
      window.location.href = '/login'
    }
    return Promise.reject(err)
  }
)

// ─── Auth ────────────────────────────────────────────────────────────────────
export const authApi = {
  login: (username: string, password: string) =>
    api.post<TokenResponse>('/auth/login', { username, password }).then((r) => r.data),
  me: () => api.get<User>('/auth/me').then((r) => r.data),
}

// ─── Users ───────────────────────────────────────────────────────────────────
export const usersApi = {
  list: () => api.get<User[]>('/users/').then((r) => r.data),
  get: (id: number) => api.get<User>(`/users/${id}`).then((r) => r.data),
}

// ─── Work Orders ─────────────────────────────────────────────────────────────
export const workOrdersApi = {
  list: () => api.get<WorkOrder[]>('/work-orders/').then((r) => r.data),
  get: (id: number) => api.get<WorkOrder>(`/work-orders/${id}`).then((r) => r.data),
}

// ─── Intake ──────────────────────────────────────────────────────────────────
export const intakeApi = {
  list: () => api.get<IntakeRecord[]>('/intake-records/').then((r) => r.data),
}

// ─── Quality ─────────────────────────────────────────────────────────────────
export const qualityApi = {
  ncrs: () => api.get<Nonconformance[]>('/nonconformances/').then((r) => r.data),
  issues: () => api.get<IssueLog[]>('/issue-logs/').then((r) => r.data),
}

export default api
