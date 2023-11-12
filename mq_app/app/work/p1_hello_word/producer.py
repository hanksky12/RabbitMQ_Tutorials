class Producer:

    @staticmethod
    def run(sender,**kwargs):
        sender.queue_declare("hello")
        sender.send_message(exchange="", routing_key="hello", body=kwargs["msg"])
        sender.close()