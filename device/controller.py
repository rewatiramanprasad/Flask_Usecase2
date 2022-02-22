from flask import Flask, request
# from flask_jwt_extended.view_decorators import jwt_required
from utility.validation import *
from device.error_handler import *
from device.SQLcontroler import *
from device.error_handler import *
from flask_jwt_extended import *
from utility.compress import *



@jwt_required()
def hour_wise():
    current_user = get_jwt_identity()

    value = select_Hour_Wise()
    response = {
        'message': str(len(value))+" rows fetched",
        'data': value,
        'sucess': True,
        'user':current_user
    }
    response=compress(response)
    return response, 200

@jwt_required()
def peak_consumption():
    current_user = get_jwt_identity()
    data = request.get_json()
    valid = date_device(data)
    if valid[0]:
        value = peak(data["date1"], data["date2"], data["device"])
        message = str(len(value))+" rows fetched"
        status_code = 200
        flag = True

    else:
        message = valid[1]
        flag = False
        status_code = 400
        value = []

    response = {
        'message': str(len(value))+" fetched rows",
        'data': value,
        'sucess': flag,
        'user':current_user
    }
    response=compress(response)
    return response, status_code

@jwt_required()
def select_duplicate_data():
    current_user = get_jwt_identity()
    flag = True
    message = "rows affected"
    result = {}
    req = request.get_json()

    query = req["query"]

    valid_query = validate_duplicate(query)

    if(valid_query):

        query_data = execute_fetchall(query)

        result = {}
        message = "rows affected" + " "+str(len(query_data))
        flag = True

        for i in range(0, len(query_data)):
            result[i] = query_data[i]

    else:
        message = valid_query[1]
        flag = False
        result = {}


    response = {'success': flag,
                 'data': result,
                  'message': message,
                  'user':current_user}
    response=compress(response)


@jwt_required()
def select_missing_data():
    current_user = get_jwt_identity()
    req = request.get_json()
    flag = True
    message = "rows affected"
    result = {}
    device = req["device"]
    valid_query = validate_missingtime(device)
    if(valid_query):
        query_data=missing_Data(device)
        for i in range(0, len(query_data)):
            result[i] = query_data[i]
            message = message+" "+str(len(result))
    else:
        flag = False


    response = {'success': flag,
                 'data': result,
                'message': message,
                'user':current_user}

    response=compress(response)
    return response

@jwt_required()
def select_query():
    current_user = get_jwt_identity()
    success = True

    response = dict()
    res_list = selectAll()
    response = {

        'success': True,
        'data': res_list,
        'msg': str(len(res_list))+' rows fetched',
        'user':current_user
    }
    response=compress(response)

    return res_list, 200


