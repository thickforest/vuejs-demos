<template>
  <div class="jumbotron">
    <h1>Markdown编辑</h1>
    <div class="row">
      <div class="col-md-12">
        <mavon-editor :ishljs="true" ref=md v-model="mdContent" @imgAdd="imgAdd" @imgDel="imgDel"></mavon-editor>
      </div>
    </div>
    <button class="btn btn-primary" @click="pushText()">加载</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Users',
  data () {
    return {
      mdContent: ''
    }
  },
  methods: {
    imgAdd (pos, file) {
      console.log('imgAdd:')
      console.log(pos)
      console.log(file)
      var formdata = new FormData()
      formdata.append('filename', file)
      axios({
        method: 'POST',
        url: global.URL_BASE + '/upload',
        data: formdata,
        headers: {'Content-Type': 'multipart/form-data'}
      }).then((res) => {
        console.log(res.data)
        this.$refs.md.img2Url(pos, res.data.data.url)
      })
    },
    imgDel (pos, file) {
      console.log('imgDel:')
      console.log(pos)
      console.log(file)
    }
  }
}
</script>
