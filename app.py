from flask import *
import json
from utility.db import *
from device.routes import *
from device.error_handler import page_not_found
import sys
from utility.validation import *
from device.SQLcontroler import *

app = Flask(__name__)
app.register_blueprint(flask_blue)
app.register_error_handler(Exception, page_not_found)


# app.register_blueprint(flask_query)
app.config["SECRET_KEY"]='mHKoDFdVP8PYztn0'
jwt = JWTManager(app)



if __name__ == '__main__':
    # sys.path.append('C:\\Users\\RAJAT\\Desktop\\ncompassPYTHON\\rajat')
    config = open("config/config.json", "r").read()
    data=json.loads(config)
    
    app.run(debug=True,host=data["host"],port=data["port"])
    
