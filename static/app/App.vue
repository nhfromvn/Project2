<template>

  <CadreHome v-if="role=='cadre'" :user_data="cadre_data"/>
  <StudentHome v-if="role=='student'" :user_data="cadre_data"/>
  <TeacherHome v-if="role=='teacher'" :user_data="cadre_data"/>

</template>
<script>
import CadreHome from "./components/CadreHome.vue";
import axios from 'axios'
import StudentHome from "./components/StudentHome.vue";
import TeacherHome from "./components/TeacherHome.vue";

export default {
  name: "App",
  components: {TeacherHome, StudentHome, CadreHome},
  data() {
    return {
      role: '',
      cadre_data: {}
    }
  },
  mounted() {
    this.cadre_data = window.user_data
    this.role = window.user_data.role
    console.log(this.role)
    console.log(this.cadre_data)
  }

}

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