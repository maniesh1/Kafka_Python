import json

from kafka import KafkaConsumer
from kafka import KafkaProducer


ORDER_KAFKA_TOPIC = "order_details"
ORDER_CONFIRMED_KAFKA_TOPIC = "order_confirmed"

consumer = KafkaConsumer(
    ORDER_KAFKA_TOPIC, 
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest"

)
producer = KafkaProducer(bootstrap_servers="localhost:9092")

consumer.subscribe([ORDER_KAFKA_TOPIC])
print("Subscribed to topic:", ORDER_KAFKA_TOPIC)

print("Gonna start listening")
print(type(consumer))
while True:
    print("Starting consumer loop...")
    for message in consumer:
        print("Received message: ", message)
        print("Message value: ", message.value)
    try:
        
        consumed_message = json.loads(message.value.decode())
        print("Decoded message: ",consumed_message)
        # user_id = consumed_message["user_id"]
        # total_cost = consumed_message["total_cost"]
        # data = {
        #     "customer_id": user_id,
        #     "customer_email": f"{user_id}@gmail.com",
        #     "total_cost": total_cost
        # }
        # print("Successful transaction..")
         # producer.send(ORDER_CONFIRMED_KAFKA_TOPIC, json.dumps(data).encode("utf-8"))
    except Exception as e:
        print("Exception: ", e)
