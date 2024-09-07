from flask import Flask, request,jsonify,session , make_response
from database_helper import adminLogin, userLogin , connect
from flask_cors import CORS
from functools import wraps
import jwt


app = Flask(__name__)
app.config['SECRET_KEY'] = "dfasdf"
CORS(app, origins=["http://localhost:8080","http://localhost:5001"])



def token_required(f):
    @wraps(f)
    def decorated(*args , **kwargs):
        token = request.json.get("token")
        print(token)
        # print("the token is ", token)
      
        try:
            payload = jwt.decode(token , app.config["SECRET_KEY"] , algorithms=["HS256"],ignoreExpiration =  True)
        except:
            return ('' , 401)

        return f(*args , **kwargs)
    return decorated

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user_type = data.get('user_type')
    username = data.get('username')
    password = data.get('password')
    print(user_type , username , password)
    if user_type == 'admin':
        admin = adminLogin(username, password)
        print(admin)
        if admin:
            token = jwt.encode({"admin_id": admin[0]}, app.config['SECRET_KEY'])
            
            response = make_response(jsonify({'message': '1' , 'token' : token}))
            response.status_code = 200
            return response
            
        else:
            return jsonify({'message': '0'}), 401
    else:
        user = userLogin(username, password)
        print(user)
        if user:
            print("here")
            token = jwt.encode({"user_id": user[0]}, app.config['SECRET_KEY'])
            print(token)
            response = make_response(jsonify({'message': '1' , 'token' : token}))
            
            response.status_code = 200

            return response
        else:
            return jsonify({'message': '0'}), 401


@app.route("/getAllBookings" , methods = ["GET", "POST"])
@token_required
def getAllBookings():
    
    connection , cursor = connect()
    
    cursor.execute("select * from bookings")
    data = cursor.fetchall()
    return ( jsonify(data), 200)
  

@app.route("/getSlots" , methods = ["GEt", "POST"])
def getSlots():
    d = request.json 
    room_id = d.get("room_id")
    date = d.get("date")
    print(date)
    print(room_id)
    connection , cursor =  connect()
    query = f"select start_time , end_time from bookings where  room_id = '{room_id}' and scheduled_date = '{date}'"
    print(query)
    cursor.execute(query)

    data = cursor.fetchall()

    return ( jsonify(data), 200 )


@app.route("/bookSlot", methods =["POST"])
def bookSlot():
    d = request.json 
    date = d.get("date")
    start_time = d.get("start_time")
    end_time = d.get("end_time")
    room_id = d.get("room_id")
    purpose = d.get("purpose")
    token = d.get("token")

    d = jwt.decode(token , app.config['SECRET_KEY'] , algorithms=['HS256'])
    user_id = d.get("user_id")

    print( date, start_time , end_time , room_id , purpose , token)

    connection , cursor = connect()
    

    query = f"select * from bookings b where scheduled_date = '{date}' and ( ( '{start_time}' >b.start_time and '{start_time}' < b.end_time  ) or ( '{end_time}' > b.start_time and '{end_time}' < b.end_time ))" 
    print(query)
    cursor.execute(query)
    data = cursor.fetchall()

    

    if len(data) == 0:
        possible = True 
    else:
        possible = False

    print(len(data))

    if possible:
        cursor.execute("select * from bookings")
        lenth = len(cursor.fetchall())
        query = f"insert into bookings( booking_id , user_id , scheduled_date , booking_date , start_time , end_time , purpose , status , room_id) values( {lenth +1}, {user_id} , '{date}' , date('now'), '{start_time}'  , '{end_time}' , '{purpose}' , 0 , {room_id} )"
        print(query)
        cursor.execute(query)
        connection.commit()

    return jsonify( { 'possible': possible }, 200)

    
@app.route("/getUserBookings", methods = ["GET", "POST"])
def getUserBookings():
    
    connection , cursor = connect()
    token = request.json.get("token")
    print(token)
    d = jwt.decode(token , app.config['SECRET_KEY'] , algorithms=['HS256'])
    user_id = d.get("user_id")
    print(user_id)
    cursor.execute(f"select booking_id , room_name , scheduled_date , start_time , end_time , purpose,  status from bookings, rooms  where   bookings.room_id = rooms.room_id and  user_id = {user_id}")
    data = cursor.fetchall()
    return ( jsonify(data), 200)

    
@app.route("/getAdminBookings", methods = ["GET", "POST"])
def getAdminBookings():
    
    connection , cursor = connect()
    token = request.json.get("token")
    print(token)
    
  
 
    cursor.execute(f"select booking_id , room_name , scheduled_date , start_time , end_time , purpose,  status from bookings, rooms  where   bookings.room_id = rooms.room_id")
    data = cursor.fetchall()
    return ( jsonify(data), 200)


    
@app.route("/approve_request" , methods = ["GET", "POST"])
def apporove_request():
    connection ,cursor = connect()
    
    booking_id = request.json.get("booking_id")
    cursor.execute(f"update bookings set status = 1 where booking_id = {booking_id}")
    connection.commit()
    return ('' , 200)
  
    


@app.route("/reject_request", methods  = ["GET", "POST"])
def reject_request():
    connection , cursor =  connect()
   
    booking_id = request.json.get("booking_id")
    cursor.execute(f"update bookings set status = -1 where booking_id = {booking_id}")
    connection.commit()
    return ('' , 200)
    
    


    

app.run(debug = True)