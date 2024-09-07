<template>

  <NavBar></NavBar>


  <Signin v-if="signed_in==false"></Signin>
  <router-view v-else ></router-view>
 
</template>

<script>

// import AllRooms from "./components/AllRooms.vue"

import NavBar from "./components/Navbar.vue"
import SignIn from "./Ski/Login.vue"

export default {
  name: 'App',
  components: {

    // AllRooms : AllRooms,
    NavBar: NavBar,
    Signin : SignIn
  },

  data(){
    return{
      signed_in: false
    }
  },

  mounted() {

    let signin= localStorage.getItem("signin")
    if(signin){
      this.signed_in =  true
    }
  }
}
</script>

<style>

*{
  padding: 0px;
  margin: 0px;
  font-family: sans-serif
}

</style>
