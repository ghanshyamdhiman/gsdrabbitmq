import pika, os

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = "amqps://zaicmnji:nwq_gWv6gm41TiBaPSc8tywaG-dOFcer@puffin.rmq2.cloudamqp.com/zaicmnji"
print(url)
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue
def callback(ch, method, properties, body):
  print(" [x] Received " + str(body))

channel.basic_consume('hello',
                      callback,
                      auto_ack=True)

print(' [*] Waiting for messages:')
channel.start_consuming()
connection.close()