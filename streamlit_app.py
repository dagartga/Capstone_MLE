# streamlit_app.property

import streamlit as st
import s3fs
import os
import pandas as pd
import datetime as dt
from datetime import date, timedelta
import traceback
import plotly.express as px


try:

    s3 = s3fs.S3FileSystem(anon=False)

    with s3.open('btcpricedata/price_df.csv', 'rb') as f:
        df = pd.read_csv(f, index_col=0)

    todays_date = df.iloc[-1, 0]
    next_day_pred = str(df.iloc[-1, 3])
    today_price = str(df.iloc[-1,1])

    today = dt.datetime.strptime(todays_date, '%Y/%m/%d')

# adjust the date for the next day for more readability of result
    pred_date = today + timedelta(days=1)

# convert to string format
    today = today.strftime('%m/%d/%Y')
    pred_date = pred_date.strftime('%m/%d/%Y')

    st.subheader('BTC Next Day Price Prediction')
    st.write(f"The average daily price of BTC for {today} was {today_price}")
    st.subheader('Prediction Date')
    st.write(pred_date)
    st.subheader('Prediction of Average Daily Price (USD)')
    st.write(next_day_pred)





# narrow down to 1-year data and create plotly figure
    one_year_df = df.iloc[-365:, :]
    fig = px.line(one_year_df, x='Date', y=df.columns[-2:])


# Print plot of Predictions and next day actual prices
    st.subheader('1 Year Historical Prices and Predictions')
    st.plotly_chart(fig)

# price and prediction raw data printed in tabular form
    st.subheader('1 Year Historical Prices and Predictions DataFrame')
    st.write(one_year_df)


except Exception as e:
    st.write(e)
