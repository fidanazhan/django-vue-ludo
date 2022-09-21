<template lang="">
    <div class="host-game">
        
        <div class="pt-4 pb-8">
            <p>Game Detail for 1030</p>
            <div class="float-right space-x-4">
                <button class="bg-cyan-200 border border-blue-400 w-20 py-1 rounded"
                @click.prevent="toggleEdit(data.id)">
                    <i class="fa-regular fa-pen-to-square"></i>
                    <span class="ml-2">Edit</span>
                </button>
                <button class="bg-red-200 border border-red-400 w-24 py-1 px-2 rounded"
                @click.prevent = "toggleDeleteGame(data.id)">
                    <i class="fa-solid fa-trash text-gray-600"></i>
                    <span class="ml-2">Delete</span>
                </button>
            </div>

            <div class="my-10 px-4 space-y-1">

    
                <p>
                    <span class="w-32 inline-block">Game ID </span>
                    <span>: {{data.id}}</span>
                </p>
                <p>
                    <span class="w-32 inline-block">Sport Type</span>
                    <span>: {{data.sport_type}}</span>
                </p>
                <p>
                    <span class="w-32 inline-block">Venue </span>
                    <span>: {{data.location1}}</span>
                </p>
                <p>
                    <span class="w-32 inline-block">Location </span>
                    <span>: {{data.location2}}</span>
                </p>
                <p>
                    <span class="w-32 inline-block">Date </span>
                    <span>: {{data.date}}</span>
                </p>
                <p>
                    <span class="w-32 inline-block">Occupied Player </span>
                    <span>: {{data.occupied_player}}</span>
                </p>

                <p>
                    <span class="w-32 inline-block">Player Needed </span>
                    <span>:  {{data.player_needed}}</span>
                </p>

                <p>
                    <span class="w-32 inline-block">Court Status </span>
                    <span>:  {{data.court_status}}</span>
                </p>

                <p>
                    <span class="w-32 inline-block">Court Name </span>
                    <span>:  {{data.court_name}}</span>
                </p>

                <p>
                    <span class="w-32 inline-block">Court Price </span>
                    <span>:  {{data.court_price}}</span>
                </p>

                <p>
                    <span class="w-32 inline-block">Price Per Player </span>
                    <span>:  {{data.price_per_player}}</span>
                </p>

                <div>
                    <p class="w-32 inline-block">Player Joined </p> : 
                    <span v-if="player_joined.length == 0">
                        No player joined yet
                    </span>
                    <span v-else>
                        <div class="block px-8 space-y-2" v-for="(p, index) in player_joined" :key="p.id">
                            <span class="w-40 inline-block">{{index + 1}}. {{p.username}}</span>
                            <button class="bg-red-100 border border-red-300 rounded text-base py-1 px-2"
                            @click.prevent="toggleRemovePlayer(p.username)">Remove Player</button>
                        </div>
                    </span>
                </div>

                <div>
                    <p class="w-32 inline-block">Join Request </p> :
                    <span v-if="request_join_data.length == 0">
                        No player send request
                    </span>
                    <span v-else>
                        <div class="block px-8 space-y-2 space-x-4" v-for="(p, index) in request_join_data" :key="p.request_id">
                            <span class="w-40 inline-block">{{index + 1}}. {{p.sender__username}}</span>
                            <button class="bg-emerald-100 border border-green-500 rounded text-base py-1 px-2"
                            @click.prevent="toggleAcceptRequest(p)">Accept</button>
                            <button class="bg-red-100 border border-red-300 rounded text-base py-1 px-2"
                            @click.prevent="toggleRejectRequest(p)">Reject</button>
                        </div>
                    </span>
                </div>

                
            </div>

            
        </div>
        
    </div>

    <DialogRemovePlayerVue 
        v-if="isVisibilityRemovePlayer" 
        :username="selectedUser"
        title="Remove "
        :cancelRemovePlayer="cancelRemovePlayer"
        :confirm="confirmRemovePlayer"
        v1_text="Yes, remove."
        >
    </DialogRemovePlayerVue>

    <DialogDeleteGame 
        v-if="isVisibilityGameDelete" 
        :game_id="selectedGames"
        title="Delete Game "
        :cancel="cancel"
        :confirm="confirmDeleteGame"
        description="Do you want to delete this game?"
        v1_text="Yes, delete it"
        >
    </DialogDeleteGame>

    <DialogJoinResponse
        v-if="isVisibilityResponseAccept" 
        :username="selectedUser"
        :request_id="requestID"
        title="Accept User "
        description="Do you want to accept this user in your game?"
        :cancelResponsePlayer="cancelResponsePlayer"
        :confirm="confirmAccept"
        v1_text="Yes"
    >
    </DialogJoinResponse>

    <DialogJoinResponse
        v-if="isVisibilityResponseReject" 
        :username="selectedUser"
        :request_id="requestID"
        title="Reject User "
        description="Do you want to reject this user request?"
        :cancelResponsePlayer="cancelResponsePlayer"
        :confirm="confirmReject"
        v1_text="Yes"
    >
    </DialogJoinResponse>

    <ModalEditGameVue v-if="isVisibilityGameEdit" :game_id="selectedGames" @toggle-edit="toggleEdit('')"></ModalEditGameVue>

