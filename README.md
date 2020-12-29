# Network-Programming-Project-2

## Overview
In this project, we simulate on how to combine stream processing and machine learning together with the email spam detection topic. First, we train the model to detect the spam messages and create two pickle files (.pkl). Then, we use the stream processing to send messages and receive the results in almost real-time duration. In addition, we apply CountVectorizer and Baye’s theorem of conditional probability to determine the possibility of the text message in out prediction model.
 
## Requirement
* Apache Zookeeper
* Apache Kafka
* Python Libraries
	* pandas
	* nltk (Natural Language Toolkit)
	* pickle
	* sklearn
	* faust
	* confluent Kafka

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
