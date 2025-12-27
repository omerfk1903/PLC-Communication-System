# Libraries
from pyModbusTCP.client import ModbusClient 
from time import sleep 
from random import randint
from datetime import datetime as dt

CONTROL = 2
register_address = 0
last_rand = 0
Socket_Status_Connect = False

# it is necssery value HOST and PORT for PLC connect 
HOST = "192.168.0.1"
PORT = 502

# client is create
client = ModbusClient(
    host=HOST,  
    port=PORT,
    auto_open=True,
    auto_close=True
)

# The client is checking the connection.
while bool(client.is_open) == False :
    
    print("{0} Port with modbus formate is not connect : {1} ".format(dt.now(),Socket_Status_Connect))

    Socket_Status_Connect = False

    sleep(1)

# İf client is active ,socket is start processings
if bool(client.is_open) == True :

    print("{0} Port with modbus formate is connect : {1} ".format(dt.now(),Socket_Status_Connect))

    Socket_Status_Connect = True

while Socket_Status_Connect == True :

    if CONTROL == 1 : 
        
        try : 
        
            recv = client.read_holding_registers(0, 10) # Data is read 

            if recv : print("Client read:", recv)

        except : print("Read is error or data is not have")

    else : 
        
        register_address = 0 

        value_to_send = int(input(" Data to be send : ")) # it will a take ınput

        rand = randint(0,100) # it is a create number random

        send = [value_to_send,rand] # it will a send the value

        if last_rand != rand : result = client.write_multiple_registers(register_address,send) # it is send data a lot

        else :

            for x in range(0,10) :

                rand = randint(0,100)

                if rand != last_rand :

                    result = client.write_multiple_registers(register_address,[value_to_send,rand]) # it is send data a lot

                    break
                 
        if result : print("✅ Data is send : ", value_to_send)

        else : print("❌ Data is not send")

        last_rand = rand 

    sleep(0.5)
