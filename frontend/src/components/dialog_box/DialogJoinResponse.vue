<template lang="">
    <div class="fixed bottom-0 inset-x-0 px-4 pb-4 sm:inset-0 sm:flex sm:items-center sm:justify-center">
        <div class="fixed inset-0 transition-opacity">
            <div class="absolute inset-0 bg-gray-500 opacity-20" @click.prevent="close">

            </div>
        </div>

        <div
            class="z-10 bg-white rounded-lg overflow-hidden shadow-xl transform transition-all sm:w-96"
            role="dialog"
            aria-modal="true"
            aria-labelledby="modal-headline"
        >
            <div class="bg-white px-4 pt-4 pb-4 sm:p-5 sm:pb-5">
                <div class="">
                    <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                        <div class="flex items-center justify-between mb-4">
                            <h3 class="text-lg leading-6 font-medium text-gray-900" id="modal-headline"
                            >
                            {{title}} {{username}}
                            </h3>
                        </div>
                        <div class="m-2">

                            <p>{{description}}</p>

                            <div class="mt-4 space-x-2 flex justify-evenly">

                                <button 
                                    @click.prevent="cancelResponsePlayer"
                                    class="w-24 rounded-md border border-gray-300 px-4 py-2 bg-white text-base leading-6 font-medium text-gray-700 shadow-sm hover:text-gray-500 focus:outline-none focus:border-blue-300 focus:shadow-outline-blue transition ease-in-out duration-150 sm:text-sm sm:leading-5">
                                 Cancel
                                </button>
    
                                <button 
                                    @click.prevent="confirm"
                                    class="w-24 rounded-md border border-gray-300 px-4 py-2 bg-gray-100 text-base leading-6 font-medium text-gray-700 shadow-sm hover:text-black focus:outline-none focus:border-blue-300 focus:shadow-outline-blue transition ease-in-out duration-150 sm:text-sm sm:leading-5">
                                {{v1_text}}
                                </button>
                                
                            </div>

                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>
   
</template>

<script>
export default {
    name: 'Modal',
    props: {
        username: {
            type: String
        },
        title: {
            type: String
        },
        description: {
            type: String
        },
        v1_text: {
            type: String
        },
        cancelResponsePlayer: {
            type: Function
        },
        confirm: {
            type: Function
        }
    }
}
</script>