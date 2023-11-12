from .utils.rabbit_mq.client_parameters import RabbitMQ

rabbit_parameters = RabbitMQ(user="root", password="1234", host="localhost", port=5672).parameters
