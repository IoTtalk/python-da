import time, DAN, requests, random

ServerIP = 'IP' #Change to your IoTtalk IP, or None for autoSearching
Reg_addr= None # if None, Reg_addr = MAC address

DAN.profile['dm_name']='Dummy_Device'
DAN.profile['df_list']=['Dummy_Sensor', 'Dummy_Control']
DAN.profile['d_name']= None # None for autoNaming
DAN.device_registration_with_retry(ServerIP, Reg_addr)


while True:
    print (DAN.state)
    print (DAN.SelectedDF)
    for DF_name in DAN.SelectedDF:
        print (DF_name+': '+DAN.get_alias(DF_name))    
    time.sleep(1)




    
