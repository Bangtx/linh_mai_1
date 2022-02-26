<template lang="pug">
  v-dialog(
      persistent
      scrollable
      max-width=400
      :value="value"
      @input="dialog => $emit('input', dialog)"
    )
      v-card
        v-card-title.title-color(color="red")
          span.white--text List patient
          v-spacer
          v-btn(icon dark @click="close()")
            v-icon mdi-close

        v-card-text.pa-0
          div(v-for="patient in patients" :key="patient.id")
            v-list-item.item(@click="handleClickPatient(patient)")
              span.name {{ patient.name }}
              v-spacer
              v-icon mdi-chevron-right

</template>

<script lang="ts">
import axios from 'axios'

const ListPatientDialog = {
  name: 'ListPatientDialog',
  props: {
    value: {
      type: Boolean,
      required: true
    }
  },
  data() {
    return {
      // baseUrl: 'https://backendlinhmai.herokuapp.com',
      baseUrl: 'http://127.0.0.1:8000',
      patients: []
    }
  },
  methods: {
    close () {
      this.$emit('on-close')
    },
    async getData () {
      const { data } = await axios.get(`${this.baseUrl}/get_patients`)
      this.patients = data
      console.log(this.patients)
    },
    handleClickPatient (patient) {
      this.$emit('click-patient', patient)
      console.log(patient.img_name, 12)
    }
  },
  watch: {
    value (val) {
      if (val) {
        this.getData()
      }
    }
  }
}

export default ListPatientDialog
</script>

<style lang="sass">
.name
  font-size: 17px
  color: #111111
.item
  cursor: pointer
</style>