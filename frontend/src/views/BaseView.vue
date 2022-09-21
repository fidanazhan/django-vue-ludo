<template>

  <div class="flex container h-screen px-40 py-8">
    <Sidebar />
    <div class="ml-8 pt-4 px-8 w-full">
        <router-view/>
    </div>
  </div>
    
  </template>
  
  <script>
  import Sidebar from '../components/Sidebar.vue'
  
  export default {
    name: 'BaseView',
    components: {
      Sidebar
    }
    
  }
  </script>
  
  <style lang="scss">
  
  </style>
  