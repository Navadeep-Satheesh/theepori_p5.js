<template>

  <SignIn v-if="signin==false"></SignIn>
  <AdminPanel v-else ></AdminPanel>

 
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import SignIn from "./components/Login.vue"
import AdminPanel from "./components/Admin.vue"

export default {
  name: 'App',
  data: ()=>{
    return{
      signin: false
    }
  },
  components: {
    SignIn : SignIn ,
    AdminPanel : AdminPanel
  },
  mounted(){

    if( localStorage.getItem("signin")=="yes"){
      this.signin= true
    }else{
      this.signin= false
    }

  }
 
}
</script>

<style>


*{
  font-family: sans-serif
}

</style>
