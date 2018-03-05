import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from '@/components/Dashboard'
import UsersList from '@/components/Users/List'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Dashboard',
      component: Dashboard
    },
    {
      path: '/Users/',
      name: 'Users',
      component: UsersList
    },
  ]
})
