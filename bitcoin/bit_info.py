import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
import base64

def get_bit_info():

    data = yf.download("BTC-CAD")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=list(data.index), y=list(data['Adj Close']), line=dict(color="#76D714")))
    fig.update_layout(
                      xaxis_title="Date",
                      yaxis_title="P rice in Canadian dollar", )
    fig.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="HTD", step="hour", stepmode="todate"),
                    dict(count=1,
                         label="1m",
                         step="month",
                         stepmode="backward"),
                    dict(count=3,
                         label="3m",
                         step="month",
                         stepmode="backward"),
                    dict(count=6,
                         label="6m",
                         step="month",
                         stepmode="backward"),
                    dict(count=1,
                         label="1y",
                         step="year",
                         stepmode="backward"),
                    dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type="date"
        )
    )
    st.header("Bitcoin All time graph")
    st.plotly_chart(fig, use_container_width=True)
