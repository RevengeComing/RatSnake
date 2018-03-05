<template>	
  <div class="ui sidebar vertical menu right  visible">
  	<ul>
  		<li class="item">
  			<a href="#/">داشبرد</a>
  		</li>
  		<li class="item">
	  		<a href="#/Users/">کاربران</a>
  		</li>
  	</ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
	name: 'Sidebar',
	data() {
		return {
			items: {},
			errors: ''
		}
	}
}
</script>