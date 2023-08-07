import yfinance as yf
import streamlit as st
import pandas as pd
st.write("""# Simple Stock Price

Shown are the stock **closing price** and ***volume*** """)
tickerSymbol = 'APP'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='id',start='2010-5-31',end='2021-5-31')
st.write("""
## Closing price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume price
""")
st.line_chart(tickerDf.Volume)