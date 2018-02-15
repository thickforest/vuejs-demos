<template>
  <div class="jumbotron">
    <h1>用户列表</h1>
    <div class="row">
      <div class="col-md-12">
        <table class="table table-hover">
          <thead>
            <tr>
              <th>#</th>
              <th>头像</th>
              <th>用户名</th>
              <th>密码</th>
              <th>年龄</th>
              <th>操作</th>
            </tr>
          </thead>
          <tbody v-for="(user,index) in users" v-bind:key="user.id">
            <tr>
              <td></td>
              <td>{{ user.id }}</td>
              <td>{{ user.username }}</td>
              <td>{{ user.password }}</td>
              <td>{{ user.age }}</td>
              <td><button class="btn btn-primary" @click="delUser(user.id, index)">删除</button></td>
            </tr>
          </tbody>
          <tbody>
            <tr>
              <td>#</td>
              <td>
                <label for="avatarId" class="btn btn-default">更换头像</label>
                <input id="avatarId" type="file" style="display:none" @change="avatarChange" ref="avatar" placeholder=""/>
                <img :src="avatarLocalURL" class="img-circle img-responsive" />
                <label v-if="avatarFile!=null">{{ avatarFile.name }} {{ avatarFile.size}}</label>
              </td>
              <td><input type="text" class="form-control" v-model="userForm.username" placeholder=""/></td>
              <td><input type="password" class="form-control" v-model="userForm.password" placeholder=""/></td>
              <td><input type="number" class="form-control" v-model="userForm.age" placeholder=""/></td>
              <td><button class="btn btn-primary" @click="addUser()">新增</button></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <button class="btn btn-primary" @click="getUsers()">加载</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Users',
  data () {
    return {
      userForm: {
        username: '',
        password: '',
        age: 30
      },
      avatarFile: null,
      avatarLocalURL: 'http://sfault-avatar.b0.upaiyun.com/147/223/147223148-573297d0913c5_huge256',
      users: []
    }
  },
  methods: {
    getUsers () {
      axios({
        method: 'GET',
        url: global.URL_BASE + '/user'
      }).then((res) => {
        this.users = res.data.data
      })
    },
    delUser (id, index) {
      axios({
        method: 'DELETE',
        url: global.URL_BASE + '/user/' + id
      }).then((res) => {
        this.users.splice(index, 1)
      })
    },
    addUser () {
      axios({
        method: 'POST',
        url: global.URL_BASE + '/user',
        data: this.userForm
      }).then((res) => {
        this.users.push({'id': res.data.data.id, 'username': this.userForm.username, 'password': this.userForm.password, 'age': this.userForm.age})
        this.userForm = { username: '', password: '', age: 30 }
      })
    },
    avatarChange () {
      this.avatarFile = this.$refs.avatar.files[0]
      console.log(this.avatarFile)
      if (typeof FileReader === 'undefined') {
        alert('FileReader not support!!!')
        return
      }
      this.avatarLocalURL = window.URL.createObjectURL(this.avatarFile) // blob:http://192.168.123.33:8080/0eeb05fb-2389-433e-b63b-39bf64673218
      var reader = new FileReader()
      reader.onload = function (e) {
        // this.avatarLocalURL = e.target.result // data:image/jpeg;base64,xxxxxxxxxxx
        // console.log(e)
      }
      reader.readAsDataURL(this.avatarFile)
    }
  }
}
</script>
