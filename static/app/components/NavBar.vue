<template>
  <div style="  position: fixed;display: flex;gap: 20px; padding: 20px; z-index: 100;width: 100%;background: #FFFFFF">
    <div @click="onClick(0)" class="navItem">
      Trang chu
    </div>
    <div @click="onClick(1)" class="navItem">
      Tin tuc
    </div>
    <div @click="onClick(2)" class="navItem">
      Thong bao
    </div>
  </div>
</template>
<script>
import {defineComponent} from 'vue'

export default defineComponent({
  name: "NavBar",
  data() {
    return {
      state_id: 0
    }
  },
  methods: {

    onClick(id) {
      this.state_id = id
      this.$emit('CustomEventChanged', this.state_id)
    },
  }
})
</script>


<style scoped>
.navBar {

}

.navItem {
  width: 100px;
  cursor: pointer;
}
</style>