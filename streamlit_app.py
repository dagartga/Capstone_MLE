# streamlit_app.property

import streamlit as st
import s3fs
import os
import pandas as pd
from datetime import datetime, date, timedelta
from model import prediction
import traceback
import plotly.express as px


try:
# run the prediction model
# outputs the next day price prediction and the date of today's data
    next_day_pred, todays_date = prediction()
    today = datetime.strptime(todays_date, '%Y/%m/%d')

# adjust the date for the next day for more readability of result
    pred_date = today + timedelta(days=1)

# convert to string format
    pred_date = pred_date.strftime('%m/%d/%Y')

    st.subheader('BTC Next Day Price Prediction')
    st.subheader('Prediction Date')
    st.write(pred_date)
    st.subheader('Prediction Price (USD)')
    st.write(next_day_pred)



# Retrieve file contents
    s3 = s3fs.S3FileSystem(anon=False)

    with s3.open('btcpricedata/price_df.csv', 'rb') as f:
        df = pd.read_csv(f)

# narrow down to 1-year data and create plotly figure
    fig = px.line(df.iloc[-365:, :], x='Date', y=df.columns[-2:])


# Print results
    st.subheader('1 Year Historical Prices and Predictions')
    st.plotly_chart(fig)

except Exception as e:
    st.write(e)
