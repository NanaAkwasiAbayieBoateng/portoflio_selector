import streamlit as st
import plotly.graph_objects as go
import yfinance as yf
import datetime as dt
import pandas as pd
import plotly.express as px
import logging
logging.basicConfig(level=logging.INFO)  # Configure logging
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




def get_stock(stock_type,stock_industry=None,tickers=None):
    return_data = []
    download_data = []
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
                    rf =  (df.pct_change() + 1).cumprod()-1
                    if len(df) > 0:
                        download_data.append(df)
                        return_data.append(rf*100)
            except Exception as e:
                pass
                logging.error(f"Error downloading ticker {ticker}: {e}")
        
        elif stock_industry == 'Health_Care':
            try:
                for ticker in Health_Care:
                    df = yf.download(ticker, start=start, end=end)['Close']
                    rf =  (df.pct_change() + 1).cumprod()-1
                    if len(df) > 0:
                        download_data.append(df)
                        return_data.append(rf*100)
            except Exception as e:
                pass
                logging.error(f"Error downloading ticker {ticker}: {e}")
                
        elif stock_industry == 'Information_Technology':
            try:
                for ticker in Health_Care:
                    df = yf.download(ticker, start=start, end=end)['Close']
                    rf =  (df.pct_change() + 1).cumprod()-1
                    if len(df) > 0:
                        download_data.append(df)
                        return_data.append(rf*100)
            except Exception as e:
                pass
                logging.error(f"Error downloading ticker {ticker}: {e}")
                
        elif stock_industry == 'Utilities':
            try:
                for ticker in Health_Care:
                    df = yf.download(ticker, start=start, end=end)['Close']
                    rf =  (df.pct_change() + 1).cumprod()-1
                    if len(df) > 0:
                        download_data.append(df)
                        return_data.append(rf*100)
            except Exception as e:
                pass
                logging.error(f"Error downloading ticker {ticker}: {e}")
                
        elif stock_industry == 'Financials':
            try:
                for ticker in Health_Care:
                    df = yf.download(ticker, start=start, end=end)['Close']
                    rf =  (df.pct_change() + 1).cumprod()-1
                    if len(df) > 0:
                        download_data.append(df)
                        return_data.append(rf*100)
            except Exception as e:
                pass
                logging.error(f"Error downloading ticker {ticker}: {e}")
                
        elif stock_industry == 'Materials':
            try:
                for ticker in Health_Care:
                    df = yf.download(ticker, start=start, end=end)['Close']
                    rf =  (df.pct_change() + 1).cumprod()-1
                    if len(df) > 0:
                        download_data.append(df)
                        return_data.append(rf*100)
            except Exception as e:
                pass
                logging.error(f"Error downloading ticker {ticker}: {e}")
                
        elif stock_industry == 'Consumer_Discretionary':
            try:
                for ticker in Health_Care:
                    df = yf.download(ticker, start=start, end=end)['Close']
                    rf =  (df.pct_change() + 1).cumprod()-1
                    if len(df) > 0:
                        download_data.append(df)
                        return_data.append(rf*100)
            except Exception as e:
                pass
                logging.error(f"Error downloading ticker {ticker}: {e}")
                
        elif stock_industry ==  'Real_Estate':
            try:
                for ticker in Health_Care:
                    df = yf.download(ticker, start=start, end=end)['Close']
                    rf =  (df.pct_change() + 1).cumprod()-1
                    if len(df) > 0:
                        download_data.append(df)
                        return_data.append(rf*100)
            except Exception as e:
                pass
                logging.error(f"Error downloading ticker {ticker}: {e}")
                
        elif stock_industry == 'Communication_Services':
            try:
                for ticker in Health_Care:
                    df = yf.download(ticker, start=start, end=end)['Close']
                    rf =  (df.pct_change() + 1).cumprod()-1
                    if len(df) > 0:
                        download_data.append(df)
                        return_data.append(rf*100)
            except Exception as e:
                pass
                logging.error(f"Error downloading ticker {ticker}: {e}")
                
        elif stock_industry == 'Consumer_Staples':
            try:
                for ticker in Health_Care:
                    df = yf.download(ticker, start=start, end=end)['Close']
                    rf =  (df.pct_change() + 1).cumprod()-1
                    if len(df) > 0:
                        download_data.append(df)
                        return_data.append(rf*100)
            except Exception as e:
                pass
                logging.error(f"Error downloading ticker {ticker}: {e}")
                
        elif stock_industry == 'Energy':
            try:
                for ticker in Health_Care:
                    df = yf.download(ticker, start=start, end=end)['Close']
                    rf =  (df.pct_change() + 1).cumprod()-1
                    if len(df) > 0:
                        download_data.append(df)
                        return_data.append(rf*100)
            except Exception as e:
                pass
                logging.error(f"Error downloading ticker {ticker}: {e}")  
    

    elif stock_type == 'Broad Market':
        
        try:
            for ticker in  tickers:
                df = yf.download(ticker, start=start, end=end)['Close']
                rf =  (df.pct_change() + 1).cumprod()-1
                if len(df) > 0:
                   download_data.append(df)
                   return_data.append(rf*100)

        except Exception as e:
             pass
             logging.error(f"Error downloading ticker {ticker}: {e}")
            
    #df  =  pd.concat(return_data,axis=1)
    #df = df.loc[:,~df.columns.duplicated()].copy()
    if return_data:  # Check if return_data is not empty
        df = pd.concat(return_data, axis=1)
        df = df.loc[:,~df.columns.duplicated()].copy()
        return df
    else:
        return pd.DataFrame()  # Return an empty DataFrame if return_data is empty
        logging.info(f"dataframe empty")
    return df     









