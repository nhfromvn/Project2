<template>
  <div>
    <h2>
      Thời khóa biểu
    </h2>
    <hr>
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
        <th></th>
        <th>
          Thứ hai
        </th>
        <th>
          Thứ ba
        </th>
        <th>
          Thứ tư
        </th>
        <th>
          Thứ năm
        </th>
        <th>
          Thứ sáu
        </th>
        <th>
          Thứ bảy
        </th>
      </tr>

      </thead>
      <tbody>
      <template v-for="(row,index) in list">
        <tr>
          <td>Tiết {{ index + 1 }}</td>
          <template v-for="schedule in row">
            <td v-if="schedule"> {{ schedule.subject }}, Phòng {{ schedule.classroom }}</td>
            <td v-else></td>
          </template>
        </tr>
      </template>
      </tbody>
    </table>
  </div>
</template>


<style scoped>

</style>
<script>
import {defineComponent} from 'vue'

export default defineComponent({
  name: "Schedule",
  props: {
    user_data: Object,
  },
  data() {
    return {
      semester: 1,
      list: new Array(5),
    }
  },
  mounted() {
    for (let i = 0; i < this.list.length; i++) {
      this.list[i] = new Array(7)
    }
    for (let schedule of this.user_data.list_schedule_student.filter(e => e.semester == this.semester)) {
      let i = schedule.class_time - 1
      let j = schedule.date_of_week - 2
      this.list[i][j] = schedule
    }
  },
  watch: {
    semester: function () {
      for (let i = 0; i < this.list.length; i++) {
        for (let j = 0; j < this.list[i].length; j++) {
          this.list[i][j] = null;
        }
      }
      for (let schedule of this.user_data.list_schedule_student.filter(e => e.semester == this.semester)) {
        let i = schedule.class_time - 1
        let j = schedule.date_of_week - 2
        this.list[i][j] = schedule
      }
    }
  }
})
</script>