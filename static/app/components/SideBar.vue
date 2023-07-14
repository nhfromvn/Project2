<template>
  <div id="container">
    <div style="display: flex;align-items: center;margin-top: 50px;gap: 10px">
      <img style="width: 40px;height: 40px;border-radius: 50%"
           :src="user_data.image_url"/>

      <p>{{ user_data.name }}</p>
    </div>
    <div style="display: flex;
                                     gap:5px">

      <div v-if="is_selected==pages[0]" class="frame_427318741 is_select">
        <p v-if="user_data.role=='student'">Thông tin học sinh</p>
        <p v-if="user_data.role=='cadre'">Thông tin cán bộ </p>
        <p v-if="user_data.role=='teacher'">Thông tin giáo viên</p>
      </div>
      <div v-else class="frame_427318741" @click="onClick(0)">
        <p v-if="user_data.role=='student'">Thông tin học sinh</p>
        <p v-if="user_data.role=='cadre'">Thông tin cán bộ </p>
        <p v-if="user_data.role=='teacher'">Thông tin giáo viên</p>
      </div>
    </div>

    <div style="display: flex;
                                     gap:5px">
      <div v-if="is_selected==pages[1]" class="frame_427318741 is_select">
        <p>
          Thời khóa biểu</p>
      </div>
      <div v-else class="frame_427318741" @click="onClick(1)">
        <p>
          Thời khóa biểu</p>
      </div>
    </div>

    <div style="display: flex;
                                     gap:5px">
      <div v-if="is_selected==pages[2]" class="frame_427318741 is_select">
        <p>
          Học tập</p>
      </div>
      <div v-else class="frame_427318741" @click="onClick(2)">
        <p>
          Học tập</p>
      </div>
    </div>
    <div style="display: flex;
                                     gap:5px">
      <div v-if="is_selected==pages[3]" class="frame_427318741 is_select">
        <p>
          Hoạt động ngoại khóa</p>
      </div>
      <div v-else class="frame_427318741" @click="onClick(3)">
        <p>
          Hoạt động ngoại khóa</p>
      </div>
    </div>
    <div v-if="user_data.role=='cadre'" style="display: flex;
                                     gap:5px">
      <div v-if="is_selected==pages[4]" class="frame_427318741 is_select">
        <p>
          Quản lý học sinh</p>
      </div>
      <div v-else class="frame_427318741" @click="onClick(4)">
        <p>
          Quản lý học sinh</p>
      </div>
    </div>
    <div v-if="user_data.role=='cadre'" style="display: flex;
                                     gap:5px">
      <div v-if="is_selected==pages[5]" class="frame_427318741 is_select">
        <p>
          Quản lý giáo viên</p>
      </div>
      <div v-else class="frame_427318741" @click="onClick(5)">
        <p>
          Quản lý giáo viên</p>
      </div>
    </div>
    <div v-if="user_data.role=='cadre'||(user_data.role=='teacher'&&user_data.main_teacher)" style="display: flex;
                                     gap:5px">
      <div v-if="is_selected==pages[6]" class="frame_427318741 is_select">
        <p>
          Quản lý lớp học</p>
      </div>
      <div v-else class="frame_427318741" @click="onClick(6)">
        <p>
          Quản lý lớp học</p>
      </div>
    </div>
      <div v-if="user_data.role=='cadre'" style="display: flex;
                                     gap:5px">
      <div v-if="is_selected==pages[7]" class="frame_427318741 is_select">
        <p>
          Quản lý tin tức</p>
      </div>
      <div v-else class="frame_427318741" @click="onClick(7)">
        <p>
          Quản lý tin tức</p>
      </div>
    </div>
    <div>
      <a href="/web/session/logout?redirect=/web">Đăng xuất</a>
    </div>
  </div>

</template>
<script>
import {defineComponent} from 'vue'

export default defineComponent({
  name: "SideBar",
  props: {
    user_data: Object
  },
  data() {
    return {
      pages: ['info', 'schedule', 'learning_outcome', 'extracurricular_activities', 'student_management', 'teacher_management', 'class_management','new_management'],
      is_selected: 'info'
    }
  },
  methods: {
    onClick(id) {
      this.is_selected = this.pages[id]
      this.$emit('CustomEventChanged', this.pages[id])
      console.log(this.is_selected)
    },
  },
  mounted() {

  }
})
</script>

<style scoped>

#container {
  height: 100%;
  width: 220px;
  position: fixed;
  padding: 0px 20px 0px 20px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 32px;
  font-family: Inter;
  top: 60px;
}

.frame_427318741 {
  height: 32px;
  width: 170px;
  text-align: center;
  background: inherit;
  display: flex;
  margin-left: 25px;
  /* Inside auto layout */
  flex: none;
  order: 0;
  flex-grow: 0;
  cursor: pointer;
}

.frame_427318741 p {
  padding: 2.5%;
}

.is_select {
  font-weight: bold;
}

#container {
  border-radius: 0px 50px 50px 0px;
  background: #f3c5c5;
}
</style>