<template lang="">
    <div class="fixed bottom-0 inset-x-0 px-4 pb-4 sm:inset-0 sm:flex sm:items-center sm:justify-center">
        <div class="fixed inset-0 transition-opacity">
            <div class="absolute inset-0 bg-gray-500 opacity-10">

            </div>
        </div>

        <div
            class="z-10 bg-white rounded-lg overflow-hidden shadow-xl transform transition-all sm:w-96 sm:w-96"
            role="dialog"
            aria-modal="true"
            aria-labelledby="modal-headline"
        >
            <div class="bg-white px-4 pt-4 pb-4 sm:p-5 sm:pb-5">
                <div class="">
                    <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                        <div class="flex items-center justify-between mb-4">
                            <h3 class="text-lg leading-6 font-medium text-gray-900" id="modal-headline">
                            Create Game
                            </h3>
                            <button 
                             class="text-md leading-6 font-medium text-gray-900"
                             @click.prevent="close">
                             <i class="fa-solid fa-x"></i>
                            </button>
                        </div>
                        <div class="m-2">
                            
                            <form @submit.prevent="createGame()" class="space-y-2">

                                <div class="space-y-1.5">
                                    <select 
                                        id="sport_type" 
                                        class="p-2 w-full border border-gray-300 text-gray-900 text-sm rounded focus:ring-blue-500 focus:border-blue-500 block w-full dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                        v-model="sport_type"
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

                                    <input
                                        type="text"
                                        class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:outline-none"
                                        id="venue"
                                        placeholder="Venue"
                                        v-model="venue"
                                    />

                                    <input
                                        type="text"
                                        class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:outline-none"
                                        id="venue"
                                        placeholder="Location"
                                        v-model="location"
                                    />

                                    <input
                                        type="text"
                                        class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:outline-none"
                                        id="venue"
                                        placeholder="Date"
                                        v-model="date"
                                    />

                                    <input
                                        type="text"
                                        class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:outline-none"
                                        id="venue"
                                        placeholder="Occupied Player"
                                        v-model="occupied_player"
                                    />

                                    <input
                                        type="text"
                                        class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:outline-none"
                                        id="venue"
                                        placeholder="Player Needed"
                                        v-model="player_needed"
                                    />

                                    <select 
                                        id="sport_type" 
                                        class="p-2 w-full border border-gray-300 text-gray-900 text-sm rounded focus:ring-blue-500 focus:border-blue-500 block w-full dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                        v-model="court_status"
                                        >
                                        <option value="Book" selected>Court Booked</option>
                                        <option value="Not Book">Still Unbook</option>
                                    </select>

                                    <input
                                        type="text"
                                        class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:outline-none"
                                        id="venue"
                                        placeholder="Court Name"
                                        v-model="court_name"
                                    />

                                    <input
                                        type="text"
                                        class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:outline-none"
                                        id="venue"
                                        placeholder="Court Price: RM 150 etc"
                                        v-model="court_price"
                                    />

                                    <input
                                        type="text"
                                        class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:outline-none"
                                        id="venue"
                                        placeholder="Price Per Player: RM 12 etc"
                                        v-model="price_per_player"
                                    />

                                </div>
                                

                                <button
                                    type="submit"
                                    class="inline-flex justify-center w-full rounded-md border border-gray-300 px-4 py-2 bg-white text-base leading-6 font-medium text-gray-700 shadow-sm hover:text-gray-500 focus:outline-none focus:border-blue-300 focus:shadow-outline-blue transition ease-in-out duration-150 sm:text-sm sm:leading-5"
                                    >
                                    Create
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
    name: 'ModalCreate',
    data() {
        return {
            sport_type: 'Football',
            venue: '',
            location: '',
            date: '',
            occupied_player: '',
            player_needed: '',
            court_status: 'Book',
            court_name : '',
            court_price : '',
            price_per_player: ''

        }
    },
    methods: {
        close() {
            this.$emit('toggle-modal')
        },

        async createGame(){
            await axios.post('games/', {
                sport_type : this.sport_type,
                location1 : this.venue,
                location2 : this.location,
                date : this.date,
                occupied_player : this.occupied_player,
                player_needed : this.player_needed,
                court_status : this.court_status,
                court_name : this.court_name,
                court_price : this.court_price,
                price_per_player : this.price_per_player
            })

            .then(response=> {
                console.log(response)
            })

            .catch(error => {
                console.log(error)
            })

            this.$emit('toggle-modal')
        }
    },
    async mounted() {
        
    }
    
}
</script>
<style lang="scss" scoped>
    
    
</style>