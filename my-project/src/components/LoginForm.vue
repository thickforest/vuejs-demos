<template>
  <div class="jumbotron">
    <h1>用户登录</h1>
    <div class="row">
      <div class="col-md-12">
        用户名:<input type="text" class="form-control" v-model="userForm.username" placeholder=""/>
        密码:<input type="password" class="form-control" v-model="userForm.password" placeholder=""/>
      </div>
    </div>
    <button class="btn btn-primary" @click="handleLogin()">加载</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'LoginForm',
  data () {
    return {
      userForm: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    handleLogin () {
      axios({
        method: 'POST',
        url: 'http://192.168.123.33:5000/login',
        data: this.userForm
      }).then((res) => {
        const token = res.data.access_token
        axios({
          method: 'GET',
          url: 'http://192.168.123.33:5000/user/detail'
        }).then((res) => {
          this.$store.commit('saveUserInfo', res.data.data)
        })
        this.$store.commit('saveToken', token)
        this.$router.replace(this.$router.currentRoute.query.redirect)
      })
    }
  }
}
</script>
