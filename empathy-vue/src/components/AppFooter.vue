<!-- empathy-vue/src/components/AppFooter.vue -->
<template>
  <footer class="bg-black/50 backdrop-blur-sm border-t border-white/10 mt-20">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div class="grid md:grid-cols-4 gap-8">
        <div class="md:col-span-2">
          <div class="flex items-center mb-4">
            <div class="w-10 h-10 bg-gradient-to-r from-cyan-400 to-blue-500 rounded-lg flex items-center justify-center mr-3">
              <span class="text-white font-bold text-lg">EM</span>
            </div>
            <span class="text-white text-xl font-bold">EmpathyMirror</span>
          </div>
          <p class="text-gray-400 max-w-md">
            Advanced AI-powered facial expression recognition with empathetic responses. 
            Understanding emotions, one expression at a time.
          </p>
        </div>
        
        <div>
          <h3 class="text-white font-semibold mb-4">Navigation</h3>
          <div class="space-y-2">
            <router-link to="/" class="block text-gray-400 hover:text-cyan-400 transition-colors">Home</router-link>
            <router-link to="/mirror" class="block text-gray-400 hover:text-cyan-400 transition-colors">Mirror</router-link>
            <router-link to="/analysis" class="block text-gray-400 hover:text-cyan-400 transition-colors">Analysis</router-link>
            <router-link to="/history" class="block text-gray-400 hover:text-cyan-400 transition-colors">History</router-link>
          </div>
        </div>
        
        <div>
          <h3 class="text-white font-semibold mb-4">Connect</h3>
          <div class="space-y-2">
            <a href="#" class="block text-gray-400 hover:text-cyan-400 transition-colors">GitHub</a>
            <a href="#" class="block text-gray-400 hover:text-cyan-400 transition-colors">Documentation</a>
            <a href="#" class="block text-gray-400 hover:text-cyan-400 transition-colors">Contact</a>
          </div>
        </div>
      </div>
      
      <div class="border-t border-white/10 mt-8 pt-8 flex flex-col md:flex-row justify-between items-center">
        <p class="text-gray-400 text-sm">
          © 2024 EmpathyMirror. Top 1 Project - Graduating Class.
        </p>
        <div class="flex space-x-6 mt-4 md:mt-0">
          <span class="text-gray-400 text-sm">Privacy Policy</span>
          <span class="text-gray-400 text-sm">Terms of Service</span>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'AppFooter'
}
</script>