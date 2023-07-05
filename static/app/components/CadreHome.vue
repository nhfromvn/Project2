<template>
  <NavBar @CustomEventChanged="changeState"></NavBar>
  <div v-if="state==states[0]">
    <div style="display: flex">

      <SideBar :user_data="user_data" :is_selected="is_selected" @CustomEventChanged="get_select_id"/>
      <DashBoard :user_data="user_data" :proptemp="management_temp" v-if="is_selected==pages[0]"
                 class="dashboard-container"/>
      <ScheduleManagement ref="schedule_ref" :proptemp="management_temp" v-if="is_selected==pages[1]"
                          class="dashboard-container"
                          @addNewSchedule="addNewSchedule"
                          @changeSchedule="changeSchedule"/>
      <LearningOutcome class="dashboard-container" v-if="is_selected==pages[2]"></LearningOutcome>
      <ExtracurricularActivities class="dashboard-container" v-if="is_selected==pages[3]"/>
      <StudentManagement ref="student_ref" :proptemp="management_temp" class="dashboard-container"
                         @addNewStudent="addNewStudent"
                         @changeStudent="changeStudent"
                         v-if="is_selected==pages[4]"/>
      <TeacherManagement ref="teacher_ref" :proptemp="management_temp" class="dashboard-container"
                         v-if="is_selected==pages[5]"
                         @addNewTeacher="addNewTeacher"
                         @changeTeacher="changeTeacher"/>
      />
      <ClassManagement :proptemp="management_temp" class="dashboard-container" v-if="is_selected==pages[6]"/>
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

export default defineComponent({
      name: "CadreHome",
      components: {
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
          pages: ['info', 'schedule', 'learning_outcome', 'extracurricular_activities', 'student_management', 'teacher_management', 'class_management'],
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
        addNewSchedule(params) {
          let self = this
          console.log('haha')
          axios.post('/thpt/add/schedule', params).then((res) => {
            console.log(res)
            if (res.data.result) {
              alert('Thêm thành công')
              self.management_temp.schedules.push(res.data.result)
              if (self.$refs.schedule_ref) {
                self.$refs.schedule_ref.state = self.$refs.schedule_ref.states[0];
                self.$refs.schedule_ref.proptemp.schedules.sort((a, b) => {
                  if (a._class.name == b._class.name) {
                    if (a.date_of_week == b.date_of_week) {
                      return a.class_time - b.class_time
                    }
                    return a.date_of_week - b.date_of_week
                  }
                  return a._class.name.localeCompare(b._class.name)
                })
              }
            }
          })
        },
        changeSchedule(params) {
          let self = this
          console.log(params)
          axios.post('/thpt/save/schedule', params).then((res) => {
            console.log(res)
            if (res.data.result) {
              alert('Sửa thành công')
              if (self.$refs.schedule_ref) {
                self.$refs.schedule_ref.changing = false
                self.$refs.schedule_ref.proptemp.schedules.sort((a, b) => {
                  if (a._class.name == b._class.name) {
                    if (a.date_of_week == b.date_of_week) {
                      return a.class_time - b.class_time
                    }
                    return a.date_of_week - b.date_of_week
                  }
                  return a._class.name.localeCompare(b._class.name)
                })
              }
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