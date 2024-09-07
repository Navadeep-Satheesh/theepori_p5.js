<template>
    <div class="book">


        <div class="message" v-show="show_message">

            <h3 v-text="message" ></h3>

        </div>

        <div class="timeline">

            <div class="date_section">

                <input type="date" class="timeline_date" @change="getSlots()" id="date">

            </div>

            <div class="timeline_div">

                <div class="marking_area">

                    <div v-for="booking in bookings" class="booked_area" :key="{ booking }"
                        v-bind:style="{ top: `${booking[0]}px`, height: `${booking[1] - booking[0]}px` }"> </div>

                </div>
                <div class="time_stamp_area">

                    <ul>
                        <li v-for="time in times" v-bind:key="time">{{ time }}</li>
                    </ul>

                </div>

            </div>

        </div>

        <div class="book_area">

            <div class="book_div">

                <h2>BOOK SLOT</h2>

                <input type="date" class="select_date" id  = "book_date">
                <div class="select_time"> <input type="time" id = "start_time" pattern="[0-9]{2}:[0-9]{2} [APap][mM]" > to 
                    <input type="time" id = "end_time"  pattern="[0-9]{2}:[0-9]{2} [APap][mM]"> </div>
                <input type="text" class="purpose" id = "purpose">
                <input type="submit" class="submit" value="BOOK" @click="submitData()">


            </div>

        </div>


    </div>
</template>

<script>


var bookings = [

    
]

var bookings_final = []

for (let item of bookings) {
    bookings_final.push([parseInt(convertTime(item[0])), parseInt(convertTime(item[1]))])


}

function convertTime(time) {


    let converted = 0
    let a = time.split(" ")[1]
    let t = time.split(" ")[0]
    let hours = parseInt(t.split(":")[0])
    if (a == "PM" && hours < 12) {
        hours += 12
    }

    hours -= 9

    let minutes = parseInt(t.split(":")[1])
    converted += hours * 100 + minutes



    let final = parseInt((converted / 1200) * (960 + 260))
    console.log(converted, final)

    return final


}

let times = []
let time;
for (let i = 9; i <= 21; i++) {

    let hour = i;
    let a = "AM"
    if (i > 12) {
        hour = i - 12;
        a = "PM"
    }

    time = `${hour}:00 ${a}`
    console.log(time)
    times.push(time)

}

console.log(bookings)


export default {
    name: "BookRoom",
    data: () => {
        return {

            times: times,
            bookings: bookings_final,
            message: "",
            show_message : false
        }
    },
    methods: {
        getSlots() {
            fetch("http://127.0.0.1:5000/getSlots", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    room_id: window.location.pathname.split('/').slice(-1)[0],
                    date: document.getElementById('date').value
                })
            }).then((response) => {

                return response.json();
            }).then((data) => {
                console.log(data)
                var bookings_final = []

                for (let item of data) {
                    bookings_final.push([parseInt(convertTime(item[0])), parseInt(convertTime(item[1]))])


                }
                this.bookings = bookings_final
            })
        },

        submitData(){

            let room_id = window.location.pathname.split('/').slice(-1)[0];
            let date =  document.getElementById("book_date").value
            let start_time = document.getElementById("start_time").value
            let end_time = document.getElementById("end_time").value
            let purpose = document.getElementById("purpose").value

            fetch("http://127.0.0.1:5000/bookSlot" , {
                method: "POST", 
                headers : {
                    "Content-Type": "application/json"
                }, 
                body : JSON.stringify({
                    room_id: room_id,
                    date: date , 
                    start_time : start_time , 
                    end_time: end_time , 
                    purpose : purpose, 
                    token : localStorage.getItem('token')
                })
            }).then((response)=>{
                    return response.json()
                }).then((data)=>{
                    console.log(data)
                    if(data['possible'] == 0){
                        this.message = "sorry the slot provided is conflicting with other slots"
                        this.show = true ;

                    }else{
                        this.message = "slot booked";
                        this.show_message = true
                    }
                    setTimeout(()=>{
                        this.show_message = false
                    } , 2000)
                })

        }
    }
}


</script>

<style scoped>
.book {
    width: 100vw;
    height: 100vh;
    padding-top: 120px;
    display: flex;
    justify-content: center;


}

.message{
    position: absolute;
    top: 50%;
    left: 050%;
    transform: translate(-50% , -50%);
    background-color: white;
    width: 60vw;
    height: 60vh;
    border: 1px solid rgb(183, 183, 183);
    box-shadow: rgba(0, 0, 0, 0.1) 0px 4px 12px;
    z-index: 40;
    display: flex;
    align-items: center;
    justify-content: center;


}

.message h3{

    font-size: 36px;
    color: rgb(110, 0, 0);
}

.book_area {
    width: 45%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center
}

.timeline {
    box-shadow: rgba(0, 0, 0, 0.1) 0px 4px 12px;
    border: 1px solid rgb(220, 220, 220);
    width: 45%;
    height: max-content;


}

.book_div {
    width: 90%;
    height: 400px;
    background-color: white;
    box-shadow: rgba(0, 0, 0, 0.1) 0px 4px 12px;
    border: 1px solid rgb(222, 222, 222);

    display: flex;


    flex-direction: column;
}

.book_div h2 {
    margin-left: 50px;
    margin-top: 25px;
    font-size: 29px;
}

.book_div input {
    margin-top: 35px;
    font-size: 16px;
    margin-left: 50px;

}

.timeline_date {

    font-size: 18px;
    padding: 5px;
}


.select_date {
    width: 40%;
    padding: 5px;
}

.select_time input {
    width: 20%;
    padding: 5px;
}

.purpose {
    padding: 5px;
    width: 80%;
}

.submit {

    width: min-content;
    padding: 8px 35px;
    background-color: black;
    color: white;
    border: 0px;
    margin-left: auto;
    border-radius: 5px;
}

.submit:hover {
    background-color: rgb(66, 66, 66);
}


.date_section {

    width: 80%;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px 0px;

}

.date_section input {

    font-size: 14px;

}

.time_stamp_area {

    width: 20%;
    height: 100%;
    background-color: rgb(225, 225, 225);
}

.marking_area {

    border: 1px solid rgb(215, 215, 215);
    width: 80%;
    height: 100%;

}


.timeline_div {

    display: flex;
    flex-direction: row;
    background-color: rgb(241, 241, 241);

    width: 45vw;

}

.time_stamp_area ul {
    list-style: none;
    display: flex;
    flex-direction: column;
    align-items: center;

}

.time_stamp_area ul li {
    margin-bottom: 80px;
    font-size: 17px;
    color: rgb(76, 76, 76);
    font-weight: 600;
    height: 20px;

}



.marking_area {

    position: relative;


}

.marking_area div {
    width: 100%;
    position: absolute;


    background-color: rgb(245, 148, 148);
}
</style>