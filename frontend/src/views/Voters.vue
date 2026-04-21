<template>
  <div class="voters-container animation-fade-in">
    <div class="header-action-wrapper">
      <div>
        <h1>Voter Roll Manager</h1>
        <p class="text-muted">Upload and manage eligible student voters</p>
      </div>
      <div>
        <input type="file" ref="fileInput" @change="handleFileUpload" accept=".csv" style="display:none" />
        <button class="btn-primary" @click="triggerFileInput">+ Upload CSV</button>
      </div>
    </div>

    <div class="glass-panel table-container">
      <div v-if="uploadMsg" class="upload-feedback" :class="{'success': isUploadSuccess, 'error': !isUploadSuccess}">
        {{ uploadMsg }}
      </div>

      <table class="data-table">
        <thead>
          <tr>
            <th>Student ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="voter in voters" :key="voter.id">
            <td>{{ voter.student_id }}</td>
            <td>{{ voter.name }}</td>
            <td>{{ voter.email }}</td>
            <td>
              <span class="badge" :class="voter.has_voted ? 'badge-success' : 'badge-warning'">
                {{ voter.has_voted ? 'Voted' : 'Pending' }}
              </span>
            </td>
          </tr>
          <tr v-if="voters.length === 0">
            <td colspan="4" class="text-center">No voters found. Upload a CSV to get started.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const voters = ref([])
const fileInput = ref(null)
const uploadMsg = ref('')
const isUploadSuccess = ref(true)

const fetchVoters = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/voters/')
        voters.value = response.data
    } catch (error) {
        console.error('Error fetching voters:', error)
    }
}

const triggerFileInput = () => {
    fileInput.value.click()
}

const handleFileUpload = async (event) => {
    const file = event.target.files[0]
    if (!file) return

    const formData = new FormData()
    formData.append('file', file)

    try {
        const response = await axios.post('http://127.0.0.1:8000/api/voters/import/', formData, {
            headers: { 'Content-Type': 'multipart/form-data' }
        })
        isUploadSuccess.value = true
        uploadMsg.value = response.data.success || 'Upload successful!'
        fetchVoters()
    } catch (error) {
        isUploadSuccess.value = false
        uploadMsg.value = error.response?.data?.error || 'Failed to upload CSV'
    }
    
    setTimeout(() => { uploadMsg.value = ''; }, 5000)
    event.target.value = null
}

onMounted(() => {
    fetchVoters()
})
</script>

<style scoped>
.voters-container {
    padding: 10px;
}
.header-action-wrapper {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 30px;
}
.header-action-wrapper h1 {
    font-size: 28px;
}
.text-muted {
    color: #94a3b8;
}
.table-container {
    overflow-x: auto;
}
.data-table {
    width: 100%;
    border-collapse: collapse;
}
.data-table th, .data-table td {
    padding: 14px 16px;
    text-align: left;
    border-bottom: 1px solid var(--glass-border);
}
.data-table th {
    color: #cbd5e1;
    font-weight: 600;
    font-size: 14px;
    text-transform: uppercase;
}
.data-table tbody tr:hover {
    background: rgba(255, 255, 255, 0.02);
}
.text-center {
    text-align: center;
    padding: 40px !important;
    color: #64748b;
}
.badge {
    padding: 4px 10px;
    border-radius: 12px;
    font-size: 12px;
    font-weight: 600;
}
.badge-success {
    background: rgba(16, 185, 129, 0.2);
    color: var(--success-color);
}
.badge-warning {
    background: rgba(245, 158, 11, 0.2);
    color: #fbbf24;
}
.upload-feedback {
    padding: 12px;
    margin-bottom: 20px;
    border-radius: 8px;
    font-weight: 500;
}
.upload-feedback.success {
    background: rgba(16, 185, 129, 0.1);
    color: var(--success-color);
    border: 1px solid var(--success-color);
}
.upload-feedback.error {
    background: rgba(239, 68, 68, 0.1);
    color: var(--danger-color);
    border: 1px solid var(--danger-color);
}
</style>
