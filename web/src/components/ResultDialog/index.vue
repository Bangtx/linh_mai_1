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
                v-row
                  v-col(cols="9")
                    v-img.im(max-width="80%" max-height="700px" :src="url")
                  v-col(cols="3")
                    v-img(max-width="90%" max-height="300" :src="urlSmall")
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
                v-tabs-items.controls(v-model="tab")
                  v-tab-item(
                    v-for="(item, index) in tabs"
                    :key="index"
                  )
                    v-card(flat)
                      div.bg-result
                        h3.white--text Khuyến nghị
                        span.white--text(v-if="tab === 0 && imgName.yes") {{ result[index].recommend }}
                        span.white--text(v-if="tab === 0 && !imgName.yes") Theo dõi sức khỏe
                        v-text-field.whitetext(v-if="tab === 1" :value="checkbox ? should : ''")

                      div.bg-result
                        h3.white--text Kết luận
                        span.white--text(v-if="tab === 0  && imgName.yes") {{ result[index].result }}
                        span.white--text(v-if="tab === 0 && !imgName.yes") 98% Không có khối u
                        v-text-field.whitetext(v-if="tab === 1" :value="checkbox ? resultAI : ''")

                      v-checkbox(v-model="checkbox" :label="'Tự đông lấy kêt quả AI'")
                      v-row
                        v-col(cols="1")
                        v-col(cols="4")
                          v-btn(color="#66bed6" width="100%" @click="handleClick()")
                            v-icon(color="white") mdi-download
                            span.white--text Lưu
                        v-col(cols="2")
                        v-col(cols="4")
                          v-btn(color="#89322b" width="100%" @click="deletePatient")
                            v-icon(color="white") mdi-delete
                            span.white--text Xóa

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
    },
    patientId: {
      type: Number,
      required: true
    }
  },
  data () {
    return {
      should: 'Theo dõi sức khỏe',
      resultAI: 'Không có khối u',
      checkbox: false,
      tab: 'Bác sĩ',
      url: '',
      urlSmall: '',
      tabs: [
        { name: 'ai', key: 'AI' }, { name: 'docter', key: 'Bác sĩ' }
      ],
      result: [
        { recommend: 'Lấy mẫu sinh thiết và phẫu thuật loại bỏ', result: '95% khả năng ung thư'},
        { recommend: 'Lấy mẫu sinh thiết và phẫu thuật loại bỏ', result: '96% khả năng ung thư'}
      ],
      baseUrl: 'http://45.117.80.122:8000'
      // baseUrl: 'https://backendlinhmai.herokuapp.com'
    }
  },
  methods: {
    close () {
      this.$emit('on-close')
    },
    async getUrl () {
      this.url = `${this.baseUrl}/vector_image?name=${this.imgName}`
    },
    async deletePatient () {
      await axios.delete(`${this.baseUrl}/delete_patient/${this.patientId}`)
      this.close()
    },
    handleClick () {
      alert('Đã lưu')
    }
  },
  watch: {
    value (val) {
      if (val) {
        this.url = `${this.baseUrl}/vector_image?name=${this.imgName.name}`
        this.urlSmall = this.url
        if (this.imgName.yes) {
          this.urlSmall = `${this.baseUrl}/vector?name=${this.imgName.name}`
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
  border: 2px solid white
.result
  border-radius: 25px
.bg-result
  background-color:  #0b1e2f
  height: 10vh
.im
  margin-left: 10%
.controls
  height: 33vh
  border-radius: 10px
.whitetext input
  color: white !important
</style>