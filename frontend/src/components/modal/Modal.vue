<template lang="">
    <div class="fixed bottom-0 inset-x-0 px-4 pb-4 sm:inset-0 sm:flex sm:items-center sm:justify-center">
        <div class="fixed inset-0 transition-opacity">
            <div class="absolute inset-0 bg-gray-500 opacity-10" @click.prevent="close">

            </div>
        </div>

        <div
            class="z-10 bg-white rounded-lg overflow-hidden shadow-xl transform transition-all sm:max-w-lg sm:w-full"
            role="dialog"
            aria-modal="true"
            aria-labelledby="modal-headline"
        >
            <div class="bg-white px-4 pt-4 pb-4 sm:p-5 sm:pb-5">
                <div class="sm:flex sm:items-start">
                    <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                        <div class="flex items-center justify-between mb-4">
                            <h3 class="text-lg leading-6 font-medium text-gray-900" id="modal-headline">
                            Game Detail For {{data.id}}
                            </h3>
                        </div>
                        <div class="m-2">
                            
                            <p>
                                <label for="">Sport Type : </label>
                                <span>{{data.sport_type}}</span>
                            </p>
                            <p>
                                <label for="">Venue : </label>
                                <span>{{data.location1}}</span>
                            </p>
                            <p>
                                <label for="">Places : </label>
                                <span>{{data.location2}}</span>
                            </p>
                            <p>
                                <label for="">Date: </label>
                                <span>{{data.date}}</span>
                            </p>
                            <p>
                                <label for="">Host : </label>
                                <span>{{data_host}}</span>
                            </p>
                            <p>
                                <label for="">Occupied Player : </label>
                                <span>{{data.occupied_player}}</span>
                            </p>
                            <p>
                                <label for="">Player Needed : </label>
                                <span>{{data.player_needed}}</span>
                            </p>
                            <p>
                                <label for="">Court Status : </label>
                                <span>{{data.court_status}}</span>
                            </p>
                            <p>
                                <label for="">Court Name : </label>
                                <span>{{data.court_name}}</span>
                            </p>
                            <p>
                                <label for="">Court Price : </label>
                                <span>{{data.court_price}}</span>
                            </p>
                            <p>
                                <label for="">Price Per Player : </label>
                                <span>{{data.price_per_player}}</span>
                            </p>

                        </div>
                    </div>
                </div>
            </div>

            <div class="bg-gray-50 px-4 py-6 sm:px-6 sm:flex sm:flex-row-reverse">
                <div class="mt-3 flex w-full rounded-md shadow-sm sm:mt-0 sm:w-auto justify-between space-x-4">
                    <button
                    type="button"
                    class="inline-flex justify-center w-full rounded-md border border-gray-300 px-4 py-2 bg-blue-500 text-base leading-6 font-medium text-white shadow-sm focus:outline-none focus:border-blue-300 focus:shadow-outline-blue transition ease-in-out duration-150 sm:text-sm sm:leading-5"
                    @click.prevent="createJoinRequest(game_id)"
                    >
                    Join
                    </button>

                    <button
                    type="button"
                    class="inline-flex justify-center w-full rounded-md border border-gray-300 px-4 py-2 bg-white text-base leading-6 font-medium text-gray-700 shadow-sm hover:text-gray-500 focus:outline-none focus:border-blue-300 focus:shadow-outline-blue transition ease-in-out duration-150 sm:text-sm sm:leading-5"
                    @click.prevent="close"
                    >
                    Cancel
                    </button>
                </div>
            </div>

        </div>
    </div>
   
</template>

<script>
import axios from 'axios'

export default {
    name: 'Modal',
    props: {
        game_id: {
            type: Number,
        }
    },
    data() {
        return {
            data: '',
            data_host: ''
        }
    },
    methods: {
        close() {
            this.$emit('toggle-modal')
        },

        async createJoinRequest(game_id){
            await axios.post(`joins/${this.game_id}/create_request`)
            
            .then(response => {
                console.log(response)
            })

            this.$emit('toggle-join')
        }


    },
    async mounted() {
        await axios.get(`games/${this.game_id}`)

        .then(response => {
            this.data = response.data.detail
            this.data_host = this.data.arranger.username

            console.log(response)
        })
    }
    
}
</script>
<style lang="">
    
</style>