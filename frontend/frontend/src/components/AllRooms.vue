<template>
    <div class="all_rooms">


        <div class="rooms_list">

            <div class="single_room" v-for="room in rooms" :key="room[0]">

                <router-link  class= "book_link" :to="`/book/${room[0]}`" >

                    <h3 class="stage_title">{{ room[1] }}</h3>
                    <h3 class="stage_location">{{ room[2] }}</h3>
                    <p class="stage_desc">
                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Porro dolore autem dolorum animi
                        temporibus veniam labore ab modi? Nesciunt, unde! Nemo, doloremque modi dignissimos accusamus
                        reiciendis, obcaecati voluptatum consectetur repellendus cum qui voluptatibus odit atque officia
                        quas quam necessitatibus impedit nisi debitis ducimus quae? Voluptatem explicabo maxime iure ad
                        molestiae.
                    </p>

                </router-link>


            </div>

        </div>


    </div>
</template>


<script>

export default {
    name: "AllRooms",
    data: () => {
        return {

            rooms: [

                [1, "CETAA HALL", "main block", ""],
                [2, "Sargam Stage", "main block", ""],
                [3, "Gazebo", "infront of canteen", ""],
                [4, "Dwani Stage", "beside gazebo", ""],
                [5, "CGPU Hall", "main block", ""],
                [6, "DJ Hall", "near indoor stadium gate", ""],
                [7, "Archi Corner", "infront of architechture entrance", ""],
                [8, "CS Seminar Hall", "cs block", ""],
            ]
        }
    }

}

</script>

<style scroped>
.all_rooms {
    background-color: rgb(255, 255, 255);
    height: 100vh;
    width: 100vw;
}

.book_link{
    text-decoration: none !important;
    color: black;
}

.rooms_list {

    display: grid;
    width: 100%;
    height: 100%;
    padding-top: 150px;
    /*background-color: red;*/
    grid-template-columns: repeat(auto-fit, minmax(300px, 320px));
    align-items: center;
    justify-content: center;
    gap: 40px;
}

.single_room {
    border: 1px solid rgb(209, 209, 209);
    box-shadow: rgba(50, 50, 93, 0.25) 0px 6px 12px -2px, rgba(0, 0, 0, 0.3) 0px 3px 7px -3px;
    width: 300px;
    height: 350px;
    padding: 20px;
    transition: 0.3s;


}

.single_room:hover {
    background-color: rgb(238, 238, 238);
}

.stage_title {

    font-size: 24px;
}

.stage_location {
    font-size: 17px;
    margin-top: 10px;
    font-weight: 500;
    color: rgb(158, 158, 158);
}

.stage_desc {
    margin-top: 40px;
    color: rgb(150, 150, 150);
}
</style>