# Create a dropdown menu to choose the graph type
graph_type = st.selectbox('Select Graph Type 1', ['Bar Chart', 'Line Chart'])
return_df = get_stock(stock_type_selected,stock_industry_selected,tickers_selected_list)
return_df.reset_index(inplace =True)
return_df['Year'] = return_df.reset_index().loc[:,'Date'].dt.year.astype(str)
stock_list =  list(set(return_df.columns).difference(['Year','Ticker','Date']))
#st.dataframe(return_df.head())
#st.dataframe(pd.DataFrame(return_df.columns))

#['S & P 500 Stocks', 'Broad Market'], stock_industry_selected
if  stock_type_selected == 'S & P 500 Stocks':
    

    
    d = return_df[stock_list + ['Year']].groupby('Year').mean().reset_index().melt(id_vars ='Year',value_vars= stock_list)
else:
    #tickers_selected_list = tickers_selected
    d = return_df[list(tickers_selected_list) + ['Year']].groupby('Year').mean().reset_index().melt(id_vars ='Year',value_vars= list(tickers_selected_list))



# Create a function to generate the graph



# Assuming return_df, tickers_selected_list, start, end, and stock_type_selected are defined elsewhere

def generate_graph(graph_type, stock_type_selected):
    fig = None  # Initialize fig

    if graph_type == 'Bar Chart':
        if 'd' in locals() or 'd' in globals():
            try:
                fig = px.bar(
                    d,
                    x="Year",
                    y="value",
                    orientation='v',
                    title=f"Mean Return Between {start} to {end}",
                    color="Ticker",
                    color_discrete_sequence=px.colors.qualitative.Set1,
                    barmode="group",
                )
                fig.update_layout(yaxis_title="Mean Return (%)")
            except Exception as e:
                st.error(f"Error creating Bar Chart: {e}")
                fig = px.bar()
        else:
            st.error("DataFrame 'd' is not defined.")
            fig = px.bar()

    elif graph_type == 'Line Chart' and stock_type_selected == 'Broad Market':
        if return_df is not None and not return_df.empty and tickers_selected_list:
            try:
                fig = px.line(
                    return_df[tickers_selected_list +['Date']].set_index('Date'),
                    title=f" Return Between {start} to {end}",
                    color_discrete_sequence=px.colors.qualitative.Set1,
                )
                fig.update_layout(yaxis_title="Daily Return (%)")
                fig.update_xaxes(tickangle=45)
            except Exception as e:
                st.error(f"Error creating Line Chart: {e}")
                fig = px.line()
        else:
            st.error("Data for Line Chart is missing or invalid.")
            fig = px.line()
    elif graph_type == 'Line Chart' and stock_type_selected == 'S & P 500 Stocks':
        if return_df is not None and not return_df.empty and tickers_selected_list:
            try:
                fig = px.line(
                    return_df[stock_list +['Date']].set_index('Date'),
                    title=f" Return Between {start} to {end}",
                    color_discrete_sequence=px.colors.qualitative.Set1,
                )
                fig.update_layout(yaxis_title="Daily Return (%)")
                fig.update_xaxes(tickangle=45)
            except Exception as e:
                st.error(f"Error creating Line Chart: {e}")
                fig = px.line()
        else:
            st.error("Data for Line Chart is missing or invalid.")
            fig = px.line()
        
    print(f"Generated fig: {fig}") #debug print
    return fig

# Create a Streamlit app
st.title('Graph App')
st.write('Select a graph type to display:')
graph_type_selected = st.selectbox('Select Graph Type 2', ['Bar Chart', 'Line Chart'])
fig = generate_graph(graph_type_selected,stock_type_selected)
st.plotly_chart(fig, use_container_width=True)
st.dataframe(d)







