<template>
  <NavBar @CustomEventChanged="changeState"></NavBar>
  <div v-if="state==states[0]">
    <div style="display: flex">

      <SideBar :user_data="user_data" :is_selected="is_selected" @CustomEventChanged="get_select_id"/>
      <DashBoard :user_data="user_data" :proptemp="management_temp" v-if="is_selected==pages[0]"
                 class="dashboard-container"/>
      <ScheduleManagement ref="schedule_ref" :proptemp="management_temp" v-if="is_selected==pages[1]"
                          class="dashboard-container"
                          @changeSchedule="changeSchedule"/>
      <LearningManagement :proptemp="management_temp" ref="learning_ref" @changeLearning="changeLearning"
                          class="dashboard-container" v-if="is_selected==pages[2]"/>
      <ExtracurricularActivities :user_data="user_data" :proptemp="management_temp" @saveActivity="saveActivity"
                                 class="dashboard-container"
                                 v-if="is_selected==pages[3]"/>
      <StudentManagement ref="student_ref" :proptemp="management_temp" class="dashboard-container"
                         @addNewStudent="addNewStudent"
                         @changeStudent="changeStudent"
                         v-if="is_selected==pages[4]"/>
      <TeacherManagement ref="teacher_ref" :proptemp="management_temp" class="dashboard-container"
                         v-if="is_selected==pages[5]"
                         @addNewTeacher="addNewTeacher"
                         @changeTeacher="changeTeacher"/>
      <ClassManagement ref="class_ref" :proptemp="management_temp" class="dashboard-container"
                       v-if="is_selected==pages[6]"
                       @addNewClass="addNewClass"
                       @changeClass="changeClass"/>
      <NewsManagement :proptemp="management_temp" class="dashboard-container"
                      v-if="is_selected==pages[7]"
                      @saveNews="saveNews"></NewsManagement>
    </div>
  </div>


</template>
<script>
import {defineComponent} from 'vue'
import ExtracurricularActivities from "./ExtracurricularActivities.vue";
import NavBar from "./NavBar.vue";
import LearningOutcome from "./LearningOutcome.vue";
import Schedule from "./Schedule.vue";
import DashBoard from "./DashBoard.vue";
import SideBar from "./SideBar.vue";
import LogIn from "./LogIn.vue";
import StudentManagement from "./StudentManagement.vue";
import TeacherManagement from "./TeacherManagement.vue";
import axios from 'axios'
import ClassManagement from "./ClassManagement.vue";
import ScheduleManagement from "./ScheduleManagement.vue";
import LearningManagement from "./LearningManagement.vue";
import NewsManagement from "./NewsManagement.vue";

