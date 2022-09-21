<template>
  <div class="about">
    <Modal v-if="isVisibility" title="This is new title. Test" @toggle-modal="toggleModal" />

    <button @click.prevent="toggleModal" class="bg-blue-500 text-white pa-2 text-sm rounded">
        Open Modal   
    </button>
  </div>
</template>

<script>
  import Modal from '../components/modal/Modal'
  export default {
      name: 'GameView',
      components: {
          Modal
      },
      data() {
          return {
              isVisibility : false
          }
      },
      methods: {
          toggleModal() {
              this.isVisibility = !this.isVisibility
          }
      }    
  }
  </script>
  
  <style lang="">
      
  </style>