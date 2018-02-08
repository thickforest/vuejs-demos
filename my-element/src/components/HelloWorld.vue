<template>
  <div>
    <el-button @click="getUserList">获取列表</el-button>
    <el-table
      :data="userlist"
      style="width: 100%"
      max-height="500">
      <el-table-column
        prop="username"
        label="用户名"
        width="150">
      </el-table-column>
      <el-table-column
        prop="password"
        label="密码"
        width="150">
      </el-table-column>
      <el-table-column
        label="操作"
        width="120">
        <template slot-scope="scope">
          <el-button
            @click.native.prevent="deleteRow(scope.row.id)"
            type="text"
            size="small">
            移除
          </el-button>
        </template>
      </el-table-column>
    </el-table>

    <el-form ref="form" action="http://localhost:5000/user" :model="form" label-width="80px">
      <el-form-item label="用户名">
        <el-input v-model="form.username"></el-input>
      </el-form-item>
      <el-form-item label="密码">
        <el-input v-model="form.password"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">立即创建</el-button>
        <el-button>取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
    }
  },
  computed: {
    form () {
      return this.$store.state.user
    },
    userlist () {
      return this.$store.state.users
    }
  },
  methods: {
    getUserList () {
      this.$store.commit('getUserList')
    },
    onSubmit () {
      this.$store.commit('saveUser')
    },
    deleteRow (idx) {
      console.log(idx)
      this.$store.commit('delUser', idx)
    }
  }
}
</script>
