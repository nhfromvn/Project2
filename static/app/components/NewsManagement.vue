<template>
  <div>
    <h2>Hoạt động ngoại khóa</h2>
    <hr>

    <div v-if="state==states[0]">
      <button @click=add()> Thêm</button>
      <div style="top: 100px;display: grid;grid-template-columns: repeat(3,1fr)">
        <temshowPageplate v-for="_news in proptemp.news">
          <a-card @click="showPage(_news)" hoverable style="width: 240px;aspect-ratio: 2">
            <template #cover>
              <img height="300" alt="example" src="/thpt/static/app/img/Anh-meo-cute-dang-yeu-de-thuong.jpg"/>
            </template>
            <a-card-meta :title="_news.title">
              <template #description>{{ _news.description }}</template>
            </a-card-meta>
          </a-card>
        </temshowPageplate>
      </div>
    </div>
    <div v-if="state==states[1]">
      <div style="display:flex;align-items: center; gap: 10px;margin-bottom: 10px">
        <h3 style="margin: 0">{{ selected_card.title }}</h3> <a v-if="!changing" @click="changing=true" style="  text-decoration: underline;
  color: #0A58CA;">Sửa</a>
      </div>
      <div v-if="!changing">

        <div>Thời gian mở : {{ selected_card.start_time }}</div>
        <div>Thời gian đóng : {{ selected_card.end_time }}</div>

        <div style="display: flex; flex-wrap: wrap; font-size: 16px">
          {{ selected_card.content }}
        </div>
        <div>
          <button @click="cancel">Quay lại</button>
        </div>
      </div>
      <div v-else>
        <div>Thời gian mở : <input type="date" v-model="selected_card.start_time"/></div>
        <div>Thời gian đóng : <input type="date" v-model="selected_card.end_time"/></div>
        <div style="display: flex; flex-wrap: wrap; font-size: 16px">
          <textarea style="padding: 10px" v-model="selected_card.content" rows="20" cols="100"></textarea>
        </div>
        <div>
          <button @click="changing=false">Quay lại</button>
          <button @click=save(selected_card)> Lưu</button>
        </div>
      </div>
    </div>
    <div v-if="state==states[2]">
      <div>Tiêu đề: <input type="text" v-model="new_card.title"/></div>
      <div>Mô tả: <input type="text" v-model="new_card.description"/></div>
      <div>Thời gian mở : <input type="date" v-model="new_card.start_time"/></div>
      <div>Thời gian đóng : <input type="date" v-model="new_card.end_time"/></div>
      <div style="display: flex; flex-wrap: wrap; font-size: 16px">
        <textarea style="padding: 10px" v-model="new_card.content" rows="20" cols="100"></textarea>
      </div>
      <div>
        <button @click="state=states[0]">Quay lại</button>
        <button @click=addNewCard()> Lưu</button>
      </div>
    </div>
  </div>
</template>
<script>
import {defineComponent} from 'vue'

export default defineComponent({
  name: "NewsManagement",
  props: {
    proptemp: Object,
  },
  methods: {
    showPage(arg) {
      console.log('haha')
      console.log(arg)
      this.selected_card = arg
      this.state = this.states[1]
    },
    cancel() {
      this.state = this.states[0]
    },
    save() {
      this.$emit('saveNews', this.selected_card)
      this.changing = false
    },
    add() {
      this.state = this.states[2]
      this.new_card = Object.assign({}, this.proptemp.news[0]);
    },
    addNewCard() {
      this.new_card.id = 0
      this.$emit('saveNews', this.new_card)
      window.location.reload()

    }
  },
  data() {
    return {
      states: ['collection', ' page detail', 'new_card'],
      state: 'collection',
      changing: false,
      selected_card: {},
      new_card: {},
    }
  }
})
</script>

<style scoped>

</style>