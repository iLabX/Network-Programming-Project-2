# Network-Programming-Project-2

## Overview
In this project, we train the model to detect spam emails and prediction in real-time by using machine learning and stream processing. For the prediction model, we apply the CountVectorizer and Baye’s theorem of conditional probability to determine the possibility of the text message.
 
## Requirement
* Apache Zookeeper
* Apache Kafka
* Python Libraries
** pandas
** nltk (Natural Language Toolkit)
** pickle
** sklearn
** Faust
** confluent Kafka

## Data
We used the SMS Spam Collection. It simulates SMS tagged messages that have been collected for SMS Spam research.\
It is a collection of 5573 English SMS messages and legally tagged spam and ham.\
https://www.kaggle.com/uciml/sms-spam-collection-dataset

## Code Execution
1. execute spam_model.py\
      $ python3 spam_model.py
2. open Zookeeper\
      $ bin/zookeeper-server-start.sh config/zookeeper.properties
3. open Kafka\
      $ bin/kafka-server-start.sh config/kafka.properties
4. create a topic\
      $ bin/kafka-topics.sh --create --topic spamchecker --bootstrap-server localhost:9092
5. execute spam_consumer.py\
      $ faust -A spam_consumer worker -l info
6.  execute spam_producer.py\
      $ python3 spam_producer.py
