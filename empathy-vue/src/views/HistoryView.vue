<!-- empathy-vue/src/views/HistoryView.vue -->
<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-900 via-slate-900 to-blue-900 py-8">
    <div class="max-w-7xl mx-auto px-4">
      <!-- Header -->
      <div class="text-center mb-12">
        <h1 class="text-4xl font-bold text-white mb-4">Emotion History</h1>
        <p class="text-xl text-gray-300">Track your emotional journey over time</p>
      </div>

      <!-- Stats Overview -->
      <div class="grid grid-cols-2 md:grid-cols-4 gap-6 mb-8">
        <div class="bg-white/5 backdrop-blur-sm rounded-2xl p-6 border border-white/10">
          <div class="text-2xl font-bold text-cyan-400 mb-2">127</div>
          <div class="text-gray-400 text-sm">Total Sessions</div>
        </div>
        <div class="bg-white/5 backdrop-blur-sm rounded-2xl p-6 border border-white/10">
          <div class="text-2xl font-bold text-green-400 mb-2">42%</div>
          <div class="text-gray-400 text-sm">Positive Emotions</div>
        </div>
        <div class="bg-white/5 backdrop-blur-sm rounded-2xl p-6 border border-white/10">
          <div class="text-2xl font-bold text-blue-400 mb-2">18%</div>
          <div class="text-gray-400 text-sm">Calm States</div>
        </div>
        <div class="bg-white/5 backdrop-blur-sm rounded-2xl p-6 border border-white/10">
          <div class="text-2xl font-bold text-purple-400 mb-2">7.2</div>
          <div class="text-gray-400 text-sm">Avg. Session (min)</div>
        </div>
      </div>

      <div class="grid lg:grid-cols-3 gap-8">
        <!-- Session History -->
        <div class="lg:col-span-2">
          <div class="bg-white/5 backdrop-blur-sm rounded-2xl p-6 border border-white/10">
            <div class="flex justify-between items-center mb-6">
              <h2 class="text-2xl font-semibold text-white">Recent Sessions</h2>
              <div class="flex space-x-3">
                <button class="bg-white/10 hover:bg-white/20 text-white px-4 py-2 rounded-xl transition-colors">
                  Filter
                </button>
                <button class="bg-cyan-500 hover:bg-cyan-600 text-white px-4 py-2 rounded-xl transition-colors">
                  Export
                </button>
              </div>
            </div>

            <div class="space-y-4">
              <div 
                v-for="session in sessions" 
                :key="session.id"
                class="bg-white/5 rounded-xl p-4 border border-white/10 hover:border-cyan-400/30 transition-all duration-300 cursor-pointer"
                @click="viewSessionDetails(session)"
              >
                <div class="flex items-center justify-between mb-3">
                  <div class="flex items-center space-x-3">
                    <div class="w-3 h-3 rounded-full" :class="emotionColor(session.dominantEmotion)"></div>
                    <span class="text-white font-semibold">{{ session.dominantEmotion }}</span>
                  </div>
                  <span class="text-gray-400 text-sm">{{ session.duration }}</span>
                </div>
                
                <div class="flex justify-between items-center">
                  <div class="text-gray-300 text-sm">
                    {{ session.date }} • {{ session.time }}
                  </div>
                  <div class="text-cyan-400 text-sm font-semibold">
                    {{ (session.confidence * 100).toFixed(1) }}% confidence
                  </div>
                </div>
                
                <!-- Emotion Distribution -->
                <div class="flex space-x-1 mt-3">
                  <div 
                    v-for="emotion in session.emotionDistribution" 
                    :key="emotion.name"
                    class="h-1 rounded-full flex-1"
                    :class="emotionColor(emotion.name)"
                    :style="{ opacity: emotion.percentage / 100 }"
                    :title="`${emotion.name}: ${emotion.percentage}%`"
                  ></div>
                </div>
              </div>
            </div>

            <!-- Load More -->
            <div class="text-center mt-6">
              <button class="bg-white/10 hover:bg-white/20 text-white px-6 py-3 rounded-xl transition-colors">
                Load More Sessions
              </button>
            </div>
          </div>
        </div>

        <!-- Analytics Sidebar -->
        <div class="space-y-6">
          <!-- Emotion Trends -->
          <div class="bg-white/5 backdrop-blur-sm rounded-2xl p-6 border border-white/10">
            <h3 class="text-white font-semibold mb-4">Weekly Trends</h3>
            <div class="space-y-4">
              <div 
                v-for="trend in emotionTrends" 
                :key="trend.emotion"
                class="flex items-center justify-between"
              >
                <div class="flex items-center space-x-3">
                  <div class="w-3 h-3 rounded-full" :class="emotionColor(trend.emotion)"></div>
                  <span class="text-gray-300 text-sm">{{ trend.emotion }}</span>
                </div>
                <div class="flex items-center space-x-2">
                  <TrendingUpIcon v-if="trend.change > 0" class="w-4 h-4 text-green-400" />
                  <TrendingDownIcon v-else class="w-4 h-4 text-red-400" />
                  <span :class="trend.change > 0 ? 'text-green-400' : 'text-red-400'" class="text-sm font-semibold">
                    {{ trend.change > 0 ? '+' : '' }}{{ trend.change }}%
                  </span>
                </div>
              </div>
            </div>
          </div>

          <!-- Most Common Emotions -->
          <div class="bg-white/5 backdrop-blur-sm rounded-2xl p-6 border border-white/10">
            <h3 class="text-white font-semibold mb-4">Most Common</h3>
            <div class="space-y-3">
              <div 
                v-for="emotion in commonEmotions" 
                :key="emotion.name"
                class="flex items-center justify-between"
              >
                <span class="text-gray-300">{{ emotion.name }}</span>
                <div class="flex items-center space-x-3">
                  <div class="w-20 bg-gray-700 rounded-full h-2">
                    <div 
                      class="h-2 rounded-full transition-all duration-1000"
                      :class="emotionColor(emotion.name)"
                      :style="{ width: `${emotion.percentage}%` }"
                    ></div>
                  </div>
                  <span class="text-gray-400 text-sm w-8">{{ emotion.percentage }}%</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Insights -->
          <div class="bg-gradient-to-r from-cyan-500/10 to-blue-500/10 border border-cyan-400/20 rounded-2xl p-6">
            <LightBulbIcon class="w-8 h-8 text-cyan-400 mb-3" />
            <h3 class="text-white font-semibold mb-2">Weekly Insight</h3>
            <p class="text-gray-200 text-sm leading-relaxed">
              You tend to feel most positive during morning sessions. Consider starting your day with a quick mirror check!
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { TrendingUpIcon, TrendingDownIcon, LightBulbIcon } from '@heroicons/vue/outline'

