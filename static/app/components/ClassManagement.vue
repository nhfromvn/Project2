<template>
  <div>
    <h2>Quản lý lớp học</h2>
    <hr/>
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
        <td>{{_class.name}}</td>
        <td>{{ _class.teacher}}</td>
        <td>{{ _class.size}}</td>
      </tr>
      </tbody>
    </table>
  </div>

</template>
<script>
import {defineComponent} from 'vue'

export default defineComponent({
  name: "ClassManagement",
  props: {
    proptemp: Object
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
</style>
<!--<template>-->
<!--  <div>-->
<!--    <h2>-->
<!--      Quản lý học sinh-->
<!--    </h2>-->
<!--    <hr>-->
<!--    <h3>Danh sách </h3>-->
<!--    <div v-if="state==states[0]">-->
<!--      <table class="table table-responsive table-bordered">-->
<!--        <thead>-->
<!--        <tr>-->
<!--          <th>-->
<!--            Họ-->
<!--          </th>-->
<!--          <th>Tên đệm</th>-->
<!--          <th> Tên</th>-->
<!--          <th>Giới tính</th>-->
<!--          <th>Ngày sinh</th>-->
<!--          <th>Dân tộc</th>-->
<!--          <th> Tôn giáo</th>-->
<!--          <th> Số điện thoại</th>-->
<!--          <th> Địa chỉ</th>-->
<!--        </tr>-->
<!--        </thead>-->
<!--        <tbody>-->
<!--        <tr v-for="student in proptemp.students">-->
<!--          <td>{{ student.first_name }}</td>-->
<!--          <td>{{ student.middle_name }}</td>-->
<!--          <td>{{ student.last_name }}</td>-->
<!--          <td>{{ student.gender.name }}</td>-->
<!--          <td>{{ student.dob }}</td>-->
<!--          <td>{{ student.ethnicity }}</td>-->
<!--          <td>{{ student.religion }}</td>-->
<!--          <td>{{ student.phone }}</td>-->
<!--          <td>{{ student.address }}</td>-->
<!--        </tr>-->
<!--        </tbody>-->
<!--      </table>-->
<!--      <div style="justify-content: flex-end; display: flex">-->
<!--        <button style="width: 300px; height: 40px" @click="formStudent">Thêm học sinh</button>-->
<!--      </div>-->
<!--    </div>-->
<!--    <div v-if="state==states[1]">-->
<!--      <div style="display: flex; gap: 15px; justify-content: end">-->
<!--        <button @click="add">Thêm học sinh</button>-->
<!--        <button @click="cancel">Quay lại</button>-->
<!--      </div>-->
<!--      <div style="display: flex">-->
<!--        <div>-->
<!--          <div class="input_form">-->
<!--            <label>-->
<!--              Họ-->
<!--            </label>-->
<!--            <input type="text" v-model="new_student.first_name"/>-->
<!--          </div>-->
<!--          <div class="input_form">-->
<!--            <label>-->
<!--              Tên đệm-->
<!--            </label>-->
<!--            <input type="text" v-model="new_student.middle_name"/>-->
<!--          </div>-->
<!--          <div class="input_form">-->
<!--            <label>-->
<!--              Tên-->
<!--            </label>-->
<!--            <input type="text" v-model="new_student.last_name"/>-->
<!--          </div>-->
<!--          <div class="input_form">-->
<!--            <label>-->
<!--              Lớp-->
<!--            </label>-->
<!--            <input type="text" v-model="new_student._class"/>-->
<!--          </div>-->
<!--          <div class="input_form">-->
<!--            <label>-->
<!--              Giới tính-->
<!--            </label>-->
<!--            <select v-model="new_student.gender">-->
<!--              <option v-for="gender in new_student.genders" :value="gender">-->
<!--                {{ gender.name }}-->
<!--              </option>-->
<!--            </select>-->
<!--          </div>-->
<!--          <div class="input_form">-->
<!--            <label>-->
<!--              Ngày sinh-->
<!--            </label>-->
<!--            <input type="date" v-model="new_student.dob"/>-->
<!--          </div>-->
<!--        </div>-->
<!--        <div>-->
<!--          <div class="input_form">-->
<!--            <label>-->
<!--              Dân tộc-->
<!--            </label>-->
<!--            <input type="text" v-model="new_student.ethnicity"/>-->
<!--          </div>-->
<!--          <div class="input_form">-->
<!--            <label>-->
<!--              Tôn giáo-->
<!--            </label>-->
<!--            <input type="text" v-model="new_student.religion"/>-->
<!--          </div>-->
<!--          <div class="input_form">-->
<!--            <label>-->
<!--              Số điện thoại-->
<!--            </label>-->
<!--            <input type="text" v-model="new_student.phone"/>-->
<!--          </div>-->
<!--          <div class="input_form">-->
<!--            <label>-->
<!--              Địa chỉ-->
<!--            </label>-->
<!--            <input type="text" v-model="new_student.address"/>-->
<!--          </div>-->

<!--        </div>-->
<!--      </div>-->
<!--    </div>-->

<!--  </div>-->
<!--</template>-->
<!--<script>-->
<!--import {defineComponent} from 'vue'-->
<!--import dayjs from 'dayjs'-->

<!--export default defineComponent({-->
<!--  name: "StudentManagement",-->
<!--  props: {-->
<!--    proptemp: Object-->
<!--  },-->
<!--  computed: {},-->
<!--  data() {-->
<!--    return {-->
<!--      state: 'dashboard',-->
<!--      states: ['dashboard', 'add_student'],-->
<!--      new_student: {-->
<!--        first_name: '',-->
<!--        middle_name: '',-->
<!--        last_name: '',-->
<!--        _class: '',-->
<!--        genders: [-->
<!--          {-->
<!--            name: 'Nam',-->
<!--            value: true,-->
<!--          },-->
<!--          {-->
<!--            name: 'Nữ',-->
<!--            value: false-->
<!--          }-->
<!--        ],-->
<!--        gender: {-->
<!--          name: 'Nam',-->
<!--          value: true-->
<!--        },-->
<!--        dob: '',-->
<!--        phone: '',-->
<!--        address: '',-->
<!--        ethnicity: '',-->
<!--        religion: '',-->
<!--        parent: [{-->
<!--          first_name: '',-->
<!--          middle_name: '',-->
<!--          last_name: '',-->
<!--          phone: '',-->
<!--          job: '',-->
<!--        }, {-->
<!--          first_name: '',-->
<!--          middle_name: '',-->
<!--          last_name: '',-->
<!--          phone: '',-->
<!--          job: '',-->
<!--        }]-->

<!--      }-->
<!--    }-->
<!--  },-->
<!--  methods: {-->
<!--    cancel() {-->
<!--      this.state = this.states[0];-->
<!--    },-->
<!--    formStudent() {-->
<!--      this.state = this.states[1]-->
<!--    },-->
<!--    add() {-->
<!--      this.$emit('addNewStudent', this.new_student)-->
<!--    }-->
<!--  },-->
<!--  mounted() {-->
<!--    this.new_student.dob = dayjs().format('YYYY-MM-DD');-->
<!--  }-->
<!--})-->
<!--</script>-->
