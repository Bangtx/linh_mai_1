<template lang="pug">
  div.full.mt-3
    div.menu
      button.btn-icon.mt-10
        v-icon(x-large) mdi-account-multiple
      button.btn-icon.mt-10
        v-icon(x-large) mdi-email-open-outline
    div.ground
      v-row
        v-col(cols="10")
          img.ml-10.mt-9(
            width="20%"
            src="https://f58-zpg-r.zdn.vn/1520915173160395324/ba831ed5b3327e6c2723.jpg"
          )
        v-col(cols="2")
          div.mt-10
            span.home-text Home
            v-icon.ml-2.mb-3 mdi-arrow-up-bold
      img.mt-2(
        width="100%"
        src="https://f45-zpg-r.zdn.vn/1027120998132103990/379474fed91914474d08.jpg"
      )
      v-row
        v-col(cols="4")
          button.btn-pro.mt-10(@click="openLoginDialog = true")
            h3 Testing tool
            span Chương Trình Chuẩn Đoán Ung Thư

        v-col(cols="4")
          button.btn-tra.mt-10
            h3 Training mode
            span Chương Trình Đào Tạo Và Huấn Luyện

        v-col(cols="4")
          button.btn-men.mt-10
            h3 About us
            span Giới Thiệu Đội Ngữ Sáng Tạo

    login-dialog(
      :value="openLoginDialog"
      @on-close="openLoginDialog = false"
    )

</template>

<script>
import LoginDialog from '@/components/LoginDialog/index.vue'

const Main = {
  components: {
    LoginDialog
  },
  data () {
    return {
      openLoginDialog: false
    }
  },
}

export default Main
</script>

<style lang="sass">
.full
  width: 100%
  height: 100vh
  background-color: #2f9aba
.menu
  width: 5%
  float: left
.ground
  width: 95%
  margin-left: 5%
  height: 100vh
  background-color: #d8ebf1
  border-radius: 20px
.home-text
  font-size: 30px
.btn-icon
  width: 100%
  height: 60px
.btn-icon:hover
  width: 100%
  height: 60px
  border-radius: 10px
  background-color: #54afcf
.btn-glo
  width: 50%
  height: 200px
.btn-pro
  width: 60%
  height: 200px
  background-color: #bcddec
  border-radius: 20px
  margin-left: 20%
.btn-pro:hover
  width: 60%
  height: 200px
  background-color: #dcedfc
  border-radius: 20px
  margin-left: 20%
.btn-tra
  width: 60%
  height: 200px
  background-color: #74baa2
  border-radius: 20px
  margin-left: 20%
.btn-tra:hover
  width: 60%
  height: 200px
  background-color: #94cab2
  border-radius: 20px
  margin-left: 20%
.btn-men
  width: 60%
  height: 200px
  background-color: #b0d5a1
  border-radius: 20px
  margin-left: 20%
.btn-men:hover
  width: 60%
  height: 200px
  background-color: #c0e5b1
  border-radius: 20px
  margin-left: 20%
</style>