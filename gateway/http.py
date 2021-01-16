import logging
import json
from pytz import timezone
from datetime import datetime

import requests
from domain import message

from config import config

def post_message(data):
    data['deviceID'] = config.device_id

    try:
        response = requests.post(
            'http://'+ config.http_address+':'+config.http_port+'/api/device/message',
            json.dumps(data),
            headers={'Content-Type': 'application/json'})

        if response.status_code >= 400 and response.status_code < 600 :
            m = message.message_data()
            m.message = ' response server error ' + response.status_code
            post_message(m.get_Data())
            # logging.error(datetime_str() + " " + response.text)
    except requests.exceptions.RequestException as e:
        print('error : ', e)

def post_asynchronous(data):

    data['deviceID'] = config.device_id
    data['datetime'] = timezone('Asia/Tokyo').localize(data['datetime']).astimezone(timezone('UTC'))
    data['datetime'] = data['datetime'].strftime('%Y-%m-%dT%H:%M:%S%z')

    try:
        response = requests.post(
            'http://'+ config.http_address+':'+config.http_port+'/api/asynchronous/add',
            json.dumps(data),
            headers={'Content-Type': 'application/json'})

        if response.status_code >= 400 and response.status_code < 600 :
            m = message.message_data()
            m.message = ' response server error ' + response.status_code
            post_message(m.get_Data())
            # logging.error(datetime_str() + " " + response.text)
    except requests.exceptions.RequestException as e:
        print('error : ', e)

def post_cyclic(data):

    data['deviceID'] = config.device_id
    data['datetime'] = timezone('Asia/Tokyo').localize(data['datetime']).astimezone(timezone('UTC'))
    data['datetime'] = data['datetime'].strftime('%Y-%m-%dT%H:%M:%S%z')

    try:
        response = requests.post(
            'http://'+ config.http_address+':'+config.http_port+'/api/cyclic/add',
            json.dumps(data),
            headers={'Content-Type': 'application/json'})

        if response.status_code >= 400 and response.status_code < 600 :
            m = message.message_data()
            m.message = ' response server error ' + response.status_code
            post_message(m.get_Data())
            # logging.error(datetime_str() + " " + response.text)
    
    except requests.exceptions.RequestException as e:
        print('error : ', e)

def datetime_str():
    dt = datetime.now()
    return dt.strftime('%Y/%m/%d %H:%M:%S')