import time


def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


class Consumer1:
    @staticmethod
    def run(receiver):
        # 要宣告exchange, 隨機queue 並且綁定queue
        receiver.exchange_declare(exchange='logs', exchange_type='fanout')
        # 可以使用隨機 或 指定，但兩個Consumer的queue_name要不一樣
        # queue_name = receiver.queue_declare(queue_name='', exclusive=True)#隨機name
        queue_name = receiver.queue_declare(queue_name='qn1')

        receiver.queue_bind_exchange('logs', queue_name)
        receiver.consume_messages(queue_name, callback)


class Consumer2:
    @staticmethod
    def run(receiver):
        receiver.exchange_declare(exchange='logs', exchange_type='fanout')
        queue_name = 'qn2'
        receiver.queue_declare(queue_name=queue_name)
        receiver.queue_bind_exchange('logs', queue_name)
        receiver.consume_messages(queue_name, callback)
