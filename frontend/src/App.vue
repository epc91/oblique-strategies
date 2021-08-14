<template>
  <div id="app">
    <div class="card">
      <div class="text" @click="randomId()">
        {{ data }}
      </div>
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
    this.data = 'Click here to select a random card'
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

  *, *::before, *::after {
      box-sizing: border-box;
  }
  #app {
    background-image: url('~@/assets/bg.png');
    background-size: cover;
    color: rgb(0, 0, 0);
    font-family: sans-serif;
    width: 100vw;
    height: 100vh;
    position: fixed;
    top: 0;
    left: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 25px;
    text-align: center;
  }
  .card {
    width: 9cm;
    height: 7cm;
    background-color: rgba(230, 230, 230, 0.7);
    border-radius: 10px;
    padding: 20px;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  .card:hover {
    background-color: rgb(0, 0, 0);
    color: rgba(204, 204, 204, 0.7);
  }
  .text {
    cursor: pointer;
  }
</style>
