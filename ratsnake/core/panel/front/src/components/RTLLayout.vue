<template>
	<div class="rtl_layout">
		<navbar :userinfo="userinfo"></navbar>
		<div class="pushable">
			<sidebar></sidebar>
		  <div class="pusher">
		  	<div dir="rtl" class="ui container p-container">
			  	<router-view/>
		  	</div>
		  </div>
	  </div>
	</div>
</template>

<script>
// import axios from 'axios';
import Navbar from './Navbar'
import Sidebar from './Sidebar'

export default {
  name: 'RTLLayout',  
  components: {
      'sidebar': Sidebar,
      'navbar': Navbar
  },
  props: {
  	userinfo: Object
  }
}
</script>

<style scoped>
.ui.menu {
	margin-bottom:0px;
}
.pusher {
	margin-left:260px;
}
.pushable {
	height: 100%;
}
.rtl_layout {
	height:100%;
}
.p-container {
	padding-top:20px;
}
</style>