<template>
	<div class="rtl_layout">
		<div class="ui top attached menu">
			<div class="ui dropdown icon item">
				test
			</div>
		</div>
		<div class="pushable">
		  <div class="ui sidebar vertical menu right  visible">
		    <a class="item">
		      1
		    </a>
		    <a class="item">
		      2
		    </a>
		    <a class="item">
		      3
		    </a>
		  </div>

		  <div class="pusher">
		  	<div class="ui container">
			  	<router-view/>
		  	</div>
		  </div>
	  </div>
	</div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'RTLLayout',
  async created() {
    try {
      const response = await axios.get(`http://localhost:5000/rs-admin/api/sidebar-links/`)
      this.posts = response.data
    } catch (e) {
      this.errors.push(e)
    }
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
</style>