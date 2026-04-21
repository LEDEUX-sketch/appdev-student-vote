<script setup>
import { useRoute } from 'vue-router'
import AppSidebar from './components/AppSidebar.vue'

const route = useRoute()
</script>

<template>
  <div id="app" :class="{ 'has-sidebar': route.name !== 'Login' }">
    <AppSidebar v-if="route.name && route.name !== 'Login'" />
    <main class="main-content">
      <router-view></router-view>
    </main>
  </div>
</template>

<style scoped>
#app {
  width: 100%;
}
.has-sidebar .main-content {
  margin-left: 290px;
  padding: 20px 20px 20px 0;
  min-height: 100vh;
}
</style>
