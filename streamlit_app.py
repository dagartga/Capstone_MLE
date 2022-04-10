# streamlit_app.property

import streamlit as st
import s3fs
import os
import pandas as pd

from model import prediction
next_day_pred, todays_date = prediction()

st.subheader('BTC Next Day Price Prediction')
st.write(todays_date)
st.write(next_day_pred)



# Retrieve file contents
s3 = s3fs.S3FileSystem(anon=False)

with s3.open('btcpricedata/Merged_Unconverted_BTC_Data.csv', 'rb') as f:
    df = pd.read_csv(f)

# Print results
st.subheader('Raw Data')
st.write(df)
