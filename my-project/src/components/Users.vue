<template>
  <div class="jumbotron">
    <h1>用户列表</h1>
    <div class="row">
      <div class="col-md-6">
        <table class="table table-hover">
          <thead>
            <tr>
              <th>#</th>
              <th>用户名</th>
              <th>密码</th>
              <th>年龄</th>
              <th>操作</th>
            </tr>
          </thead>
          <tbody v-for="(user,index) in users" v-bind:key="user.id">
            <tr>
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
      users: []
    }
  },
  methods: {
    getUsers () {
      axios({
        method: 'GET',
        url: 'http://localhost:5000/user'
      }).then((res) => {
        this.users = res.data.data
      })
    },
    delUser (id, index) {
      axios({
        method: 'DELETE',
        url: 'http://localhost:5000/user/' + id
      }).then((res) => {
        this.users.splice(index, 1)
      })
    },
    addUser () {
      axios({
        method: 'POST',
        url: 'http://localhost:5000/user',
        data: this.userForm
      }).then((res) => {
        this.users.push({'id': res.data.data.id, 'username': this.userForm.username, 'password': this.userForm.password, 'age': this.userForm.age})
        this.userForm = { username: '', password: '', age: 30 }
      })
    }
  }
}
</script>
