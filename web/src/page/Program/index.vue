<template lang="pug">
  div
    v-row.header-top.white--text
      v-col(cols="1")
        span ANTICANCER
      v-col(cols="1")
        span Danh sách ra
      v-col(cols="1")
        span Trợ giúp
      v-col(cols="7")
      v-col(cols="1")
        span Home
      v-col(cols="1")
        v-icon(color="white") mdi-account-multiple

    v-menu(
      open-on-hover
      top
      offset-y
      max-width="200px"
    )
      template(v-slot:activator="{ on, attrs }")
        v-row.header-top
          v-col.ml-2(cols="1")
            v-icon(color="white") mdi-keyboard-backspace
            v-icon(v-bind="attrs" v-on="on" @click="openMenu").ml-5(color="white") mdi-dialpad

      v-list
        v-list-item.hover-content  Add Image
        v-list-item.hover-content(@click="openAddPatient = true")  Add patient

    div.bg-content.mt-3
      div.info
        v-list-item
          v-icon(x-large color="white") mdi-credit-card
          v-container
            span.ttkb.white--text THÔNG TIN KHÁM BỆNH
        hr
        div.info-detail
          v-list-item
            span.white--text Sổ lưu trữ: 12345
          v-list-item
            span.white--text Ngày nhập viện: 20-02-2022
          v-list-item
            span.white--text Họ và tên: Phùng Văn Kiệm
          v-list-item
            span.white--text Tuổi: 18
          v-list-item
            span.white--text Địa chỉ: Vĩnh Phúc
          v-list-item
            span.white--text Lý do: hehe hihi đi chơi
          v-list-item
            span.white--text Lý do: Không
      div.app
        v-list-item.ttls
          v-spacer
          span.white--text.pa-4 TRIỆU CHỨNG LÂM SÀNG
          v-spacer
        hr
        table
          tr
            th ID
            th Họ và tên đệm
          tr
            td 1
            td Nguyễn Minh
          tr
            td 2
            td Vũ Kim
          tr
            td 3
            td Nguyễn Linh
          tr
            td 4
            td Vi Đại

    add-patient-dialog(
      :value="openAddPatient"
      @on-close="openAddPatient = false"
    )

</template>

<script lang="ts">
import AddPatientDialog from '@/components/AddPatientDialog/index.vue'
const Program = {
  name: 'Program',
  components: {
    AddPatientDialog
  },
  data () {
    return {
      openAddPatient: false,
      hover: [
        { title: 'Click Me' },
        { title: 'Click Me' },
      ]
    }
  },
  methods: {
    openMenu () {
      console.log('openMenu')
    }
  }
}

export default Program
</script>

<style lang="sass">
.header-top
  background-color: #212f38
.hover-content
  cursor: pointer
.bg-content
  background-color: #2d4a5c
  width: 100%
  height: 95vh
  position: relative
.v-application .info
  width: 23%
  height: 80vh
  position: absolute
  left: 2%
  top: 5vh
  background-color: #275f6e !important
  border-radius: 20px
.v-application .app
  width: 72%
  height: 80vh
  position: absolute
  left: 26%
  top: 5vh
  background-color: #275f6e !important
  border-radius: 20px
.ttkb
  font-size: 27px
.ttls
  font-size: 35px
.info-detail
  font-size: 20px
table
  width: 100%
table th td
  border: 1px solid white

</style>