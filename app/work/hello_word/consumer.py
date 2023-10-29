def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")


class Consumer:
    @staticmethod
    def run(receiver):
        receiver.consume_messages("hello", callback)
