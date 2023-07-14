<template>
  <div>
    <h2>Hoạt động ngoại khóa</h2>
    <hr>

    <div v-if="state==states[0]">
      <div style="top: 100px;display: grid;grid-template-columns: repeat(3,1fr)">
        <temshowPageplate v-for="activty in user_data.extracurricular_activities">
          <a-card @click="showPage(activty)" hoverable style="width: 240px;aspect-ratio: 2">
            <template #cover>
              <img height="300" alt="example" src="/thpt/static/app/img/Anh-meo-cute-dang-yeu-de-thuong.jpg"/>
            </template>
            <a-card-meta :title="activty.title">
              <template #description>{{ activty.description }}</template>
            </a-card-meta>
          </a-card>
        </temshowPageplate>
      </div>
    </div>
    <div v-if="state==states[1]">
      <div style="display:flex;align-items: center; gap: 10px;margin-bottom: 10px">
        <h3 style="margin: 0">{{ selected_card.title }}</h3>
        <div v-if="user_data.role=='student'&&selected_card.participants.includes(user_data.id)"> Đã đăng ký</div>
        <button  v-if="user_data.role=='student'&&!selected_card.participants.includes(user_data.id)" @click="register()"> Đăng ký</button>
      </div>
      <div>
        <div>Thời gian mở đăng ký: {{ selected_card.start_time }}</div>
        <div>Thời gian đóng đăng ký: {{ selected_card.end_time }}</div>
        <div>Đã đăng ký: {{ selected_card.participants.length }}</div>
        <div>Đăng ký tối đa:{{ selected_card.max_participant }}</div>
        <div>Diễn ra trong: {{ selected_card.time }} giờ</div>
        <div>Tại: {{ selected_card.location }}</div>
        <div>Giáo viên phụ trách: {{ selected_card.teacher_in_charge.name }}</div>
        <div>Các giáo viên hỗ trợ:
          {{ selected_card.support_teacher1.name }},{{
            selected_card.support_teacher2.name
          }},{{ selected_card.support_teacher3.name }}
        </div>
        <div style="display: flex; flex-wrap: wrap; font-size: 16px">
          {{ selected_card.content }}
        </div>
        <div>
          <button @click="cancel">Quay lại</button>
        </div>
      </div>
    </div>

  </div>
</template>
<script>
import {defineComponent} from 'vue'

export default defineComponent({
  name: "ExtracurricularActivity",
  props: {
    user_data: Object
  },
  computed: {},
  methods: {
    showPage(arg) {
      console.log('haha')
      console.log(arg)
      this.selected_card = arg
      this.state = this.states[1]
    },
    register() {
      if (this.selected_card.participants) {
        if (this.selected_card.participants.length >= this.selected_card.max_participant) {
          alert('Đã hết lượt đăng ký')
        } else {
          let param = {
            activity_id: this.selected_card.id,
            user_id: this.user_data.id
          }
          this.$emit('register', param)
        }
      } else {
        let param = {
          activity_id: this.selected_card.id,
          user_id: this.user_data.id
        }
        this.$emit('register', param)
      }
    },
    cancel() {
      this.state = this.states[0]
    },
  },
  data() {
    return {
      states: ['collection', ' page detail', 'new_card'],
      state: 'collection',
      selected_card: {},
      new_card: {},
    }
  }
})
</script>

<style scoped>

</style>