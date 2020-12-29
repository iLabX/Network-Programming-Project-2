import pandas as pd
import string
import nltk
import pickle
from joblib import dump, load
from nltk.corpus import stopwords
from collections import Counter
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
nltk.download('stopwords')

def clean_word(mess):
    nopunc = [char for char in mess if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    word_tokens = nopunc.split()
    stopwords_ac =  stopwords.words('english')
    filtered_sentence = []
    for w in word_tokens: 
        if w not in stopwords_ac: 
            filtered_sentence.append(w) 
    return ' '.join(filtered_sentence)

def model(x_train, x_test, y_train, y_test):
        vect = CountVectorizer()
        vect.fit(x_train)
        X_train_dim = vect.transform(x_train)
        X_test_dim = vect.transform(x_test)

        clf_mnb = MultinomialNB(alpha=0.2)
        clf_mnb.fit(X_train_dim, y_train)
        y_test_pd = clf_mnb.predict(X_test_dim)
        metrics.accuracy_score(y_test, y_test_pd)

        print('creating filename.joblib...')
        dump(clf_mnb, 'filename.joblib')
        clf_mnb = load('filename.joblib')
        print('creating spam_G1_model.pkl...')
        filename = 'spam_G1_model.pkl'
        pickle.dump(clf_mnb, open(filename, 'wb'))
        vect = CountVectorizer()
        X = vect.fit_transform(x_train)
        print('creating tranform.pkl...')
        pickle.dump(vect, open('tranform.pkl', 'wb'))
        clf = pickle.load(open(filename, 'rb'))
        cv = pickle.load(open('tranform.pkl', 'rb'))
        return clf, cv

sms = pd.read_csv("spam.csv", encoding='latin-1')
sms_len = len(sms)
sms.dropna(inplace=True, axis=1)
sms.columns = ["label","msg"]
sms.groupby("label").describe()
sms["label_sign"] = sms.label.map({"ham":0, "spam":1})

#apply clean_word() to every messages
sms["clean_msg"] = sms.msg.apply(clean_word)
words = sms[sms.label=='spam'].clean_msg.apply(lambda x: [word.lower() for word in x.split()])

ham_words = Counter()
for msg in words:
        ham_words.update(msg)

#print("Top 5 Most Common: ", ham_words.most_common(5))

#run the model
X_train, X_test, Y_train, Y_test = train_test_split(sms.clean_msg, sms.label_sign, random_state=1)
clf, cv = model(X_train, X_test, Y_train, Y_test)