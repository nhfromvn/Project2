<!--<template>-->
<!--  <div>-->
<!--    <h2>Quản lý lớp học</h2>-->
<!--    <hr/>-->
<!--    <table class="table table-responsive table-bordered">-->
<!--      <thead>-->
<!--      <tr>-->
<!--        <th>Tên lớp</th>-->
<!--        <th>Giáo viên chủ nhiệm</th>-->
<!--        <th>Tổng học sinh</th>-->
<!--      </tr>-->
<!--      </thead>-->
<!--      <tbody>-->
<!--      <tr v-for="_class in proptemp.classes">-->
<!--        <td>{{_class.name}}</td>-->
<!--        <td>{{ _class.teacher}}</td>-->
<!--        <td>{{ _class.size}}</td>-->
<!--      </tr>-->
<!--      </tbody>-->
<!--    </table>-->
<!--  </div>-->

<!--</template>-->
<script>
import {defineComponent} from 'vue'

export default defineComponent({
  name: "ClassManagement",
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

      state: 'dashboard',
      states: ['dashboard', 'add', 'show'],
      changing: false,
      subjects: ['Toán', 'Vật lý', 'Hóa học', 'Sinh học', 'Văn', 'Lịch sử', 'Địa lý', 'Giáo dục công dân', 'Công nghệ', 'Tin học', 'Thể dục'],
      selected__class: {},
      new__class: {
        name: '',
        teacher: {
          id: null,
          name: '',
        }
      }
    }
  },
  methods: {
    saveChange(_class) {
      if (!this.changing) {
        alert('Không có gì để lưu')
      } else {
        this.$emit('changeClass', _class)
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
      if ( !this.new__class.teacher || !this.new__class.name) {
        alert('Chưa điền đủ thông tin bắt buộc')
      } else {
        this.$emit('addNewClass', this.new__class)
      }
    },
    show(_class) {
      this.selected__class = _class
      this.state = this.states[2]
    }
  },
  mounted() {
    this.test = window
    this.proptemp.classes.sort((a, b) => {

      return a.name.localeCompare(b.name)
    })
  }
})
</script>
<template>
  <div>
    <h2>
      Quản lý lớp học
    </h2>
    <hr>
    <div v-if="state==states[0]">
      <h3>Danh sách </h3>
      <table class="table table-responsive table-bordered">
        <thead>
        <tr>
          <th>Tên lớp</th>
          <th>Giáo viên chủ nhiệm</th>
          <th>Tổng học sinh</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="_class in proptemp.classes">
          <td>{{ _class.name }}</td>
          <td>{{ _class.teacher.name }}</td>
          <td>{{ _class.size }}</td>
          <td style="display: flex; gap: 15px">
            <a @click="show(_class)" style="    text-decoration: underline;
    color: #0A58CA;"> Chi tiết</a>
          </td>
        </tr>
        </tbody>

      </table>
      <div style="justify-content: flex-end; display: flex">
        <button style="width: 300px; height: 40px" @click="formStudent">Thêm lớp học</button>
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
              Giáo viên
            </label>
            <select required v-model="new__class.teacher">
              <option v-for="teacher in list_teacher" :value="teacher">{{ teacher.name }}
              </option>
            </select>
          </div>
          <div class="input_form">
            <label>
              Tên lớp
            </label>
            <input type="text" v-model="new__class.name "/>
          </div>
        </div>
      </div>
    </div>
    <div v-if="state==states[2]">
      <div style="display:flex;align-items: center; gap: 10px;margin-bottom: 10px">
        <h3 style="margin: 0">Quản lý tiết học</h3> <a v-if="!changing" @click="changeStudent" style="  text-decoration: underline;
  color: #0A58CA;">Sửa</a>
      </div>
      <div v-if="!changing" >

        <div class="infomation">Tên lớp: {{ selected__class.name }}
        </div>
        <div class="infomation">Giáo viên: {{ selected__class.teacher.name }}
        </div>
      </div>
      <div v-else style="display: flex">

        <div class="input_form">
          <label>
            Tên lớp
          </label>
         <input type="text" v-model="selected__class.name">
        </div>
        <div class="input_form">
          <label>
            Giáo viên
          </label>
          <select required v-model="selected__class.teacher">
            <option v-for="teacher in list_teacher" :value="teacher">{{ teacher.name }}
            </option>
          </select>
        </div>

      </div>
      <button @click="saveChange(selected__class)">Lưu</button>
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