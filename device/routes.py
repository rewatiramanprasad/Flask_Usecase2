from flask import Blueprint
from device.controller import *
from utility.auth import *

flask_blue=Blueprint('routes',__name__)

flask_blue.add_url_rule("/hour_wise/","hour_wise",hour_wise,methods=['GET'])
flask_blue.add_url_rule("/peak_consumption/","peak_consumption",peak_consumption,methods=['POST'])
flask_blue.add_url_rule("/send_duplicate_data","send_duplicate_data",select_duplicate_data,methods=['GET'])
flask_blue.add_url_rule("/send_missing_timestamp","send_missing_timestamp",select_missing_data,methods=['GET'])
flask_blue.add_url_rule('/fetch_all/','fetch_all',select_query,methods=['GET'])
flask_blue.add_url_rule('/fetch_all/','fetch_all',select_query,methods=['GET'])
flask_blue.add_url_rule('/authentication/','authentication',authentication,methods=['POST'])


