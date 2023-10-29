import os
import sys

from utils.rabbit_mq.message import MessageReceiver
from work.base import rabbit_parameters
from work.hello_word.consumer import Consumer as HelloWordConsumer
from work.work_queue.consumer import Consumer as WorkQueueConsumer
from work.publish_subscribe.consumer import Consumer1 as PublishSubscribeConsumer


class Consumer:
    @staticmethod
    def run(ob):
        receiver = MessageReceiver(rabbit_parameters)
        ob.run(receiver)


if __name__ == "__main__":
    try:
        Consumer.run(PublishSubscribeConsumer)
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
