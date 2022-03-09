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
    return {}
  },
  methods: {
    close () {
      this.$emit('on-close')
    },
  }
}
export default TrainingMode
</script>