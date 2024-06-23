import time
import zmq
from lamport_clock import LamportClock, Message

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
clock = LamportClock()

while True:
    received_message = socket.recv_pyobj()
    clock.increment()
    clock.update(received_message.timestamp)
    print(received_message)

    time.sleep(1)

    clock.increment()
    sent_message = Message("Response", clock.get_timestamp())
    socket.send_pyobj(sent_message)