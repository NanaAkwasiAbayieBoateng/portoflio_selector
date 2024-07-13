import streamlit as st
import yfinance as yf
import pandas as pd

def get_closing_prices(indices):
  """Fetches closing prices for a list of indices."""
  data = yf.download(indices, period="1d")["Close"]
  return data.iloc[-1]  # Get the last row (closing prices)

def main():
  st.title("Stock Index Closing Prices")

  indices = st.text_input("Enter stock indices (comma-separated):", "")
  indices_list = indices.split(",")

  if indices:
    try:
      closing_prices = get_closing_prices(indices_list)
      st.dataframe(closing_prices)
    except Exception as e:
      st.error(f"Error fetching data: {e}")

if __name__ == "__main__":
  main()