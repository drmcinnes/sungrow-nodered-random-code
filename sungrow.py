import socket
import time

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
start_time = time.time()
# Connect to the remote host and port
sock.connect(("192.168.0.30", 9999))
modbus_string = ""
# Send a request to the host
#sock.send("Why don't you call me any more?\r\n")

# Get the host's response, no more than, say, 1,024 bytes
while True:
    response_data = sock.recv(8)
    current_time = time.time()
    elapsed_time = current_time - start_time
    start_time = current_time
    modbus_string = modbus_string + "" + response_data.hex()
    if elapsed_time > .05:
        #print("Finished iterating in: " + str(elapsed_time)  + " seconds")
        print(modbus_string)
        modbus_string = ""
#    break
    #print(len(response_data))
#    print(response_data)
#    print (elapsed_time)

# Terminate

sock.close(  )
