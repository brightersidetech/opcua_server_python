from time import sleep
import random
from opcua import Server
import datetime

server = Server()

url = "opc.tcp://127.0.0.1:12345"
server.set_endpoint(url)

name = "OPCUA_SERVER"
address_space = server.register_namespace(name)

objects = server.get_objects_node()

param = objects.add_object(address_space, "Parameters")

temp = param.add_variable(address_space, "Temperature", 0)
pressure = param.add_variable(address_space, "Pressure", 1)
time = param.add_variable(address_space, "Time", 0)

temp.set_writable()
pressure.set_writable()
time.set_writable()

server.start()
print()
print(f"Server started at {url}")
print()

while True:
    Temperature = random.uniform(22, 25)
    Pressure = random.uniform(200, 500)
    Time = datetime.datetime.now()

    temp.set_value(Temperature)
    print(f"New Temperature:  {temp.get_value():.2f}")

    pressure.set_value(Pressure)
    print(f"New Pressure: {pressure.get_value():.2f}")

    time.set_value(Time)
    print(f"New Time: {time.get_value()}")
    print()

    sleep(2)
