<template>
  <nav class="fixed w-full top-0 left-0 z-50 bg-cyan-700 px-4 md:px-20 py-3 flex justify-between items-center">
    <div class="">
      <img src="@/assets/logo.png" alt="Logo" class="h-30 w-30"/>
    </div>
    <ul class="hidden md:flex space-x-6 text-white font-medium">
      <li><a href="/#main" class="hover:text-cyan-300 transition-colors max-xl:hidden">Main</a></li>
      <li><a href="/#tech-stack" class="hover:text-cyan-300 transition-colors">Technical Details</a></li>
      <li><a href="/#risks" class="hover:text-cyan-300 transition-colors max-xl:hidden">Risks Detection</a></li>
      <li><a href="/#features" class="hover:text-cyan-300 transition-colors">Features</a></li>
      <li><a href="/#how-to-use" class="hover:text-cyan-300 transition-colors">How it works</a></li>
      <li><a href="/samples" class="hover:text-cyan-300 transition-colors">Samples</a></li>
      <li><a href="/#ai" class="hover:text-cyan-300 transition-colors max-xl:hidden">Artificial Intelligence</a></li>
      <li><a href="/faq" class="hover:text-cyan-300 transition-colors">FAQ</a></li>
      <li><a href="/register" class="hover:text-cyan-300 transition-colors max-xl:hidden">Register</a></li>
      <li><a href="/login" class="hover:text-cyan-300 transition-colors">Log In</a></li>
    </ul>

    <button 
      class="md:hidden text-white focus:outline-none"
      @click="isOpen = !isOpen"
    >
      <svg v-if="!isOpen" xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none"
        viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
          d="M4 6h16M4 12h16M4 18h16" />
      </svg>

      <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none"
          viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M6 18L18 6M6 6l12 12" />
      </svg>
    </button>

    <div 
      v-if="isOpen"
      class="absolute top-full left-0 w-full bg-cyan-700 shadow-md flex flex-col items-center space-y-4 py-4 md:hidden text-white"
    >
      <a href="/#main" class="hover:text-cyan-300" @click="isOpen = false">Main</a>
      <a href="/#tech-stack" class="hover:text-cyan-300 transition-colors" @click="isOpen = false">Technical Details</a>
      <a href="/#risks" class="hover:text-cyan-300" @click="isOpen = false">Risks</a>
      <a href="/#features" class="hover:text-cyan-300" @click="isOpen = false">Detection Features</a>
      <a href="/#how-to-use" class="hover:text-cyan-300" @click="isOpen = false">How it works</a>
      <a href="/samples" class="hover:text-cyan-300" @click="isOpen = false">Samples</a>
      <a href="/#ai" class="hover:text-cyan-300" @click="isOpen = false">Artificial Intelligence</a>
      <a href="/faq" class="hover:text-cyan-300" @click="isOpen = false">FAQ</a>
      <a href="/register" class="hover:text-cyan-300 bg-cyan-800 rounded-full px-8 py-2" @click="isOpen = false">Register</a>
      <a href="/login" class="border border-white px-9 py-2 rounded-full" @click="isOpen = false">Log In</a>
    </div>
  </nav>
</template>

<script setup>
import { ref } from "vue";

const isOpen = ref(false);
</script>
