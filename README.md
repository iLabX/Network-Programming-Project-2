# Network-Programming-Project-2

## Overview

## Requirement
* Apache zookeeper
* Apache Kafka
* pandas
* nltk (Natural Language Toolkit)
* pickle
* sklearn
* Faust
* confluent Kafka

## Data
We used the SMS Spam Collection. It simulates SMS tagged messages that have been collected for SMS Spam research.\
It is a collection of 5573 English SMS messages and legally tagged spam and ham.\
https://www.kaggle.com/uciml/sms-spam-collection-dataset

## Code Execution
1. execute spam_model.py\
      $ python3 spam_model.py<br>
2. open zookeeper\
      $ bin/zookeeper-server-start.sh config/zookeeper.properties<br>
3. open Kafka\
      $ bin/kafka-server-start.sh config/kafka.properties<br>
4. create a topic\
      $ bin/kafka-topics.sh --create --topic spamchecker --bootstrap-server localhost:9092<br>
5. execute spam_consumer.py\
      $ faust -A spam_consumer worker -l info<br>
6.  execute spam_producer.py\
      $ python3 spam_producer.py
