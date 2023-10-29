class Producer:

    @staticmethod
    def run(sender):
        sender.queue_declare("hello")
        for i in range(10):
            msg = f"Hello World {i}!"
            sender.send_message(exchange="", routing_key="hello", body=msg)
        sender.close()
