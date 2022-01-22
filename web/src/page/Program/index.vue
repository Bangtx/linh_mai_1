<template lang="pug">
  div.pa-3
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
</style>