<template>
  <div id="app">
    <rtl-layout :userinfo="userinfo"></rtl-layout>    
  </div>
</template>

<script>
import axios from "axios"
import RTLLayout from './components/RTLLayout'
import sem_styles from './assets/css/semantic.min.css'
import panel_styles from './assets/css/panel.css'


export default {
  name: 'Layout',
  inherit: true,
  components: {
      'rtl-layout': RTLLayout
  },
  data() {
    return {
      userinfo: {},
      errors: [],
    }
  },
  async created() {
    try {
      const response = await axios.get(process.env.BASE_URL + 'rs-admin/api/profile/')
      this.userinfo = response.data
    } catch (e) {
      this.errors.push(e)
    }
  }
}
</script>

<style>
#app {
  text-align: right;
  color: #2c3e50;
  height:100%;
}
</style>
