<template lang="">
    <div class="host-game">
        <div class="pt-2">
            <p>Here is list of games that you had sent request to join. Waiting for response from the host.</p>
        </div>
        <div class="border rounded w-fit divide-y divide-gray-700 divide-opacity-25 text-gray-800 m-auto mt-9">

            <table class="table-fixed rounded">
                <thead>
                    <tr class="flex bg-teal-100">
                        <th class="w-24 inline-block px-4 py-2">ID</th>
                        <th class="w-24 inline-block px-4 py-2">Game</th>
                        <th class="w-28 inline-block px-4 py-2">Date</th>
                        <th class="w-24 inline-block py-4 px-2">Location</th>
                        <th class="inline-block py-4 px-2" style="width: 15rem;">Actions</th>
                    </tr>
                </thead>
                <tbody >
                    <tr v-for="request_join in request_join_list" :key="request_join.request_id">
                        <td class="w-24 inline-block py-4 px-2">{{request_join.game.id}}</td>
                        <td class="w-24 inline-block px-4 py-2">{{request_join.game.sport_type}}</td>
                        <td class="w-28 inline-block py-4 px-2">{{request_join.game.date}}</td>
                        <td class="w-28 inline-block px-4 py-2" v-if="request_join.game.location1.length > 10">
                            {{truncate(request_join.game.location1, 10)}}... 
                        </td>
                        <td class="w-28 inline-block px-4 py-2" v-else>
                            {{request_join.game.location1}}
                        </td>
                        <td class="inline-block mx-a">
                            
                            <button @click.prevent="toggleJoinerGameDetail(request_join.game.id)" class="px-2 mx-2 py-1 bg-green-100 rounded">
                                Details
                            </button>

                            <button @click.prevent="toggleCancelRequestDialog(request_join.request_id)" class="px-2 py-1 bg-red-100 rounded">
                                Cancel Request
                            </button>
                        </td>
                        <hr>
                        
                    </tr>
                </tbody>
            </table>

        </div>

        <ul class="flex justify-center py-4">
              <li class="page-item px-4 py-1 hover:bg-cyan-100 rounded">
                <a class="page-link">Previous</a>
              </li>
              <li class="page-item px-4 py-1 hover:bg-cyan-100 rounded">
                <a class="page-link">Next</a>
              </li>
              <li class="page-item px-4 py-1 hover:bg-cyan-100 rounded">
                <a class="page-link">{{lastPage}}</a>
              </li>
        </ul>
        
    </div>

    <ModalJoinerGameDetail 
        v-if="isVisibility" 
        :game_id="selectedGame"
        :close_detail="close" >
    </ModalJoinerGameDetail>

    <DialogCancelRequest 
        v-if="isVisibilityCancelRequest" 
        :request_id="request_id"
        :close_detail="close"
        :confirm="confirmCancelRequest"
        title="Cancel Joining"
        description="Do you want to cancel request from joining this game?"
        v1_text = "Yes, cancel request.">
        
    </DialogCancelRequest>

</template>

<script>
import axios from 'axios'
import ModalJoinerGameDetail from '@/components/modal/ModalJoinerGameDetail.vue';
import DialogCancelRequest from '@/components/dialog_box/DialogCancelRequest.vue';

export default {
    data() {
        return{
            request_join_list:[],
            isVisibility : false,
            isVisibilityCancelRequest: false,
            lastPage: ''
        }
    },
    components: {
        ModalJoinerGameDetail,
        DialogCancelRequest
    },
    methods:{
        async fetchDataRequestList() {
            await axios.get('joins/joiner/join-list')

            .then(response => {
                this.request_join_list = response.data
            })

            .catch(error=> {
                console.log(error)
            })
        },

        close(){
            this.isVisibility = false
            this.isVisibilityCancelRequest = false
        },

        toggleJoinerGameDetail(game_id) {
            this.isVisibility = true
            this.selectedGame = game_id
        },

        toggleCancelRequestDialog(request_id) {
            this.isVisibilityCancelRequest = true
            this.request_id = request_id
        },

        async confirmCancelRequest(){
            await axios.post('joins/' + this.request_id + '/cancel_request')

            .then(response=> {
                console.log(response)
            })

            .catch(error=> {
                console.log(error)
            } )

            this.isVisibilityCancelRequest = false

            this.fetchDataRequestList()
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
            
            this.fetchDataRequestList()

        }
        
    }
}
</script>

<style lang="scss" scoped>
    
</style>