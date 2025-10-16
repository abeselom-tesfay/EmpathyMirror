<template>
  <div class="mt-6 p-4 bg-white rounded-lg shadow-md w-full max-w-lg">
    <h2 class="text-xl font-semibold mb-2">Emotion History</h2>
    <div v-if="history.length">
      <ul>
        <li v-for="(item, idx) in history" :key="idx" class="flex justify-between py-1 border-b">
          <span>{{ item.timestamp.toLocaleTimeString() }}</span>
          <span class="font-bold text-indigo-600">{{ item.emotion }}</span>
        </li>
      </ul>
    </div>
    <p v-else class="text-gray-400">No data yet...</p>
  </div>
</template>

<script>
export default {
  name: 'EmotionGraph',
  props: ['history']
}
</script>

<style scoped></style>
