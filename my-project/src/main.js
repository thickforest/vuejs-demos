// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import axios from 'axios'

import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'

Vue.use(mavonEditor)

Vue.config.productionTip = false

global.HOST = '192.168.123.33'
global.PORT = 5000
global.URL_BASE = 'http://' + global.HOST + ':' + global.PORT

axios.interceptors.request.use(function (config) {
  console.log('axios.interceptors.request:')
  console.log(config)
  if (store.state.token != null) {
    config.headers.Authorization = 'jwt ' + store.state.token
  }
  return config
}, function (error) {
  return Promise.reject(error)
})

axios.interceptors.response.use(function (response) {
  return response
}, function (error) {
  console.log('axios.interceptors.error:')
  console.log(error)
  if (error.response.status === 401) {
    store.commit('deleteToken')
    router.replace({
      path: '/loginForm',
      query: {redirect: router.currentRoute.fullPath}
    })
  }
  return Promise.reject(error)
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
