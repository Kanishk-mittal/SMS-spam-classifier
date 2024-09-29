# SMS Spam Detection
## Introduction
This project is about detecting spam messages using machine learning algorithms. The dataset used in this project is the SMS Spam Collection dataset from the UCI Machine Learning Repository. The dataset contains 5574 messages, out of which 747 are spam messages and 4827 are ham messages. The dataset is divided into two columns: label and message. The label column contains the class of the message, which can be either spam or ham. The message column contains the text of the message. The goal of this project is to build a machine learning model that can predict whether a message is spam or ham based on its text.

## How to use this project
1. Download model.pkl
2. Run the following code in Python:
```python
import pickle
pipeline = pickle.load(open('model.pkl', 'rb'))

# Test the model with a custom message
message = input("Enter a message: ")
prediction=int(pipeline.predict([message])[0])
if prediction == 1:
    print("Spam")
else:
    print("Not Spam")
```

## About Model

To know more about the model, please refer to the [sms-spam-detection.ipynb](sms-spam-detection.ipynb) notebook.
