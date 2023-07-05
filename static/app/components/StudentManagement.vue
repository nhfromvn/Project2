<template>
  <div>
    <h2>
      Quản lý học sinh
    </h2>
    <hr>

    <div v-if="state==states[0]">
      <h3>Danh sách </h3>
      <table class="table table-responsive table-bordered">
        <thead>
        <tr>
          <th>
            Họ
          </th>
          <th>Tên đệm</th>
          <th> Tên</th>
          <th>Lớp</th>
          <th>Giới tính</th>
          <th>Ngày sinh</th>
          <th>Dân tộc</th>
          <th> Tôn giáo</th>
          <th> Số điện thoại</th>
          <th> Địa chỉ</th>
          <th>Quản lý</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="student in proptemp.students">
          <td>{{ student.first_name }}</td>
          <td>{{ student.middle_name }}</td>
          <td>{{ student.last_name }}</td>
          <td v-if="student._class">{{ student._class.name }}</td>
          <td v-else></td>
          <td>{{ student.gender.name }}</td>
          <td>{{ student.dob }}</td>
          <td>{{ student.ethnicity }}</td>
          <td>{{ student.religion }}</td>
          <td>{{ student.phone }}</td>
          <td>{{ student.address }}</td>
          <td style="display: flex; gap: 15px">
            <a @click="showStudent(student)" style="    text-decoration: underline;
    color: #0A58CA;"> Chi tiết</a>
          </td>
        </tr>
        </tbody>
      </table>
      <div style="justify-content: flex-end; display: flex">
        <button style="width: 300px; height: 40px" @click="formStudent">Thêm học sinh</button>
      </div>
    </div>
    <div v-if="state==states[1]">
      <h3>Thêm học sinh</h3>
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
            <input type="text" v-model="new_student.first_name"/>
            *
          </div>
          <div class="input_form">
            <label>
              Tên đệm
            </label>
            <input type="text" v-model="new_student.middle_name"/>
          </div>
          <div class="input_form">
            <label>
              Tên
            </label>
            <input type="text" v-model="new_student.last_name"/>
            *
          </div>
          <div class="input_form">
            <label>
              Lớp
            </label>
            <select required v-model="new_student._class">
              <option v-for="_class in proptemp.classes" :value="_class">{{ _class.name }}
              </option>
            </select>
            *
          </div>
          <div class="input_form">
            <label>
              Giới tính
            </label>
            <select v-model="new_student.gender">
              <option v-for="gender in genders" :value="gender">
                {{ gender.name }}
              </option>
            </select>
          </div>
          <div class="input_form">
            <label>
              Ngày sinh
            </label>
            <input type="date" v-model="new_student.dob"/>
          </div>
        </div>
        <div>
          <div class="input_form">
            <label>
              Dân tộc
            </label>
            <input type="text" v-model="new_student.ethnicity"/>
          </div>
          <div class="input_form">
            <label>
              Tôn giáo
            </label>
            <input type="text" v-model="new_student.religion"/>
          </div>
          <div class="input_form">
            <label>
              Số điện thoại
            </label>
            <input type="text" v-model="new_student.phone"/>
          </div>
          <div class="input_form">
            <label>
              Địa chỉ
            </label>
            <input type="text" v-model="new_student.address"/>
          </div>
        </div>
      </div>
    </div>
    <div v-if="state==states[2]">
      <div style="display:flex;align-items: center; gap: 10px;margin-bottom: 10px">
        <h3 style="margin: 0">Thông tin học sinh</h3> <a v-if="!changing" @click="changeStudent" style="  text-decoration: underline;
  color: #0A58CA;">Sửa</a>
      </div>
      <div v-if="!changing" style="display: flex">
        <div style="flex:1">
          <div class="infomation">Họ và tên: {{ selected_student.first_name }} {{ selected_student.middle_name }}
            {{ selected_student.last_name }}
          </div>
          <div class="infomation" v-if="selected_student._class">Lớp: {{ selected_student._class.name }}</div>
          <div class="infomation">Giới tính: {{ selected_student.gender.name }}</div>
          <div class="infomation">Ngày sinh: {{ selected_student.dob }}</div>

        </div>
        <div style="flex:1">
          <div class="infomation">Dân tộc: {{ selected_student.ethnicity }}</div>
          <div class="infomation">Tôn giáo: {{ selected_student.religion }}</div>
          <div class="infomation">Số điện thoại {{ selected_student.phone }}</div>
          <div class="infomation"> Địa chỉ: {{ selected_student.address }}</div>
        </div>
      </div>
      <div v-else style="display: flex">
        <div>
          <div class="input_form">
            <label>
              Họ
            </label>
            <input type="text" v-model="selected_student.first_name"/>

          </div>
          <div class="input_form">
            <label>
              Tên đệm
            </label>
            <input type="text" v-model="selected_student.middle_name"/>
          </div>
          <div class="input_form">
            <label>
              Tên
            </label>
            <input type="text" v-model="selected_student.last_name"/>
          </div>
          <div class="input_form">
            <label>
              Lớp
            </label>
            <select required v-model="selected_student._class">
              <option v-for="_class in proptemp.classes" :value="_class">{{ _class.name }}
              </option>
            </select>
          </div>
          <div class="input_form">
            <label>
              Giới tính
            </label>
            <select v-model="selected_student.gender">
              <option v-for="gender in genders" :value="gender">
                {{ gender.name }}
              </option>
            </select>
          </div>
          <div class="input_form">
            <label>
              Ngày sinh
            </label>
            <input type="date" v-model="selected_student.dob"/>
          </div>
        </div>
        <div>
          <div class="input_form">
            <label>
              Dân tộc
            </label>
            <input type="text" v-model="selected_student.ethnicity"/>
          </div>
          <div class="input_form">
            <label>
              Tôn giáo
            </label>
            <input type="text" v-model="selected_student.religion"/>
          </div>
          <div class="input_form">
            <label>
              Số điện thoại
            </label>
            <input type="text" v-model="selected_student.phone"/>
          </div>
          <div class="input_form">
            <label>
              Địa chỉ
            </label>
            <input type="text" v-model="selected_student.address"/>
          </div>
        </div>
      </div>
      <button @click="saveChange(selected_student)">Lưu</button>
      <button @click="cancel">Quay lại</button>
    </div>
  </div>
