import os
import sys

from app.utils.rabbit_mq.message import MessageReceiver
from app.rabbit_parameters import rabbit_parameters
from app.work.p3_publish_subscribe.consumer import Consumer2 as PublishSubscribeConsumer2
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
        routing_key_list_default = []
        if sys.argv[1] == "3":
            consumer = PublishSubscribeConsumer2()
        elif sys.argv[1] == "4":
            consumer = RoutingConsumer()
            routing_key_list_default = ['error']
        elif sys.argv[1] == "5":
            consumer = TopicsConsumer()
            routing_key_list_default = ["*.error", "*.critical"]
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
