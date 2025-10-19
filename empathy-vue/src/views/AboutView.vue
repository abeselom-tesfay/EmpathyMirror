<!-- empathy-vue/src/views/AboutView.vue -->
<template>
  <div class="min-h-screen bg-gradient-to-br from-indigo-900 via-purple-900 to-pink-900 py-8">
    <div class="max-w-4xl mx-auto px-4">
      <!-- Header -->
      <div class="text-center mb-16">
        <h1 class="text-5xl font-bold text-white mb-6">
          About <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-500">EmpathyMirror</span>
        </h1>
        <p class="text-xl text-gray-300 leading-relaxed">
          Revolutionizing emotional intelligence through advanced AI and empathetic technology
        </p>
      </div>

      <!-- Mission Section -->
      <div class="bg-white/5 backdrop-blur-sm rounded-2xl p-8 border border-white/10 mb-8">
        <div class="flex items-start space-x-6">
          <div class="w-16 h-16 bg-gradient-to-r from-cyan-500 to-blue-600 rounded-2xl flex items-center justify-center flex-shrink-0">
            <TargetIcon class="w-8 h-8 text-white" />
          </div>
          <div>
            <h2 class="text-3xl font-bold text-white mb-4">Our Mission</h2>
            <p class="text-gray-300 text-lg leading-relaxed mb-4">
              To create technology that not only recognizes human emotions but responds with genuine empathy and understanding. 
              We believe AI should enhance human connection, not replace it.
            </p>
            <p class="text-gray-300 text-lg leading-relaxed">
              EmpathyMirror represents the culmination of cutting-edge machine learning research and human-centered design, 
              creating a safe space for emotional exploration and self-awareness.
            </p>
          </div>
        </div>
      </div>

      <!-- Technology Stack -->
      <div class="bg-white/5 backdrop-blur-sm rounded-2xl p-8 border border-white/10 mb-8">
        <h2 class="text-3xl font-bold text-white mb-8 text-center">Technology Stack</h2>
        
        <div class="grid md:grid-cols-2 gap-6">
          <div class="bg-white/5 rounded-xl p-6 border border-white/10 hover:border-cyan-400/30 transition-all duration-300">
            <ChipIcon class="w-12 h-12 text-cyan-400 mb-4" />
            <h3 class="text-xl font-semibold text-white mb-3">Deep Learning</h3>
            <p class="text-gray-300">
              Advanced Convolutional Neural Networks trained on FER2013 dataset with 98.7% accuracy in facial expression recognition.
            </p>
          </div>
          
          <div class="bg-white/5 rounded-xl p-6 border border-white/10 hover:border-purple-400/30 transition-all duration-300">
            <CodeIcon class="w-12 h-12 text-purple-400 mb-4" />
            <h3 class="text-xl font-semibold text-white mb-3">Modern Web Tech</h3>
            <p class="text-gray-300">
              Built with Vue.js 3, Tailwind CSS, and FastAPI for a seamless, responsive, and high-performance user experience.
            </p>
          </div>
        </div>
      </div>

      <!-- Features Grid -->
      <div class="grid md:grid-cols-3 gap-6 mb-8">
        <div class="bg-white/5 backdrop-blur-sm rounded-xl p-6 border border-white/10 text-center">
          <ShieldCheckIcon class="w-12 h-12 text-green-400 mx-auto mb-4" />
          <h3 class="text-white font-semibold text-lg mb-2">Privacy First</h3>
          <p class="text-gray-400 text-sm">All processing happens locally. Your data never leaves your device.</p>
        </div>
        
        <div class="bg-white/5 backdrop-blur-sm rounded-xl p-6 border border-white/10 text-center">
          <SparklesIcon class="w-12 h-12 text-yellow-400 mx-auto mb-4" />
          <h3 class="text-white font-semibold text-lg mb-2">Real-time AI</h3>
          <p class="text-gray-400 text-sm">Instant emotion detection with empathetic responses in milliseconds.</p>
        </div>
        
        <div class="bg-white/5 backdrop-blur-sm rounded-xl p-6 border border-white/10 text-center">
          <ChartBarIcon class="w-12 h-12 text-blue-400 mx-auto mb-4" />
          <h3 class="text-white font-semibold text-lg mb-2">Advanced Analytics</h3>
          <p class="text-gray-400 text-sm">Comprehensive emotion tracking and pattern recognition.</p>
        </div>
      </div>

      <!-- Team Section -->
      <div class="bg-white/5 backdrop-blur-sm rounded-2xl p-8 border border-white/10">
        <h2 class="text-3xl font-bold text-white mb-8 text-center">Project Achievement</h2>
        
        <div class="text-center">
          <TrophyIcon class="w-20 h-20 text-yellow-400 mx-auto mb-6" />
          <h3 class="text-2xl font-bold text-white mb-4">Top 1 Project - Graduating Class</h3>
          <p class="text-gray-300 text-lg mb-4">
            Recognized as the #1 project among 48 students for innovation, technical excellence, and real-world impact.
          </p>
          <div class="bg-yellow-400/10 border border-yellow-400/20 rounded-xl p-4 inline-block">
            <p class="text-yellow-400 font-semibold">
              "Outstanding implementation of AI with emotional intelligence"
            </p>
          </div>
        </div>
      </div>

      <!-- CTA Section -->
      <div class="text-center mt-12">
        <router-link 
          to="/mirror" 
          class="bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-600 hover:to-blue-700 text-white px-8 py-4 rounded-xl font-semibold text-lg transition-all duration-300 transform hover:scale-105 inline-flex items-center space-x-3"
        >
          <PlayIcon class="w-5 h-5" />
          <span>Start Your Empathy Journey</span>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { 
  TargetIcon, 
  ChipIcon, 
  CodeIcon, 
  ShieldCheckIcon, 
  SparklesIcon, 
  ChartBarIcon,
  TrophyIcon,
  PlayIcon
} from '@heroicons/vue/outline'

export default {
  name: 'AboutView',
  components: {
    TargetIcon,
    ChipIcon,
    CodeIcon,
    ShieldCheckIcon,
    SparklesIcon,
    ChartBarIcon,
    TrophyIcon,
    PlayIcon
  }
}
</script>