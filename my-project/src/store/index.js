import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
  totalTime: 0,
  list: [],
  token: null,
  userInfo: null
}

const mutations = {
  addTotalTime (state, time) {
    state.totalTime = state.totalTime + ~~time
  },
  decTotalTime (state, time) {
    state.totalTime = state.totalTime - time
  },
  savePlan (state, plan) {
    const avatar = 'https://sfault-avatar.b0.upaiyun.com/147/223/147223148-573297d0913c5_huge256'
    state.list.push(
      Object.assign({ name: '二哲', avatar: avatar }, plan)
    )
  },
  deletePlan (state, idx) {
    state.list.splice(idx, 1)
  },
  saveToken (state, _token) {
    state.token = _token
    window.localStorage.setItem('accessToken', _token)
  },
  saveUserInfo (state, _userInfo) {
    state.userInfo = _userInfo
  },
  deleteToken (state) {
    state.token = null
    window.localStorage.setItem('accessToken', '')
    state.userInfo = null
  }
}

export default new Vuex.Store({
  state,
  mutations
})
