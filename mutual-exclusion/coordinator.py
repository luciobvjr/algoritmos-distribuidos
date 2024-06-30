import zmq
import queue

context = zmq.Context()

# ROUTER socket for handling requests and releases
router = context.socket(zmq.ROUTER)
router.bind("tcp://*:5555")

is_resource_available = True
waiting_clients = queue.Queue()

while True:
    # Receive client ID and message
    client_id, rcv_message = router.recv_multipart()

    if rcv_message == b"request":
        if is_resource_available:
            router.send_multipart([client_id, b"True"])
            is_resource_available = False
        else:
            waiting_clients.put(client_id)
            router.send_multipart([client_id, b"False"])

    elif rcv_message == b"release":
        is_resource_available = True
        router.send_multipart([client_id, b"True"])

        if not waiting_clients.empty():
            next_client_id = waiting_clients.get()
            router.send_multipart([next_client_id, b"True"])
            is_resource_available = False