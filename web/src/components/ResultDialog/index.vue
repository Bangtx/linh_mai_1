<template lang="pug">
  v-dialog(
      persistent
      scrollable
      max-width="1800"
      :value="value"
      @input="dialog => $emit('input', dialog)"
    )
      v-card
        v-card-title.title-color(color="red")
          span.white--text Result
          v-spacer
          v-btn(icon dark @click="close()")
            v-icon mdi-close

        div.pa-4.content
          v-row
            v-col.pa-0(cols="9")
              div.images
                v-img.im(max-width="700px" max-height="700px" :src="url")
            v-col.pa-0(cols="3")
              div.result
                v-tabs(
                  v-model="tab"
                  align-with-title
                )
                  v-tabs-slider(color="red")

                  v-tab(
                    v-for="(item, index) in tabs"
                    item-text="name"
                    item-value="key"
                    :key="index"
                  ) {{ item.key }}
                v-tabs-items(v-model="tab")
                  v-tab-item(
                    v-for="(item, index) in tabs"
                    :key="index"
                  )
                    v-card(flat)
                      div.bg-result
                        h3.white--text Khuyến nghị
                        span.white--text(v-if="tab === 0 && imgName.yes") {{ result[index].recommend }}
                        span.white--text(v-if="tab === 0 && !imgName.yes") Theo dõi sức khỏe
                        v-text-field.white--text(v-if="tab === 1")

                      div.bg-result
                        h3.white--text Kết luận
                        span.white--text(v-if="tab === 0  && imgName.yes") {{ result[index].result }}
                        span.white--text(v-if="tab === 0 && !imgName.yes") 98% Không có khối u
                        v-text-field.white--text(v-if="tab === 1")
              v-img.ml-16(max-width="300" max-height="300" :src="urlSmall")
</template>

<script lang="ts">
import axios from 'axios'

const ResultDialog = {
  name: 'ResultDialog',
  props: {
    value: {
      type: Boolean,
      required: true
    },
    imgName: {
      type: Object,
      required: true
    }
  },
  data () {
    return {
      tab: 'Bác sĩ',
      url: '',
      urlSmall: '',
      tabs: [
        { name: 'ai', key: 'AI' }, { name: 'docter', key: 'Bác sĩ' }
      ],
      result: [
        { recommend: 'Lấy mẫu sinh thiết và phẫu thuật loại bỏ', result: '95% khả năng ung thư'},
        { recommend: 'Lấy mẫu sinh thiết và phẫu thuật loại bỏ', result: '96% khả năng ung thư'}
      ]
    }
  },
  methods: {
    close () {
      this.$emit('on-close')
    },
    async getUrl () {
      this.url = `https://backendlinhmai.herokuapp.com/vector_image?name=${this.imgName}`
    }
  },
  watch: {
    value (val) {
      if (val) {
        this.url = `https://backendlinhmai.herokuapp.com/vector_image?name=${this.imgName.name}`
        this.urlSmall = this.url
        if (this.imgName.yes) {
          this.urlSmall = `https://backendlinhmai.herokuapp.com/vector?name=${this.imgName.name}`
        }
      }
    }
  }
}
export default ResultDialog
</script>

<style lang="sass">
.title-color
  background-color: #212f38
.content
  height: 100vh
  background-color: #2d4a5c
.content-bottom
  background-color: #2d4a5c
.images
  color: white
  border: 2px solid white
.result
  color: white
  border: 2px solid white
.bg-result
  background-color: #2d4a5c
  height: 20vh
.im
  margin-left: 15%
</style>