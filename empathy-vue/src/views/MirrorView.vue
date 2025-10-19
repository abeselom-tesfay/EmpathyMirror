<!-- empathy-vue/src/views/MirrorView.vue -->
<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-900 via-purple-900 to-violet-900">
    <div class="container mx-auto px-4 py-8">
      <!-- Header Section -->
      <div class="text-center mb-12">
        <h1 class="text-5xl font-bold text-white mb-4">
          Empathy <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-500">Mirror</span>
        </h1>
        <p class="text-xl text-gray-300 max-w-2xl mx-auto">
          Real-time facial expression analysis with empathetic AI responses. Let the mirror understand how you feel.
        </p>
      </div>

      <!-- Main Mirror Component -->
      <EmpathyMirror />
      
      <!-- Features Grid -->
      <div class="grid md:grid-cols-3 gap-6 mt-16 max-w-6xl mx-auto">
        <div class="bg-white/5 backdrop-blur-sm rounded-2xl p-6 border border-white/10 hover:border-cyan-400/30 transition-all duration-300">
          <div class="w-12 h-12 bg-gradient-to-r from-cyan-500 to-blue-600 rounded-xl flex items-center justify-center mb-4">
            <ClockIcon class="w-6 h-6 text-white" />
          </div>
          <h3 class="text-white font-semibold text-lg mb-2">Real-time Analysis</h3>
          <p class="text-gray-400">Instant emotion detection powered by advanced CNN models</p>
        </div>
        
        <div class="bg-white/5 backdrop-blur-sm rounded-2xl p-6 border border-white/10 hover:border-purple-400/30 transition-all duration-300">
          <div class="w-12 h-12 bg-gradient-to-r from-purple-500 to-pink-600 rounded-xl flex items-center justify-center mb-4">
            <HeartIcon class="w-6 h-6 text-white" />
          </div>
          <h3 class="text-white font-semibold text-lg mb-2">Empathetic AI</h3>
          <p class="text-gray-400">Caring responses that understand and validate your emotions</p>
        </div>
        
        <div class="bg-white/5 backdrop-blur-sm rounded-2xl p-6 border border-white/10 hover:border-green-400/30 transition-all duration-300">
          <div class="w-12 h-12 bg-gradient-to-r from-green-500 to-emerald-600 rounded-xl flex items-center justify-center mb-4">
            <ChartBarIcon class="w-6 h-6 text-white" />
          </div>
          <h3 class="text-white font-semibold text-lg mb-2">Emotion Tracking</h3>
          <p class="text-gray-400">Comprehensive analytics and historical emotion patterns</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import EmpathyMirror from '../components/EmpathyMirror.vue'
import { ClockIcon, HeartIcon, ChartBarIcon } from '@heroicons/vue/outline'

export default {
  name: 'MirrorView',
  components: {
    EmpathyMirror,
    ClockIcon,
    HeartIcon,
    ChartBarIcon
  }
}
</script>