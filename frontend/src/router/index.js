import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/HomePage.vue'
import Edit from '../views/EditPage.vue'
import Authorize from '../views/AuthorizePage.vue'
import Register from '../views/RegisterPage.vue'
import Profile from '../views/ProfilePage.vue'

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: Home
  },
  {
    path: '/edit',
    name: 'Edit',
    component: Edit
  },
  {
    path: '/authorize',
    name: 'Authorize',
    component: Authorize
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
