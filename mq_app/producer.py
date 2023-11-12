import sys

from app.utils.rabbit_mq.message import MessageSender
from app.rabbit_parameters import rabbit_parameters
from app.work.p1_hello_word.producer import Producer as HelloWordProducer
from app.work.p2_work_queue.producer import Producer as WorkQueuesProducer
from app.work.p3_publish_subscribe.producer import Producer as PublishSubscribeProducer
from app.work.p4_routing.producer import Producer as RoutingProducer
from app.work.p5_topics.producer import Producer as TopicsProducer


class Producer:

    @classmethod
    def run(cls):
        sender = MessageSender(rabbit_parameters)
        producer, message, routing_key = cls.__get_parm_from_args()
        producer.run(sender, msg=message, routing_key=routing_key)

    @classmethod
    def __get_parm_from_args(cls):
        if len(sys.argv) < 2:
            raise Exception("未選擇生產者")
        producer = None
        routing_key_default = ''
        if sys.argv[1] == "1":
            producer = HelloWordProducer()
        elif sys.argv[1] == "2":
            producer = WorkQueuesProducer()
        elif sys.argv[1] == "3":
            producer = PublishSubscribeProducer()
        elif sys.argv[1] == "4":
            producer = RoutingProducer()
            routing_key_default = 'info'
        elif sys.argv[1] == "5":
            producer = TopicsProducer()
            routing_key_default = 'anonymous.info'
        routing_key = sys.argv[2] if len(sys.argv) > 2 else routing_key_default
        message = ' '.join(sys.argv[3:]) or 'Hello World!'
        print(f" [x] Sending {producer} {routing_key}:{message}")
        return producer, message, routing_key


if __name__ == "__main__":
    Producer.run()
