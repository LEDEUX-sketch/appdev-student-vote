<template>
  <div class="elections-container animation-fade-in">
    <div class="header-action-wrapper">
      <div>
        <h1>Election Configurations</h1>
        <p class="text-muted">Set up active election cycles and ballot positions</p>
      </div>
      <div>
        <button class="btn-primary" @click="showModal = true">+ New Election</button>
      </div>
    </div>

    <div v-for="election in elections" :key="election.id" class="glass-panel election-card">
      <div class="election-header">
        <h2>{{ election.title }}</h2>
        <span class="status-badge" :class="election.status.toLowerCase()">{{ election.status }}</span>
      </div>
      <div class="election-details">
        <p><strong>Starts:</strong> {{ new Date(election.start_date).toLocaleString() }}</p>
        <p><strong>Ends:</strong> {{ new Date(election.end_date).toLocaleString() }}</p>
      </div>
      <div class="election-actions">
        <button class="btn-text">Manage Positions</button>
        <button class="btn-text">Edit Details</button>
      </div>
    </div>

    <div v-if="elections.length === 0" class="glass-panel text-center empty-state">
      <h3>No elections defined</h3>
      <p class="text-muted">Create an election to begin setting up positions and candidates.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const elections = ref([])
const showModal = ref(false)

const fetchElections = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/elections/')
        elections.value = response.data
    } catch (error) {
        console.error('Error fetching elections:', error)
    }
}

onMounted(() => {
    fetchElections()
})
</script>

<style scoped>
.elections-container {
    padding: 10px;
}
.header-action-wrapper {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 30px;
}
.text-muted {
    color: #94a3b8;
}
.election-card {
    margin-bottom: 20px;
}
.election-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid var(--glass-border);
    padding-bottom: 15px;
    margin-bottom: 15px;
}
.election-header h2 {
    font-size: 20px;
    color: var(--primary-color);
    margin: 0;
}
.status-badge {
    padding: 4px 12px;
    border-radius: 12px;
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
}
.status-badge.draft {
    background: rgba(148, 163, 184, 0.2);
    color: #94a3b8;
}
.status-badge.active {
    background: rgba(16, 185, 129, 0.2);
    color: var(--success-color);
}
.status-badge.completed {
    background: rgba(59, 130, 246, 0.2);
    color: var(--primary-color);
}
.election-details p {
    margin-bottom: 8px;
    font-size: 15px;
}
.election-actions {
    display: flex;
    justify-content: flex-end;
    gap: 15px;
    margin-top: 15px;
}
.btn-text {
    background: transparent;
    color: var(--primary-color);
    padding: 5px 10px;
}
.btn-text:hover {
    background: rgba(255, 255, 255, 0.05);
}
.text-center {
    text-align: center;
}
.empty-state {
    padding: 60px;
}
</style>
