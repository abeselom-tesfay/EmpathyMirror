<template>
  <div class="mt-6 p-4 bg-white rounded-lg shadow-md w-80 text-center">
    <h2 class="text-xl font-semibold mb-2">Current Emotion</h2>
    <p v-if="emotion" class="text-2xl font-bold text-indigo-600">{{ emotion }}</p>
    <p v-else class="text-gray-400">Waiting for detection...</p>
  </div>
</template>

<script>
export default {
  name: 'MoodMeter',
  props: ['emotion']
}
</script>

<style scoped></style>
