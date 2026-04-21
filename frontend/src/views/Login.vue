<template>
  <div class="login-container">
    <div class="glass-panel login-box">
      <div class="login-header">
        <h1>SOAVS Admin</h1>
        <p>Student Organization Automated Voting System</p>
      </div>
      <form @submit.prevent="handleLogin" class="login-form">
        <div class="input-group">
          <label>Username</label>
          <input type="text" v-model="username" class="input-glass" required placeholder="admin" />
        </div>
        <div class="input-group">
          <label>Password</label>
          <input type="password" v-model="password" class="input-glass" required placeholder="••••••••" />
        </div>
        <div v-if="errorMsg" class="error-msg">{{ errorMsg }}</div>
        <button type="submit" class="btn-primary login-btn" :disabled="isLoading">
          {{ isLoading ? 'Authenticating...' : 'Sign In' }}
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../store/auth'

const router = useRouter()
const authStore = useAuthStore()

const username = ref('')
const password = ref('')
const isLoading = ref(false)
const errorMsg = ref('')

const handleLogin = async () => {
    isLoading.value = true
    errorMsg.value = ''
    const success = await authStore.login(username.value, password.value)
    if (success) {
        router.push('/')
    } else {
        errorMsg.value = 'Invalid username or password'
    }
    isLoading.value = false
}
</script>

<style scoped>
.login-container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    padding: 20px;
}
.login-box {
    width: 100%;
    max-width: 400px;
    animation: fadeIn 0.5s ease-out;
}
.login-header {
    text-align: center;
    margin-bottom: 30px;
}
.login-header h1 {
    font-size: 24px;
    font-weight: 700;
    color: var(--primary-color);
    margin-bottom: 8px;
}
.login-header p {
    font-size: 14px;
    color: #94a3b8;
}
.login-form {
    display: flex;
    flex-direction: column;
    gap: 20px;
}
.input-group label {
    display: block;
    margin-bottom: 8px;
    font-size: 14px;
    font-weight: 500;
    color: #cbd5e1;
}
.login-btn {
    margin-top: 10px;
    padding: 12px;
    font-size: 16px;
    box-shadow: 0 4px 14px 0 rgba(59, 130, 246, 0.39);
}
.error-msg {
    color: var(--danger-color);
    font-size: 14px;
    text-align: center;
}
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}
</style>
