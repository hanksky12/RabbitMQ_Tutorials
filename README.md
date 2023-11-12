# RabbitMQ Tutorials

根據官方教學，使用 Python 實作 RabbitMQ 的教學。依序實作以下範例：

使用docker，可串接到本地的RabbitMQ或是Amazon MQ
1. [Hello World](https://www.rabbitmq.com/tutorials/tutorial-one-python.html)
2. [Work Queues](https://www.rabbitmq.com/tutorials/tutorial-two-python.html)
3. [Publish/Subscribe](https://www.rabbitmq.com/tutorials/tutorial-three-python.html)
4. [Routing](https://www.rabbitmq.com/tutorials/tutorial-four-python.html)
5. [Topics](https://www.rabbitmq.com/tutorials/tutorial-five-python.html)


## 筆記
交換機=>負責轉發訊息

queue=>負責接收與累積訊息

使用交換機的三種模式下，如果消費者斷線後，重新上線要能拿到訊息，queue必須已經宣告過且存在，才能累積斷線時的訊息，所以不適合使用臨時queue

### 兩種會自動刪除的queue

1.臨時queue，當消費者斷線後，queue會自動刪除

2.宣告queue時，去設定auto_delete=True，當消費者斷線後，queue會自動刪除