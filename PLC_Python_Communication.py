# Libraries
from pyModbusTCP.client import ModbusClient 
from time import sleep 
from random import randint
from datetime import datetime as dt
from logger import setup_logger

# Tanımlar
CONTROL = True
register_address = 0
last_rand = 0
last_recv = 0
step = 0
Data_send_control = 0

# Data is tn send 
send = [None,None,None]# Value , rand, processing
send[2] = 0

# it is necssery value HOST and PORT for PLC connect 
HOST = "192.168.0.1"
PORT = 502

# log is create
logger = setup_logger(" PLC_Python_Com")

# client is create
client = ModbusClient(
    host=HOST,  
    port=PORT,
    auto_open=True,
    auto_close=True)

while CONTROL :

    date = dt.now()# date

    try : # recv

        if step == 2 :
        
            recv = client.read_holding_registers(0,3) # Data is read 

            Data_send_control = 0
            Data_recv_control = 0

            if recv and recv[2] == 1  : 
                
                logger.info(f"✅ Data is recv : {str(recv)}")
                
                step = 0 # İŞLEM SIRASI

                send[2] = 0 # PLC İLETİŞİM SIRASI

    except : 
         
        logger.warning("Read is error or data is not have")

        CONTROL = False

    try : # send

        rand = randint(0,100) # it is a create number random

        if last_rand != rand :
        
            if step == 0 and send[2] == 0 : 

                value_to_send = int(input(" Data to be send : ")) # it will a take ınput

                # it will a send the value
                send[0] = value_to_send 
                send[1] = rand
            
                result = client.write_multiple_registers(register_address,send) # it is send data a lot

                step = 2 # İŞLEM SIRASI 
                Data_send_control = 1 # Print processing
                 
            if result and Data_send_control == 1 : logger.info(f"✅ Data is send : {str(send)}", )

        last_rand = rand 

    except : 
         
        logger.warning(" Send is create error block ")

        CONTROL = False

    sleep(0.5)

if CONTROL == False : logger.warning(" Data is error send or recv ")
