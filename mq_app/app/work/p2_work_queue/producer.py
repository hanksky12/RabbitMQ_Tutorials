class Producer:

    @staticmethod
    def run(sender,**kwargs):
        sender.queue_declare("hello")
        for i in range(10):
            sender.send_message(exchange="", routing_key="hello", body=kwargs["msg"]+ str(i))
        sender.close()
