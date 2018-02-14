import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import TimeEntries from '@/components/TimeEntries'
import LogTime from '@/components/LogTime'
import Users from '@/components/Users'
import Markdown from '@/components/Markdown'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: Home
    }, {
      path: '/users',
      component: Users
    }, {
      path: '/markdown',
      component: Markdown
    }, {
      path: '/time-entries',
      component: TimeEntries,
      children: [{
        path: 'log-time',
        component: LogTime
      }]
    }]
})
