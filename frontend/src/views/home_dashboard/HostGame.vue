<template lang="">
    <div class="host-game">
        <div class="pt-2">
            <p>Here is list of games that you host.</p>
        </div>
        <div class="border rounded w-fit divide-y divide-gray-700 divide-opacity-25 text-gray-800 m-auto mt-9">
            <table class="table-fixed rounded">
                <thead>
                    <tr class="flex bg-teal-100">
                        <th class="w-24 inline-block px-4 py-2">ID</th>
                        <th class="w-24 inline-block px-4 py-2">Game</th>
                        <th class="w-28 inline-block px-4 py-2">Date</th>
                        <th class="w-32 inline-block py-4 px-2">Location</th>
                        <th class="inline-block py-4 px-2" style="width: 17rem;">Actions</th>
                    </tr>
                </thead>
                <tbody >
                    <tr v-for="game in game_host" :key="game.id">
                        <td class="w-24 inline-block py-4 px-2">{{game.pk}}</td>
                        <td class="w-24 inline-block px-4 py-2">{{game.sport_type}}</td>
                        <td class="w-28 inline-block py-4 px-2">{{game.date}}</td>
                        <td class="w-32 inline-block px-4 py-2" v-if="game.location1.length > 10">
                            {{truncate(game.location1, 10)}}... 
                        </td>
                        <td class="w-32 inline-block px-4 py-2" v-else>
                            {{game.location1}}
                        </td>
                        <td class="inline-block mx-a">
                            <!-- 
                            <button @click.prevent="toggleModal(game.pk)" class="px-2 mx-2 py-1 bg-green-100 rounded">
                                Details
                            </button> 
                            -->

                            <button @click.prevent="toggleJoin(game.pk)" class="px-2 mx-2 py-1 bg-yellow-100 rounded">
                                {{game.request_user__count}} Request
                            </button>

                            <button @click.prevent="toggleEdit(game.pk)" class="px-2 mx-2 py-1 bg-cyan-100 rounded">
                                Edit
                            </button>

                            <button @click.prevent="toggleDialogBoxDelete(game.pk)" class="px-2 py-1 bg-red-100 rounded">
                                Delete
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

    <ModalHostGameDetailVue 
        v-if="isVisibility" 
        :game_id="selectedGames"
        :close_detail="closeDetail" 
        @toggle-modal="toggleModal('')">
    </ModalHostGameDetailVue>
    <ModalEditGameVue v-if="isVisibilityEdit" :game_id="selectedGames" @toggle-edit="toggleEdit('')"></ModalEditGameVue>
    <DialogVue 
        v-if="isVisibilityDelete" 
        :game_id="selectedGames"
        :cancel="cancel"
        :confirm="confirm"
        title="Delete Game "
        description="Do you want to delete this game?"
        v1_text="Yes, delete it"
        @toggle-delete-dialog="toggleDialogBoxDelete('')">
    </DialogVue>

</template>

<script>
import axios from 'axios'
import ModalHostGameDetailVue from '@/components/modal/ModalHostGameDetail.vue';
import ModalEditGameVue from '@/components/modal/ModalEditGame.vue';
import DialogVue from '@/components/dialog_box/DialogDeleteGame.vue';

export default {
    data() {
        return{
            game_host:[],
            isVisibility : false,
            isVisibilityJoin: false,
            isVisibilityEdit: false,
            isVisibilityDelete: false,
            currentPage: 1,
            nextPage: '',
            backPage: '',
            lastPage: ''
        }
    },
    components: {
        ModalHostGameDetailVue,
        ModalEditGameVue,
        DialogVue
    },
    methods:{
        async callGameListFunction() {
            await axios.get('users/game-list')
            
            .then(response => {
                this.game_host = response.data.game_host
                this.lastPage = response.data.meta.last_page
                this.backPage = this.currentPage - 1
                this.nextPage = this.currentPage + 1
            })
        },

        async loadNext() {
            
            this.currentPage = this.currentPage + 1
            this.backPage = this.currentPage - 1
            this.nextPage = this.currentPage + 1

            await axios.get('users/game-list?page=' + this.currentPage)
            
            .then(response => {
                this.game_host = response.data.game_host
                
            })
        },

        async loadBack(){

            this.currentPage = this.currentPage - 1
            this.backPage = this.currentPage - 1
            this.nextPage = this.currentPage + 1
            await axios.get('users/game-list?page=' + this.currentPage)
            
            .then(response => {
                this.game_host = response.data.game_host
                
            })
        },

        async loadBackPage() {
            
            this.currentPage = this.backPage
            this.backPage = this.currentPage - 1
            this.nextPage = this.currentPage + 1  

            await axios.get('users/game-list?page=' + this.currentPage)
            
            .then(response => {
                this.game_host = response.data.game_host
                
            })
        },

        async loadNextPage() {
            this.currentPage = this.nextPage
            this.backPage = this.currentPage - 1
            this.nextPage = this.currentPage + 1  

            await axios.get('users/game-list?page=' + this.currentPage)
            
            .then(response => {
                this.game_host = response.data.game_host
                
            })
        },

        closeDetail(){
            this.isVisibility = !this.isVisibility
        },

        cancel() {
            this.isVisibilityDelete = !this.isVisibilityDelete
        },

        async confirm(game_id) {
            this.cancel()
            await axios.delete(`games/${game_id}`)

            .then(response=> {
                console.log(response)
            })

            .catch(error=> {
                console.log(error)
            })
            

            this.callGameListFunction()
        },

        toggleModal(game_id) {
            this.isVisibility = !this.isVisibility
            this.selectedGames = game_id
        },

        toggleJoin(game_id) {
            this.$router.push('/home/host/game/' + game_id + '/detail')
        },

        toggleEdit(game_id) {
            this.isVisibilityEdit = !this.isVisibilityEdit
            this.selectedGames = game_id

            this.callGameListFunction()
        },

        toggleDialogBoxDelete(game_id) {
            this.isVisibilityDelete = !this.isVisibilityDelete
            this.selectedGames = game_id

            this.callGameListFunction()

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
            const data = await axios.get('users/game-list')

            .then(response => {
                this.game_host = response.data.game_host
                this.lastPage = response.data.meta.last_page
                this.backPage = this.currentPage - 1
                this.nextPage = this.currentPage + 1
            })

        }
        
    }
}
</script>

<style lang="scss" scoped>
    
</style>