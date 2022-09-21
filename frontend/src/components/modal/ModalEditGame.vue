<template lang="">
    <div class="fixed bottom-0 inset-x-0 px-4 pb-4 sm:inset-0 sm:flex sm:items-center sm:justify-center">
        <div class="fixed inset-0 transition-opacity">
            <div class="absolute inset-0 bg-gray-500 opacity-10">

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
                            <button 
                             class="text-md leading-6 font-medium text-gray-900"
                             @click.prevent="close">
                             <i class="fa-solid fa-x"></i>
                            </button>
                        </div>
                        <div class="m-2">

                            <form @submit.prevent="updateGame()" class="space-y-2">
                                <p>
                                    <label class="w-40 inline-block">Sport Type</label>
                                    <span>: 
                                        <select 
                                            id="sport_type" 
                                            class="p-2 w-64 border border-gray-300 text-gray-900 text-sm rounded focus:ring-blue-500 focus:border-blue-500 inline-block w-full dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                            v-model="data.sport_type"
                                            >
                                            <option value="Football" selected>Football</option>
                                            <option value="Rugby">Rugby</option>
                                            <option value="Basketball">Basketball</option>
                                            <option value="Tennis">Tennis</option>
                                            <option value="Baseball">Baseball</option>
                                            <option value="Badminton">Badminton</option>
                                            <option value="Cricket">Cricket</option>
                                            <option value="Hiking">Hiking</option>
                                            <option value="Cycling">Cycling</option>
                                        </select>
                                    </span>
                                </p>
                                <p>
                                    <label class="w-40 inline-block">Venue</label>
                                    <span>: <input
                                            type="text"
                                            class="form-control inline-block w-64 px-3 py-1 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:outline-none"
                                            id="venue"
                                            v-model="data.location1"
                                        /></span>
                                    
                                </p>
                                <p>
                                    <label class="w-40 inline-block">Location</label>
                                    <span>: <input
                                            type="text"
                                            class="form-control inline-block w-64 px-3 py-1 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:outline-none"
                                            id="location"
                                            v-model="data.location2"
                                        /></span>
                                    
                                </p>
                                <p>
                                    <label class="w-40 inline-block">Date</label>
                                    <span>: <input
                                            type="text"
                                            class="form-control inline-block w-64 px-3 py-1 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:outline-none"
                                            id="date"
                                            v-model="data.date"
                                        /></span>
                                    
                                </p>
                                <p>
                                    <label class="w-40 inline-block">Occupied Player</label>
                                    <span>: <input
                                            type="text"
                                            class="form-control inline-block w-64 px-3 py-1 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:outline-none"
                                            id="occupied_player"
                                            v-model="data.occupied_player"
                                        /></span>
                                    
                                </p>
                                <p>
                                    <label class="w-40 inline-block">Player Needed</label>
                                    <span>: <input
                                            type="text"
                                            class="form-control inline-block w-64 px-3 py-1 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:outline-none"
                                            id="player_needed"
                                            v-model="data.player_needed"
                                        /></span>
                                    
                                </p>
                                <p>
                                    <label class="w-40 inline-block">Court Status</label>
                                    <span>: 
                                        <select 
                                                id="sport_type" 
                                                class="p-2 w-64 border border-gray-300 text-gray-900 text-sm rounded focus:ring-blue-500 focus:border-blue-500 inline-block w-full dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                                v-model="data.court_status"
                                                >
                                                <option value="Book" selected>Court Booked</option>
                                                <option value="Not Book">Still Unbook</option>
                                        </select>
                                    </span>
                                </p>
                                <p>
                                    <label class="w-40 inline-block">Court Name</label>
                                    <span>: <input
                                            type="text"
                                            class="form-control inline-block w-64 px-3 py-1 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:outline-none"
                                            id="sport_type"
                                            v-model="data.court_name"
                                        /></span>
                                </p>
                                <p>
                                    <label class="w-40 inline-block">Court Price</label>
                                    <span>: <input
                                            type="text"
                                            class="form-control inline-block w-64 px-3 py-1 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:outline-none"
                                            id="sport_type"
                                            v-model="data.court_price"
                                        /></span>
                                </p>
    
                                <p>
                                    <label class="w-40 inline-block">Price Per Player</label>
                                    <span>: <input
                                            type="text"
                                            class="form-control inline-block w-64 px-3 py-1 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:outline-none"
                                            id="sport_type"
                                            v-model="data.price_per_player"
                                        /></span>
                                </p>

                                <button
                                    type="submit"
                                    class="inline-flex justify-center mt-4 w-full rounded-md border border-blue-300 px-4 py-2 bg-cyan-100 text-base leading-6 font-medium text-gray-700 shadow-sm hover:text-blue-500 focus:outline-none focus:border-blue-300 focus:shadow-outline-blue transition ease-in-out duration-150 sm:text-sm sm:leading-5"
                                > Edit
                                </button>
                            
                            
                            </form>
                            

                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>
    
   
</template>

<script>
import axios from 'axios'

export default {
    name: 'ModalHostGameDetail',
    components: {
        
    },
    props: {
        game_id: {
            type: Number,
        }
    },
    data() {
        return {
            data: '',
        }
    },
    methods: {
        close() {
            this.$emit('toggle-edit')
        },

        async updateGame() {
            await axios.put(`games/${this.game_id}`,{
                sport_type : this.data.sport_type,
                location1 : this.data.location1,
                location2 : this.data.location2,
                date : this.data.date,
                occupied_player : this.data.occupied_player,
                player_needed : this.data.player_needed,
                court_status : this.data.court_status,
                court_name : this.data.court_name,
                court_price : this.data.court_price,
                price_per_player : this.data.price_per_player
            })

            .then(response=> {
                console.log(response)
            })

            .catch(error => {
                console.log(error)
            })

            this.$emit('toggle-edit')

        }

    },
    async mounted() {
        await axios.get(`games/${this.game_id}`)

        .then(response => {
            this.data = response.data.detail
        })

        .catch(error=>{
            console.log(error)
        })
    }
    
}
</script>
<style lang="">
    
</style>