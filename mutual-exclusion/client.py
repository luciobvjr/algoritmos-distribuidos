import sys
import time
import zmq

context = zmq.Context()

# DEALER socket for requesting and releasing the resource
dealer = context.socket(zmq.DEALER)
dealer.connect("tcp://coordinator:5555")

use_time = int(sys.argv[1])
dealer.send_multipart([b"request"])
response = dealer.recv_multipart()

if response[0] == b"True":
    print("Resource granted")
    time.sleep(use_time)

    dealer.send_multipart([b"release"])
    response = dealer.recv_multipart()
    if response[0] == b"True":
        print("Resource released")
else:
    print("Resource denied, waiting for resource...")

    # Wait for resource to become available
    response = dealer.recv_multipart()
    if response[0] == b"True":
        print("Resource granted")
        time.sleep(use_time)

        dealer.send_multipart([b"release"])
        response = dealer.recv_multipart()
        if response[0] == b"True":
            print("Resource released")
