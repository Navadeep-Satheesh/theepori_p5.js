<template>
    <div className = "navbar">


        <div class = "title">BookMyStage</div>

        <div></div>
        <span class = "side_links">
        <router-link class = "bookings_link" to = "/"><div class= "bookings"> Book</div></router-link>
        <router-link class = "bookings_link" to = "/bookings"><div class= "bookings"> Bookings</div></router-link>
        </span>
        
    </div>
</template>

<script>

export default {
    name: "NavBar"
}

</script>

<style scoped>

.navbar{
    position: fixed;
    width: 100vw;
    z-index: 100;
    height: 80px;
    background-color: white;
    box-shadow: rgba(50, 50, 93, 0.25) 0px 13px 27px -5px, rgba(0, 0, 0, 0.3) 0px 8px 16px -8px;
    display: flex;
    align-items: center;
    justify-content: space-between
}

.title{
    font-size: 28px;
    margin-left: 10px;
    color: rgb(190, 3, 3);
    font-weight: 600;
}

.side_links{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center
}

.bookings{

    font-size: 20px;
    margin-right: 20px;
    padding: 5px 10px;
    
    border-radius: 5px
}

.bookings:hover{
    color: rgb(222, 25, 25);
    cursor: pointer;
    background-color: rgb(255, 163, 163);
}


.bookings_link{
    text-decoration: none !important;
    color: black;
    
}

</style>