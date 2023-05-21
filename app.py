# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u9RJnljvnQ75ngTCVxXeU4pM9xkC5tQd
"""

import streamlit as st
from datetime import datetime
import pandas as pd
import numpy as np
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

model = load_model('gru_model.hdf5')

import streamlit as st
from datetime import datetime
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model

# Load the scaler
scaler = MinMaxScaler(feature_range=(0, 1))
# Assuming you have a trained model saved as 'model.h5', load the model
model = load_model('gru_model.hdf5')

# Define the sidebar with input options
st.sidebar.title('Student Submission Prediction')
input_date = st.sidebar.date_input('Select a date:', value=datetime.today())

# Define the main content
st.title('Student Submission Prediction')
st.write(f'Predicted submission for {input_date.strftime("%d-%b-%Y")}:')

# Preprocess the input date
input_date_str = input_date.strftime('%d-%b-%y')
input_date_scaled = scaler.transform(np.array([[input_date_str]]))

# Perform prediction using the GRU model
prediction = model.predict(np.reshape(input_date_scaled, (1, 1, 1)))
predicted_submission = scaler.inverse_transform(prediction)[0, 0]

# Display the predicted submission number
st.write(predicted_submission)