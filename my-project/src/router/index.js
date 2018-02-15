import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import TimeEntries from '@/components/TimeEntries'
import LogTime from '@/components/LogTime'
import Users from '@/components/Users'
import Markdown from '@/components/Markdown'
import LoginForm from '@/components/LoginForm'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/',
      component: Home
    }, {
      path: '/users',
      component: Users
    }, {
      path: '/loginForm',
      component: LoginForm
    }, {
      path: '/markdown',
      component: Markdown,
      meta: {
        requiresAuth: true
      }
    }, {
      path: '/time-entries',
      component: TimeEntries,
      children: [{
        path: 'log-time',
        component: LogTime
      }]
    }]
})

router.beforeEach((to, from, next) => {
  if (to.path === '/loginForm') {
    next()
  } else {
    let token = window.localStorage.getItem('accessToken')
    if (to.meta.requiresAuth && (!token || token === null)) {
      next({
        path: '/loginForm',
        query: { redirect: to.fullPath }
      })
    } else {
      next()
    }
  }
})

export default router