</template>

<script>
import axios from 'axios'
import DialogDeleteGame from '@/components/dialog_box/DialogDeleteGame.vue';
import ModalEditGameVue from '@/components/modal/ModalEditGame.vue';
import DialogRemovePlayerVue from '@/components/dialog_box/DialogRemovePlayer.vue';
import DialogJoinResponse from '@/components/dialog_box/DialogJoinResponse.vue';

export default {
    data() {
        return{
            data : [],
            player_joined : [],
            request_join_data: [],
            isVisibilityGameDelete: false,
            isVisibilityGameEdit: false,
            isVisibilityRemovePlayer: false,
            isVisibilityResponseAccept: false,
            isVisibilityResponseReject: false
        }
    },
    components: {
        DialogDeleteGame,
        ModalEditGameVue,
        DialogRemovePlayerVue,
        DialogJoinResponse
    },
    methods:{

        // -------------------- FETCH GAME DETAIL (MAIN) --------------------
        async fetchDataGameDetail(){
            await axios.get('users/game-host/'+ this.$route.params.id + '/detail')

            .then(response => {
                this.data = response.data.detail
                this.player_joined = this.data.player_joined
            })
        },

        // --------------------- FETCH REQUEST LIST (SECONDARY) -----------------

        async fetchDataRequest(){
            await axios.get(`joins/host/${this.$route.params.id}/join-list`)

        .then(response => {
            this.request_join_data = response.data
        })
        },

        // -------------------- TOGGLE REMOVE PLAYER ----------------------

        toggleRemovePlayer(username) {
            this.isVisibilityRemovePlayer = !this.isVisibilityRemovePlayer
            this.selectedUser = username

        },

        cancelRemovePlayer(){
            this.isVisibilityRemovePlayer = !this.isVisibilityRemovePlayer
        },

        async confirmRemovePlayer() {
            this.cancelRemovePlayer()
            await axios.post('joins/'+ this.data.id  + "/" + this.selectedUser + '/remove_player')
            
            .then(response=> {
                console.log(response)
            })

            .catch(error=> {
                console.log(error)
            })

            this.fetchDataGameDetail()
            this.fetchDataRequest()
        },


        // --------------------- RESPONSE TO REQUEST ----------------------

        // Response to the request
        cancelResponsePlayer() {
            this.isVisibilityResponseAccept = false 
            this.isVisibilityResponseReject = false
        },
        
        toggleAcceptRequest(array) {
            this.isVisibilityResponseAccept = !this.isVisibilityResponseAccept
            this.selectedUser = array.sender__username
            this.requestID = array.request_id
        },

        async confirmAccept() {
            this.cancelResponsePlayer()
            await axios.post('joins/'+ this.requestID + '/response', {
                Response: 'Accept'
            })
            
            .then(response=> {
                console.log(response)
            })

            .catch(error=> {
                console.log(error)
            })

            this.fetchDataGameDetail()
            this.fetchDataRequest()
        },

        toggleRejectRequest(array) {
            this.isVisibilityResponseReject = !this.isVisibilityResponseReject
            this.requestID = array.request_id
            this.selectedUser = array.sender__username
        },

        async confirmReject() {
            this.cancelResponsePlayer()
            await axios.post('joins/'+ this.requestID + '/response', {
                Response: 'Reject'
            })
            
            .then(response=> {
                console.log(response)
            })

            .catch(error=> {
                console.log(error)
            })

            this.fetchDataGameDetail()
            this.fetchDataRequest()
        },

        // --------------------- TOGGLE DELETE GAME -------------------------

        toggleDeleteGame(data_id) {
            this.isVisibilityGameDelete = !this.isVisibilityGameDelete
            this.selectedGames = data_id
        },

        cancel() {
            this.isVisibilityGameDelete = !this.isVisibilityGameDelete
        },

        async confirmDeleteGame(game_id) {
            this.cancel()
            await axios.delete(`games/${game_id}`)

            .then(response=> {
                console.log(response)
            })

            .catch(error=> {
                console.log(error)
            })

            this.$router.push('/home/host/game')
        },

        // --------------------- TOGGLE EDIT GAME -------------------------

        toggleEdit(data_id) {
            this.isVisibilityGameEdit = !this.isVisibilityGameEdit
            this.selectedGames = data_id

            this.fetchDataGameDetail()
            this.fetchDataRequest()

        },

        truncate(data, num) {
            const reqdString = data.split("").slice(0, num).join("");
            return reqdString;
        }
    },
    mounted() {
        const getCookieValue = (name) => (
            document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)')?.pop() || ''
        )

        let cookie = getCookieValue('jwt')
        if(!cookie) {
            this.$router.push('/login')
        }
        else{
            this.fetchDataGameDetail()
            this.fetchDataRequest()

        }
        
    }
}
</script>

<style lang="scss" scoped>
    
</style>