<template lang="pug">
  div
    v-dialog(
      persistent
      scrollable
      max-width=400
      :value="value"
      @input="dialog => $emit('input', dialog)"
    )
      v-card
        v-card-title.title-color(color="red")
          span.white--text Add patient
          v-spacer
          v-btn(icon dark @click="close()")
            v-icon mdi-close

        div.pa-4
          v-list-item
            v-text-field(:label="'Nhập ngày'" v-model="data.date")
          v-list-item
            v-text-field(:label="'Nhập tên'" v-model="data.name")
          v-list-item
            v-text-field(:label="'Nhập tuổi'" type="number" v-model="data.age")
          v-list-item
            v-text-field(:label="'Nhập tỉnh thành'" v-model="data.province")
          v-list-item
            v-text-field(:label="'Nhập giới tính'" v-model="data.sex")
          v-list-item
            v-text-field(:label="'Nhập lý do (không bắt buộc)'" v-model="data.reason")
          v-list-item
            v-text-field(:label="'Bệnh nền (không bắt buộc)'" v-model="data.backgroundDisease")
          v-list-item
            input(type="file" id="file" ref="file" v-on:change="handleFileUpload()")
          v-img(max-width="100" max-height="100" src="url")

        v-card-actions
          v-btn.relative-btn(
            :large="!$vuetify.breakpoint.xsOnly"
            block
            color="rough_black"
            @click="clickOK()"
          ) Ok
</template>

<script lang="ts">
import axios from 'axios'
import moment from 'moment'
const AddPatientDialog = {
  name: 'AddPatientDialog',
  props: {
    value: {
      type: Boolean,
      required: true
    }
  },
  data () {
    return  {
      baseUrl: 'http://127.0.0.1:8000',
      chosenFile: null,
      show: true,
      file: '',
      url: '',
      data: {
        name: '',
        date: moment().format('YYYY-MM-DD'),
        age: '',
        sex: '',
        reason: '',
        status: '',
        province: '',
        backgroundDisease: ''
      }
    }
  },
  methods: {
    close (data) {
      this.$emit('on-close', this.data)
    },
    async clickOK () {
      let formData = new FormData();
      formData.append('file', this.file);
      const nameImg = await axios.post(`${this.baseUrl}/image`, formData)
      const dataPatient = {
        date: this.data.date,
        name: this.data.name,
        age: this.data.age,
        province: this.data.province,
        sex: this.data.sex,
        reason: this.data.reason,
        background_disease: this.data.backgroundDisease,
        img_name: nameImg.data.name
      }
      // await axios.post(`${this.baseUrl}/add_patient`, dataPatient)
      // this.url = `https://backendlinhmai.herokuapp.com/vector_image?name=${nameImg.data.name}`
      // this.$emit('set-img-name', nameImg.data)
      this.$emit('set-data-patient', dataPatient)
      this.close()
      // const url = await axios.get(`http://127.0.0.1:8000/vector_image?name=${nameImg.data.name}`)
    },
    async handleFileUpload () {
      this.file = this.$refs.file.files[0];
    },
  }
}
export default AddPatientDialog
</script>

<style lang="sass">
.title-color
  background-color: dimgrey
</style>