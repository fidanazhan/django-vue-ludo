<template lang="">
    <div class="game">
        <div class="pt-2">
            <p>Here is game list that you can join</p>
        </div>

        <div class="my-4">
            <button class="border-2 border-emerald-100 bg-emerald-100 rounded"
            @click.prevent="CreateGameToggle"

            >
                <i class="fa-solid fa-plus p-2 bg-emerald-200"></i>
                <span class="p-2">Create Game</span>
            </button>
        </div>

        <div class="mt-4">

            <div class="border rounded w-fit divide-y divide-gray-700 divide-opacity-25 text-gray-800 m-auto mt-9">

                <table class="table-fixed rounded">
                    <thead>
                        <tr class="bg-teal-100">
                            <th class="w-24 inline-block px-4 py-2">Sport</th>
                            <th class="w-32 inline-block px-4 py-2">Venue</th>
                            <th class="w-32 inline-block px-4 py-2">Places</th>
                            <th class="w-28 inline-block py-4 px-2">Date</th>
                            <th class="w-32 inline-block py-4 px-2">Host</th>
                            <th class="w-32 inline-block py-4 px-2">Join</th>
                        </tr>
                    </thead>
                    <tbody >
                        <tr v-for="game in games" :key="game.id">
                            <td class="w-24 inline-block px-4 py-2">{{game.sport_type}}</td>
                            <td class="w-32 inline-block px-4 py-2" v-if="game.location1.length > 10">
                                {{truncate(game.location1, 10)}}... 
                            </td>
                            <td class="w-32 inline-block px-4 py-2" v-else>
                                {{game.location1}}
                            </td>
                            <td class="w-32 inline-block px-4 py-2" v-if="game.location2.length > 10">
                                {{truncate(game.location2, 10)}}... 
                            </td>
                            <td class="w-32 inline-block px-4 py-2" v-else>
                                {{game.location2}}
                            </td>
                            <td class="w-28 inline-block py-4 px-2">{{game.date}}</td>
                            <td class="w-32 inline-block py-4 px-2" v-if="game.arranger.username.length > 10">
                                {{truncate(game.arranger.username, 10)}}
                            </td>
                            <td class="w-32 inline-block px-4 py-2" v-else>
                                {{game.arranger.username}}
                            </td>
                            <td class="w-36 inline-block py-4 px-2">
                                <button @click.prevent="toggleModal(game.id)" class="px-3 py-1 bg-green-100 rounded">
                                    More Detail
                                </button>
                            </td>
                            <hr>
                            
                        </tr>
                    </tbody>
                </table>

            </div>

            <ul class="flex justify-center py-4">
                
              <span v-if="currentPage != 1">
                <button class="page-link" @click.prevent="loadBack()">
                    <li class="page-item px-4 py-1 hover:bg-cyan-100 rounded cursor-pointer">
                        <i class="fa-solid fa-chevron-left"></i>
                    </li>
                </button>
                <button @click.prevent="loadBackPage()">
                    <li class="page-item px-4 py-1 hover:bg-cyan-100 rounded cursor-pointer">
                      <a class="page-link">{{backPage}}</a>
                    </li>  
                </button>
              </span>
              <li class="page-item px-4 py-1 hover:bg-cyan-100 rounded cursor-pointer">
                <a class="page-link">{{currentPage}}</a>
              </li> 
              <span v-if="currentPage != lastPage">
                <button @click.prevent="loadNextPage()">
                    <li class="page-item px-4 py-1 hover:bg-cyan-100 rounded cursor-pointer">
                      <a class="page-link">{{nextPage}}</a>
                    </li>       
                </button>
                <button class="page-link" @click.prevent="loadNext()">
                    <li class="page-item px-4 py-1 hover:bg-cyan-100 rounded cursor-pointer">
                          <i class="fa-solid fa-chevron-right"></i>
                    </li>
                 </button>
              </span>
              
            </ul>
        </div>
    </div>

    <Modal v-if="isVisibility" :game_id="selectedGames" @toggle-modal="toggleModal('')" @toggle-join="toggleJoin()"></Modal>
    <ModalCreate v-if="isVisibilityCreateGame"  @toggle-modal="CreateGameToggle"></ModalCreate>
</template>

<script>
import Modal from '../components/modal/Modal'
import ModalCreate from '../components/modal/ModalCreate'
import axios from 'axios'

export default {
    name: 'GameView',
    components: {
        Modal,
        ModalCreate
    },
    data() {
        return {
            games: [],
            isVisibility : false,
            isVisibilityCreateGame : false,
            selectedGames: '',
            currentPage: 1,
            nextPage: '',
            backPage: '',
            lastPage: ''
        }
    },
    computed(){
        return {
            nextPage: currentPage + 1
        }
    },
    methods: {
        async fetchDataGames(){
            await axios.get('games')
            
            .then(response => {
                this.games = response.data.data
                this.lastPage = response.data.meta.last_page
                this.backPage = this.currentPage - 1
                this.nextPage = this.currentPage + 1
            })
        },

        async loadNext() {
            
            this.currentPage = this.currentPage + 1
            this.backPage = this.currentPage - 1
            this.nextPage = this.currentPage + 1

            await axios.get('games/?page=' + this.currentPage)
            
            .then(response => {
                this.games = response.data.data
                
            })
        },

        async loadBack(){

            this.currentPage = this.currentPage - 1
            this.backPage = this.currentPage - 1
            this.nextPage = this.currentPage + 1
            await axios.get('games/?page=' + this.currentPage)
            
            .then(response => {
                this.games = response.data.data
                
            })
        },

        async loadBackPage() {
            
            this.currentPage = this.backPage
            this.backPage = this.currentPage - 1
            this.nextPage = this.currentPage + 1  

            await axios.get('games/?page=' + this.currentPage)
            
            .then(response => {
                this.games = response.data.data
            })
        },

        async loadNextPage() {
            this.currentPage = this.nextPage
            this.backPage = this.currentPage - 1
            this.nextPage = this.currentPage + 1  

            await axios.get('games/?page=' + this.currentPage)
            
            .then(response => {
                this.games = response.data.data
            })
        },

        CreateGameToggle() {
            this.isVisibilityCreateGame = !this.isVisibilityCreateGame
        },

        toggleModal(game_id) {
            this.isVisibility = !this.isVisibility
            this.selectedGames = game_id
        },

        async toggleJoin() {
            this.isVisibility = !this.isVisibility

            await axios.get('games')
            
            .then(response => {
                this.games = response.data.data
                this.lastPage = response.data.meta.last_page
            })
        },

        truncate(data, num) {
            const reqdString = data.split("").slice(0, num).join("");
            return reqdString;
        }
    },
    async mounted() {
        const getCookieValue = (name) => (
            document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)')?.pop() || ''
        )

        let cookie = getCookieValue('jwt')
        if(!cookie) {
            this.$router.push('/login')
        }
        else{
            this.fetchDataGames()
        }
        
    }  
}
</script>

<style lang="">
    
</style>