import Vue from 'vue'
import VueRouter from 'vue-router'
import Myapp from '@/views/myapp/myapp'

Vue.use(VueRouter)

const routes = [
  {
    path: '/myapp',
    name: 'Myapp',
    component: Myapp,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
