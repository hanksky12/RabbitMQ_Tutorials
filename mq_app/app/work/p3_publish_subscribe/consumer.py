import time


def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(" [x] Done")


class Consumer1:
    @staticmethod
    def run(receiver, **kwargs):
        receiver.exchange_declare(exchange='logs', exchange_type='fanout')  # 避免生產者還未建立exchange
        # 可以使用隨機 或 指定兩個Consumer的queue_name要不一樣
        queue_name = receiver.queue_declare(queue_name='', exclusive=True)  # 隨機name 斷線及消失

        receiver.queue_bind_exchange('logs', queue_name)
        receiver.consume_messages(queue_name, callback)


class Consumer2:
    @staticmethod
    def run(receiver, **kwargs):
        receiver.exchange_declare(exchange='logs', exchange_type='fanout') # 避免生產者還未建立exchange
        queue_name = 'qn2'  # 具有累積性
        receiver.queue_declare(queue_name=queue_name)

        receiver.queue_bind_exchange('logs', queue_name)
        receiver.consume_messages(queue_name, callback)
