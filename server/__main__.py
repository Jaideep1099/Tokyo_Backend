from flask_pymongo import PyMongo

from .DataClasses import*
from .Utils import *
from . import *

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
        return jsonify({"ERROR":"NOT_JSON"})

@app.route('/signin',methods=['POST'])
def signIN():
    if(request.is_json):
        details=request.get_json()
        un=details['uname']
        pwd=details['passwd']
        
        #print(f"uname={un} pwd={pwd}")

        pwd = hashPwd(pwd)

        dat = mongo.db.StudentList.find_one({"RollNo":un})
        if dat==None:
            return jsonify({"token":"Invalid User"})
        else:
            cur = mongo.db.OnlineList.find_one({"RollNo": dat['RollNo']})
            if cur==None:
                cur = mongo.db.OnlineList.insert_one({"RollNo":dat['RollNo']})
                cur = mongo.db.OnlineList.find_one({"RollNo":dat['RollNo']})
                token = str(cur["_id"])
                return jsonify({"token":token})
            else:
                return jsonify({"ERROR":"USER_ALREADY_LOGGED_IN"})
    else:
        print("Received data is not json")
        return jsonify({"ERROR":"NOT_JSON"})


@app.route('/signup',methods=['POST'])
def signUP():
    details=request.get_json()
    stud = Student(
        Name = details['name'],
        RollNo = details['uname'],
        Gender = details['gnd'],
        BGroup = details['bgroup'],
        Mob = details['mob'],
        Pwd = hashPwd(details['passwd'])
    )
    try:
        cur = list(mongo.db.StudentList.find({"RollNo":stud.RollNo}))
        if len(cur)!=0:
            return jsonify({"ERROR":"USER_ALREADY_EXISTS"})
        else:
            cur = mongo.db.StudentList.insert_one(stud._dict())
            return jsonify({"status":"done"})            
    except:
        return jsonify({"ERROR":"DATABASE_CONNECTION_ERROR"})

if __name__=='__main__':
    app.run(host='0.0.0.0',port='8000')