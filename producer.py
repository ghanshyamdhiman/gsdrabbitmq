import pika, os


# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
#url = os.environ.get("CLOUDAMQP_URL", "amqps://zaicmnji:nwq_gWv6gm41TiBaPSc8tywaG-dOFcer@puffin.rmq2.cloudamqp.com/zaicmnji")
#url = "amqps://zaicmnji:nwq_gWv6gm41TiBaPSc8tywaG-dOFcer@puffin.rmq2.cloudamqp.com/zaicmnji"
url="amqps://localhost"
url=os.environ.get('AMQP_HOST')
print(url)
#params = pika.URLParameters(url)
params ="localhost"

try:
  connection = pika.BlockingConnection(params)
except Exception:
  print("exception occurred")
channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello CloudAMQP!')

print(" [x] Sent 'Hello World!'")
connection.close()
