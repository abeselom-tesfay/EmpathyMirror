<template>
  <div class="flex flex-col items-center">
    <video ref="video" autoplay muted class="w-96 h-72 rounded-lg border-2 border-indigo-500"></video>
    <button @click="captureFrame" class="mt-4 px-4 py-2 bg-indigo-600 text-white rounded hover:bg-indigo-700">
      Detect Emotion
    </button>
  </div>
</template>

<script>
export default {
  name: 'ReflectFace',
  emits: ['emotion-detected'],
  mounted() {
    navigator.mediaDevices.getUserMedia({ video: true })
      .then(stream => { this.$refs.video.srcObject = stream })
      .catch(err => console.error("Error accessing webcam:", err))
  },
  methods: {
    async captureFrame() {
      const canvas = document.createElement('canvas')
      canvas.width = this.$refs.video.videoWidth
      canvas.height = this.$refs.video.videoHeight
      const ctx = canvas.getContext('2d')
      ctx.drawImage(this.$refs.video, 0, 0)
      const dataURL = canvas.toDataURL('image/jpeg')

      // Send to backend
      try {
        const res = await fetch('http://localhost:8000/predict', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ image: dataURL })
        })
        const data = await res.json()
        this.$emit('emotion-detected', data.emotion)
      } catch (err) {
        console.error(err)
      }
    }
  }
}
</script>

<style scoped>
/* Optional: add shadow or hover effects */
</style>
