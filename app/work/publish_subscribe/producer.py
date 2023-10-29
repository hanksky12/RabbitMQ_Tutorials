class Producer:

    @staticmethod
    def run(sender):
        # 只宣告exchange，不宣告queue
        sender.exchange_declare(exchange='logs',
                                exchange_type='fanout')
        sender.send_message(exchange='logs',
                            routing_key='',
                            body='Hello World!')
        sender.close()
