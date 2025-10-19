<!-- empathy-vue/src/components/EmpathyMirror.vue -->
<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-900 to-black py-8">
    <div class="max-w-6xl mx-auto px-4">
      <!-- Header -->
      <div class="text-center mb-8">
        <h1 class="text-4xl font-bold text-white mb-4">Empathy Mirror</h1>
        <p class="text-gray-400 text-lg">Real-time facial expression analysis with empathetic AI responses</p>
      </div>

      <div class="grid lg:grid-cols-2 gap-8">
        <!-- Camera Feed -->
        <div class="bg-white/5 backdrop-blur-sm rounded-2xl p-6 border border-white/10">
          <div class="flex justify-between items-center mb-4">
            <h2 class="text-xl font-semibold text-white">Live Camera</h2>
            <div class="flex space-x-2">
              <button 
                @click="toggleCamera"
                :class="[
                  'px-4 py-2 rounded-lg font-semibold transition-all duration-300',
                  isCameraActive 
                    ? 'bg-red-500 hover:bg-red-600 text-white' 
                    : 'bg-green-500 hover:bg-green-600 text-white'
                ]"
              >
                {{ isCameraActive ? 'Stop' : 'Start' }} Camera
              </button>
            </div>
          </div>

          <div class="relative bg-black rounded-xl overflow-hidden aspect-video">
            <video 
              ref="videoRef" 
              autoplay 
              playsinline
              class="w-full h-full object-cover"
            ></video>
            <canvas ref="canvasRef" class="absolute inset-0 w-full h-full pointer-events-none" />
            
            <!-- Loading overlay -->
            <div v-if="isLoading" class="absolute inset-0 bg-black/50 flex items-center justify-center">
              <div class="text-white text-center">
                <div class="w-12 h-12 border-4 border-cyan-400 border-t-transparent rounded-full animate-spin mx-auto mb-2"></div>
                <p>Analyzing emotions...</p>
              </div>
            </div>

            <!-- Emotion overlay -->
            <div v-if="currentEmotion && !isLoading" class="absolute bottom-4 left-4">
              <div class="bg-black/70 backdrop-blur-sm rounded-lg p-3 border border-white/20">
                <div class="flex items-center space-x-3">
                  <div class="w-3 h-3 rounded-full animate-pulse" :class="emotionColor"></div>
                  <span class="text-white font-semibold">{{ currentEmotion }}</span>
                  <span class="text-gray-300 text-sm">({{ (confidence * 100).toFixed(1) }}%)</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Empathy Response -->
        <div class="space-y-6">
          <!-- Response Card -->
          <div class="bg-white/5 backdrop-blur-sm rounded-2xl p-6 border border-white/10">
            <h2 class="text-xl font-semibold text-white mb-4">Empathetic Response</h2>
            <div class="min-h-[120px] flex items-center justify-center">
              <div v-if="empatheticResponse" class="text-center">
                <div class="w-16 h-16 bg-gradient-to-r from-cyan-400 to-blue-500 rounded-full flex items-center justify-center mx-auto mb-4">
                  <HeartIcon class="w-8 h-8 text-white" />
                </div>
                <p class="text-gray-200 text-lg leading-relaxed">{{ empatheticResponse }}</p>
              </div>
              <div v-else class="text-gray-400 text-center">
                <ChatIcon class="w-12 h-12 mx-auto mb-3 opacity-50" />
                <p>Start the camera to see empathetic responses to your emotions</p>
              </div>
            </div>
          </div>

          <!-- Emotion Chart -->
          <div class="bg-white/5 backdrop-blur-sm rounded-2xl p-6 border border-white/10">
            <h2 class="text-xl font-semibold text-white mb-4">Emotion Distribution</h2>
            <div class="space-y-3">
              <div 
                v-for="emotion in emotionHistory" 
                :key="emotion.name"
                class="flex items-center justify-between"
              >
                <span class="text-gray-300 text-sm w-20">{{ emotion.name }}</span>
                <div class="flex-1 bg-gray-700 rounded-full h-2 mx-4">
                  <div 
                    class="h-2 rounded-full transition-all duration-500"
                    :class="emotion.color"
                    :style="{ width: `${emotion.percentage}%` }"
                  ></div>
                </div>
                <span class="text-gray-400 text-sm w-12">{{ emotion.percentage.toFixed(1) }}%</span>
              </div>
            </div>
          </div>

          <!-- Session Stats -->
          <div class="grid grid-cols-3 gap-4">
            <div class="bg-white/5 backdrop-blur-sm rounded-xl p-4 text-center border border-white/10">
              <div class="text-2xl font-bold text-cyan-400 mb-1">{{ sessionStats.detections }}</div>
              <div class="text-gray-400 text-sm">Detections</div>
            </div>
            <div class="bg-white/5 backdrop-blur-sm rounded-xl p-4 text-center border border-white/10">
              <div class="text-2xl font-bold text-blue-400 mb-1">{{ sessionStats.confidence }}%</div>
              <div class="text-gray-400 text-sm">Avg Confidence</div>
            </div>
            <div class="bg-white/5 backdrop-blur-sm rounded-xl p-4 text-center border border-white/10">
              <div class="text-2xl font-bold text-purple-400 mb-1">{{ sessionStats.duration }}</div>
              <div class="text-gray-400 text-sm">Duration</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { HeartIcon, ChatIcon } from '@heroicons/vue/outline'

