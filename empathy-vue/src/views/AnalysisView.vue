<!-- empathy-vue/src/views/AnalysisView.vue -->
<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-900 via-blue-900 to-indigo-900 py-8">
    <div class="max-w-6xl mx-auto px-4">
      <!-- Header -->
      <div class="text-center mb-12">
        <h1 class="text-4xl font-bold text-white mb-4">Advanced Analysis</h1>
        <p class="text-xl text-gray-300">Upload images for detailed emotional analysis and insights</p>
      </div>

      <div class="grid lg:grid-cols-2 gap-8">
        <!-- Upload Section -->
        <div class="bg-white/5 backdrop-blur-sm rounded-2xl p-8 border border-white/10">
          <h2 class="text-2xl font-semibold text-white mb-6">Upload Image</h2>
          
          <!-- Drag & Drop Zone -->
          <div 
            @drop="handleDrop"
            @dragover="handleDragOver"
            @dragleave="handleDragLeave"
            :class="[
              'border-2 border-dashed rounded-2xl p-8 text-center cursor-pointer transition-all duration-300 mb-6',
              isDragging ? 'border-cyan-400 bg-cyan-400/10' : 'border-gray-600 hover:border-cyan-400'
            ]"
            @click="triggerFileInput"
          >
            <input 
              type="file" 
              ref="fileInput"
              @change="handleFileSelect"
              accept="image/*"
              class="hidden"
            />
            <CloudUploadIcon class="w-16 h-16 text-gray-400 mx-auto mb-4" />
            <p class="text-white text-lg font-semibold mb-2">Drop your image here</p>
            <p class="text-gray-400">or click to browse files</p>
            <p class="text-gray-500 text-sm mt-2">Supports JPG, PNG, WEBP (Max 10MB)</p>
          </div>

          <!-- URL Input -->
          <div class="mb-6">
            <label class="block text-white font-semibold mb-3">Or enter image URL</label>
            <div class="flex gap-3">
              <input 
                v-model="imageUrl"
                type="url" 
                placeholder="https://example.com/image.jpg"
                class="flex-1 bg-white/10 border border-white/20 rounded-xl px-4 py-3 text-white placeholder-gray-400 focus:outline-none focus:border-cyan-400 transition-colors"
              />
              <button 
                @click="analyzeFromUrl"
                :disabled="!imageUrl"
                class="bg-cyan-500 hover:bg-cyan-600 disabled:bg-gray-600 disabled:cursor-not-allowed text-white px-6 py-3 rounded-xl font-semibold transition-colors"
              >
                Analyze
              </button>
            </div>
          </div>

          <!-- Recent Uploads -->
          <div v-if="recentUploads.length > 0">
            <h3 class="text-white font-semibold mb-4">Recent Uploads</h3>
            <div class="grid grid-cols-3 gap-4">
              <div 
                v-for="upload in recentUploads" 
                :key="upload.id"
                class="relative group cursor-pointer"
                @click="analyzeRecent(upload)"
              >
                <img :src="upload.preview" class="w-full h-20 object-cover rounded-lg" />
                <div class="absolute inset-0 bg-black/50 opacity-0 group-hover:opacity-100 transition-opacity rounded-lg flex items-center justify-center">
                  <EyeIcon class="w-5 h-5 text-white" />
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Results Section -->
        <div class="space-y-6">
          <!-- Analysis Results -->
          <div v-if="analysisResult" class="bg-white/5 backdrop-blur-sm rounded-2xl p-8 border border-white/10">
            <h2 class="text-2xl font-semibold text-white mb-6">Analysis Results</h2>
            
            <!-- Image Preview -->
            <div class="mb-6">
              <img :src="currentImage" class="w-full max-w-md mx-auto rounded-xl shadow-2xl" />
            </div>

            <!-- Emotion Results -->
            <div class="grid gap-4 mb-6">
              <div 
                v-for="emotion in analysisResult.emotions" 
                :key="emotion.name"
                class="flex items-center justify-between p-4 bg-white/5 rounded-xl"
              >
                <div class="flex items-center space-x-4">
                  <div class="w-3 h-3 rounded-full" :class="emotionColor(emotion.name)"></div>
                  <span class="text-white font-medium">{{ emotion.name }}</span>
                </div>
                <div class="flex items-center space-x-4">
                  <div class="w-32 bg-gray-700 rounded-full h-2">
                    <div 
                      class="h-2 rounded-full transition-all duration-1000"
                      :class="emotionColor(emotion.name)"
                      :style="{ width: `${emotion.confidence * 100}%` }"
                    ></div>
                  </div>
                  <span class="text-gray-300 w-12 text-right">{{ (emotion.confidence * 100).toFixed(1) }}%</span>
                </div>
              </div>
            </div>

            <!-- Empathetic Response -->
            <div class="bg-gradient-to-r from-cyan-500/10 to-blue-500/10 border border-cyan-400/20 rounded-xl p-6">
              <div class="flex items-start space-x-4">
                <div class="w-12 h-12 bg-gradient-to-r from-cyan-500 to-blue-600 rounded-full flex items-center justify-center flex-shrink-0">
                  <HeartIcon class="w-6 h-6 text-white" />
                </div>
                <div>
                  <h3 class="text-white font-semibold mb-2">Empathetic Response</h3>
                  <p class="text-gray-200 leading-relaxed">{{ analysisResult.empathetic_response }}</p>
                </div>
              </div>
            </div>
          </div>

          <!-- No Results State -->
          <div v-else class="bg-white/5 backdrop-blur-sm rounded-2xl p-12 border border-white/10 text-center">
            <ChartBarIcon class="w-16 h-16 text-gray-500 mx-auto mb-4" />
            <h3 class="text-white text-xl font-semibold mb-2">No Analysis Yet</h3>
            <p class="text-gray-400">Upload an image to see detailed emotional analysis</p>
          </div>

          <!-- Export Options -->
          <div v-if="analysisResult" class="bg-white/5 backdrop-blur-sm rounded-2xl p-6 border border-white/10">
            <h3 class="text-white font-semibold mb-4">Export Results</h3>
            <div class="flex space-x-4">
              <button class="flex-1 bg-green-500 hover:bg-green-600 text-white py-3 rounded-xl font-semibold transition-colors flex items-center justify-center space-x-2">
                <DocumentDownloadIcon class="w-5 h-5" />
                <span>PDF Report</span>
              </button>
              <button class="flex-1 bg-blue-500 hover:bg-blue-600 text-white py-3 rounded-xl font-semibold transition-colors flex items-center justify-center space-x-2">
                <ShareIcon class="w-5 h-5" />
                <span>Share</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { CloudUploadIcon, EyeIcon, DocumentDownloadIcon, ShareIcon, HeartIcon, ChartBarIcon } from '@heroicons/vue/outline'

