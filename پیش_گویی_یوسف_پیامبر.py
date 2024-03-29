# -*- coding: utf-8 -*-
"""پیش گویی یوسف پیامبر.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xqgCJ5WblGgqLBzId76smbK82RpCECbv

!pip install pystan~=2.14
"""

import yfinance
import datetime as dt

start = dt.datetime(2020,1,1)
end = dt.datetime.now()
data = yfinance.download("AAPL", start, end)

data.to_csv("Stock_data.csv")

import pandas as pd
data = pd.read_csv("Stock_data.csv")

data = data[["Date","Close"]]

data.columns = ["ds", "y"]

data

from prophet import Prophet

prophet = Prophet(daily_seasonality=True)
prophet.fit(data)

future_dates = prophet.make_future_dataframe(periods=90)
predictions = prophet.predict(future_dates)

from prophet.plot import plot_plotly

plot_plotly(prophet, predictions)

future = pd.DataFrame({'ds': pd.to_datetime(['2024-01-20'])})
forecast = prophet.predict(future)
print(forecast[['ds', 'yhat']])

future = pd.DataFrame({'ds': pd.to_datetime(['2024-01-20 00:00:00'])})
forecast = prophet.predict(future)
print(forecast[['ds', 'yhat']])

unknown_data = data.iloc[-90:]
data = data.iloc[:-90]

prophet = Prophet(daily_seasonality=True)
prophet.fit(data)

future_dates = (prophet.make_future_dataframe(periods=365))
predictions = prophet.predict(future_dates)

plot_plotly(prophet, predictions)