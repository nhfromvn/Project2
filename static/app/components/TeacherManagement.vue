<script>
import {defineComponent} from 'vue'
import dayjs from 'dayjs'

export default defineComponent({
  name: "TeacherManagement",
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
      genders: [
        {
          name: 'Nam',
          value: true,
        },
        {
          name: 'Nữ',
          value: false
        }
      ],
      state: 'dashboard',
      states: ['dashboard', 'add', 'show'],
      changing: false,
      subjects: ['Toán', 'Vật lý', 'Hóa học', 'Sinh học', 'Văn', 'Lịch sử', 'Địa lý', 'Giáo dục công dân', 'Công nghệ', 'Tin học', 'Thể dục'],
      literacies: ['Thạc sỹ', 'Tiến sĩ', 'Đại học', 'Phổ thông'],
      selected_teacher: {},
      new_teacher: {
        first_name: '',
        middle_name: '',
        last_name: '',
        _class: '',
        subject: '',
        gender: {
          name: 'Nam',
          value: true
        },
        dob: '',
        phone: '',
        address: '',
        ethnicity: '',
        religion: '',
        literacy: 'Thạc sỹ',
        main_teacher: ''
      }
    }
  },
  methods: {
    saveChange(teacher) {
      if (!this.changing) {
        alert('Không có gì để lưu')
      } else {

        this.$emit('changeTeacher', teacher)
      }

    },
    changeTeacher() {
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
      if (!this.new_teacher.main_teacher) {
        if (!this.new_teacher.first_name || !this.new_teacher.last_name) {
          alert('Chưa điền đủ thông tin bắt buộc')
        } else {
          this.$emit('addNewTeacher', this.new_teacher)
        }

      } else {
        if (!this.new_teacher.first_name || !this.new_teacher.last_name || !this.new_teacher._class) {
          alert('Chưa điền đủ thông tin bắt buộc')
        } else {
          this.$emit('addNewTeacher', this.new_teacher)
        }
      }

    },
    show(teacher) {
      this.selected_teacher = teacher
      this.state = this.states[2]
    }
  },
  mounted() {
    this.new_teacher.dob = dayjs().format('YYYY-MM-DD');
    this.test = window
    this.proptemp.teachers.sort((a, b) => {
      if (a.last_name == b.last_name) {
        return a.first_name.localeCompare(b.first_name)
      }
      return a.last_name.localeCompare(b.last_name)
    })

  }
})
</script>

<!--<template>-->
<!--  <div>-->
<!--    <h2>Quản lý giáo viên</h2>-->
<!--    <hr/>-->
<!--    <h3>Danh sách giáo viên</h3>-->
<!--    <table class="table table-responsive table-bordered">-->
<!--      <thead>-->
<!--      <tr>-->
<!--        <th>Họ</th>-->
<!--        <th>Tên đệm</th>-->
<!--        <th>Tên</th>-->
<!--        <th>Trình độ học vấn</th>-->
<!--        <th>Ngày sinh</th>-->
<!--        <th> Bộ môn</th>-->
<!--      </tr>-->
<!--      </thead>-->
<!--      <tbody>-->
<!--      <tr v-for="teacher in proptemp.teachers">-->
<!--        <td>{{ teacher.first_name }}</td>-->
<!--        <td>{{ teacher.middle_name }}</td>-->
<!--        <td>{{ teacher.last_name }}</td>-->
<!--        <td>{{ teacher.literacy }}</td>-->
<!--        <td>{{ teacher.dob }}</td>-->

<!--        <td style="display: flex;gap: 10px;text-decoration: underline; color: #1c21a8"><a-->
<!--            v-for="subject in teacher.subjects">-->
<!--          {{ subject.name }} </a></td>-->
<!--      </tr>-->
<!--      </tbody>-->
<!--    </table>-->
<!--  </div>-->
<!--</template>-->

