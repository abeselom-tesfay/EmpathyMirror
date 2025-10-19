<!-- empathy-vue/src/components/FeatureCard.vue -->
<template>
  <div class="bg-white/5 backdrop-blur-sm rounded-2xl p-8 border border-white/10 hover:border-cyan-400/30 transition-all duration-300 group hover:transform hover:-translate-y-2">
    <div class="w-16 h-16 bg-gradient-to-r from-cyan-500 to-blue-600 rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
      <component :is="icon" class="w-8 h-8 text-white" />
    </div>
    <h3 class="text-2xl font-bold text-white mb-4">{{ title }}</h3>
    <p class="text-gray-300 leading-relaxed">{{ description }}</p>
  </div>
</template>

<script>
export default {
  name: 'FeatureCard',
  props: {
    title: String,
    description: String,
    icon: Object,
    color: String
  }
}
</script>