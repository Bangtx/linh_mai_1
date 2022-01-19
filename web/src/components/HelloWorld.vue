<template>
  <div class="hello">
    <h1 @click="myClick">{{ name }}</h1>
    <header></header>
  </div>
</template>

<script lang="ts">
import { defineComponent } from '@vue/composition-api'

const HelloWorld = defineComponent({
  setup() {
    const name = 'hehe'
    const myClick = () => {
      console.log('hshs')
    }
    return {
      name,
      myClick
    }
  }
})
export default HelloWorld
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
