<template>
  <div id="app">
    <rtl-layout></rtl-layout>    
  </div>
</template>

<script>
import RTLLayout from './components/RTLLayout'

export default {
  name: 'Layout',
  components: {
      'rtl-layout': RTLLayout
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: right;
  color: #2c3e50;
  height:100%;
}
</style>
