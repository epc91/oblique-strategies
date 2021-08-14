<template>
  <div>
    {{ data }}}
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      data: null
    }
  },
  components: {
  },
  mounted() {
    axios
    .get('http://127.0.0.1:8000/api/v1/cards/')
    .then(response => this.data = response.data)
  }
}
</script>

<style>
</style>
