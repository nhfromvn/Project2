<template>
  <div>
    <div>
      <img style="height: 200px;width: 200px" src="/thpt/static/app/img/Anh-meo-cute-dang-yeu-de-thuong.jpg">
    </div>
    <div class="label-form">Thông tin cá nhân</div>
    <div style="display: flex">
      <div style="flex:1">
        <div class="infomation">Họ và tên:</div>
        <div class="infomation">Lớp:</div>
        <div class="infomation">Giới tính:</div>
        <div class="infomation">Ngày sinh:</div>
      </div>
      <div style="flex:1">
        <div class="infomation">Dân tộc:</div>
        <div class="infomation">Tôn giáo:</div>
        <div class="infomation">Số điện thoại</div>
        <div class="infomation"> Địa chỉ:</div>
      </div>
    </div>
    <div class="label-form">Thông tin gia đình</div>
    <div style="display: flex">
      <div style="flex:1">
        <div class="infomation">
          Họ và tên bố:
        </div>
        <div class="infomation">
          Số điện thoại:
        </div>
        <div class="infomation">
          Nghề nghiệp:
        </div>
      </div>
      <div style="flex:1">
        <div class="infomation">
          Họ và tên mẹ:
        </div>
        <div class="infomation">
          Số điện thoại:
        </div>
        <div class="infomation">
          Nghề nghiệp:
        </div>
      </div>
    </div>
    <div style="display: flex;gap: 10px; align-items: center">
      <div class="label-form">Thông tin lớp</div>
      <font-awesome-icon v-if="!show_table" :icon="['fass', 'caret-down']"
                         style="cursor: pointer;z-index: 10;width: 30px;"
                         @click="this.show_table=!this.show_table"/>
      <font-awesome-icon v-else :icon="['fas', 'caret-up']"
                         style="cursor: pointer;z-index: 10;width: 30px;"
                         @click="this.show_table=!this.show_table"/>
    </div>

    <table v-if="show_table" class="table table-responsive table-bordered">
      <thead>
      <tr>
        <th>STT</th>
        <th>
          Họ
        </th>
        <th>
          Tên đệm
        </th>
        <th>
          Tên
        </th>
        <th>
          Ngày sinh
        </th>
      </tr>
      </thead>
      <tbody>
      <tr>
        <td>1</td>
        <td> Hoàng</td>
        <td></td>
        <td>Nam</td>
        <td>21/04/2001</td>
      </tr>
      <tr>
        <td>1</td>
        <td> Hoàng</td>
        <td></td>
        <td>Nam</td>
        <td>21/04/2001</td>
      </tr>
      <tr>
        <td>1</td>
        <td> Hoàng</td>
        <td></td>
        <td>Nam</td>
        <td>21/04/2001</td>
      </tr>

      <tr>
        <td>1</td>
        <td> Hoàng</td>
        <td></td>
        <td>Nam</td>
        <td>21/04/2001</td>
      </tr>
      <tr>
        <td>1</td>
        <td> Hoàng</td>
        <td></td>
        <td>Nam</td>
        <td>21/04/2001</td>
      </tr>


      </tbody>
    </table>
  </div>
</template>

<script>
import {defineComponent} from 'vue'

export default defineComponent({
  name: "DashBoard",
  data() {
    return {
      show_table: false,
    }

  }

})
</script>

<style scoped>
.label-form {
  margin: 20px 0px;
  font-weight: bold;
  font-size: 22px;
  font-family: Inter;
}

.infomation {
  font-weight: 400;
  font-size: 19px;
  font-family: Inter;
}
</style>