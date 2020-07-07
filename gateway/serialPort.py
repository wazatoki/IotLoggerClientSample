import threading
import time
from datetime import datetime
import logging

import serial

from config import config
from gateway import http
from domain import cyclic_data,asynchronous

def map_asynchronous_data(data_array):

    log_data = asynchronous.Log_data()

    for item in asynchronous.index:
        if data_array[4] == item.get('code'):
            log_data.version = data_array[1]
            log_data.dt = datetime.strptime(data_array[2]+' '+data_array[3], '%d.%m.%Y %H:%M:%S')
            log_data.code = item.get('code')
            log_data.category = item.get('category')
            log_data.name = item.get('name')
            break

    return log_data

def map_cyclic_data(data_array):
    i = 3
    log_data = cyclic_data.Log_data()

    log_data.version = data_array[1]
    log_data.dt = datetime.strptime(data_array[2]+' '+data_array[3], '%d.%m.%Y %H:%M:%S')
    log_data.pven = data_array[1 + i]
    log_data.pint = data_array[6 + i]
    log_data.part = data_array[11 + i]
    log_data.deltap = data_array[21 + i]
    log_data.flow = data_array[24 + i]
    log_data.speed = data_array[27 + i]
    log_data.svo2 = data_array[30 + i]
    log_data.hct = data_array[36 + i]
    log_data.tven = data_array[39 + i]
    log_data.tart = data_array[42 + i]
    return log_data

def parse_data(recv_data):
    logging.info('sereal recive data is : ' + recv_data.decode('utf-8'))
    r = recv_data.strip(';').decode('utf-8')
    
    if r[0] == 'ZT':
        log_data = map_cyclic_data(r)
        http.post_cyclic(log_data)
    elif r[0] == 'MT':
        log_data = map_asynchronous_data(r)
        http.post_asynchronous(log_data)
    else:
        logging.info('sereal recive data is broken : ' + recv_data.decode('utf-8'))

def watch():

    comport = serial.Serial(config.serial_port, baudrate=115200, bytesize=8, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,timeout=1)
    recv_data = comport.readline()
    comport.close()
    parse_data(recv_data)
    t=threading.Timer(2, watch)
    t.start()

def start_watch():
    t=threading.Thread(target=watch)
    t.start()