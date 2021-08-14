<template>
  <div id="app">
    {{ data }}
    <div>
      <button @click="randomId()">Random</button>
    </div>
  </div>

</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      data: null,
      total: null,
      idCard: null,
    }
  },
  components: {
  },
  mounted() {
    this.data = 'Press choose to draw a random card'
    this.getTotal()
  },
  methods: {
    // GET TOTAL
    getTotal() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/v1/cards/',
      })
      .then(response => this.total = response.data['count'])
    },
      // GET CARD
      getCard(id) {
        axios({
          method: 'get',
          url: 'http://127.0.0.1:8000/api/v1/cards/' + id
        })
        .then(response => this.data = response.data['description'])
      },
    // RANDOM ID
    randomId() {
      this.idCard = Math.floor((Math.random() * this.total) + 1)
      this.getCard(this.idCard)
    },
  },
  
}
</script>

<style>
</style>
