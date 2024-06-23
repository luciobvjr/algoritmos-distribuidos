import zmq
from lamport_clock import LamportClock, Message

context = zmq.Context()
server_name = "server"
port = 5555

print(f"Connecting to server (container: {server_name}, port: {port})")
socket = context.socket(zmq.REQ)
socket.connect(f"tcp://{server_name}:{port}")
clock = LamportClock()

for request in range(10):
    clock.increment()
    sent_message = Message("Request", clock.get_timestamp())
    socket.send_pyobj(sent_message)

    received_message = socket.recv_pyobj()
    clock.increment()
    clock.update(received_message.timestamp)
    print(f"{request} - {received_message}")
