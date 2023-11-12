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
        message = None
        routing_key = None

        if sys.argv[1] == "1":
            producer = HelloWordProducer()
            message = ' '.join(sys.argv[2:]) or 'Hello World!'
        elif sys.argv[1] == "2":
            producer = WorkQueuesProducer()
            message = ' '.join(sys.argv[2:]) or 'WorkQueues!'
        elif sys.argv[1] == "3":
            producer = PublishSubscribeProducer()
            message = ' '.join(sys.argv[2:]) or 'PublishSubscribe!'
        elif sys.argv[1] == "4":
            producer = RoutingProducer()
            routing_key = sys.argv[2] if len(sys.argv) > 2 else 'info'
            message = ' '.join(sys.argv[3:]) or 'Routing!'
        elif sys.argv[1] == "5":
            producer = TopicsProducer()
            routing_key = sys.argv[2] if len(sys.argv) > 2 else 'anonymous.info'
            message = ' '.join(sys.argv[3:]) or 'Topics!'
        print(f" [x] Sending {producer} {routing_key}:{message}")
        return producer, message, routing_key


if __name__ == "__main__":
    """
    python producer.py argv1 argv2 argv3 
    """
    Producer.run()
