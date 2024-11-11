# Email Spam Classifier

This is a Python GUI application built using Tkinter to classify emails as "spam" or "ham" (not spam) based on a trained machine learning model. The app allows users to input an email message and receive a classification result in real-time.

## Features
- Simple and user-friendly Tkinter-based GUI.
- Classifies emails as "spam" or "ham" using a pre-trained Naive Bayes model.
- Allows users to enter any email text for classification.

## Setup

### Prerequisites
- Python 3.x
- Install required packages:
  ```
  pip install scikit-learn joblib pandas

**Directory Structure**
The project structure should look like this:


email_classifier/
├── data/
│   └── spam.csv           # Dataset file
├── model/
│   └── spam_classifier.pkl # Trained model (generated after training)
├── app.py                 # Main application file
└── train_model.py         # Model training file


**Training the Model**
To train the model, run the following command:

  ```
    python train_model.py
  ```
Running the Application
     Once the model is trained and saved, you can run the application using:
     ```
       python app.py
      ```
**How It Works**
The application uses a Naive Bayes model trained on the UCI spam dataset.
The train_model.py script loads, trains, and saves the model.
The app.py file loads the saved model and uses it for predictions within a Tkinter GUI.

**Example**
Open the application.
Enter an email message in the provided text box.
Click "Classify" to see if the email is spam or ham.
