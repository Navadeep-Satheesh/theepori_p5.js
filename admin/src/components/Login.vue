<template>
    <div class="top-container">
      <div class="container">
        <p class="heading">Login!</p>
        <div class="login-container">
          <form>
            <label class="labels">Email</label>
            <div class="input-box">
              <input type="email" placeholder="Email" required v-model="username" />
            </div>
            <label class="labels">Password</label>
            <div class="input-box">
              <input
                type="password"
                placeholder="Password"
                required
                v-model="pwd"
              />
            </div>
            <button class="submit-btn" type="submit" v-on:click="tryUser($event)">
              Login
            </button>
          </form>
        </div>
      </div>
      <!-- <p>password : {{ pwd }}</p> -->
    </div>
  </template>
  <script>
  
  export default {
    name : "SignIn",
    data() {
      return {
        username: "",
        pwd: "",
      };
    },
    methods: {
      async tryUser(event) {
        event.preventDefault();
        
        fetch("http://127.0.0.1:5000/login", {
          method: "POST", 
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            username : this.username,
            password : this.pwd,
            user_type : "admin"
          })
        }).then((response)=>{
          if(response.status == 200){
            return response.json()
          }
        }).then((data)=>{
          localStorage.setItem("signin", "yes");
          localStorage.setItem("token", data['token'])
          window.location.reload()
        })
      },
    },
  };
  </script>
  <style scoped>
  .top-container {
    min-height: 100vh;
    min-width: 100vw;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .heading {
    margin-top: 30px;
    padding: 20px;
    font-size: 30px;
    margin-bottom: 25px;
    font-weight: 600;
  }
  .container {
    min-height: 60vh;
    min-width: 40vw;
    background-color: rgb(255, 255, 255);
    display: flex;
    flex-direction: column;
    align-items: center;
    box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;
  }
  .login-container {
    display: flex;
  
    width: 60%;
    flex-direction: column;
  }
  .input-box {
    padding: 20px;
    width: 80%;
  
  
  }
  .input-box input{
    padding: 5px;
    width: 100%;
  } 
  
  .labels {
    padding: 20px;
  }
  .input {
    min-height: 6vh;
    
  }
  .submit-btn {
    width: 10vw;
    height: 3vh;
    margin: 18px;
    background-color: black;
    padding: 15px 10px;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
  
  }
  </style>
  