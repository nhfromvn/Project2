<script>
import {defineComponent} from 'vue'

export default defineComponent({
  name: "HomeroomClass",
  props: {
    user_data: Object
  }, data() {
    return {
      semester: 1,
    }
  },
  methods: {
    saveChange() {
      this.$emit('changeSemester',this.user_data.list_class_student)
    }
  }
})
</script>

<template>
  <div>
    <h2>Quản lý lớp chủ nhiệm</h2>
    <hr>
    <h3 class="infomation"> Danh sách lớp:</h3>
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
        <th>STT</th>
        <th>
          Họ và tên
        </th>
        <th>
          Ngày sinh
        </th>
        <th>
          Học lực
        </th>
        <th>Hạnh kiểm</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="(student,index) in user_data.list_class_student">
        <td>{{ index + 1 }}</td>
        <td> {{ student.first_name }} {{ student.middle_name }} {{ student.last_name }}</td>
        <td>{{ student.dob }}</td>
        <template v-for="outcome in student.list_outcome">
          <td v-if="outcome.semester==semester">
            <select v-model="outcome.conduct">
              <option v-for="option in ['Tốt','Khá','Trung Bình','Yếu']" :value="option">{{ option }}</option>
            </select>
          </td>
          <td v-if="outcome.semester==semester">
            <select v-model="outcome.academic_ability">
              <option v-for="option in ['Giỏi','Khá','Trung Bình','Yếu']" :value="option">{{ option }}</option>
            </select>
          </td>
        </template>
      </tr>
      </tbody>
    </table>
    <div style="position: fixed;right: 15px">
      <button @click="saveChange()">Lưu</button>
    </div>
  </div>

</template>

<style scoped>

</style>