class Producer:

    @staticmethod
    def run(sender, **kwargs):
        # 'info', 'warning', 'error'.
        sender.exchange_declare(exchange='direct_logs',
                                exchange_type='direct')
        sender.send_message(exchange='direct_logs',
                            routing_key=kwargs["routing_key"],
                            body=kwargs["msg"])
        sender.close()
