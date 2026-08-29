import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/HomePage.vue'
import Edit from '../views/EditPage.vue'
import Authorize from '../views/AuthorizePage.vue'
import Register from '../views/RegisterPage.vue'
import Profile from '../views/ProfilePage.vue'
import EditProfile from '../views/EditProfilePage.vue'

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: Home
  },
  {
    path: '/edit',
    name: 'EditPage',
    component: Edit
  },
  {
    path: '/edit-profile',
    name: 'EditProfilePage',
    component: EditProfile
  },
  {
    path: '/authorize',
    name: 'AuthorizePage',
    component: Authorize
  },
  {
    path: '/register',
    name: 'RegisterPage',
    component: Register
  },
  {
    path: '/profile',
    name: 'ProfilePage',
    component: Profile
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
