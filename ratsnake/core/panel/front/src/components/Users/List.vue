<template>
	<div>
		<h1>کاربران</h1>
		<table class="ui single line table">
			<thead>
		    <tr>
		      <th>نام کاربری</th>
		      <th>نام</th>
		      <th>نام خانوادگی</th>
		      <th>آدرس ایمیل</th>
		      <th>مدیریت ؟</th>
		      <th>کارمند ؟</th>
		      <th>گروه</th>
		    </tr>			
			</thead>
			<tbody>
		    <tr v-for="data in table_datas">
		      <td>{{data.username}}</td>
		      <td>{{data.first_name}}</td>
		      <td>{{data.last_name}}</td>
		      <td>{{data.email}}</td>
		      <td v-if="data.is_admin">بله</td>
		      <td v-else>خیر</td>
		      <td v-if="data.is_staff">بله</td>
		      <td v-else>خیر</td>
		      <td>{{data.group}}</td>
		    </tr>			
			</tbody>
		</table>
	</div>
</template>

<script>
import axios from "axios"

export default {
	name: "UsersList",
	data() {
		return {
			table_datas: [],
			errors: []
		}
	},
	async created() {		
    try {
      const response = await axios.get(process.env.BASE_URL + 'rs-admin/api/users/')
      this.table_datas = response.data
      console.log(this.table_datas)
    } catch (e) {
      console.log(e)
    }
	}
}
</script>