<template>
  <div>
    <h2>Quản lý giáo viên</h2>
    <hr/>

    <div v-if="state==states[0]">
      <h3>Danh sách giáo viên</h3>
      <table class="table table-responsive table-bordered">
        <thead>
        <tr>
          <th>Họ</th>
          <th>Tên đệm</th>
          <th>Tên</th>
          <th>Trình độ học vấn</th>
          <th>Ngày sinh</th>
          <th> Bộ môn</th>
          <th>Quản lý</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="teacher in proptemp.teachers">
          <td>{{ teacher.first_name }}</td>
          <td>{{ teacher.middle_name }}</td>
          <td>{{ teacher.last_name }}</td>
          <td>{{ teacher.literacy }}</td>
          <td>{{ teacher.dob }}</td>
          <td>
            {{ teacher.subject}}
          </td>
          <td>
            <div style="display: flex; gap: 15px">
              <a @click="show(teacher)" style="    text-decoration: underline;
    color: #0A58CA;"> Chi tiết</a>
            </div>
          </td>
        </tr>
        </tbody>
      </table>
      <div style="justify-content: flex-end; display: flex">
        <button style="width: 300px; height: 40px" @click="formStudent">Thêm giáo viên</button>
      </div>
    </div>
    <div v-if="state==states[1]">
      <h3>Thêm giáo viên</h3>
      <div style="display: flex; gap: 15px; justify-content: end">
        <button @click="add">Thêm</button>
        <button @click="cancel">Quay lại</button>
      </div>
      <i style="font-family: Inter; color: red">Những thông tin có dấu * là thông tin bắt buộc</i>
      <div style="display: flex">
        <div>
          <div class="input_form">
            <label>
              Họ
            </label>
            <input type="text" v-model="new_teacher.first_name"/>
            *
          </div>
          <div class="input_form">
            <label>
              Tên đệm
            </label>
            <input type="text" v-model="new_teacher.middle_name"/>
          </div>
          <div class="input_form">
            <label>
              Tên
            </label>
            <input type="text" v-model="new_teacher.last_name"/>
            *
          </div>
          <div v-if="new_teacher.main_teacher" class="input_form">
            <label>
              Lớp chủ nhiệm
            </label>
            <select required v-model="new_teacher._class">
              <option v-for="_class in proptemp.classes" :value="_class">{{ _class.name }}
              </option>
            </select>
            *
          </div>
          <div class="input_form">
            <label>
              Bộ môn
            </label>
            <select v-model="new_teacher.subject">
              <option  v-for="subject in subjects" :value="subject">{{ subject }}
              </option>
            </select>
          </div>
          <div class="input_form">
            <label>
              Giới tính
            </label>
            <select v-model="new_teacher.gender">
              <option v-for="gender in genders" :value="gender">
                {{ gender.name }}
              </option>
            </select>
          </div>
          <div class="input_form">
            <label>
              Ngày sinh
            </label>
            <input type="date" v-model="new_teacher.dob"/>
          </div>
          <div class="input_form">
            <label>
              Chủ nhiệm
            </label>
            <input type="checkbox" v-model="new_teacher.main_teacher"/>
          </div>

        </div>
        <div>
          <div class="input_form">
            <label>
              Học vấn
            </label>
            <select v-model="new_teacher.literacy">
              <option v-for="literacy in literacies" :value="literacy">
                {{ literacy }}
              </option>
            </select>
          </div>
          <div class="input_form">
            <label>
              Dân tộc
            </label>
            <input type="text" v-model="new_teacher.ethnicity"/>
          </div>
          <div class="input_form">
            <label>
              Tôn giáo
            </label>
            <input type="text" v-model="new_teacher.religion"/>
          </div>
          <div class="input_form">
            <label>
              Số điện thoại
            </label>
            <input type="text" v-model="new_teacher.phone"/>
          </div>
          <div class="input_form">
            <label>
              Địa chỉ
            </label>
            <input type="text" v-model="new_teacher.address"/>
          </div>
        </div>
      </div>
    </div>
    <div v-if="state==states[2]">
      <div style="display:flex;align-items: center; gap: 10px;margin-bottom: 10px">
        <h3 style="margin: 0">Thông tin giáo viên</h3> <a v-if="!changing" @click="changeTeacher" style="  text-decoration: underline;
  color: #0A58CA;">Sửa</a>
      </div>
      <div v-if="!changing" style="display: flex">
        <div style="flex:1">
          <div class="infomation">Họ và tên: {{ selected_teacher.first_name }} {{ selected_teacher.middle_name }}
            {{ selected_teacher.last_name }}
          </div>
          <div v-if="selected_teacher.main_teacher" class="infomation">Lớp chủ nhiệm: {{
              selected_teacher._class.name
            }}
          </div>
          <div class="infomation">Giới tính: {{ selected_teacher.gender.name }}</div>
          <div class="infomation">Ngày sinh: {{ selected_teacher.dob }}</div>
          <div class="infomation">Học vấn: {{ selected_teacher.literacy }}</div>
          <div class="infomation">Bộ môn: {{selected_teacher.subject}}
          </div>
        </div>
        <div style="flex:1">

          <div class="infomation">Dân tộc: {{ selected_teacher.ethnicity }}</div>
          <div class="infomation">Tôn giáo: {{ selected_teacher.religion }}</div>
          <div class="infomation">Số điện thoại {{ selected_teacher.phone }}</div>
          <div class="infomation"> Địa chỉ: {{ selected_teacher.address }}</div>
        </div>
      </div>
      <div v-else style="display: flex">
        <div>
          <div class="input_form">
            <label>
              Họ
            </label>
            <input type="text" v-model="selected_teacher.first_name"/>

          </div>
          <div class="input_form">
            <label>
              Tên đệm
            </label>
            <input type="text" v-model="selected_teacher.middle_name"/>
          </div>
          <div class="input_form">
            <label>
              Tên
            </label>
            <input type="text" v-model="selected_teacher.last_name"/>
          </div>
          <div v-if="selected_teacher.main_teacher" class="input_form">
            <label>
              Lớp chủ nhiệm
            </label>
            <select required v-model="selected_teacher._class">
              <option v-for="_class in proptemp.classes" :value="_class">{{ _class.name }}
              </option>
            </select>
          </div>
           <div class="input_form">
            <label>
              Bộ môn
            </label>
            <select v-model="selected_teacher.subject">
              <option  v-for="subject in subjects" :value="subject">{{ subject }}
              </option>
            </select>
          </div>
          <div class="input_form">
            <label>
              Giới tính
            </label>
            <select v-model="selected_teacher.gender">
              <option v-for="gender in genders" :value="gender">
                {{ gender.name }}
              </option>
            </select>
          </div>
          <div class="input_form">
            <label>
              Ngày sinh
            </label>
            <input type="date" v-model="selected_teacher.dob"/>
          </div>
          <div class="input_form">
            <label>
              Chủ nhiệm
            </label>
            <input type="checkbox" v-model="selected_teacher.main_teacher"/>
          </div>
        </div>
        <div>
          <div class="input_form">
            <label>
              Dân tộc
            </label>
            <input type="text" v-model="selected_teacher.ethnicity"/>
          </div>
          <div class="input_form">
            <label>
              Học vấn
            </label>
            <select v-model="new_teacher.literacy">
              <option v-for="literacy in literacies" :value="literacy">
                {{ literacy }}
              </option>
            </select>
          </div>
          <div class="input_form">
            <label>
              Tôn giáo
            </label>
            <input type="text" v-model="selected_teacher.religion"/>
          </div>
          <div class="input_form">
            <label>
              Số điện thoại
            </label>
            <input type="text" v-model="selected_teacher.phone"/>
          </div>
          <div class="input_form">
            <label>
              Địa chỉ
            </label>
            <input type="text" v-model="selected_teacher.address"/>
          </div>
        </div>
      </div>
      <button @click="saveChange(selected_teacher)">Lưu</button>
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

}

.input_form input[type=checkbox] {
  appearance: auto;
  flex: 0;
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