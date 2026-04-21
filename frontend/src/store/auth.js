import { defineStore } from 'pinia'
import axios from 'axios'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: null,
    user: null,
  }),
  getters: {
    isAuthenticated: (state) => !!state.token,
  },
  actions: {
    async login(username, password) {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/auth/login/', {
          username,
          password
        })
        this.token = response.data.access
        axios.defaults.headers.common['Authorization'] = `Bearer ${this.token}`
        // In a real app we would decode JWT to get user info, or fetch profile
        this.user = { username } 
        return true
      } catch (error) {
        console.error('Login failed', error)
        return false
      }
    },
    logout() {
      this.token = null
      this.user = null
      delete axios.defaults.headers.common['Authorization']
    }
  }
})
