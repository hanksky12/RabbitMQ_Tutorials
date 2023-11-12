import os
import sys

from app.utils.rabbit_mq.message import MessageReceiver
from app.rabbit_parameters import rabbit_parameters
from app.work.p1_hello_word.consumer import Consumer as HelloWordConsumer
from app.work.p2_work_queue.consumer import Consumer as WorkQueuesConsumer
from app.work.p3_publish_subscribe.consumer import Consumer1 as PublishSubscribeConsumer1
from app.work.p4_routing.consumer import Consumer as RoutingConsumer
from app.work.p5_topics.consumer import Consumer as TopicsConsumer


class Consumer:
    @classmethod
    def run(cls):
        receiver = MessageReceiver(rabbit_parameters)
        consumer, routing_key_list = cls.__get_parm_from_args()
        consumer.run(receiver, routing_key_list=routing_key_list)

    @classmethod
    def __get_parm_from_args(cls):
        if len(sys.argv) < 2:
            raise Exception("未選擇消費者")
        consumer = None
        routing_key_list_default = []
        if sys.argv[1] == "1":
            consumer = HelloWordConsumer()
        elif sys.argv[1] == "2":
            consumer = WorkQueuesConsumer()
        elif sys.argv[1] == "3":
            consumer = PublishSubscribeConsumer1()
        elif sys.argv[1] == "4":
            consumer = RoutingConsumer()
            routing_key_list_default = ['info']
        elif sys.argv[1] == "5":
            consumer = TopicsConsumer()
            routing_key_list_default = ["kern.*", "*.critical"]
        routing_key_list = sys.argv[2:] or routing_key_list_default
        return consumer, routing_key_list


if __name__ == "__main__":
    try:
        Consumer.run()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)