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
    <img :src="files.length ? files[0].url : 'https://www.gravatar.com/avatar/default?s=200&r=pg&d=mm'"/>
    <file-upload
       extensions="gif,jpg,jpeg,png,webp"
       accept="image/png,image/gif,image/jpeg,image/webp"
       name="avatar"
       v-model="files"
       @input-filter="inputFilter"
       @input-file="inputFile"
       ref="upload">
       Upload avatar
    </file-upload>
    <mt-switch v-model="value">开关</mt-switch>
  </div>
</template>

<script>
import FileUpload from 'vue-upload-component'
import { Indicator } from 'mint-ui'
import axios from 'axios'
export default {
  name: 'HelloWorld',
  components: {
    FileUpload
  },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      value: true,
      username: 'forest',
      password: 'xxx',
      email: '',
      form_date: '',
      files: []
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
      Indicator.open({
        text: 'hello',
        spinnerType: 'fading-circle'
      })
      axios({
        method: 'post',
        url: 'http://localhost:5000/user',
        data: {
          username: this.username,
          password: this.password
        }
      }).then(function (res) {
        Indicator.close()
      })
    },
    alert: function () {
      this.$messagebox.confirm('确定？').then(action => {
        console.log('确定' + action)
      }).catch(action => {
        console.log('取消' + action)
      })
    },
    inputFile (newFile, oldFile, prevent) {
    },
    inputFilter (newFile, oldFile, prevent) {
      if (newFile && !oldFile) {
        // Before adding a file
        // 添加文件前
        // Filter system files or hide files
        // 过滤系统文件 和隐藏文件
        if (/(\/|^)(Thumbs\.db|desktop\.ini|\..+)$/.test(newFile.name)) {
          return prevent()
        }
        // Filter php html js file
        // 过滤 php html js 文件
        if (/\.(php5?|html?|jsx?)$/i.test(newFile.name)) {
          return prevent()
        }
        newFile.url = ''
        let URL = window.URL || window.webkitURL
        if (URL && URL.createObjectURL) {
          newFile.url = URL.createObjectURL(newFile.file)
          newFile.data = newFile.file
        }
      }
    }
  }
}
</script>
