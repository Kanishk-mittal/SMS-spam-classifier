import streamlit as st
import nltk
import dill
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# Load the model
with open('model.pkl', 'rb') as f:
    model = dill.load(f)

# Create the UI
st.title('SMS Spam Classifier')
imput_sms=st.text_area('Enter the message', key='msg')
if st.button('Predict'):
    result=int(model.predict([imput_sms])[0])
    if result:
        st.header('Spam')
    else:
        st.header('Not Spam')
