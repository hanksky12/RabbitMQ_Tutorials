import time


def callback(ch, method, properties, body):
    print(f" [x] {method.routing_key}:{body}")
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(" [x] Done")


class Consumer:
    @staticmethod
    def run(receiver, **kwargs):
        receiver.exchange_declare(exchange='direct_logs', exchange_type='direct')
        queue_name = receiver.queue_declare(queue_name='', exclusive=True)  # 隨機name
        for routing_key in kwargs["routing_key_list"]:
            receiver.queue_bind_exchange(exchange='direct_logs',
                                         queue_name=queue_name,
                                         routing_key=routing_key)
        receiver.consume_messages(queue_name, callback)