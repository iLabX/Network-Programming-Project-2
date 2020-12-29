# Network-Programming-Project-2

## Overview
In this project, we simulate on how to combine stream processing and machine learning together with the email spam detection topic. First, we train the model to detect the spam messages and create two pickle files (.pkl). Then, we use the stream processing to load the pickle files, send messages and receive the results in almost real-time duration. In addition, we apply CountVectorizer and Baye’s theorem of conditional probability to determine the possibility of the text message in out prediction model.
 
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


## References
Karmali, T. (2017, August 03). Spam Classifier in Python from scratch. Retrieved December 29, 2020, from https://towardsdatascience.com/spam-classifier-in-python-from-scratch-27a98ddd8e73
	
Cojocar, B. (2020, July 21). How to build a real-time fraud detection pipeline using Faust and MLFlow. Retrieved December 29, 2020, from https://towardsdatascience.com/how-to-build-a-real-time-fraud-detection-pipeline-using-faust-and-mlflow-24e787dd51fa

Ortega, D. (2019, September 24). Why Is Stream Processing Important to Your Business? Retrieved December 29, 2020, from https://hazelcast.com/blog/what-is-stream-processing-and-why-is-it-important-to-your-business/
	
DSE_G1_2020, D. (2020, September 02). Spam or Ham. Retrieved December 29, 2020, from https://medium.com/botnoi-classroom/spam-or-ham-fe7e8befd1c1
