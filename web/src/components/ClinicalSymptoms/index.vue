<template lang="pug">
  div
    v-list-item.ttls
      v-spacer
      span.white--text.pa-4 TRIỆU CHỨNG LÂM SÀNG
      v-spacer
    hr
    div(v-for="(item, index) in symptoms")
      div.ttls-content.pa-2
        span.white--text {{ item.name }}
        v-slider.mt-9.white--text(:label="'Mức độ'" :thumb-color="thumColor[index]" thumb-label="always" v-model="value[index]")
    v-list-item
      v-spacer
      v-btn.mt-10(@click="$emit('open-dialog')") Submit
</template>

<script lang="ts">

const ClinicalSymptoms = {
  props: {
    value: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
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
        { name: 'Đau đầu thường xuyên và nghiêm trọng' },
        { name: 'Thay đổi tính cách, hành vi và suy nghĩ' },
        { name: 'Rối loạn chức năng hoặc nhầm lẫn trí nhớ' },
        { name: 'Nghe bất thường' },
        { name: 'Giao tiếp cản trở' },
        { name: 'Vấn đề cân bằng' },
        { name: 'Buồn nôn, nôn mửa và buồn ngủ' },
        { name: 'Tê tay chân' }
      ]
    }
  }
}
export default ClinicalSymptoms
</script>

<style lang="sass">
.ttls-content
  width: 50%
  border: 2px solid #2b6e7f
  float: left
  span
    font-size: 22px
</style>