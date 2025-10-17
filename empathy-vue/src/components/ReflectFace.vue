<template>
  <div class="flex flex-col items-center">
    <video ref="video" autoplay muted class="w-80 h-64 rounded-lg border-2 border-blue-400 shadow"></video>
    <button 
      class="mt-4 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
      @click="captureFrame">
      Detect Emotion
    </button>
  </div>
</template>

<script>
import { sendImageForPrediction } from '../services/api.js'

export default {
  emits: ['emotion'],
  mounted() {
    navigator.mediaDevices.getUserMedia({ video: true })
      .then(stream => { this.$refs.video.srcObject = stream })
      .catch(console.error)
  },
  methods: {
    async captureFrame() {
      const canvas = document.createElement('canvas')
      canvas.width = this.$refs.video.videoWidth
      canvas.height = this.$refs.video.videoHeight
      const ctx = canvas.getContext('2d')
      ctx.drawImage(this.$refs.video, 0, 0)
      const dataURL = canvas.toDataURL('image/jpeg')

      const emotion = await sendImageForPrediction(dataURL)
      if (emotion) this.$emit('emotion', emotion)
    }
  }
}
</script>
