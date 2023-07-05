<template>
  <div>
    <h2>Hoạt động ngoại khóa</h2>
    <hr>
    <div v-if="state==states[0]" style="top: 100px;display: grid;grid-template-columns: repeat(3,1fr)">
      <temshowPageplate v-for="i in [0,1,2,3]">
        <a-card @click="showPage" hoverable style="width: 240px;aspect-ratio: 2">
          <template #cover>
            <img height="300" alt="example" src="/thpt/static/app/img/Anh-meo-cute-dang-yeu-de-thuong.jpg"/>
          </template>
          <a-card-meta title="Giai dau lien quan mobile">
            <template #description>chao mung den voi binh nguyen vo tan ....</template>
          </a-card-meta>
        </a-card>
      </temshowPageplate>
    </div>
  </div>
</template>
<script>
import {defineComponent} from 'vue'

export default defineComponent({
  name: "ExtracurricularActivities",
  methods: {
    showPage() {
      console.log('haha')
    }
  },
  data() {
    return {
      states: ['collection', ' page detail'],
      state: 'collection'
    }
  }
})
</script>

<style scoped>

</style>