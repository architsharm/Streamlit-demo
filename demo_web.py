import streamlit as st
import yfinance as yf
import datetime
st.title("Welcome to Stock World")
# ticker_map={
#     'GOOGLE': 'GOOG',
#     'Microsoft':'MSFT'
# }
# stock_ticker = st.text_input('Stock Chooser', 'GOOGLE')
stock_ticker = st.text_input('Stock Chooser', 'GOOG')
# msft = yf.Ticker(ticker_map[stock_ticker])
ticker = yf.Ticker(stock_ticker)
# st.dataframe(hist.head(100))
col1, col2 = st.columns(2)
with col1:
   d = st.date_input("Start Date", datetime.date(2019, 7, 6))
with col2:
   e = st.date_input("End Date", datetime.date(2021, 7, 6))

hist = ticker.history(period="1d", start=d,end=e)

col1, col2 = st.columns(2)
with col1:
   st.line_chart(hist['Close'])
with col2:
   st.line_chart(hist['Volume'])




