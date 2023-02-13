import socket
from flask   import Flask ,request

from flask_pymongo import PyMongo

from bson.json_util import dumps

from bson.objectid import ObjectId

from flask import jsonify,request

from werkzeug.security import  generate_password_hash,   check_password_hash

from pymongo   import MongoClient
import base64

from flask import make_response





app = Flask(__name__)

app.secret_key="secretkey"


client = MongoClient ("mongodb+srv://tree:tree@cluster0.8hhaxuz.mongodb.net/?retryWrites=true&w=majority")
db = client["upcl"]




# mongo = MongoClient(app)


@app.route('/add',methods =['POST' ])
def kkumh():
    _json =request.json
    _consumer =_json['consumer']
    _registration_moblie_no = _json['reg']



    if  _consumer and _registration_moblie_no and  request.method =='POST' :

        db.view_bill.insert_one({'consumer':_consumer,
                                'reg':_registration_moblie_no})




        resp = jsonify("User add successfully")

        resp._status_code = 200

        return resp

    else:
        return not_found()




@app.route('/users',methods =['GET'])
def yhth():
    users =  db.view_bill.find()
    resp = dumps(users)
    return resp



@app.route('/user/<id>' ,methods =['GET'])
def ghjkk(id):
    user = db.view_bill.find_one({'id ':  id})
    resp = dumps(user)
    return resp




@app.route('/delete_v/<id>',methods=['DELETE'])
def delete_klhk(id):
    db.view_bill.delete_one({'id': ObjectId(id)})
    resp = jsonify("user deleted successfully")


    resp.status_code = 200

    return resp





app.route('/update_u/<id>',methods=['PUT'])
def update_n(id):
    _id = id
    _json = request.json
    _consumer = _json['consumer']
    __registration_moblie_no = _json['reg']
    if _consumer and   __registration_moblie_no and request.method =='PUT':



        db.view_bill.update_one({'_id':ObjectId(_id['$oid'])  if '$oid' in _id else ObjectId(_id)},{'$set': {"consumer" : _consumer,"reg":__registration_moblie_no}})
        resp = jsonify("user updated successfully")


        resp.status_code = 200

        return resp

    else:
        return not_found




@app.route('/image/<image_id>')
def retrieve_image(image_id):
    image = db.images.find_one({'_id': ObjectId('63e1f714418856f2ca268ade')})
    if not image:
        return "Image not found", 404

    image_data = image['image']
    encoded_image = base64.b64encode(image_data).decode('utf-8')
    response = make_response(encoded_image)
    response.headers['Content-Type'] = 'image/jpeg'
    return response




@app.errorhandler(404)
def not_found(error =None):
    message ={
        'status':404,
        'message':"not found" + request.url

    }
    resp =jsonify(message)

    resp.status_code=404

    return resp



socket.getaddrinfo('localhost', 4000)



if __name__=="__main__":
    app.run(host='127.0.0.2', port =5000)