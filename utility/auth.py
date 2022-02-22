from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import *
from flask import jsonify
from flask import Flask,request
from utility.validation import *
from device.SQLcontroler import *
import hashlib
def authentication():
    flag=True
    message=None
    value=None
    data=request.get_json()
    valid=credential(data)
    if valid[0]:
        mdpass = hashlib.md5(data["password"].encode("utf-8")).hexdigest() #For MD5 hash
        value=checking_credential(data["email"],mdpass)
        if value :
            access_token = create_access_token(identity=data["email"])
            return jsonify(access_token=access_token,success=True,message=" Token sucessfully generated "),200
            
        return jsonify(data={},success=False,message="wrong combination of email and password"),400
    else:
        message=valid[1]
    return "login failed "



# @jwt_required()
# def protected():
#     current_user = get_jwt_identity()
#     return jsonify(logged_in_as=current_user), 200
