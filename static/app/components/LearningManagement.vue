<script>
import {defineComponent} from 'vue'

export default defineComponent({
  name: "LearningManagement",
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
      selected_subject: '',
      selected_class: {},
      subjects: ['Toán', 'Vật lý', 'Hóa học', 'Sinh học', 'Văn', 'Lịch sử', 'Địa lý', 'Giáo dục công dân', 'Công nghệ', 'Tin học', 'Tiếng anh', 'Thể dục'],
    }
  },
  methods: {
    saveChange() {
      this.$emit('changeLearning', this.proptemp.subjects)
    },

  },
  mounted() {
    this.test = window
    this.selected_class = this.proptemp.classes[0]
    this.proptemp.subjects.sort((a, b) => {
      return a.student.serial - b.student.serial
    })
  }
})
</script>
<template>
  <div>
    <h2>
      Quản lý học tập
    </h2>
    <hr>
    <div>
      <div style="display:flex;gap: 20px">
        <div style="display: flex;gap: 15px">
          <div>Học kỳ :</div>
          <select v-model="semester">
            <option v-for="i in [1,2]" :value="i">
              {{ i }}
            </option>
          </select>
        </div>
        <div style="display: flex;gap: 15px">
          <div>Lớp :</div>
          <select v-model="selected_class">
            <option v-for="_class in proptemp.classes" :value="_class">
              {{ _class.name }}
            </option>
          </select>
        </div>
        <div style="display: flex;gap: 15px">
          <div>Môn :</div>
          <select v-model="selected_subject">
            <option v-for="subject in subjects" :value="subject">
              {{ subject }}
            </option>
          </select>
        </div>
        <div style="position: fixed;right: 15px">
          <button @click="saveChange()">Lưu</button>
        </div>
      </div>
      <h3>Danh sách </h3>
      <table class="table table-responsive table-bordered">
        <thead>
        <tr>
          <th>STT</th>
          <th>
            Học sinh
          </th>
          <th>
            Giáo viên bộ môn
          </th>
          <th>
            Điểm hệ số 1
          </th>
          <th>
            Điểm hệ số 2
          </th>
          <th>
            Điểm cuối kì
          </th>
          <th>
            Điểm trung bình môn
          </th>
        </tr>

        </thead>
        <tbody>
        <template v-for="subject in proptemp.subjects">
          <tr v-if="subject.student._class==selected_class.name&&subject.name==selected_subject">
            <td style="width: 30px">{{ subject.student.serial }}</td>
            <td style="width: 200px">{{ subject.student.name }}</td>
            <td>
              <select class="table_select" required v-model="subject.teacher">
                  <option class="table_select" v-for="teacher in list_teacher" :value="teacher">{{ teacher.name }}
                  </option>
                </select>
            </td>
            <td style="width: 300px">
              <template style="width: 300px" v-for="subject_info in subject.subject_infos">
                <template v-if="subject_info.semester==semester&&subject_info.multiplier==1">
                  <input class="score" type="number" min="0" max="10" v-model="subject_info.score">
                </template>
              </template>
            </td>
            <td style="width: 300px">
              <template v-for="subject_info in subject.subject_infos">
                <template v-if="subject_info.semester==semester&&subject_info.multiplier==2">
                  <input class="score" type="number" min="0" max="10" v-model="subject_info.score">
                </template>
              </template>
            </td>
            <td>
              <template v-for="subject_info in subject.subject_infos">
                <template v-if="subject_info.semester==semester&&subject_info.multiplier==3">
                  <input class="score" type="number" min="0" max="10" v-model="subject_info.score">
                </template>
              </template>
            </td>
            <td style="width: 200px">{{ subject.average_score.toFixed(1)}}</td>
          </tr>

        </template>
        </tbody>
      </table>

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

.table_select {
  width: 100%;
  border: none;
  background-color: inherit;
}

.score {
  border: none;
  width: 55px;
}
</style>