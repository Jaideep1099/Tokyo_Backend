from flask import Flask,request,jsonify
from flask_pymongo import PyMongo
import hashlib

app = Flask("TokyoServer")
app.config['MONGO_URI']= "mongodb://127.0.0.1:27017/NITCHC"
mongo = PyMongo(app)

@app.route('/test',methods=['POST'])
def test():
    if(request.is_json):
        print("json data received")
        data=request.get_json()
        d = request.headers
        print(d)
        nam=data['name']
        print("Name received",nam)
        return jsonify({'result':'success'})
    else:
        print("Not json")
        return jsonify({"result":"Invalid data: Not json"})

@app.route('/signin',methods=['POST'])
def signIN():
    if(request.is_json):
        details=request.get_json()
        un=details['uname']
        pwd=details['passwd']
        
        print(f"uname={un} pwd={pwd}")
        pwd=hashlib.sha512(pwd.encode()).hexdigest()

        dat = mongo.db.StudentList.find_one({"RollNo":un})
        try:
            login = (dat["Pwd"]==pwd)
            token = str(dat["_id"])
        except:
            return jsonify({"token":"Invalid User"})
        if(login):
            return jsonify({"token":token})
        else:
            return jsonify({"token":"Invalid Password"})
    else:
        print("Received data is not json")
        return jsonify({"token":"Invalid Input:Not JSON"})


@app.route('/signup',methods=['POST'])
def signUP():
    details=request.get_json()
    roll=details['uname']
    nm=details['name']
    gd=details['gnd']
    bg=details['bgroup']
    mob=details['mob']
    pwd=details['passwd']

    pwd=hashlib.sha512(pwd.encode()).hexdigest()
    try:
        cur = list(mongo.db.StudentList.find({"RollNo":roll}))
        if len(cur)!=0:
            return jsonify({"ERROR":"USER ALREADY EXISTS"})
        else:
            cur = mongo.db.StudentList.insert_one({"Name":nm, "RollNo":roll, "Gender":gd, "BGroup":bg, "Mob":mob, "Pwd":pwd})
            return jsonify({"status":"done"})            
    except:
        return jsonify({"ERROR":"DATABASE CONNECTION ERROR"})


if __name__=='__main__':
    app.run(host='0.0.0.0',port='8000')