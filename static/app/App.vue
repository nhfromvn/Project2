<template>
  <NavBar @CustomEventChanged="changeState"></NavBar>
  <div v-if="state==states[0]">
    <div style="display: flex">
      <SideBar :is_selected="is_selected" @CustomEventChanged="get_select_id"/>
      <DashBoard v-if="is_selected==pages[0]" class="dashboard-container"/>
      <Schedule v-if="is_selected==pages[1]" class="dashboard-container"/>
      <LearningOutcome class="dashboard-container" v-if="is_selected==pages[2]"/>
      <ExtracurricularActivities class="dashboard-container"  v-if="is_selected==pages[3]"/>
    </div>
  </div>


</template>
<script>
import DashBoard from "./components/DashBoard.vue";
import SideBar from "./components/SideBar.vue";
import LogIn from "./components/LogIn.vue";
import NavBar from "./components/NavBar.vue";
import Schedule from "./components/Schedule.vue";
import LearningOutcome from "./components/LearningOutcome.vue";
import ExtracurricularActivities from "./components/ExtracurricularActivities.vue";
export default {
  name: "App",
  components: {ExtracurricularActivities, LearningOutcome, Schedule, NavBar, LogIn, SideBar, DashBoard},
  data() {
    return {
      pages: ['info', 'schedule', 'learning_outcome', 'extracurricular_activities'],
      states: ['home','news', 'notification'],
      state: 'home',
      is_selected: 'info',
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
    }

  },

  mounted() {
    console.log("Hello shopify")
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