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
        span.white--text Training
        v-spacer
        v-btn(icon dark @click="close()")
          v-icon mdi-close

      div.pa-4
        v-row
          v-col(cols="4")
            span.pt-2 Tập ảnh có khối u
          v-col(cols="8")
            v-file-input(
              accept="image/*"
              multiple
              label="File input"
              v-model="dataSet.yes"
            )
        v-row
          v-col(cols="4")
            span.pt-2 Tập ảnh không khối u
          v-col(cols="8")
            v-file-input(
              accept="image/*"
              multiple
              label="File input"
              v-model="dataSet.no"
            )
        v-row
          v-col(cols="4")
            span.pt-2 Tập ảnh khối u
          v-col(cols="8")
            v-file-input(
              accept="image/*"
              multiple
              label="File input"
              v-model="dataSet.tumors"
            )
          v-btn(width="90%" style="margin-left: 5%" @click="submitImg()") Submit
      div.pa-4(v-if="isTraining")
        p Chương trình đang được training lại, bạn vẫn có thể thao tác bình thường mà không ảnh hưởng tới hiệu năng

</template>

<script lang="ts">
const TrainingMode = {
  props: {
    value: {
      type: Boolean,
      required: true
    }
  },
  data () {
    return {
      isTraining: false,
      dataSet: {
        yes: [],
        no: [],
        tumors: []
      }
    }
  },
  methods: {
    close () {
      this.$emit('on-close')
    },
    submitImg () {
      // if (this.dataSet.yes.length > 0 && this.dataSet.no.length > 0 && this.dataSet.tumors.length > 0) {
      //   this.isTraining = true
      // }
      this.isTraining = true
    }
  }
}
export default TrainingMode
</script>