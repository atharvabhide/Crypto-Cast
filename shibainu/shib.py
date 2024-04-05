import os
import matplotlib.pyplot as plt
import yfinance as yf
import streamlit as st
from datetime import datetime
import plotly.express as px
import statsmodels.api as sm
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from functools import lru_cache


@lru_cache(maxsize=128)
def load_model(path):
    return tf.keras.models.load_model(path)

def get_shib():
    shib = yf.download('SHIB-CAD')
    shib = shib.drop(['Open', 'High', 'Low', 'Close', 'Volume'], axis=1)

    # Load LSTM model
    lstm_model = load_model(os.path.join(os.getcwd(), "lstm", "models", "SHIB-CAD.h5"))
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(shib['Adj Close'].values.reshape(-1, 1))

    # Predict using LSTM model
    future_data = scaled_data[-10:].reshape(1, 10, 1)
    future_predictions_lstm = []
    for i in range(365):  # Adjust the number of future predictions as needed for one year
        prediction = lstm_model.predict(future_data)
        future_predictions_lstm.append(prediction[0, 0])
        future_data = np.append(future_data[:, 1:, :], prediction.reshape(1, 1, 1), axis=1)

    # Inverse transform the predictions to get actual prices
    future_predictions_lstm = scaler.inverse_transform(np.array(future_predictions_lstm).reshape(-1, 1))

    # SARIMAX model
    modelhigh = sm.tsa.statespace.SARIMAX(shib['Adj Close'],
                                          order=(0, 1, 1),
                                          seasonal_order=(1, 1, 1, 12),
                                          enforce_stationarity=False,
                                          enforce_invertibility=False)
    resultshigh = modelhigh.fit()
    pred = resultshigh.get_prediction(start=datetime(2021, 3, 3), dynamic=False)
    pred_ci = pred.conf_int()
    ax = shib['2018':].plot(label='Observed (SARIMAX)')
    pred.predicted_mean.plot(ax=ax, label='Forecasted (SARIMAX)', alpha=.2, figsize=(14, 7))
    pred_uc = resultshigh.get_forecast(steps=365)
    pred_ci = pred_uc.conf_int()
    ax = shib.plot(label='Observed (SARIMAX)', color='grey', figsize=(20, 8))
    One_week_values_sarimax = pred_uc.predicted_mean[:7]
    One_week_values_sarimax = round(One_week_values_sarimax, 2)
    pred_uc.predicted_mean.plot(ax=ax, color='green', label='Forecast (SARIMAX)')
    ax.set_xlabel('Date')
    ax.set_ylabel('CAD price')
    ax.patch.set_facecolor('white')
    plt.legend()

    # Plot LSTM predictions
    plt.figure(figsize=(10, 7))
    shib['Adj Close'].plot(label='Observed (LSTM)', color='blue')
    future_index = pd.date_range(start=shib.index[-1], periods=366, closed='right')  # One extra day for leap year
    future_df = pd.DataFrame({'Adj Close': future_predictions_lstm.flatten()}, index=future_index)
    future_df.plot(label='Forecasted (LSTM)', color='green')
    plt.title('Shibainu (SHIB) Forecasting (LSTM)')
    plt.xlabel('Date')
    plt.ylabel('CAD price')
    plt.legend()
    with st.expander("👁 (All time graph + predicted graph)"):
        st.pyplot(plt, use_container_width=True)

        # printing one week values
    st.header("One Week Forecasting (SARIMAX)")
    fig = px.line(x=One_week_values_sarimax.index, y=One_week_values_sarimax.values,
                      labels={'x': 'Date', 'y': 'CAD Dollars'}, title="Shibainu (SHIB) forecasting (SARIMAX) - One Week",
                      markers=True)
    fig.update_traces(line_color='#76D714', line_width=5)  # 00ff00
    with st.expander("👁 ", True):
            st.plotly_chart(fig, use_container_width=True)

    # printing 6 months values
    st.header("1 Month Forecasting (SARIMAX)")
    fig = px.line(x=pred_uc.predicted_mean.index, y=pred_uc.predicted_mean.values,
                  labels={'x': 'Date', 'y': 'CAD Dollars'}, title="Shibainu (SHIB) forecasting (SARIMAX) - One Month",
                  markers=True)
    fig.update_traces(line_color='#76D714', line_width=5)
    with st.expander("👁 ", True):
        st.plotly_chart(fig, use_container_width=True)

    # Plot one-week forecast (LSTM)
    st.header("One Week Forecasting (LSTM)")
    fig = px.line(x=future_index[:7], y=future_predictions_lstm[:7].flatten(),
                      labels={'x': 'Date', 'y': 'CAD Dollars'}, title="Shibainu (SHIB) forecasting (LSTM) - One Week",
                      markers=True)
    fig.update_traces(line_color='#76D714', line_width=5)  # 00ff00
    with st.expander("👁 ", True):
            st.plotly_chart(fig, use_container_width=True)

    # Plot one-month forecast (LSTM)
    st.header("1 Month Forecasting (LSTM)")
    fig = px.line(x=future_index, y=future_predictions_lstm.flatten(),
                  labels={'x': 'Date', 'y': 'CAD Dollars'}, title="Shibainu (SHIB) forecasting (LSTM) - One Month",
                  markers=True)
    fig.update_traces(line_color='#76D714', line_width=5)
    with st.expander("👁 ", True):
        st.plotly_chart(fig, use_container_width=True)

    # Plot one-year forecast (LSTM)
    st.header("One Year Forecasting (LSTM)")
    fig = px.line(x=future_index, y=future_predictions_lstm.flatten(),
                  labels={'x': 'Date', 'y': 'CAD Dollars'}, title="Shibainu (SHIB) forecasting (LSTM) - One Year",
                  markers=True)
    fig.update_traces(line_color='#76D714', line_width=5)
    with st.expander("👁 ", True):
        st.plotly_chart(fig, use_container_width=True)