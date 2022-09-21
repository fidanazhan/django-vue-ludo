import { createRouter, createWebHistory } from 'vue-router'

import LoginView from '../views/auth/LoginView.vue'
import RegisterView from '../views/auth/RegisterView.vue'

import BaseView from '../views/BaseView.vue'

import HomeView from '../views/home_dashboard/HomeView.vue'
import HostGame from '../views/home_dashboard/HostGame.vue'
import HostGameDetail from '../views/home_dashboard/HostGameDetail.vue'
import ParticipantGame from '../views/home_dashboard/ParticipantGame.vue'

import GameView from '../views/GameView.vue'
import NotificationView from '../views/NotificationView.vue'
import CompetitionView from '../views/CompetitionView.vue'
import SettingsView from '../views/SettingsView.vue'

const routes = [
  {
    path: '/login',
    component: LoginView
  },
  {
    path: '/register',
    component: RegisterView
  },
  {
    path: '',
    component: BaseView,
    children: [
      {path: '', redirect: '/home'},
      {path: '/home', component: HomeView},
      {path: '/game', component: GameView},
      {path: '/notification', component: NotificationView},
      {path: '/competition', component: CompetitionView},
      {path: '/settings', component: SettingsView},

      {path: '/home/host/game', component: HostGame},
      {path: '/home/host/game/:id/detail', component: HostGameDetail},
      {path: '/home/join/request', component: ParticipantGame},
    ]
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
