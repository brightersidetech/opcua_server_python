# opcua_server_python
Demonstration on how to create an OPC UA server in python
#### Step 1 : Install required packages
```
 pip install -r requirements.txt
```
#### Step 2: Replace the endpoint with your own system configuration
This endpoint configuration works on most machines, use the loopback address (127.0.0.1) or Machine's Public IP Address to access the OPC UA Server
```
url = "opc.tcp://0.0.0.0:4840/opcua/server"
```
#### Step 4: Run the program
```
python opc_ua_server.py
```