import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '../store/auth'

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/',
    name: 'Dashboard',
    component: () => import('../views/Dashboard.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/candidates',
    name: 'Candidates',
    component: () => import('../views/Candidates.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/elections',
    name: 'Elections',
    component: () => import('../views/Elections.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/voters',
    name: 'Voters',
    component: () => import('../views/Voters.vue'),
    meta: { requiresAuth: true }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next('/login')
  } else {
    next()
  }
})

export default router
