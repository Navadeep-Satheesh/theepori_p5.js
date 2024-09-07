<template>
    <div class="bookings">


        <h1>ALL BOOKINGS</h1>

        <div class="single_booking" v-for="booking in bookings" :key="booking[0]">

            <h3 class="stage_name">{{ booking[1] }}</h3>
            <h3 class="booked_date">{{ booking[2] }}</h3>
            <div class="time">
                <h3 class="start_time">{{ booking[3] }}</h3>
                <h3>TO</h3>
                <h3 class="end_time">{{ booking[4] }}</h3>
            </div>
            <div class="purpose">

                <!-- {{ booking[5] }} -->
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Debitis incidunt magnam deserunt ipsum adipisci
                ab, ipsa minima laudantium assumenda, doloribus omnis fugiat ad? Hic expedita, sapiente sed blanditiis
                commodi voluptates?


            </div>
            <div class="status">

                <div v-if="booking[6] == 0" class="buttom_buttons">

                    <button  @click="acceptBooking(booking[0])">ACCEPT</button>
                    <button @click="rejectBooking(booking[0])">REJECT</button>

                </div>

                <div v-else>

                    <span v-if="booking[6] == 1" class="status_span accepted"  >ACCPETED</span>
                    <span v-else-if="booking[6] == -1" class="status_span rejected" >REJECTED</span>

                </div>
            </div>

        </div>



    </div>
</template>

<script>

var bookings = [

    [1, "Sargam", "05 Aug 2024", "9:00 AM", "10:00 AM", "", 0],
    [1, "Sargam", "05 Aug 2024", "9:00 AM", "10:00 AM", "", 0],
    [1, "Sargam", "05 Aug 2024", "9:00 AM", "10:00 AM", "", -1],
    [1, "Sargam", "05 Aug 2024", "9:00 AM", "10:00 AM", "", -1],
    [1, "Sargam", "05 Aug 2024", "9:00 AM", "10:00 AM", "", -1],
    [1, "Sargam", "05 Aug 2024", "9:00 AM", "10:00 AM", "", 1],
    [1, "Sargam", "05 Aug 2024", "9:00 AM", "10:00 AM", "", 1],
    [1, "Sargam", "05 Aug 2024", "9:00 AM", "10:00 AM", "", 1],
    [1, "Sargam", "05 Aug 2024", "9:00 AM", "10:00 AM", "", 1],
    [1, "Sargam", "05 Aug 2024", "9:00 AM", "10:00 AM", "", 1]

]

export default {

    "name": "AdminPanel",
    "data": () => {
        return {

            bookings: bookings
        }
    },
    "methods": {

        getBookings() {

            fetch("http://127.0.0.1:5000/getAdminBookings", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    token: localStorage.getItem("token")
                })

            }).then((response) => {
                return response.json()
            }).then((data) => {
                this.bookings = data
                console.log(data)
            })
        },

        acceptBooking(booking_id) {
            fetch("http://127.0.0.1:5000/approve_request", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    booking_id: booking_id
                })

            }).then((response) => {
                console.log(response)
                this.getBookings()
            })

        },
        rejectBooking(booking_id) {
            fetch("http://127.0.0.1:5000/reject_request", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    booking_id: booking_id
                })

            }).then((response) => {
                console.log(response)
            
                this.getBookings()
            })

        }

        
    },
    mounted() {

        this.getBookings()
    }
}

</script>


<style>
h1 {
    text-align: left;

    width: 85%;
    font-size: 36px;
    margin-left: 10px;
}

.bookings {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-top: 150px;
}

.single_booking {

    border: 1px solid rgb(229, 229, 229);
    width: 80vw;
    box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
    margin: 10px;
    padding: 20px;
}

.stage_name {
    font-size: 30px;
    margin-bottom: 20px;
}

.booked_date {
    font-size: 14px
}

.time {
    display: flex;
    align-items: center;
    font-size: 14px;
}

.time h3 {
    font-size: 14px;
    margin-right: 5px;
}

.status {
    padding: 7px 10px;

    width: 100%;
    display: flex;
    justify-content: flex-end;
    color: white
}

.buttom_buttons {
    margin-top: 20px;

    display: flex;
    justify-content: flex-end;
}

.purpose {
    color: rgb(143, 143, 143)
}

.accepted {
    background-color: green;
}

.pending {
    background-color: orange;
}

.rejected {
    background-color: red;
}

.buttom_buttons button {
    margin: 10px;
    color: white;
    background-color: black;
    padding: 10px 15px;
    border: 0px;
}

.buttom_buttons button:hover {
    background-color: rgb(86, 86, 86);
}

.status_span {
    padding: 8px 10px;
    margin-right: 10px;
    border-radius: 4px;

}
</style>