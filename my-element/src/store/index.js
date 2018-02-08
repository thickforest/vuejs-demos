import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'

Vue.use(Vuex)

const state = {
  users: [],
  user: {
    username: '',
    password: ''
  }
}

const mutations = {
  getUserList () {
    axios({
      method: 'get',
      url: 'http://localhost:5000/user'
    }).then(function (res) {
      console.log(res.data.data)
      state.users = res.data.data
    }).catch(function (res) {
      console.log('Error' + res)
    })
  },
  delUser (state, index) {
    console.log(index)
    axios({
      method: 'delete',
      url: 'http://localhost:5000/user/' + index
    })
  },
  saveUser () {
    axios({
      method: 'post',
      url: 'http://localhost:5000/user',
      data: state.user
    })
  }
}

export default new Vuex.Store({
  state,
  mutations
})
