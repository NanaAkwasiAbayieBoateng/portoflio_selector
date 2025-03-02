import streamlit as st
import plotly.graph_objects as go
import yfinance as yf
import datetime as dt
import pandas as pd
import plotly.express as px
pd.options.plotting.backend = "plotly"


# Create a dropdown menu to choose the graph type
#graph_type = st.selectbox('Select Graph Type 1', ['Bar Chart', 'Line Chart', 'Scatter Plot'])
stock_type_selected = st.selectbox('Select Stock Type 1', ['S & P 500 Stocks', 'Broad Market'])
stock_industry_selected = st.selectbox('Select Stock Industry 1', ['Industrials', 'Health_Care', 'Information_Technology',
       'Utilities', 'Financials', 'Materials', 'Consumer_Discretionary',
       'Real_Estate', 'Communication_Services', 'Consumer_Staples',
       'Energy'])
       
tickers_selected = st.text_input("Enter stock indices (comma-separated):", value="", max_chars= 1000, placeholder= 'AAPL', disabled=False, label_visibility="visible")
tickers_selected_list = tickers_selected.split(",")

 


look_back_years = 1

default_start_date = dt.datetime(dt.date.today().year - look_back_years, dt.date.today().month, dt.date.today().day)
default_end_date  = dt.datetime(dt.date.today().year, dt.date.today().month, dt.date.today().day)


start =   st.text_input("Enter start date", value="", max_chars= 10, placeholder= default_start_date, disabled=False, label_visibility="visible")
end =     st.text_input("Enter start date", value="", max_chars= 10, placeholder= default_end_date, disabled=False, label_visibility="visible")

#start = '2024-01-01'
#end  = '2024-06-30'



data = pd.DataFrame()
return_df  = pd.DataFrame()





