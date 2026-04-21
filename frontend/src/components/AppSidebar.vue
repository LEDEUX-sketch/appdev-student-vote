<template>
  <div class="sidebar glass-panel">
    <div class="brand">
      <h2>SOAVS</h2>
    </div>
    <nav class="nav-links">
      <router-link to="/" class="nav-item">Dashboard</router-link>
      <router-link to="/elections" class="nav-item">Elections</router-link>
      <router-link to="/candidates" class="nav-item">Candidates</router-link>
      <router-link to="/voters" class="nav-item">Voters</router-link>
    </nav>
    <div class="logout-container">
      <button class="nav-item logout-btn" @click="handleLogout">Logout</button>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '../store/auth'
import { useRouter } from 'vue-router'

const authStore = useAuthStore()
const router = useRouter()

const handleLogout = () => {
    authStore.logout()
    router.push('/login')
}
</script>

<style scoped>
.sidebar {
    width: 250px;
    height: calc(100vh - 40px);
    position: fixed;
    top: 20px;
    left: 20px;
    display: flex;
    flex-direction: column;
    padding: 24px;
}
.brand {
    margin-bottom: 40px;
    text-align: center;
}
.brand h2 {
    color: var(--primary-color);
    letter-spacing: 1px;
}
.nav-links {
    display: flex;
    flex-direction: column;
    gap: 12px;
    flex: 1;
}
.nav-item {
    padding: 12px 16px;
    border-radius: 8px;
    color: var(--text-color);
    text-decoration: none;
    font-weight: 500;
    transition: all 0.2s;
    background: transparent;
    border: none;
    text-align: left;
    cursor: pointer;
    font-size: 15px;
    display: block;
}
.nav-item:hover, .router-link-exact-active {
    background: rgba(59, 130, 246, 0.15);
    color: var(--primary-color);
}
.logout-btn {
    width: 100%;
    color: var(--danger-color);
}
.logout-btn:hover {
    background: rgba(239, 68, 68, 0.15);
}
</style>
