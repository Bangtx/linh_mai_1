<template lang="pug">
  div
    v-row.header-top.white--text
      v-col(cols="1")
        span ANTICANCER
      v-col(cols="2")
        span(@click="openListPatientDialog = true") Danh sách Bệnh Nhân
      v-col(cols="2")
        span Trợ giúp
      v-col(cols="5")
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
        //v-list-item.hover-content  Add Image
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
            span.white--text Sổ lưu trữ:
          v-list-item
            span.white--text Ngày nhập viện: {{ data.date }}
          v-list-item
            span.white--text Họ và tên: {{ data.name }}
          v-list-item
            span.white--text Tuổi: {{ data.age }}
          v-list-item
            span.white--text Địa chỉ: {{ data.province }}
          v-list-item
            span.white--text Lý do: {{ data.reason }}
          v-list-item
            span.white--text Tiền bệnh: {{ data.backgroundDisease }}
      div.app
        clinical-symptoms(
          v-model="point"
          @open-dialog="openResultDialog()"
        )
        //v-list-item.ttls
        //  v-spacer
        //  span.white--text.pa-4 TRIỆU CHỨNG LÂM SÀNG
        //  v-spacer
        //hr
        //div(v-for="(item, index) in symptoms")
        //  div.ttls-content.pa-2
        //    span.white--text {{ item.name }}
        //    v-slider.mt-9.white--text(:label="'Mức độ'" :thumb-color="thumColor[index]" thumb-label="always" v-model="item.point")
        //v-list-item
        //  v-spacer
        //  v-btn.mt-10(@click="isOpenResultDialog = true") Submit

    add-patient-dialog(
      :value="openAddPatient"
      @on-close="closeDialog"
      @set-data-patient="setDataPatient($event)"
    )
    result-dialog(
      :value="isOpenResultDialog"
      :img-name="imageName"
      :patient-id="patientId"
      @on-close="isOpenResultDialog = false"
    )
    list-patient-dialog(
      :value="openListPatientDialog"
      @on-close="openListPatientDialog = false"
      @click-patient="clickPatient"
    )

</template>

<script lang="ts">
import AddPatientDialog from '@/components/AddPatientDialog/index.vue'
import ResultDialog from '@/components/ResultDialog/index.vue'
import ListPatientDialog from '@/components/ListPatientDialog/index.vue'
import ClinicalSymptoms from '@/components/ClinicalSymptoms/index.vue'
import axios from "axios";
const Program = {
  name: 'Program',
  components: {
    AddPatientDialog,
    ResultDialog,
    ListPatientDialog,
    ClinicalSymptoms
  },
  data () {
    return {
      baseUrl: 'http://45.117.80.122:8000',
      point: [0, 0, 0, 0, 0, 0, 0, 0],
      imageName: {name: '', yes: false},
      dataPatient: {},
      isOpenResultDialog: false,
      openAddPatient: false,
      openListPatientDialog: false,
      thumColor: [
        'orange darken-7',
        'orange darken-7',
        'orange darken-7',
        'orange darken-7',
        'orange darken-7',
        'orange darken-7',
        'orange darken-7',
        'orange darken-7'
      ],
      symptoms: [
        { name: 'Đau đầu thường xuyên và nghiêm trọng', point: 0 },
        { name: 'Thay đổi tính cách, hành vi và suy nghĩ', point: 0 },
        { name: 'Rối loạn chức năng hoặc nhầm lẫn trí nhớ', point: 0 },
        { name: 'Nghe bất thường', point: 0 },
        { name: 'Giao tiếp cản trở', point: 0 },
        { name: 'Vấn đề cân bằng', point: 0 },
        { name: 'Buồn nôn, nôn mửa và buồn ngủ', point: 0 },
        { name: 'Tê tay chân', point: 0 }
      ],
      data: {
        name: '',
        province: '',
        date: '',
        age: '',
        sex: '',
        reason: '',
        status: '',
        backgroundDisease: ''
      },
      patientId: 0
    }
  },
  watch: {
    symptoms: {
      handler: (after, before) => {
        // after.forEach((e, index) => {
        //   console.log(this)
        //   // this.thumColor[index] = e.point < 30 ? 'green darken-7' : e.point < 70 ? 'yellow darken-7' : 'red darken-7'
        // })
      },
      deep: true
    }
  },
  methods: {
    openMenu () {
      console.log('openMenu')
    },
    closeDialog (data) {
      this.data = data
      this.openAddPatient = false
    },
    setDataPatient (data) {
      this.dataPatient = data
      this.imageName.name = data.img_name
    },
    clickPatient (patientData) {
      this.isOpenResultDialog = true
      Object.keys(patientData).forEach((key) => {
        this.data = patientData[key]
      })
      this.imageName.name = patientData.img_name
      // console.log(patientData)
    },
    async openResultDialog () {
      this.isOpenResultDialog = true
      this.dataPatient['point_1'] = this.point[0],
      this.dataPatient['point_2'] = this.point[1],
      this.dataPatient['point_3'] = this.point[2],
      this.dataPatient['point_4'] = this.point[3],
      this.dataPatient['point_5'] = this.point[4],
      this.dataPatient['point_6'] = this.point[5],
      this.dataPatient['point_7'] = this.point[6],
      this.dataPatient['point_8'] = this.point[7]
      console.log(this.dataPatient)
      this.patientId = (await axios.post(`${this.baseUrl}/add_patient`, this.dataPatient)).data.id
    }
  }
}

export default Program
</script>

<style lang="sass">
.header-top
  background-color: #212f38
  span
    cursor: pointer
.hover-content
  cursor: pointer
.bg-content
  background-color: #2d4a5c
  width: 100%
  height: 95vh
  position: relative
.v-application .info
  width: 23%
  height: 65vh
  position: absolute
  left: 2%
  top: 5vh
  background-color: #275f6e !important
  border-radius: 20px
.v-application .app
  width: 72%
  height: 85vh
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
.ttls-content
  width: 50%
  border: 2px solid #2b6e7f
  float: left
  span
    font-size: 22px
</style>