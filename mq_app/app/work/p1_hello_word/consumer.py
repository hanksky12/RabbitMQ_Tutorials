def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")


class Consumer:
    @staticmethod
    def run(receiver, **kwargs):
        receiver.consume_messages(queue_name="hello", callback=callback)
