<script>
import {defineComponent} from 'vue'
import LearningOutcome from "./LearningOutcome.vue";
import ClassManagement from "./ClassManagement.vue";
import DashBoard from "./DashBoard.vue";
import SideBar from "./SideBar.vue";
import StudentManagement from "./StudentManagement.vue";
import TeacherManagement from "./TeacherManagement.vue";
import NavBar from "./NavBar.vue";
import ExtracurricularActivities from "./ExtracurricularActivities.vue";
import Schedule from "./Schedule.vue";
import axios from "axios";

export default defineComponent({
  name: "StudentHome",
  components: {
    Schedule,
    ExtracurricularActivities,
    NavBar,
    TeacherManagement,
    StudentManagement,
    SideBar,
    DashBoard,
    ClassManagement,
    LearningOutcome
  }, props: {
    user_data: Object
  },
  data() {
    return {
      pages: ['info', 'schedule', 'learning_outcome', 'extracurricular_activities', 'student_management', 'teacher_management', 'class_management'],
      states: ['home', 'news', 'notification'],
      state: 'home',
      is_selected: 'info',
      student_management_temp: {},
      class_management_temp: {},
      teacher_management_temp: {},

    }
  },
  methods: {
    get_select_id(data) {
      this.is_selected = data
      console.log(data)
    },
    changeState(data) {
      this.state = this.states[data]
      console.log(this.states[data])
    },
    addNewStudent(params) {
      let self = this
      console.log('haha')
      axios.post('thpt/add/student', params).then((res) => {
        console.log(res)
        if (res.data.result) {
          alert('Thêm thành công')
          self.student_management_temp.students.push(res.data.result)
          if (self.$refs.student_ref) {
            self.$refs.student_ref.state = self.$refs.student_ref.states[0];
          }
        }
      })
    }

  },
  mounted() {
    console.log(this.user_data)
    let self = this
    axios.get('thpt/get/data').then((res) => {
      console.log(res)
      self.student_management_temp = res.data
      self.class_management_temp = res.data.classes
      self.teacher_management_temp = res.data.teachers
      console.log(self.student_management_temp)
      console.log(self.user_data)
    })
  }
})
</script>

<template>
  <div>
    <NavBar @CustomEventChanged="changeState"></NavBar>
    <div v-if="state==states[0]">
      <div style="display: flex">

        <SideBar :user_data="user_data" :is_selected="is_selected" @CustomEventChanged="get_select_id"/>
        <DashBoard :user_data="user_data" :proptemp="student_management_temp" v-if="is_selected==pages[0]"
                   class="dashboard-container"/>
        <Schedule :user_data="user_data" v-if="is_selected==pages[1]" class="dashboard-container"/>
        <LearningOutcome class="dashboard-container" v-if="is_selected==pages[2]"></LearningOutcome>
        >
        <ExtracurricularActivities class="dashboard-container" v-if="is_selected==pages[3]"/>
      </div>
    </div>
  </div>
</template>

<style scoped>
NavBar {
  z-index: 0;
}

SideBar {
  z-index: 1;
}
</style>