import os
import logging

# coding: utf-8
import configparser

# --------------------------------------------------
# configparserの宣言とiniファイルの読み込み
# --------------------------------------------------
config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')
config_default = config_ini['default']

http_address = config_default.get('address')
http_port = config_default.get('port')
serial_port = config_default.get('serial_port')
device_id = config_default.get('device_id')

logging.basicConfig(filename = '.' + os.sep + 'log' + os.sep + 'logger.log', level=logging.INFO)
