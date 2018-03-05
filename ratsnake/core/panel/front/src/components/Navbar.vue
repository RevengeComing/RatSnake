<template>
	<div class="ui top attached menu">
		<!-- <div class="icon item left">
		</div> -->
		<div class="right menu">
			<div class="ui dropdown item icon">
				<span v-if="userinfo.username">{{userinfo.username}}</span>
				<span v-else>کاربر</span>
				<div class="menu">
					<div class="item">
						صفحه کاربری
					</div>
					<div class="item">
						<a href="/rs-admin/logout/">خروج</a>
					</div>
				</div>
			</div>
			<div class="item icon">
				RatSnake CMS
			</div>
		</div>
	</div>
</template>

<script>
import axios from 'axios';
var jQuery = require('../assets/js/jquery.min.js')
var semantic_js = require('../assets/js/semantic.min.js')

export default {
	name: 'Navbar',
	data() {
		return {
			errors: [],
		}
	},
	props: {
		userinfo: Object
	},
	mounted() {
		$('.ui.dropdown').dropdown();
	}
}
</script>