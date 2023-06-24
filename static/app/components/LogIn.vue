<script>
import {defineComponent} from 'vue'

export default defineComponent({
  name: "LogIn"
})
</script>

<template>
   <div>
        <form @submit.prevent="login">
            <label>Ma so sv:</label>
            <input type="email" v-model="email" required>
            <label>Password:</label>
            <input type="password" v-model="password" required>
            <button type="submit">Đăng nhập</button>
        </form>
    </div>
</template>

<style scoped>

</style>