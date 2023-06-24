<template>
  <div id="container">
    <div style="display: flex;align-items: center;margin-top: 50px;gap: 10px">
      <img style="width: 40px;height: 40px;border-radius: 50%"
           src="/thpt/static/app/img/Anh-meo-cute-dang-yeu-de-thuong.jpg"/>

      <p>Nguyen Van A</p>
    </div>
    <div id="dashboard" style="display: flex;
                                     gap:5px">

      <div v-if="is_selected==pages[0]" class="frame_427318741 is_select">
        <p>
          Thông tin học sinh</p>
      </div>
      <div v-else class="frame_427318741" @click="onClick(0)">
        <p>
          Thông tin học sinh</p>
      </div>
    </div>

    <div id="integration" style="display: flex;
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

    <div id="meida_source" style="display: flex;
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
    <div id="widgets" style="display: flex;
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
    <div>
       <a href="/web/session/logout?redirect=/web">Đăng xuất</a>
    </div>
  </div>

</template>
<script>
import {defineComponent} from 'vue'

export default defineComponent({
  name: "SideBar",
  data() {
    return {
      pages: ['info', 'schedule', 'learning_outcome', 'extracurricular_activities'],
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