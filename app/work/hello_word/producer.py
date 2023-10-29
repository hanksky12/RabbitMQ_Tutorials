class Producer:

    @staticmethod
    def run(sender):
        sender.queue_declare("hello")
        sender.send_message(exchange="", routing_key="hello", body="Hello World!")
        sender.close()