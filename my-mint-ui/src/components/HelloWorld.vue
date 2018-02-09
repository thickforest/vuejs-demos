<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <mt-button type="primary" @click="pop_toast"> 选择操作 </mt-button>
    <mt-button type="primary" @click="pop_indicator"> 加载 </mt-button>
    <mt-button type="primary" @click="alert"> Alert </mt-button>
    <mt-cell title="标题文字" value="说明文字"/>
    <mt-field label="用户名" placeholder="请输入用户名" v-model="username"></mt-field>
    <mt-field label="密码" placeholder="请输入密码" type='password' v-model="password"></mt-field>
    <mt-field label="邮箱" placeholder="请输入邮箱" type='email' state='error' v-model="email"></mt-field>
    <mt-field label="日期" placeholder="请输入日期" type='date' v-model="form_date"></mt-field>
    <mt-field label="文件" placeholder="请选择文件" type='file' v-model="filename"></mt-field>
    <mt-switch v-model="value">开关</mt-switch>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      value: true,
      username: 'forest',
      password: 'xxx',
      email: '',
      form_date: '',
      filename: ''
    }
  },
  methods: {
    pop_toast: function () {
      this.$toast({
        message: 'hello, world!!',
        iconClass: 'icon icon-success'
      })
    },
    pop_indicator: function () {
      this.$indicator.open({
        text: 'hello',
        spinnerType: 'fading-circle'
      })
    },
    alert: function () {
      this.$messagebox.confirm('确定？').then(action => {
        console.log('确定' + action)
      }).catch(action => {
        console.log('取消' + action)
      })
    }
  }
}
</script>
