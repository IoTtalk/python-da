import time
import DAN
import requests
import random

ServerIP = '140.113.215.6' #Change to your VM IP

DAN.profile['dm_name']='Dummy_Device'
DAN.profile['d_name']='MyDummy'
DAN.profile['df_list']=['Dummy_Sensor', 'Dummy_Control']
DAN.device_registration_with_retry(ServerIP)

while True:
    try:
        #Pull data from a device feature called "Dummy_Control"
        value1=DAN.pull('Dummy_Control')
        if value1 != None:
            print (value1[0])

        #Push data to a device feature called "Dummy_Sensor"
        value2=random.uniform(1, 10)
        DAN.push ('Dummy_Sensor', value2)

    except requests.exceptions.ConnectionError:
        print("requests.exceptions.ConnectionError")
        DAN.device_registration_with_retry(ServerIP)

    time.sleep(1)