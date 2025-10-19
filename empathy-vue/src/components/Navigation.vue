<!-- empathy-vue/src/components/Navigation.vue -->
<template>
  <nav class="bg-white/10 backdrop-blur-md border-b border-white/20 sticky top-0 z-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between h-16">
        <div class="flex items-center">
          <router-link to="/" class="flex-shrink-0 flex items-center">
            <div class="w-10 h-10 bg-gradient-to-r from-cyan-400 to-blue-500 rounded-lg flex items-center justify-center mr-3">
              <span class="text-white font-bold text-lg">EM</span>
            </div>
            <span class="text-white text-xl font-bold bg-gradient-to-r from-cyan-400 to-blue-500 bg-clip-text text-transparent">
              EmpathyMirror
            </span>
          </router-link>
        </div>

        <div class="hidden md:flex items-center space-x-8">
          <router-link 
            v-for="item in navigation" 
            :key="item.name" 
            :to="item.path"
            class="text-gray-300 hover:text-white px-3 py-2 rounded-md text-sm font-medium transition-all duration-300 hover:bg-white/10"
            active-class="text-white bg-white/20"
          >
            {{ item.name }}
          </router-link>
        </div>

        <div class="flex items-center space-x-4">
          <button 
            @click="toggleTheme"
            class="p-2 rounded-lg bg-white/10 hover:bg-white/20 transition-all duration-300 text-white"
          >
            <SunIcon v-if="darkMode" class="w-5 h-5" />
            <MoonIcon v-else class="w-5 h-5" />
          </button>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
import { SunIcon, MoonIcon } from '@heroicons/vue/outline'

export default {
  name: 'Navigation',
  components: {
    SunIcon,
    MoonIcon
  },
  data() {
    return {
      darkMode: true,
      navigation: [
        { name: 'Home', path: '/' },
        { name: 'Mirror', path: '/mirror' },
        { name: 'Analysis', path: '/analysis' },
        { name: 'History', path: '/history' },
        { name: 'About', path: '/about' }
      ]
    }
  },
  methods: {
    toggleTheme() {
      this.darkMode = !this.darkMode
      if (this.darkMode) {
        document.documentElement.classList.add('dark')
      } else {
        document.documentElement.classList.remove('dark')
      }
    }
  }
}
</script>