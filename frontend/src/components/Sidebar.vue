<template>

    <div class="w-64 border border-lighter px-8 pt-2 pb-8 h-fit rounded-lg space-y-16">
      <div>
        <router-link to="/" class="h-12 w-24 hover:bg-cyan-50 text-3xl rounded-lg text-blue ease-in duration-200">
          Ludo
        </router-link>
        <router-link v-for="tab in tabs" :key="tab.id" :to="tab.link" class="group flex items-center py-2 px-4 hover:bg-cyan-50 rounded-full mr-auto">
            <i :class="`${tab.icon} text-2xl mr-4 text-left w-6 text-gray-600 group-hover:text-blue-500`"></i>
            <p class="text-lg font-medium text-gray-400 group-hover:text-blue-500">{{tab.title}}</p>
        </router-link>
      </div>
      <button type="button" @click.prevent="logout" class="px-4 rounded-full">
          <p class="text-lg font-medium text-gray-400">Logout</p>
      </button>
    </div>
    


</template>

<script>
import axios from 'axios';

export default {
  name: 'Sidebar',
  data() {
    return {
      tabs: [
        {icon: 'fas fa-home', title: 'Home', id: 'home', link:'/'},
        {icon: 'fas fa-volleyball', title: 'Game', id: 'game', link:'/game'},
        {icon: 'fas fa-bell', title: 'Notification', id: 'notification', link:'/notification'},
        {icon: 'fas fa-person-biking', title: 'Competititon', id: 'competition', link:'/competition'},
        {icon: 'fas fa-cogs', title: 'Settings', id: 'settings', link:'/settings'},
      ]
    }
  },
  methods :{
    async logout(){
      await axios.post('users/logout')

      .then(response => {
      })

      this.$router.push('/login')

    }
  }
}
</script>

<style>
</style>

