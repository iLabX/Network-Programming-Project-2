import faust
from typing import List
from joblib import dump, load
from sklearn.feature_extraction.text import CountVectorizer
import requests
import json
import pickle
from spam_model import X_train

app = faust.App(
        'spam-detection-app',
        broker = 'kafka://localhost:9092',
        value_serializer='raw',
)

project_topic = app.topic('spamchecker')

clf_mnb = load('filename.joblib')
filename = 'spam_G1_model.pkl'
pickle.dump(clf_mnb, open(filename, 'wb'))
vect = CountVectorizer()
X = vect.fit_transform(X_train)
pickle.dump(vect, open('tranform.pkl', 'wb'))
filename = 'spam_G1_model.pkl'
clf = pickle.load(open(filename, 'rb'))
cv = pickle.load(open('tranform.pkl','rb'))


def get_sentiment(sen):
        data = [sen]
        vect = cv.transform(data).toarray()
        my_prediction = clf.predict(vect)[0]
        if my_prediction == 1:
                my_prediction = 'Spam!'
        elif my_prediction == 0:
                my_prediction = 'Normal Message'
        return {'result': my_prediction}

@app.agent(project_topic)
async def producer_get_msg(messages):
        async for message in messages:
                print('Input data: ', str(message))
                print(str(get_sentiment(message)))

if '__name__' == '__main__':
        app.main()
