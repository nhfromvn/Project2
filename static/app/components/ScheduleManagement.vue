<script>
import {defineComponent} from 'vue'

export default defineComponent({
  name: "ScheduleManagement",
  props: {
    proptemp: Object
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
  data() {
    return {

      semester: 1,
      state: 'dashboard',
      states: ['dashboard', 'add', 'show'],
      changing: false,
      subjects: ['Toán', 'Vật lí', 'Hóa học', 'Sinh học', 'Văn', 'Lịch sử', 'Địa lí', 'Giáo dục công dân', 'Công nghệ', 'Tin học', 'Thể dục'],
      selected_schedule: {},
      new_schedule: {
        class_time: 1,
        class: {
          id: null,
          name: null,
          teacher: null,
          size: null
        },
        subject: 'Toán',
        teacher: {
          id: null,
          name: '',
        },
        date_of_week: 2,
        semester: 1,
        classroom: '',
      }
    }
  },
  methods: {
    saveChange(schedule) {
      if (!this.changing) {
        alert('Không có gì để lưu')
      } else {

        this.$emit('changeSchedule', schedule)
      }

    },
    changeStudent() {
      console.log(this.changing)
      this.changing = true
    },
    cancel() {

      if (this.changing) {
        this.changing = false
      } else {
        this.state = this.states[0];
      }
    },
    formStudent() {
      this.state = this.states[1]
    },
    add() {
      if (!this.new_schedule._class || !this.new_schedule.date_of_week || !this.new_schedule.class_time ||
          !this.new_schedule.semester || !this.new_schedule.subject || !this.new_schedule.teacher || !this.new_schedule.classroom) {
        alert('Chưa điền đủ thông tin bắt buộc')
      } else {
        this.$emit('addNewSchedule', this.new_schedule)
      }
    },
    show(schedule) {
      this.selected_schedule = schedule
      this.state = this.states[2]
    }
  },
  mounted() {
    this.test = window
    this.proptemp.schedules.sort((a, b) => {
      if (a._class.name == b._class.name) {
        if (a.date_of_week == b.date_of_week) {
          return a.class_time - b.class_time
        }
        return a.date_of_week - b.date_of_week
      }
      return a._class.name.localeCompare(b._class.name)
    })
  }
})
</script>
<template>
  <div>
    <h2>
      Quản lý thời khóa biểu
    </h2>
    <hr>
    <div v-if="state==states[0]">
      <div style="display: flex;gap: 15px">
        <div>Học kỳ :</div>
        <select v-model="semester">
          <option v-for="i in [1,2]" :value="i">
            {{ i }}
          </option>
        </select>
      </div>
      <h3>Danh sách </h3>
      <table class="table table-responsive table-bordered">
        <thead>
        <tr>
          <th>
            Lớp
          </th>
          <th>
            Thứ
          </th>
          <th>
            Tiết
          </th>
          <th>
            Môn
          </th>
          <th>
            Giáo viên
          </th>
          <th>
            Phòng học
          </th>
        </tr>

        </thead>
        <tbody>
        <template v-for="schedule in proptemp.schedules">
          <tr v-if="schedule.semester==semester">
            <td>{{ schedule._class.name }}</td>
            <td>{{ schedule.date_of_week }}</td>
            <td>{{ schedule.class_time }}</td>
            <td>{{ schedule.subject }}</td>
            <td>{{ schedule.teacher.name }}</td>
            <td>{{ schedule.classroom }}</td>
            <td style="display: flex; gap: 15px">
              <a @click="show(schedule)" style="    text-decoration: underline;
    color: #0A58CA;"> Chi tiết</a>
            </td>
          </tr>
        </template>

        </tbody>
      </table>
      <div style="justify-content: flex-end; display: flex">
        <button style="width: 300px; height: 40px" @click="formStudent">Thêm tiết học</button>
      </div>
    </div>
    <div v-if="state==states[1]">
      <h3>Thêm tiết học</h3>
      <div style="display: flex; gap: 15px; justify-content: end">
        <button @click="add">Thêm</button>
        <button @click="cancel">Quay lại</button>
      </div>
      <div style="display: flex">
        <div>
          <div class="input_form">
            <label>
              Lớp
            </label>
            <select required v-model="new_schedule._class">
              <option v-for="_class in proptemp.classes" :value="_class">{{ _class.name }}
              </option>
            </select>
          </div>
          <div class="input_form">
            <label>
              Thứ
            </label>
            <input type="number" min="2" max="7" v-model="new_schedule.date_of_week"/>
          </div>
          <div class="input_form">
            <label>
              Tiết
            </label>
            <input type="number" min="1" max="5" v-model="new_schedule.class_time"/>
          </div>
          <div class="input_form">
            <label>
              kỳ học
            </label>
            <input type="number" min="1" max="2" v-model="new_schedule.semester"/>
          </div>
        </div>
        <div>
          <div class="input_form">
            <label>
              Môn
            </label>
            <select v-model="new_schedule.subject">
              <option v-for="subject in subjects">{{ subject }}</option>
            </select>

          </div>
          <div class="input_form">
            <label>
              Giáo viên
            </label>
            <select required v-model="new_schedule.teacher">
              <option v-for="teacher in list_teacher" :value="teacher">{{ teacher.name }}
              </option>
            </select>
          </div>
          <div class="input_form">
            <label>
              Phòng học
            </label>
            <input type="text" v-model="new_schedule.classroom "/>
          </div>
        </div>
      </div>
    </div>
    <div v-if="state==states[2]">
      <div style="display:flex;align-items: center; gap: 10px;margin-bottom: 10px">
        <h3 style="margin: 0">Quản lý tiết học</h3> <a v-if="!changing" @click="changeStudent" style="  text-decoration: underline;
  color: #0A58CA;">Sửa</a>
      </div>
      <div v-if="!changing" style="display: flex">
        <div style="flex:1">
          <div class="infomation">Lớp: {{ selected_schedule._class.name }}
          </div>
          <div class="infomation">Thứ: {{ selected_schedule.date_of_week }}</div>
          <div class="infomation">Tiết: {{ selected_schedule.class_time }}</div>
          <div class="infomation">Kỳ học: {{ selected_schedule.semester }}</div>


        </div>
        <div style="flex:1">
          <div class="infomation">Môn: {{ selected_schedule.subject }}
          </div>
          <div class="infomation">Giáo viên: {{ selected_schedule.teacher.name }}
          </div>
          <div class="infomation">Phòng học: {{ selected_schedule.classroom }}
          </div>
        </div>
      </div>
      <div v-else style="display: flex">
        <div>
          <div class="input_form">
            <label>
              Lớp
            </label>
            <select required v-model="selected_schedule._class">
              <option v-for="_class in proptemp.classes" :value="_class">{{ _class.name }}
              </option>
            </select>
          </div>
          <div class="input_form">
            <label>
              Thứ
            </label>
            <input type="number" min="2" max="7" v-model="selected_schedule.date_of_week"/>
          </div>
          <div class="input_form">
            <label>
              Tiết
            </label>
            <input type="number" min="1" max="5" v-model="selected_schedule.class_time"/>
          </div>
          <div class="input_form">
            <label>
              Kỳ học
            </label>
            <input type="number" min="1" max="2" v-model="selected_schedule.semester"/>
          </div>
        </div>
        <div>
          <div class="input_form">
            <label>
              Môn
            </label>
            <select v-model="selected_schedule.subject">
              <option v-for="subject in subjects">{{ subject }}</option>
            </select>

          </div>
          <div class="input_form">
            <label>
              Giáo viên
            </label>
            <select required v-model="selected_schedule.teacher">
              <option v-for="teacher in list_teacher" :value="teacher">{{ teacher.name }}
              </option>
            </select>
          </div>
          <div class="input_form">
            <label>
              Phòng học
            </label>
            <input type="text" v-model="selected_schedule.classroom "/>
          </div>
        </div>
      </div>
      <button @click="saveChange(selected_schedule)">Lưu</button>
      <button @click="cancel">Quay lại</button>
    </div>
  </div>
</template>


<style scoped>
.input_form {
  display: flex;
  gap: 15px;
  padding: 10px;
}

.input_form label {
  width: 150px;
  margin: 0px 0px 20px 0px;
}

.input_form input {
  flex: 1;
  text-size-adjust: 100%;
  fill: currentColor;
  -webkit-font-smoothing: antialiased;
  -webkit-box-direction: normal;
  padding: .5rem 1rem;
  background-color: #fff;
  border: .1rem solid #c4cdd5;
  border-radius: .3rem;
  color: #31373d;
  display: block;
  font-size: 15px;
  width: 100%;
  vertical-align: baseline;
  height: auto;
  margin: 0;
  max-width: 100%;
  font-family: -apple-system, blinkmacsystemfont, san francisco, roboto, segoe ui, helvetica neue, sans-serif;
  box-shadow: 0 0 0 1px transparent, 0 1px 0 0 rgba(22, 29, 37, .05);
  box-sizing: border-box;
  transition: box-shadow .2s cubic-bezier(.64, 0, .35, 1);
  appearance: none;
}

.input_form select {
  flex: 1;
  text-size-adjust: 100%;
  fill: currentColor;
  -webkit-font-smoothing: antialiased;
  -webkit-box-direction: normal;
  padding: .5rem 1rem;
  background-color: #fff;
  border: .1rem solid #c4cdd5;
  border-radius: .3rem;
  color: #31373d;
  display: block;
  font-size: 15px;
  width: 100%;
  vertical-align: baseline;
  height: auto;
  margin: 0;
  max-width: 100%;
  font-family: -apple-system, blinkmacsystemfont, san francisco, roboto, segoe ui, helvetica neue, sans-serif;
  box-shadow: 0 0 0 1px transparent, 0 1px 0 0 rgba(22, 29, 37, .05);
  box-sizing: border-box;
  transition: box-shadow .2s cubic-bezier(.64, 0, .35, 1);
  appearance: none;
  background-image: url(data:image/svg+xml;charset=utf8;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHZpZXdCb3g9JzAgMCAyMCAyMCc+PHBhdGggZmlsbD0ncmdiKDk5LDExNSwxMjkpJyBkPSdNMTMgOGwtMy0zLTMgM2g2em0tLjEgNEwxMCAxNC45IDcuMSAxMmg1Ljh6JyBmaWxsLXJ1bGU9J2V2ZW5vZGQnPjwvcGF0aD48L3N2Zz4=);
  background-position: right .7rem top .7rem;
  background-size: 21px 21px;
  background-repeat: no-repeat;
}

a {
  text-decoration: underline;
  color: #0A58CA;
}


.infomation {
  font-weight: 400;
  font-size: 19px;
  font-family: Inter;
}
</style>