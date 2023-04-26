---------------- In the 'C:/kafka directory'-------------------
# Zookeper start
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties

# kafka-server-start
.\bin\windows\kafka-server-start.bat .\config\server.properties

# create kafka topic 
.\bin\windows\kafka-topics.bat --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic DummyTopic

# check topics
 .\bin\windows\kafka-topics.bat --list --bootstrap-server localhost:9092

# produce message on the topic
.\bin\windows\kafka-console-producer.bat --broker-list localhost:9092 --topic DummyTopic

# consume data from the topic
.\bin\windows\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic DummyTopic --from-beginning

-----------------------------------------------------------


# describe consumer group
.\bin\windows\kafka-consumer-groups.bat --bootstrap-server localhost:9092 --describe --group console-consumer-87766
