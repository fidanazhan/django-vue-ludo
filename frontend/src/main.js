import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './assets/tailwind.css'
import axios from 'axios'

axios.defaults.baseURL = 'http://localhost:5000/api/';
axios.defaults.withCredentials = true;

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

createApp(App).component('font-awesome-icon', FontAwesomeIcon).use(store).use(router).mount('#app')


