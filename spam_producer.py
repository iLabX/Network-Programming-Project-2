import pandas as pd
import uuid
from random import randint
from confluent_kafka import Producer
import json
import nltk
import string
from nltk.corpus import stopwords
nltk.download('stopwords')

bootstrap_servers = '127.0.0.1:9092'
topic = 'spamchecker'
msg_count = 10

def clean_word(mess):
        nopunc = [char for char in mess if char not in string.punctuation]
        nopunc = ''.join(nopunc)
        word_tokens = nopunc.split()
        stopwords_ac = stopwords.words('english')
        filtered_sentence = []
        for w in word_tokens:
                if w not in stopwords_ac:
                        filtered_sentence.append(w)
        return ' '.join(filtered_sentence)

def delivery_report(err, msg):
        if err is not None:
                print("Message delivery failed: {}".format(err))
        else:
                print("Message delivered to {}".format(msg.topic()))

def kafka_producer():
        p = Producer({'bootstrap.servers': bootstrap_servers})
        for msg in prod_msgs:
                record_key = str(uuid.uuid4())
                base_message = [clean_word(msg)]
                record_value = json.dumps(base_message)
                p.produce(topic, key=record_key, value=record_value, on_delivery=delivery_report)
                p.poll(0)
        p.flush()
        print('Sent {count} messages to {brokers}'.format(count=len(prod_msgs), brokers=bootstrap_servers))

#read .csv file
print('reading csv...')
sms = pd.read_csv("spam.csv", encoding='latin-1')
sms_len = len(sms)
sms.dropna(inplace=True, axis=1)
sms.columns = ["label", "msg"]
sms.groupby("label").describe()
sms["label_sign"] = sms.label.map({"ham":0, "spam":1})
sms.head()

print('randoming messages for producer...')
prod_msgs = []
for i in range(10):
        ran_num = randint(0, sms_len)
        prod_msgs.append(sms.msg[ran_num])
#print(len(prod_msgs))

#print('calling producer()')
kafka_producer()
