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
import HomeroomClass from "./HomeroomClass.vue";
import SubjectManagement from "./SubjectManagement.vue";
import LearningManagement from "./LearningManagement.vue";
import ExtracurricularActivity from "./ExtracurricularActivity.vue";

export default defineComponent({
  name: "TeacherHome",
  components: {
    ExtracurricularActivity,
    LearningManagement,
    SubjectManagement,
    HomeroomClass,
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
    changeLearning(params) {
      let self = this
      console.log(params)
      axios.post('/thpt/save/subject', {subjects: params}).then((res) => {
        console.log(res)
        if (res.data.result) {
          alert('Sửa thành công')
        }
      })
    },
    changeState(data) {
      this.state = this.states[data]
      console.log(this.states[data])
    },
    changeSemester(params) {
      axios.post('/thpt/save/outcome', {outcomes: params}).then((res) => {
        console.log(res)
        if (res.data.result) {
          alert('Sửa thành công')
        }
      })
    }
  },
  mounted() {
    console.log(this.user_data)
  }
})
</script>

<template>
  <div>
    <NavBar @CustomEventChanged="changeState"></NavBar>
    <div v-if="state==states[0]">
      <div style="display: flex">

        <SideBar :user_data="user_data" :is_selected="is_selected" @CustomEventChanged="get_select_id"/>
        <DashBoard :user_data="user_data" v-if="is_selected==pages[0]"
                   class="dashboard-container"/>
        <Schedule :user_data="user_data" v-if="is_selected==pages[1]" class="dashboard-container"/>
        <SubjectManagement ref="learning_ref" @changeLearning="changeLearning" :user_data="user_data"
                           class="dashboard-container"
                           v-if="is_selected==pages[2]"></SubjectManagement>
        <ExtracurricularActivity :user_data="user_data" class="dashboard-container" v-if="is_selected==pages[3]"/>
        <HomeroomClass :user_data="user_data" @changeSemester="changeSemester" class="dashboard-container"
                       v-if="is_selected==pages[6]"/>

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