import time

def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(" [x] Done")


class Consumer:
    @staticmethod
    def run(receiver, **kwargs):
        receiver.consume_messages(queue_name="hello", callback=callback)
