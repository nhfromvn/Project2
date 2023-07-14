<template>

  <div>
    <h2 v-if="user_data.role=='student'">Thông tin học sinh</h2>
    <h2 v-if="user_data.role=='cadre'">Thông tin cán bộ </h2>
    <h2 v-if="user_data.role=='teacher'">Thông tin giáo viên</h2>
    <hr>
    <div>
      <img style="height: 200px;width: 200px" :src="user_data.image_url">
    </div>
    <div class="label-form">Thông tin cá nhân</div>
    <div style="display: flex">
      <div style="flex:1">
        <div class="infomation">Họ và tên: {{ user_data.name }}</div>
        <div v-if="user_data.role=='student'" class="infomation">Lớp: {{ user_data._class.name }}</div>
        <div class="infomation">Giới tính: {{ user_data.gender.name }}</div>
        <div class="infomation">Ngày sinh: {{ user_data.dob }}</div>
        <div v-if="user_data.role=='cadre'||user_data.role=='teacher'" class="infomation">Học vấn: {{ user_data.literacy }}</div>
        <div v-if="user_data.role=='teacher'" class="infomation">Bộ môn: {{ user_data.subject }}</div>
        <div v-if="user_data.role=='cadre'" class="infomation">Thời gian làm việc: {{ user_data.working_time }} năm</div>
           <div v-if="user_data.role=='cadre'" class="infomation">Văn phòng: {{ user_data.team_in_charge }}</div>
      </div>
      <div style="flex:1">
        <div class="infomation">Dân tộc: {{ user_data.ethnicity }}</div>
        <div class="infomation">Tôn giáo: {{ user_data.religion }}</div>
        <div class="infomation">Số điện thoại {{ user_data.phone }}</div>
        <div class="infomation"> Địa chỉ: {{ user_data.address }}</div>
      </div>
    </div>
    <template v-if="user_data.role=='student'">
      <div class="label-form">Thông tin gia đình</div>
      <div style="display: flex">
        <div style="flex:1">
          <div class="infomation">
            Họ và tên bố: Hoàng Nam
          </div>
          <div class="infomation">
            Số điện thoại: 0817710104
          </div>
          <div class="infomation">
            Nghề nghiệp: Lập trình viên
          </div>
        </div>
        <div style="flex:1">
          <div class="infomation">
            Họ và tên mẹ: Trần Ngọc Minh
          </div>
          <div class="infomation">
            Số điện thoại: 0817710104
          </div>
          <div class="infomation">
            Nghề nghiệp: Tự do
          </div>
        </div>
      </div>
    </template>
    <div v-if="user_data.role=='student'" style="display: flex;gap: 10px; align-items: center">
      <div class="label-form">Thông tin lớp</div>
      <font-awesome-icon v-if="!show_table" :icon="['fass', 'caret-down']"
                         style="cursor: pointer;z-index: 10;width: 30px;"
                         @click="this.show_table=!this.show_table"/>
      <font-awesome-icon v-else :icon="['fas', 'caret-up']"
                         style="cursor: pointer;z-index: 10;width: 30px;"
                         @click="this.show_table=!this.show_table"/>
    </div>
    <template v-if="show_table&&user_data.role=='student'">
      <div class="infomation"> Danh sách lớp:</div>
      <table class="table table-responsive table-bordered">
        <thead>
        <tr>
          <th>STT</th>
          <th>
            Họ
          </th>
          <th>
            Tên đệm
          </th>
          <th>
            Tên
          </th>
          <th>
            Ngày sinh
          </th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="(student,index) in user_data.list_class_student">
          <td>{{ index + 1 }}</td>
          <td> {{ student.first_name }}</td>
          <td>{{ student.middle_name }}</td>
          <td>{{ student.last_name }}</td>
          <td>{{ student.dob }}</td>
        </tr>
        </tbody>

      </table>
      <div class="infomation">Giáo viên chủ nhiệm: {{ user_data._class.teacher }}</div>
    </template>
  </div>
</template>

<script>
import {defineComponent} from 'vue'

export default defineComponent({
  name: "DashBoard",
  props: {
    proptemp: Object,
    user_data: Object
  },
  data() {
    return {
      show_table: false,
    }

  },
  mounted() {
    console.log(this.user_data)
    if (this.user_data.role == 'student') {
      this.user_data.list_class_student.sort((a, b) => {
        if (a.last_name == b.last_name) {
          return a.first_name.localeCompare(b.first_name)
        }
        return a.last_name.localeCompare(b.last_name)
      })
    }
  }

})
</script>

<style scoped>
.label-form {
  margin: 20px 0px;
  font-weight: bold;
  font-size: 22px;
  font-family: Inter;
}

.infomation {
  font-weight: 400;
  font-size: 19px;
  font-family: Inter;
}
</style>