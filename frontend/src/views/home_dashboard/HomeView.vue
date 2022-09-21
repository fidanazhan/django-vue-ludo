<template>
  <div class="home">
    <div class="pt-2">
      <h3>Hi, {{user}}</h3>
      <p>Here is your dashboard</p>
    </div>
    <div class="mt-8 space-y-9">
      
      <!-- First Row -->
      <div class="flex justify-around">
        <router-link 
            class="border border-1 border-black-400 w-56 text-center h-16 p-1 rounded-lg"
            to="/game"
        >
          <p class="text-gray-400 font-semibold">Game Played</p>
          <span class="text-sm">1 Games Completed</span>
        </router-link>
        <router-link 
            class="border border-1 border-black-400 w-56 text-center h-16 p-1 rounded-lg"
            to="/home/host/game"    
        >
          <p class="text-gray-400 font-semibold">Game Host</p>
          <span class="text-sm">{{gameHostNumber}} Games Actively Hosted</span>
        </router-link>
        <router-link 
            class="border border-1 border-black-400 w-56 text-center h-16 p-1 rounded-lg"
            to="/home/join/request"
        >
          <p class="text-gray-400 font-semibold">Game Requested</p>
          <span class="text-sm">{{gameJoinerRequestNumber}} Games Requested To Join</span>
        </router-link>
      </div>

      <!-- Second Row -->
      <div class="flex justify-around">
        <div class="bg-red-100 w-72 text-center h-48 p-1 rounded-lg"></div>
        <div class="bg-cyan-100 w-72 text-center h-48 p-1 rounded-lg"></div>
      </div>

      <!-- Third Row -->
      <div class="border rounded w-fit divide-y divide-gray-700 divide-opacity-25 text-gray-800 m-auto">

        <span v-for="game in games.slice((page - 1) * perPage, page * perPage)"  :key="game.id" class="px-4 py-2 w-full block">
            <span class="w-24 inline-block">{{game.game_type}}</span>
            <span class="w-32 inline-block" v-if="game.location1.length>10">
              {{truncate(game.location1, 15)}}... 
            </span>
            <span class="w-32 inline-block" v-else>
              {{game.location1}}
            </span>
            <span class="w-32 inline-block">{{game.location2}}</span>
            <span class="w-32 inline-block" v-if="game.is_active">
              <span class="bg-green-200 py-1 px-1.5">
                Completed
              </span>
            </span>
            <span class="w-32 inline-block" v-else>
              <span class="bg-red-200 py-1 px-1.5 items-center">
                Soon
              </span>
            </span>
            <span class="w-28 inline-block">{{game.date}}</span>
            <span class="w-24 inline-block">{{game.host}}</span>
          </span>

          <nav>
            <ul class="flex justify-center py-2">
              <li class="page-item px-4 py-1 hover:bg-cyan-100 rounded">
                <a href="javascript:void(0)" class="page-link">Previous</a>
              </li>
              <li class="page-item px-4 py-1 hover:bg-cyan-100 rounded">
                <a href="javascript:void(0)" class="page-link">Next</a>
              </li>
            </ul>
          </nav>
      </div>
    </div>

  </div>
</template>

<script>
import Modal from '@/components/modal/Modal.vue';
import axios from 'axios'

export default {
    name: "HomeView",
    data() {
        return {
            games: [
                { id: 0, game_type: "Futsal", location1: "Lavana", location2: "Subang Jaya", is_active: true, date: "12/8/2022", host: "Izdan" },
                { id: 1, game_type: "Basketball", location1: "Basketball UM", location2: "Shah Alam", is_active: false, date: "12/8/2022", host: "Izad" },
                { id: 2, game_type: "Football", location1: "Sport Centre", location2: "Puchong", is_active: false, date: "12/8/2022", host: "Hadafi" },
                { id: 3, game_type: "Tennis", location1: "Sport Centre", location2: "Bangi", is_active: true, date: "12/8/2022", host: "Hadafi" }
            ],
            page: 1,
            perPage: 2,
            lastPage: 0,
            next:true,
            previous:true,
            user: '',
            gameHostNumber: '',
            gameJoinerRequestNumber: ''
            
        };
    },
    methods: {
        truncate(data, num) {
            const reqdString = data.split("").slice(0, num).join("");
            return reqdString;
        }
    },
    components: { Modal },
    async mounted() {
        const getCookieValue = (name) => (
            document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)')?.pop() || ''
        )

        let cookie = getCookieValue('jwt')
        if(!cookie) {
            this.$router.push('/login')
        }
        else{
            const {data} = await axios.get('users/auth-user')
            
            this.user = data.data.username

            const gameHostCount = await axios.get('users/game-host')

            this.gameHostNumber = gameHostCount.data.game_host

            const gameJoinerRequestCount = await axios.get('users/join-request')

            this.gameJoinerRequestNumber = gameJoinerRequestCount.data.joiner_request_count



        }
        
    }
}
</script>
