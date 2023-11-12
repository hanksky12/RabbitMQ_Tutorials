import ssl
from dataclasses import dataclass
import pika

from ...interfaces.parameters import IParameters


@dataclass
class RabbitMQ(IParameters):
    user: str
    password: str
    host: str
    port: int
    parameters: pika.URLParameters = None

    def __post_init__(self):
        credentials = pika.PlainCredentials(self.user, self.password)
        self.parameters = pika.ConnectionParameters(host=self.host,
                                                    port=self.port,
                                                    credentials=credentials)


@dataclass
class AmazonRabbitMQ(IParameters):
    user: str
    password: str
    broker_id: str
    region: str
    parameters: pika.URLParameters = None

    def __post_init__(self):
        # SSL Context for TLS configuration of Amazon MQ for RabbitMQ
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        ssl_context.set_ciphers('ECDHE+AESGCM:!ECDSA')

        url = f"amqps://{self.user}:{self.password}@{self.broker_id}.mq.{self.region}.amazonaws.com:5671"
        self.parameters = pika.URLParameters(url)
        self.parameters.ssl_options = pika.SSLOptions(context=ssl_context)
