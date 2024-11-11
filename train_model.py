import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib
import os
import shutil

def train_spam_model():
    try:
        if not os.path.exists('model'):
            os.makedirs('model')
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(current_dir, 'data', 'spam.csv')
        
        temp_file = os.path.join(current_dir, 'temp_spam.csv')
        shutil.copy2(data_path, temp_file)
        
        try:
           
            data = pd.read_csv(temp_file, encoding="ISO-8859-1")
            
            data = data[['v1', 'v2']]
            data.columns = ['label', 'message']
          
            X_train, X_test, y_train, y_test = train_test_split(
                data['message'], 
                data['label'], 
                test_size=0.2, 
                random_state=42
            )
           
            pipeline = Pipeline([
                ('vectorizer', CountVectorizer()),
                ('classifier', MultinomialNB())
            ])
           
            pipeline.fit(X_train, y_train)
           
            y_pred = pipeline.predict(X_test)
            print("\nModel Performance:")
            print(classification_report(y_test, y_pred))
           
            model_path = os.path.join('model', 'spam_classifier.pkl')
            joblib.dump(pipeline, model_path)
            print(f"\nModel trained and saved as '{model_path}'")
            
        finally:
            if os.path.exists(temp_file):
                os.remove(temp_file)
                
    except PermissionError:
        print("\nPermission Error: Unable to access the file.")
        print("Please try the following:")
        print("1. Close any programs that might be using the file")
        print("2. Run the script as administrator")
        print("3. Check file permissions in File Explorer")
        
    except FileNotFoundError:
        print("\nError: spam.csv file not found.")
        print(f"Expected location: {data_path}")
        print("Please ensure the file exists in the correct location.")
        
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    print("Starting script...")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, 'data', 'spam.csv')
    print(f"Current directory: {current_dir}")
    print(f"Looking for file at: {data_path}")
    print(f"File exists: {os.path.exists(data_path)}")
   
    train_spam_model()