export default {
  name: 'AnalysisView',
  components: {
    CloudUploadIcon,
    EyeIcon,
    DocumentDownloadIcon,
    ShareIcon,
    HeartIcon,
    ChartBarIcon
  },
  data() {
    return {
      isDragging: false,
      imageUrl: '',
      currentImage: null,
      analysisResult: null,
      recentUploads: [],
      isLoading: false
    }
  },
  methods: {
    handleDragOver(e) {
      e.preventDefault()
      this.isDragging = true
    },
    
    handleDragLeave(e) {
      e.preventDefault()
      this.isDragging = false
    },
    
    handleDrop(e) {
      e.preventDefault()
      this.isDragging = false
      const files = e.dataTransfer.files
      if (files.length > 0) {
        this.processFile(files[0])
      }
    },
    
    triggerFileInput() {
      this.$refs.fileInput.click()
    },
    
    handleFileSelect(e) {
      const file = e.target.files[0]
      if (file) {
        this.processFile(file)
      }
    },
    
    processFile(file) {
      // Validate file type and size
      if (!file.type.startsWith('image/')) {
        alert('Please select an image file')
        return
      }
      
      if (file.size > 10 * 1024 * 1024) {
        alert('File size must be less than 10MB')
        return
      }
      
      const reader = new FileReader()
      reader.onload = (e) => {
        this.currentImage = e.target.result
        this.analyzeImage(e.target.result)
        this.addToRecentUploads(e.target.result, file.name)
      }
      reader.readAsDataURL(file)
    },
    
    async analyzeImage(imageData) {
      this.isLoading = true
      try {
        // Simulate API call - replace with actual backend integration
        await new Promise(resolve => setTimeout(resolve, 2000))
        
        // Mock analysis result
        this.analysisResult = {
          emotions: [
            { name: 'Happy', confidence: 0.85 },
            { name: 'Surprise', confidence: 0.10 },
            { name: 'Neutral', confidence: 0.03 },
            { name: 'Sad', confidence: 0.02 }
          ],
          empathetic_response: "This image radiates joy and positivity! The genuine happiness is truly uplifting to see.",
          timestamp: new Date().toISOString()
        }
        
      } catch (error) {
        console.error('Analysis failed:', error)
        alert('Analysis failed. Please try again.')
      } finally {
        this.isLoading = false
      }
    },
    
    async analyzeFromUrl() {
      if (!this.imageUrl) return
      
      this.currentImage = this.imageUrl
      await this.analyzeImage(this.imageUrl)
    },
    
    analyzeRecent(upload) {
      this.currentImage = upload.preview
      this.analyzeImage(upload.preview)
    },
    
    addToRecentUploads(preview, filename) {
      this.recentUploads.unshift({
        id: Date.now(),
        preview,
        filename,
        timestamp: new Date()
      })
      
      // Keep only last 6 uploads
      if (this.recentUploads.length > 6) {
        this.recentUploads = this.recentUploads.slice(0, 6)
      }
    },
    
    emotionColor(emotion) {
      const colors = {
        'Happy': 'bg-green-500',
        'Sad': 'bg-blue-500',
        'Angry': 'bg-red-500',
        'Surprise': 'bg-yellow-500',
        'Fear': 'bg-purple-500',
        'Disgust': 'bg-orange-500',
        'Neutral': 'bg-gray-500'
      }
      return colors[emotion] || 'bg-cyan-500'
    }
  }
}
</script>