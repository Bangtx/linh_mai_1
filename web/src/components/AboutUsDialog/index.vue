<template lang="pug">
  div
    v-dialog(
      persistent
      scrollable
      max-width=1000
      :value="value"
      @input="dialog => $emit('input', dialog)"
    )
      v-card
        v-card-title.title-color(color="red")
          span.white--text About us
          v-spacer
          v-btn(icon dark @click="close()")
            v-icon mdi-close
        div
          v-img(
            width="100%"
            src="https://b.f9.photo.talk.zdn.vn/5445712682470814763/81b3cdbfc34b0c15555a.jpg"
          )
</template>

<script lang="ts">
const AboutUsDialog = {
  props: {
    value: {
      type: Boolean,
      required: true
    }
  },
  methods: {
    close() {
      this.$emit('on-close')
    },
  }
}

export default AboutUsDialog
</script>

<style lang="sass"></style>