export default {
  name: 'HistoryView',
  components: {
    TrendingUpIcon,
    TrendingDownIcon,
    LightBulbIcon
  },
  data() {
    return {
      sessions: [
        {
          id: 1,
          date: '2024-01-15',
          time: '09:30 AM',
          duration: '12m 34s',
          dominantEmotion: 'Happy',
          confidence: 0.89,
          emotionDistribution: [
            { name: 'Happy', percentage: 65 },
            { name: 'Neutral', percentage: 20 },
            { name: 'Surprise', percentage: 10 },
            { name: 'Other', percentage: 5 }
          ]
        },
        {
          id: 2,
          date: '2024-01-14',
          time: '07:15 PM',
          duration: '8m 12s',
          dominantEmotion: 'Calm',
          confidence: 0.76,
          emotionDistribution: [
            { name: 'Neutral', percentage: 45 },
            { name: 'Calm', percentage: 35 },
            { name: 'Happy', percentage: 15 },
            { name: 'Other', percentage: 5 }
          ]
        },
        {
          id: 3,
          date: '2024-01-14',
          time: '02:45 PM',
          duration: '15m 23s',
          dominantEmotion: 'Focused',
          confidence: 0.82,
          emotionDistribution: [
            { name: 'Focused', percentage: 50 },
            { name: 'Neutral', percentage: 30 },
            { name: 'Determined', percentage: 15 },
            { name: 'Other', percentage: 5 }
          ]
        }
      ],
      emotionTrends: [
        { emotion: 'Happy', change: 12 },
        { emotion: 'Calm', change: 5 },
        { emotion: 'Focused', change: 8 },
        { emotion: 'Anxious', change: -3 }
      ],
      commonEmotions: [
        { name: 'Happy', percentage: 35 },
        { name: 'Neutral', percentage: 25 },
        { name: 'Calm', percentage: 15 },
        { name: 'Focused', percentage: 12 },
        { name: 'Other', percentage: 13 }
      ]
    }
  },
  methods: {
    emotionColor(emotion) {
      const colors = {
        'Happy': 'bg-green-500',
        'Sad': 'bg-blue-500',
        'Angry': 'bg-red-500',
        'Surprise': 'bg-yellow-500',
        'Fear': 'bg-purple-500',
        'Neutral': 'bg-gray-500',
        'Calm': 'bg-cyan-500',
        'Focused': 'bg-indigo-500',
        'Determined': 'bg-orange-500',
        'Anxious': 'bg-pink-500'
      }
      return colors[emotion] || 'bg-cyan-500'
    },
    
    viewSessionDetails(session) {
      // Navigate to session details or show modal
      console.log('View session:', session)
      // this.$router.push(`/session/${session.id}`)
    }
  }
}
</script>