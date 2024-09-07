![Vuejs notion](https://github.com/TH-Activities/saturday-hack-night-template/assets/117498997/b879ba9f-2057-431b-99db-e86a0010b1ea)
# BookMyStage

In our college campus  whenever there is an event like a workshop , orientation session , talk sessions , jamming sessions , competitions organized by various clubs and departments , we have to take the permission from the authorities though a request letter , To Make this process more easier for the colleges , we have introduced this platform where  coordinators of events can book a venue for their event online thought a web app and the authorities can verify the request and approve or reject them 
## Team members

1. [Navadeep Satheesh](https://github.com/Navadeep-Satheesh/)
2. [Meenakshi Sudhir](https://github.com/meenakshysudhir)
3. [Jiya Rose Joshy](https://github.com/j1i2y3a4)
4. [Renjith Rajan](https://github.com/Renjith312)




## How it Works ?

1.  There are two apps user app and admin app  , the user app is for the club coordinators and managers of the even where they can book venues 
2. The Person has login using a id and password provided ,
3. They have to select a stage from the list of stages and they will be redirected to the book page where they can see the availability of the venue on the date selected in a timeline chart , 
4. The can do the booking by filling the details and pressing the book button
5. The bookings that we have done and their status can be seen in the bookings tab 
6. The Admin can view the bookings and can either accept it or reject it 


## Images 

### User

#### Login Page


![WhatsApp Image 2024-05-05 at 2 48 15 PM](https://github.com/Navadeep-Satheesh/theepori/assets/65801179/b775a4ff-8a6d-4312-a995-8d174232a390)


#### select the desired venue


![WhatsApp Image 2024-05-05 at 2 46 36 PM](https://github.com/Navadeep-Satheesh/theepori/assets/65801179/fa87ae14-5d5d-4b20-b390-5b431756853b)


#### Book the Slot


![WhatsApp Image 2024-05-05 at 2 47 53 PM](https://github.com/Navadeep-Satheesh/theepori/assets/65801179/dbe296c7-6363-4d47-be3d-7af104d599d6)
![WhatsApp Image 2024-05-05 at 2 48 15 PM](https://github.com/Navadeep-Satheesh/theepori/assets/65801179/167ca0e6-455b-4e9d-a3cd-030cc7f11c57)


#### View Your Bookings



![WhatsApp Image 2024-05-05 at 2 46 56 PM](https://github.com/Navadeep-Satheesh/theepori/assets/65801179/72ed5cf4-db18-4ee3-9d3d-cf4e4b915e91)


### Admin

#### approve or reject bookings

![WhatsApp Image 2024-05-05 at 3 02 25 PM](https://github.com/Navadeep-Satheesh/theepori/assets/65801179/07414a84-d1d0-4273-8dc6-50c0987542c8)

## Libraries used

1. Vue.js for front end
2. flask as Backend
3. Sqllite as database

## How to configure

run ```
```bash
npm install  # to install the required modules 
vue serve # to run the vue project
```

##### note
vue serve sometimes dont work with powershell , in such case either run it other terminals like git bash and cmd

## How to Run

##### User app

inside the frontend/frontent/ 
run **vue serve** to to run the user app

##### Admin App
inside the admin/ folder
run **vue serve** to run admin app 

##### Backend 

inside the backend folder 
run **python app.py**  to the flask server

### login credentials 

#### for user app

email : tinkerhub@gmail.com
password : 1234

#### for the admin app
email: principal@gmail.com
password : 1234

