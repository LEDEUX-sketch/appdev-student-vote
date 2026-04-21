<template>
  <div class="dashboard-container animation-fade-in">
    <div class="header">
      <h1>Election Dashboard</h1>
      <p>System Overview & Current Metrics</p>
    </div>

    <div class="stats-grid">
      <div class="stat-card glass-panel" v-for="(stat, index) in statItems" :key="index">
        <div class="stat-icon" :style="{ color: stat.color }">
          <i :class="stat.icon"></i>
        </div>
        <div class="stat-info">
          <div class="stat-title">{{ stat.title }}</div>
          <div class="stat-value" :class="{ 'loading-pulse': loading }">
            {{ loading ? '...' : stat.value }}
          </div>
        </div>
      </div>
    </div>

    <div class="main-content-grid">
      <div class="chart-container glass-panel">
        <div class="panel-header">
          <h3>Turnout Progression</h3>
          <span class="badge">Live</span>
        </div>
        <div class="chart-content">
          <p v-if="loading" class="text-muted">Analyzing voting patterns...</p>
          <div v-else class="placeholder-chart">
            <div class="empty-state">
              <p>Voting data will appear here as the election progresses.</p>
            </div>
          </div>
        </div>
      </div>

      <div class="recent-activity-container glass-panel">
        <h3>System Activity</h3>
        <div v-if="loading" class="loading-activity">
          <div class="activity-skeleton" v-for="i in 3" :key="i"></div>
        </div>
        <ul v-else class="activity-list">
          <li v-if="stats.total_voters > 0">
            <span class="dot success"></span>
            Voter roster updated with {{ stats.total_voters }} eligible voters.
          </li>
          <li v-if="stats.active_elections > 0">
            <span class="dot primary"></span>
            {{ stats.active_elections }} election(s) currently accepting votes.
          </li>
          <li v-if="stats.total_votes > 0">
            <span class="dot warning"></span>
            Total of {{ stats.total_votes }} votes successfully recorded.
          </li>
          <li v-if="Object.values(stats).every(v => v === 0)" class="text-muted">
            No activity detected yet. Start by setting up an election.
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import axios from '../axios';

const stats = ref({
  active_elections: 0,
  total_candidates: 0,
  total_voters: 0,
  total_votes: 0
});

const loading = ref(true);

const statItems = computed(() => [
  { title: 'Active Elections', value: stats.value.active_elections, color: '#3b82f6', icon: 'fas fa-poll' },
  { title: 'Total Candidates', value: stats.value.total_candidates, color: '#10b981', icon: 'fas fa-user-tie' },
  { title: 'Total Voters', value: stats.value.total_voters?.toLocaleString(), color: '#8b5cf6', icon: 'fas fa-users' },
  { title: 'Votes Cast', value: stats.value.total_votes?.toLocaleString(), color: '#f59e0b', icon: 'fas fa-vote-yea' }
]);

const fetchStats = async () => {
  try {
    loading.value = true;
    const response = await axios.get('/api/dashboard-stats/');
    stats.value = response.data;
  } catch (error) {
    console.error('Failed to fetch dashboard stats:', error);
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  fetchStats();
});
</script>

<style scoped>
.dashboard-container {
  padding: 20px;
}
.header {
  margin-bottom: 30px;
}
.header h1 {
  font-size: 32px;
  font-weight: 800;
  background: linear-gradient(to right, #fff, #94a3b8);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 5px;
}
.header p {
  color: #94a3b8;
  font-size: 16px;
}
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}
.stat-card {
  display: flex;
  align-items: center;
  gap: 20px;
  transition: transform 0.3s ease, border-color 0.3s ease;
}
.stat-card:hover {
  transform: translateY(-5px);
  border-color: rgba(255, 255, 255, 0.2);
}
.stat-icon {
  width: 50px;
  height: 50px;
  border-radius: 12px;
  background: rgba(255, 255, 255, 0.05);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
}
.stat-title {
  font-size: 13px;
  color: #94a3b8;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-weight: 600;
  margin-bottom: 4px;
}
.stat-value {
  font-size: 28px;
  font-weight: 800;
}
.main-content-grid {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 25px;
}
@media (max-width: 1024px) {
  .main-content-grid {
      grid-template-columns: 1fr;
  }
}
.panel-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}
.badge {
  background: rgba(16, 185, 129, 0.1);
  color: #10b981;
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
}
.placeholder-chart {
  height: 300px;
  background: rgba(255, 255, 255, 0.02);
  border: 1px dashed rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.empty-state {
  text-align: center;
  color: #64748b;
  max-width: 300px;
}
.activity-list {
  list-style: none;
  padding: 0;
}
.activity-list li {
  padding: 15px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
  font-size: 14px;
  display: flex;
  align-items: center;
  gap: 12px;
}
.dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
}
.dot.primary { background: #3b82f6; }
.dot.success { background: #10b981; }
.dot.warning { background: #f59e0b; }

.loading-pulse {
  animation: pulse 1.5s infinite;
  color: #334155;
}
@keyframes pulse {
  0% { opacity: 1; }
  50% { opacity: 0.5; }
  100% { opacity: 1; }
}

.animation-fade-in {
  animation: fadeIn 0.6s ease-out;
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
