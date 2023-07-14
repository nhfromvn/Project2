<template>
  <div>
    <h2>Hoạt động ngoại khóa</h2>
    <hr>

    <div v-if="state==states[0]">
      <button @click=add()> Thêm</button>
      <div style="top: 100px;display: grid;grid-template-columns: repeat(3,1fr)">
        <temshowPageplate v-for="activty in proptemp.extracurricular_activities">
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
        <h3 style="margin: 0">{{ selected_card.title }}</h3> <a v-if="!changing" @click="changing=true" style="  text-decoration: underline;
  color: #0A58CA;">Sửa</a>
      </div>
      <div v-if="!changing">

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
      <div v-else>
        <div>Thời gian mở đăng ký: <input type="date" v-model="selected_card.start_time"/></div>
        <div>Thời gian đóng đăng ký: <input type="date" v-model="selected_card.end_time"/></div>
        <div>Đăng ký tối đa: <input type="number" v-model="selected_card.max_participant"/>
        </div>
        <div>Diễn ra trong: <input type="number" v-model="selected_card.time"/> giờ</div>
        <div>Tại: <input type="text" v-model="selected_card.location"/></div>
        <div>Giáo viên phụ trách: <select required v-model="selected_card.teacher_in_charge">
          <option v-for="teacher in list_teacher" :value="teacher">{{ teacher.name }}
          </option>
        </select></div>
        <div>Các giáo viên hỗ trợ:
          <select required v-model="selected_card.support_teacher1">
            <option v-for="teacher in list_teacher" :value="teacher">{{ teacher.name }}
            </option>
          </select>,<select required v-model="selected_card.support_teacher2">
            <option v-for="teacher in list_teacher" :value="teacher">{{ teacher.name }}
            </option>
          </select>,<select required v-model="selected_card.support_teacher3">
            <option v-for="teacher in list_teacher" :value="teacher">{{ teacher.name }}
            </option>
          </select>
        </div>
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
      <div>Thời gian mở đăng ký: <input type="date" v-model="new_card.start_time"/></div>
      <div>Thời gian đóng đăng ký: <input type="date" v-model="new_card.end_time"/></div>
      <div>Đăng ký tối đa: <input type="number" v-model="new_card.max_participant"/>
      </div>
      <div>Diễn ra trong: <input type="number" v-model="new_card.time"/> giờ</div>
      <div>Tại: <input type="text" v-model="new_card.location"/></div>
      <div>Giáo viên phụ trách: <select required v-model="new_card.teacher_in_charge">
        <option v-for="teacher in list_teacher" :value="teacher">{{ teacher.name }}
        </option>
      </select></div>
      <div>Các giáo viên hỗ trợ:
        <select required v-model="new_card.support_teacher1">
          <option v-for="teacher in list_teacher" :value="teacher">{{ teacher.name }}
          </option>
        </select>,<select required v-model="new_card.support_teacher2">
          <option v-for="teacher in list_teacher" :value="teacher">{{ teacher.name }}
          </option>
        </select>,<select required v-model="new_card.support_teacher3">
          <option v-for="teacher in list_teacher" :value="teacher">{{ teacher.name }}
          </option>
        </select>
      </div>
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
  name: "ExtracurricularActivities",
  props: {
    proptemp: Object,
    user_data: Object
  },
  computed: {
    list_teacher() {
      return this.proptemp.teachers.map(function (e) {
        return {
          id: e.id,
          name: e.first_name + ' ' + e.middle_name + ' ' + e.last_name
        }
      })
    }
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
      this.$emit('saveActivity', this.selected_card)
      this.changing = false
    },
    add() {
      this.state = this.states[2]
      this.new_card = Object.assign({}, this.proptemp.extracurricular_activities[0]);
    },
    addNewCard() {
      this.new_card.id = 0
      this.$emit('saveActivity', this.new_card)
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