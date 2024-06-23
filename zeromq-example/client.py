#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq

context = zmq.Context()
server_name = "server"
port = 5555

#  Socket to talk to server
print(f"Connecting to hello world server (container: {server_name}, port: {port}")
socket = context.socket(zmq.REQ)
socket.connect(f"tcp://{server_name}:{port}")

#  Do 10 requests, waiting each time for a response
for request in range(10):
    print(f"Sending request {request} ...")
    socket.send_string("Hello")

    #  Get the reply.
    message = socket.recv()
    print(f"Received reply {request} [ {message} ]")