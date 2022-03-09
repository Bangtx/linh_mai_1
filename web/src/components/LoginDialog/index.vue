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
          span.white--text Login
          v-spacer
          v-btn(icon dark @click="close()")
            v-icon mdi-close

        div.pa-4
          v-list-item
          v-row
            v-col(cols="4")
              div.mt-6.ml-2 User name
            v-col(cols="8")
              v-text-field(:label="'enter user name'" v-model="userName")

          v-row
            v-col(cols="4")
              div.mt-6.ml-2 Pass word
            v-col(cols="8")
              v-text-field(:label="'enter pass word'" type="password" v-model="passWord")

        v-card-actions
          v-btn.relative-btn(
            :large="!$vuetify.breakpoint.xsOnly"
            block
            color="rough_black"
            @click="clickLogin()"
          ) Login

</template>

<script lang="ts">
const LoginDialog = {
  name: 'LoginDialog',
  props: {
    value: {
      type: Boolean,
      required: true
    }
  },
  methods: {
    close () {
      this.$emit('on-close')
    },
    clickLogin () {
      if (this.userName === 'admin' && this.passWord === 'admin') {
        this.$emit('on-close')
        this.$emit('update-is-login')
        this.$emit('login-ok')
      }
    }
  },
  data() {
    return {
      userName: 'admin',
      passWord: 'admin'
    }
  }
}

export default LoginDialog
</script>

<style lang="sass">
.title-color
  background-color: dimgrey
</style>