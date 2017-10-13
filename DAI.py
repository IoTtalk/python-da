import time, DAN, requests, random

ServerIP = '127.0.0.1' #Change to your IoTtalk IP or None for autoSearching
Reg_addr = None # if None, Reg_addr = MAC address
profile1 = { 'dm_name' : 'Dummy_Device',
            'df_list' : ['Dummy_Sensor'],
            'is_sim': False,
            # None for autoNaming
            'd_name' : None  }
profile2 = { 'dm_name' : 'Dummy_Device',
            'df_list' : ['Dummy_Control'],
            'is_sim': False,
            # None for autoNaming
            'd_name' : None  }         
dan1 = DAN.DAN()
dan2 = DAN.DAN()
dan1.device_registration_with_retry(profile1, ServerIP, Reg_addr)
dan2.device_registration_with_retry(profile2, ServerIP, Reg_addr)

while True:
    try:
        #Pull data from a device feature called "Dummy_Control"
        value1=dan2.pull('Dummy_Control')
        if value1 != None:
            print (value1[0])

        #Push data to a device feature called "Dummy_Sensor"
        value2=random.uniform(1, 10)
        dan1.push ('Dummy_Sensor', value2)

    except requests.exceptions.ConnectionError:
        print("requests.exceptions.ConnectionError")
        dan1.device_registration_with_retry(profile1, ServerIP, Reg_addr)
        dan2.device_registration_with_retry(profile2, ServerIP, Reg_addr)
    time.sleep(1)