export default {
  name: 'EmpathyMirror',
  components: {
    HeartIcon,
    ChatIcon
  },
  data() {
    return {
      isCameraActive: false,
      isLoading: false,
      currentEmotion: null,
      confidence: 0,
      empatheticResponse: '',
      emotionHistory: [
        { name: 'Happy', percentage: 35, color: 'bg-green-500' },
        { name: 'Neutral', percentage: 25, color: 'bg-gray-500' },
        { name: 'Sad', percentage: 15, color: 'bg-blue-500' },
        { name: 'Angry', percentage: 10, color: 'bg-red-500' },
        { name: 'Surprise', percentage: 8, color: 'bg-yellow-500' },
        { name: 'Fear', percentage: 5, color: 'bg-purple-500' },
        { name: 'Disgust', percentage: 2, color: 'bg-orange-500' }
      ],
      sessionStats: {
        detections: 142,
        confidence: 87.5,
        duration: '12:34'
      },
      mediaStream: null,
      analysisInterval: null
    }
  },
  computed: {
    emotionColor() {
      const colors = {
        'Happy': 'bg-green-500',
        'Sad': 'bg-blue-500',
        'Angry': 'bg-red-500',
        'Surprise': 'bg-yellow-500',
        'Fear': 'bg-purple-500',
        'Disgust': 'bg-orange-500',
        'Neutral': 'bg-gray-500'
      }
      return colors[this.currentEmotion] || 'bg-cyan-500'
    }
  },
  methods: {
    async toggleCamera() {
      if (this.isCameraActive) {
        this.stopCamera()
      } else {
        await this.startCamera()
      }
    },

    async startCamera() {
      try {
        this.mediaStream = await navigator.mediaDevices.getUserMedia({ 
          video: { width: 640, height: 480 } 
        })
        this.$refs.videoRef.srcObject = this.mediaStream
        this.isCameraActive = true
        
        // Start analysis interval
        this.analysisInterval = setInterval(this.analyzeFrame, 1000)
        
      } catch (error) {
        console.error('Error accessing camera:', error)
        alert('Unable to access camera. Please ensure you have granted camera permissions.')
      }
    },

    stopCamera() {
      if (this.analysisInterval) {
        clearInterval(this.analysisInterval)
        this.analysisInterval = null
      }
      
      if (this.mediaStream) {
        this.mediaStream.getTracks().forEach(track => track.stop())
        this.mediaStream = null
      }
      
      this.isCameraActive = false
      this.currentEmotion = null
      this.empatheticResponse = ''
    },

    async analyzeFrame() {
      if (!this.isCameraActive || this.isLoading) return

      this.isLoading = true
      
      try {
        const canvas = this.$refs.canvasRef
        const video = this.$refs.videoRef
        const context = canvas.getContext('2d')
        
        canvas.width = video.videoWidth
        canvas.height = video.videoHeight
        context.drawImage(video, 0, 0, canvas.width, canvas.height)
        
        const imageData = canvas.toDataURL('image/jpeg')
        
        // Simulate API call - replace with actual backend call
        await this.simulateAnalysis(imageData)
        
      } catch (error) {
        console.error('Analysis error:', error)
      } finally {
        this.isLoading = false
      }
    },

    async simulateAnalysis(imageData) {
      // Simulate API delay
      await new Promise(resolve => setTimeout(resolve, 500))
      
      // Mock responses for demonstration
      const emotions = ['Happy', 'Sad', 'Angry', 'Surprise', 'Neutral', 'Fear']
      const mockEmotion = emotions[Math.floor(Math.random() * emotions.length)]
      const mockConfidence = 0.7 + Math.random() * 0.3
      
      const responses = {
        'Happy': "Your smile is beautiful! 😊 Keep spreading that positive energy!",
        'Sad': "I sense some sadness. Remember, storms don't last forever. You're stronger than you think.",
        'Angry': "I see the frustration. Taking a moment to breathe can help regain perspective.",
        'Surprise': "Wow! Something unexpected? Hope it's a pleasant surprise!",
        'Neutral': "A moment of calm reflection. Peaceful presence is powerful.",
        'Fear': "I sense some apprehension. You've overcome challenges before - you can handle this."
      }
      
      this.currentEmotion = mockEmotion
      this.confidence = mockConfidence
      this.empatheticResponse = responses[mockEmotion]
      
      // Update session stats
      this.sessionStats.detections++
      this.sessionStats.confidence = ((this.sessionStats.confidence + mockConfidence * 100) / 2).toFixed(1)
    }
  },

  beforeUnmount() {
    this.stopCamera()
  }
}
</script>