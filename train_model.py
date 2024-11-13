import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib
import os
import shutil

data = pd.read_csv("data/spam.csv", encoding="ISO-8859-1")
data = data[['v1', 'v2']]
data.columns = ['label', 'message']

X_train, X_test, y_train, y_test = train_test_split(data['message'], data['label'], test_size=0.2, random_state=42)

pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])

pipeline.fit(X_train, y_train)

joblib.dump(pipeline, 'model/spam_classifier.pkl')
print("Model trained and saved as 'spam_classifier.pkl'")
     
                
   