export default defineComponent({
      name: "CadreHome",
      components: {
        NewsManagement,
        LearningManagement,
        ScheduleManagement,
        ClassManagement,
        TeacherManagement,
        StudentManagement,
        ExtracurricularActivities, LearningOutcome, Schedule, NavBar, LogIn, SideBar, DashBoard
      },
      props: {
        user_data: Object
      },
      data() {
        return {
          pages: ['info', 'schedule', 'learning_outcome', 'extracurricular_activities', 'student_management', 'teacher_management', 'class_management', 'new_management'],
          states: ['home', 'news', 'notification'],
          state: 'home',
          is_selected: 'info',
          management_temp: {},
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
          axios.post('/thpt/add/student', params).then((res) => {
            console.log(res)
            if (res.data.result) {
              alert('Thêm thành công')
              self.management_temp.students.push(res.data.result)
              if (self.$refs.student_ref) {
                self.$refs.student_ref.state = self.$refs.student_ref.states[0];
                self.$refs.student_ref.proptemp.students.sort((a, b) => {
                  if (a.last_name == b.last_name) {
                    return a.first_name.localeCompare(b.first_name)
                  }
                  return a.last_name.localeCompare(b.last_name)
                })
              }
            }
          })
        },
        changeStudent(params) {
          let self = this
          console.log(params)
          axios.post('/thpt/save/student', params).then((res) => {
            console.log(res)
            if (res.data.result) {
              alert('Sửa thành công')
              if (self.$refs.student_ref) {
                self.$refs.student_ref.changing = false
                self.$refs.student_ref.proptemp.students.sort((a, b) => {
                  if (a.last_name == b.last_name) {
                    return a.first_name.localeCompare(b.first_name)
                  }
                  return a.last_name.localeCompare(b.last_name)
                })

              }
            }
          })
        },
        changeSchedule(params) {
          let self = this
          console.log(params)
          axios.post('/thpt/save/schedule', {schedules: params}).then((res) => {
            console.log(res)
            if (res.data.result) {
              alert('Sửa thành công')
            }
          })
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
        addNewTeacher(params) {
          let self = this
          console.log('haha')
          axios.post('/thpt/add/teacher', params).then((res) => {
            console.log(res)
            if (res.data.result) {
              alert('Thêm thành công')
              self.management_temp.teachers.push(res.data.result)
              if (self.$refs.teacher_ref) {
                self.$refs.teacher_ref.state = self.$refs.teacher_ref.states[0];
                self.$refs.teacher.proptemp.teachers.sort((a, b) => {
                  if (a.last_name == b.last_name) {
                    return a.first_name.localeCompare(b.first_name)
                  }
                  return a.last_name.localeCompare(b.last_name)
                })
              }
            }
          })
        },
        changeTeacher(params) {
          let self = this
          console.log(params)
          axios.post('/thpt/save/teacher', params).then((res) => {
            console.log(res)
            if (res.data.result) {
              alert('Sửa thành công')
              if (self.$refs.teacher_ref) {
                self.$refs.teacher_ref.changing = false
                self.$refs.teacher_ref.proptemp.teachers.sort((a, b) => {
                  if (a.last_name == b.last_name) {
                    return a.first_name.localeCompare(b.first_name)
                  }
                  return a.last_name.localeCompare(b.last_name)
                })

              }
            }
          })
        },
        addNewClass(params) {
          let self = this
          console.log('haha')
          axios.post('/thpt/add/class', params).then((res) => {
            console.log(res)
            if (res.data.result) {
              alert('Thêm thành công')
              self.management_temp.classes.push(res.data.result)
              if (self.$refs.class_ref) {
                self.$refs.class_ref.state = self.$refs.class_ref.states[0];
                self.$refs.class_ref.proptemp.classes.sort((a, b) => {
                  return a.name.localeCompare(b.name)
                })
              }
            }
          })
        },
        changeClass(params) {
          let self = this
          console.log(params)
          axios.post('/thpt/save/class', params).then((res) => {
            console.log(res)
            if (res.data.result) {
              alert('Sửa thành công')
              if (self.$refs.class_ref) {
                self.$refs.class_ref.changing = false
                self.$refs.class_ref.proptemp.classes.sort((a, b) => {

                  return a.name.localeCompare(b.name)
                })
              }
            }
          })
        },
        saveActivity(param) {
          console.log('haha')
          axios.post('thpt/save/activity', param).then((res) => {
            console.log(res)
            if (res.data.result) {
              alert('lưu thành công')
            }
          })
        },
        saveNews(param) {
          console.log('haha')
          axios.post('thpt/save/news', param).then((res) => {
            console.log(res)
            if (res.data.result) {
              alert('lưu thành công')
            }
          })
        },
      },
      mounted() {
        console.log(this.user_data)
        let self = this
        axios.get('/thpt/get/data').then((res) => {
          console.log(res)
          self.management_temp = res.data
          console.log(self.student_management_temp)
          console.log(self.user_data)
        })
      }
    }
)
</script>
<style>


body {

}

NavBar {
  z-index: 0;
}

SideBar {
  z-index: 1;
}

</style>