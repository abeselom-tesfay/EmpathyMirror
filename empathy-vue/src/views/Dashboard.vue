<!-- empathy-vue/src/views/Dashboard.vue -->
<template>
  <div class="min-h-screen pt-16">
    <!-- Hero Section -->
    <section class="relative py-20 overflow-hidden">
      <div class="absolute inset-0 bg-black/40"></div>
      <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h1 class="text-5xl md:text-7xl font-bold text-white mb-6">
          Welcome to
          <span class="bg-gradient-to-r from-cyan-400 to-blue-500 bg-clip-text text-transparent">
            EmpathyMirror
          </span>
        </h1>
        <p class="text-xl text-gray-300 mb-8 max-w-3xl mx-auto">
          Advanced AI-powered facial expression recognition that understands and responds to your emotions with empathy and care.
        </p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <router-link 
            to="/mirror" 
            class="bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-600 hover:to-blue-700 text-white px-8 py-4 rounded-xl font-semibold text-lg transition-all duration-300 transform hover:scale-105 shadow-2xl"
          >
            Start Mirror Session
          </router-link>
          <router-link 
            to="/analysis" 
            class="border-2 border-white/30 hover:border-white/50 text-white px-8 py-4 rounded-xl font-semibold text-lg transition-all duration-300 backdrop-blur-sm"
          >
            Upload Analysis
          </router-link>
        </div>
      </div>

      <!-- Animated background elements -->
      <div class="absolute top-0 left-0 w-72 h-72 bg-cyan-400 rounded-full mix-blend-multiply filter blur-3xl opacity-20 animate-pulse"></div>
      <div class="absolute top-0 right-0 w-72 h-72 bg-blue-400 rounded-full mix-blend-multiply filter blur-3xl opacity-20 animate-pulse animation-delay-2000"></div>
      <div class="absolute bottom-0 left-1/2 w-72 h-72 bg-purple-400 rounded-full mix-blend-multiply filter blur-3xl opacity-20 animate-pulse animation-delay-4000"></div>
    </section>

    <!-- Features Section -->
    <section class="py-20 bg-white/5 backdrop-blur-sm">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-4xl font-bold text-white mb-4">Why EmpathyMirror?</h2>
          <p class="text-xl text-gray-300">Advanced emotion recognition with empathetic AI responses</p>
        </div>

        <div class="grid md:grid-cols-3 gap-8">
          <FeatureCard 
            v-for="feature in features"
            :key="feature.title"
            :title="feature.title"
            :description="feature.description"
            :icon="feature.icon"
            :color="feature.color"
          />
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import FeatureCard from '../components/FeatureCard.vue'
import { CameraIcon, ChartBarIcon, HeartIcon } from '@heroicons/vue/outline'

export default {
  name: 'Dashboard',
  components: {
    FeatureCard
  },
  data() {
    return {
      features: [
        {
          title: 'Real-time Analysis',
          description: 'Instant emotion detection using advanced CNN models trained on FER2013 dataset',
          icon: CameraIcon,
          color: 'from-cyan-400 to-blue-500'
        },
        {
          title: 'Empathetic Responses',
          description: 'AI-powered empathetic feedback that understands and responds to your emotional state',
          icon: HeartIcon,
          color: 'from-pink-400 to-rose-500'
        },
        {
          title: 'Advanced Analytics',
          description: 'Comprehensive emotion tracking and historical analysis with beautiful visualizations',
          icon: ChartBarIcon,
          color: 'from-purple-400 to-indigo-500'
        }
      ]
    }
  }
}
</script>

<style scoped>
.animation-delay-2000 {
  animation-delay: 2s;
}

.animation-delay-4000 {
  animation-delay: 4s;
}
</style>