<template>
  <div id="wrapper">
    <nav class="navbar navbar-default" role="navigation">
      <div class="container-fluid">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar-collapse-id">
            <span class="sr-only">切换导航</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">
            <i class="glyphicon glyphicon-time"></i>
            计划板
          </a>
        </div>
        <div class="collapse navbar-collapse" id="navbar-collapse-id">
          <ul class="nav navbar-nav">
            <li><router-link to="/">首页</router-link></li>
            <li><router-link to="/time-entries">计划列表</router-link></li>
            <li><router-link to="/users">用户列表 </router-link></li>
            <li><router-link to="/markdown">Markdown</router-link></li>
            <li v-if="userInfo == null"><router-link to="/loginForm">LoginForm</router-link></li>
            <li v-if="userInfo != null"><router-link to="/">{{ userInfo.username }}</router-link></li>
          </ul>
        </div>
      </div>
    </nav>
    <div class="container">
      <div class="col-sm-3">
        <SideBar></SideBar>
      </div>
      <div class="col-sm-9">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
import SideBar from './components/Sidebar.vue'
export default {
  name: 'app',
  components: {
    SideBar
  },
  computed: {
    userInfo () {
      return this.$store.state.userInfo
    }
  }
}
</script>
