<template>
  <div>
    <h2>
      Học tập
    </h2>
    <hr>
    <h3>Kết quả học tập</h3>
    <div style="display: flex;gap: 15px">
      <div>Học kỳ :</div>
      <select v-model="semester">
        <option v-for="i in [1,2]" :value="i">
          {{ i }}
        </option>
      </select>
    </div>
    <table class="table table-responsive table-bordered">
      <thead>
      <tr>
        <th>
          Môn học
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
          Điểm thi cuối kì
        </th>
        <th>
          Điểm trung bình
        </th>
      </tr>

      </thead>
      <tbody>
      <tr v-for="subject in user_data.list_subject">
        <td>{{ subject.name }}</td>
        <td>{{ subject.teacher.name }}</td>
        <td style="width: 300px">
          <template style="width: 300px" v-for="subject_info in subject.subject_infos">
            <template v-if="subject_info.semester==semester&&subject_info.multiplier==1">
              {{ subject_info.score }}&nbsp
            </template>
          </template>
        </td>
        <td style="width: 300px">
          <template v-for="subject_info in subject.subject_infos">
            <template v-if="subject_info.semester==semester&&subject_info.multiplier==2">
              {{ subject_info.score }}&nbsp
            </template>
          </template>
        </td>
        <td>
          <template v-for="subject_info in subject.subject_infos">
            <template v-if="subject_info.semester==semester&&subject_info.multiplier==3">
              {{ subject_info.score }}&nbsp
            </template>
          </template>
        </td>
        <td>{{ subject.average_score.toFixed(1)}}</td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import {defineComponent} from 'vue'

export default defineComponent({
  name: "LearningOutcome",
  props: {
    user_data: Object
  },
  data() {
    return {
      semester: 1,
    }
  }
})
</script>


<style scoped>
a {
  color: #1890ff !important;
  background-color: transparent;
  text-decoration: underline !important;
  outline: none;
  cursor: pointer;
  transition: color 0.3s;
}

.score {
  border: none;
  width: 55px;
}
</style>