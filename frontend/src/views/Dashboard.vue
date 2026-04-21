<template>
  <div class="dashboard-container animation-fade-in">
    <div class="header">
      <h1>Election Dashboard</h1>
      <p>System Overview & Current Metrics</p>
    </div>

    <div class="stats-grid">
      <div class="stat-card glass-panel">
        <div class="stat-title">Active Elections</div>
        <div class="stat-value">1</div>
      </div>
      <div class="stat-card glass-panel">
        <div class="stat-title">Total Candidates</div>
        <div class="stat-value">15</div>
      </div>
      <div class="stat-card glass-panel">
        <div class="stat-title">Total Voters</div>
        <div class="stat-value">1,240</div>
      </div>
      <div class="stat-card glass-panel">
        <div class="stat-title">Votes Cast</div>
        <div class="stat-value">856</div>
      </div>
    </div>

    <div class="main-content-grid">
      <div class="chart-container glass-panel">
        <h3>Turnout Progression</h3>
        <p class="text-muted">A live chart will be rendered here...</p>
        <div class="placeholder-chart"></div>
      </div>

      <div class="recent-activity-container glass-panel">
        <h3>Recent Activity</h3>
        <ul class="activity-list">
          <li><strong>System Admin</strong> created election "USTP Supreme Student Council 2026"</li>
          <li><strong>System Admin</strong> uploaded 250 voters via CSV.</li>
          <li><strong>Voting</strong> started for "USTP Supreme Student Council 2026".</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.dashboard-container {
  padding: 10px;
}
.header {
  margin-bottom: 30px;
}
.header h1 {
  font-size: 28px;
  color: var(--text-color);
}
.header p {
  color: #94a3b8;
}
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}
.stat-card {
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.stat-title {
  font-size: 14px;
  color: #cbd5e1;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 8px;
}
.stat-value {
  font-size: 32px;
  font-weight: 700;
  color: var(--primary-color);
}
.main-content-grid {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 20px;
}
@media (max-width: 900px) {
  .main-content-grid {
      grid-template-columns: 1fr;
  }
}
.chart-container h3, .recent-activity-container h3 {
  margin-bottom: 10px;
}
.text-muted {
  color: #64748b;
  font-size: 14px;
}
.placeholder-chart {
  height: 250px;
  background: linear-gradient(180deg, rgba(59, 130, 246, 0.1) 0%, rgba(59, 130, 246, 0) 100%);
  border-bottom: 1px solid var(--primary-color);
  margin-top: 20px;
  border-radius: 8px;
}
.activity-list {
  list-style-type: none;
  padding: 0;
  margin-top: 15px;
}
.activity-list li {
  padding: 12px 0;
  border-bottom: 1px solid var(--glass-border);
  font-size: 14px;
}
.activity-list li:last-child {
  border-bottom: none;
}
.animation-fade-in {
  animation: fadeIn 0.4s ease-out;
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
