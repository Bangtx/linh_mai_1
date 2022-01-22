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
            v-text-field(:label="'Enter date'" v-model="data.date")
          v-list-item
            v-text-field(:label="'Enter name'" v-model="data.name")
          v-list-item
            v-text-field(:label="'Enter age'" v-model="data.age")
          v-list-item
            v-text-field(:label="'Enter sex'" v-model="data.sex")
          v-list-item
            v-text-field(:label="'Enter reason'" v-model="data.reason")
          v-list-item
            v-text-field(:label="'background disease'" v-model="data.backgroundDisease")
          v-list-item
            v-file-input(label="File input" filled repend-icon="mdi-camera")

        v-card-actions
          v-btn.relative-btn(
            :large="!$vuetify.breakpoint.xsOnly"
            block
            color="rough_black"
            @click="clickLogin()"
          ) Ok
</template>

<script lang="ts">
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
      show: true,
      data: {
        name: '',
        date: `${(new Date()).getUTCFullYear()}-${(new Date()).getUTCMonth() + 1}-${(new Date()).getDate()}`,
        age: '',
        sex: '',
        reason: '',
        status: '',
        backgroundDisease: ''
      }
    }
  },
  methods: {
    close () {
      this.$emit('on-close')
    }
  }
}
export default AddPatientDialog
</script>

<style lang="sass">
.title-color
  background-color: dimgrey
</style>