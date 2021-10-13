<template>
  <div>
    <h1>My app!!!!</h1>
    <button @click="getData">getData</button>
    <h3>request : {{request}}</h3>
    <h3>error : {{error}}</h3>
  </div>
</template>

<script>
import axios from 'axios'


export default {
  name: 'Myapp',
  data: function() {
      return {
          request: '',
          error: []
      }
  },
  methods: {
    getData: function () {
      axios({
        method: 'get',
        url: 'api/myapp/',
      })
        .then(res => {
          console.log(res)   
          this.request = res.data       
        })
        .catch(err => {
        //   console.log(err)
          this.error = err
        })
    }
  }
  
  
}
</script>
<style scoped>

</style>
