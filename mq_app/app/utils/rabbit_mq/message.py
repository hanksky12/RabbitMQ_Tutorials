import pika


class Client:

    def __init__(self, parameters: pika.ConnectionParameters):
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()

    def close(self):
        self.channel.close()
        self.connection.close()

    def queue_declare(self, queue_name="", exclusive=False):
        print(f"Trying to declare queue({queue_name})...")
        # 沒有就創建
        result = self.channel.queue_declare(queue=queue_name, exclusive=exclusive)
        # exclusive=True: 當消費者斷開連接後，queue自動刪除
        if queue_name == "":
            queue_name = result.method.queue
        return queue_name

    def exchange_declare(self, exchange, exchange_type):
        self.channel.exchange_declare(exchange=exchange,
                                      exchange_type=exchange_type)


class MessageSender(Client):

    def send_message(self, exchange, routing_key, body):
        channel = self.connection.channel()
        channel.basic_publish(exchange=exchange,
                              routing_key=routing_key,  # queue name
                              body=body,
                              properties=pika.BasicProperties(
                                  delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
                              )  # 當rabbitmq重啟後，任然存在
                              )

        print(f"Sent message. Exchange: {exchange}, Routing Key: {routing_key}, Body: {body}")


class MessageReceiver(Client):

    def get_message(self, queue):
        method_frame, header_frame, body = self.channel.basic_get(queue)
        if method_frame:
            print(method_frame, header_frame, body)
            self.channel.basic_ack(method_frame.delivery_tag)
            return method_frame, header_frame, body
        else:
            print('No message returned')

    def consume_messages(self, queue_name, callback, auto_ack=False):
        self.channel.basic_qos(prefetch_count=1)  # 一次只接收一個消息
        self.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=auto_ack)
        # auto ack: 一旦rabbitmq將消息發送給消費者，就從內存中刪除，無論消費者是否處理完畢，所以要關閉，並在程式內確認

        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()

    def queue_bind_exchange(self, exchange, queue_name, routing_key=""):
        self.channel.queue_bind(exchange=exchange, queue=queue_name, routing_key=routing_key)
