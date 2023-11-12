class Producer:

    @staticmethod
    def run(sender, **kwargs):
        # 'anonymous.info'
        sender.exchange_declare(exchange='topic_logs',
                                exchange_type='topic')
        sender.send_message(exchange='topic_logs',
                            routing_key=kwargs["routing_key"],
                            body=kwargs["msg"])
        sender.close()
