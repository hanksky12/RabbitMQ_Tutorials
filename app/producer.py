from utils.rabbit_mq.message import MessageSender
from work.base import rabbit_parameters
from work.hello_word.producer import Producer as HelloWordProducer
from work.work_queue.producer import Producer as WorkQueueProducer
from work.publish_subscribe.producer import Producer as PublishSubscribeProducer

class Producer:

    @staticmethod
    def run(ob):
        sender = MessageSender(rabbit_parameters)
        ob.run(sender)


if __name__ == "__main__":
    Producer.run(PublishSubscribeProducer)