def get_stock(stock_type,stock_industry=None,tickers=None):
    if stock_type == 'S & P 500 Stocks':
       #retrieve table of list of companies on  s & p 500
       url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
       df = pd.read_html(url)
       #sectors of economy
       Industrials  = df[0]['Symbol'][df[0]['GICS Sector'].str.contains(pat='Industrials')]
       Financials = df[0]['Symbol'][df[0]['GICS Sector'].str.contains(pat='Financials')]
       Information_Technology  = df[0]['Symbol'][df[0]['GICS Sector'].str.contains(pat='Information Technology')]
       Health_Care   = df[0]['Symbol'][df[0]['GICS Sector'].str.contains(pat='Health Care')]
       Consumer_Discretionary = df[0]['Symbol'][df[0]['GICS Sector'].str.contains(pat='Consumer Discretionary')]
       Consumer_Staples  = df[0]['Symbol'][df[0]['GICS Sector'].str.contains(pat='Consumer Staples')]
       Utilities   = df[0]['Symbol'][df[0]['GICS Sector'].str.contains(pat='Utilities')]
       Real_Estate  = df[0]['Symbol'][df[0]['GICS Sector'].str.contains(pat='Real Estate')]
       Materials  = df[0]['Symbol'][df[0]['GICS Sector'].str.contains(pat='Materials')]
       Communication_Services = df[0]['Symbol'][df[0]['GICS Sector'].str.contains(pat='Communication Services')]
       Energy  = df[0]['Symbol'][df[0]['GICS Sector'].str.contains(pat='Energy')]


        
       if   stock_industry == 'Industrials':
            try:
               for ticker in Industrials:
                   df = yf.download(ticker, start=start, end=end)['Close']
                   #df  = pdr.get_data_yahoo(ticker, start, end)['Close'] 
                   #cumulative daily return
                   #rf  = df.pct_change().cumsum()
                   rf =  (df.pct_change() + 1).cumprod()-1
                   if len(df) > 0:
                      data[ticker] = df
                      return_df[ticker]  = rf*100

            except:
                pass
        
       elif stock_industry == 'Health_Care':
            try:
               for ticker in Health_Care:
                   df = yf.download(ticker, start=start, end=end)['Close']
                   rf =  (df.pct_change() + 1).cumprod()-1
                   if len(df) > 0:
                      data[ticker] = df
                      return_df[ticker]  = rf*100

            except:
                pass
        
       elif stock_industry == 'Information_Technology':
            try:
               for ticker in Information_Technology:
                   df = yf.download(ticker, start=start, end=end)['Close']
                   rf =  (df.pct_change() + 1).cumprod()-1
                   if len(df) > 0:
                      data[ticker] = df
                      return_df[ticker]  = rf*100

            except:
                pass
        

        
       elif stock_industry == 'Utilities':
            try:
                for ticker in Utilities:
                    df = yf.download(ticker, start=start, end=end)['Close']
                    rf =  (df.pct_change() + 1).cumprod()-1
                    if len(df) > 0:
                       data[ticker] = df
                       return_df[ticker]  = rf*100
            except:
              pass
       
       
       
       elif stock_industry == 'Financials':
            try:
               for ticker in  Financials:
                   df = yf.download(ticker, start=start, end=end)['Close']
                   rf =  (df.pct_change() + 1).cumprod()-1
                   if len(df) > 0:
                      data[ticker] = df
                      return_df[ticker]  = rf*100

            except:
                pass
        
       elif stock_industry == 'Materials':
            try:
               for ticker in  Materials :
                   df = yf.download(ticker, start=start, end=end)['Close']
                   rf =  (df.pct_change() + 1).cumprod()-1
                   if len(df) > 0:
                      data[ticker] = df
                      return_df[ticker]  = rf*100
            except:
                pass                      
        
       elif stock_industry == 'Consumer_Discretionary':
            try:
               for ticker in  Consumer_Discretionary:
                   df = yf.download(ticker, start=start, end=end)['Close']
                   rf =  (df.pct_change() + 1).cumprod()-1
                   if len(df) > 0:
                      data[ticker] = df
                      return_df[ticker]  = rf*100  
            except:
                pass                      

       elif stock_industry == 'Real_Estate':
            try:
               for ticker in  Real_Estate:
                   df = yf.download(ticker, start=start, end=end)['Close']
                   rf =  (df.pct_change() + 1).cumprod()-1
                   if len(df) > 0:
                      data[ticker] = df
                      return_df[ticker]  = rf*100 
            except:
                pass                      
        
        
       elif stock_industry == 'Communication_Services':
            try:
               for ticker in  Communication_Services:
                   df = yf.download(ticker, start=start, end=end)['Close']
                   rf =  (df.pct_change() + 1).cumprod()-1
                   if len(df) > 0:
                      data[ticker] = df
                      return_df[ticker]  = rf*100  
            except:
                pass                      

       elif stock_industry == 'Consumer_Staples':
            try:
               for ticker in  Consumer_Staples:
                   df = yf.download(ticker, start=start, end=end)['Close']
                   rf =  (df.pct_change() + 1).cumprod()-1
                   if len(df) > 0:
                      data[ticker] = df
                      return_df[ticker]  = rf*100  
            except:
                pass                      
        
        
       elif stock_industry == 'Energy':
            try:
               for ticker in  Energy:
                   df = yf.download(ticker, start=start, end=end)['Close']
                   rf =  (df.pct_change() + 1).cumprod()-1
                   if len(df) > 0:
                      data[ticker] = df
                      return_df[ticker]  = rf*100                        

            except:
     
                pass   

    elif stock_type == 'Broad Market':
        
        try:
           for ticker in  tickers:
                df = yf.download(ticker, start=start, end=end)['Close']
                rf =  (df.pct_change() + 1).cumprod()-1
                if len(df) > 0:
                    data[ticker] = df
                    return_df[ticker]  = rf*100  

        except:
     
            pass     
           
    return return_df



# Create a dropdown menu to choose the graph type
graph_type = st.selectbox('Select Graph Type 1', ['Bar Chart', 'Line Chart'])
return_df = get_stock(stock_type_selected,stock_industry_selected,tickers_selected_list)
#return_df['Year']  = return_df.index.year.astype(str)

st.dataframe(return_df.head())