</template>
<script>
import {defineComponent} from 'vue'
import dayjs from 'dayjs'

export default defineComponent({
  name: "StudentManagement",
  props: {
    proptemp: Object
  },
  computed: {},
  data() {
    return {
      state: 'dashboard',
      states: ['dashboard', 'add_student', 'show_student'],
      changing: false,
      selected_student: {},
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
      new_student: {
        first_name: '',
        middle_name: '',
        last_name: '',
        _class: '',
        gender: {
          name: 'Nam',
          value: true
        },
        dob: '',
        phone: '',
        address: '',
        ethnicity: '',
        religion: '',
        parent: [{
          first_name: '',
          middle_name: '',
          last_name: '',
          phone: '',
          job: '',
        }, {
          first_name: '',
          middle_name: '',
          last_name: '',
          phone: '',
          job: '',
        }]

      }
    }
  },
  methods: {
    saveChange(student) {
      if (!this.changing) {
        alert('Không có gì để lưu')
      } else {

        this.$emit('changeStudent', student)
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
      if (!this.new_student._class || !this.new_student.first_name || !this.new_student.last_name) {
        alert('Chưa điền đủ thông tin bắt buộc')
      } else {
        this.$emit('addNewStudent', this.new_student)
      }
    },
    showStudent(student) {
      this.selected_student = student
      this.state = this.states[2]
    }
  },
  mounted() {
    this.new_student.dob = dayjs().format('YYYY-MM-DD');
    this.test = window
    this.proptemp.students.sort((a, b) => {
      if (a.last_name == b.last_name) {
        return a.first_name.localeCompare(b.first_name)
      }
      return a.last_name.localeCompare(b.last_name)
    })

  }
})
</script>
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