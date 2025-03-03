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

#start = '2025-01-01'
#end  = '2025-01-15'



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
            except:
                pass
        
        elif stock_industry == 'Health_Care':
            try:
                for ticker in Health_Care:
                    df = yf.download(ticker, start=start, end=end)['Close']
                    rf =  (df.pct_change() + 1).cumprod()-1
                    if len(df) > 0:
                        download_data.append(df)
                        return_data.append(rf*100)
            except:
                pass
        elif stock_industry == 'Information_Technology':
            try:
                for ticker in Health_Care:
                    df = yf.download(ticker, start=start, end=end)['Close']
                    rf =  (df.pct_change() + 1).cumprod()-1
                    if len(df) > 0:
                        download_data.append(df)
                        return_data.append(rf*100)
            except:
                pass
        elif stock_industry == 'Utilities':
            try:
                for ticker in Health_Care:
                    df = yf.download(ticker, start=start, end=end)['Close']
                    rf =  (df.pct_change() + 1).cumprod()-1
                    if len(df) > 0:
                        download_data.append(df)
                        return_data.append(rf*100)
            except:
                pass
        elif stock_industry == 'Financials':
            try:
                for ticker in Health_Care:
                    df = yf.download(ticker, start=start, end=end)['Close']
                    rf =  (df.pct_change() + 1).cumprod()-1
                    if len(df) > 0:
                        download_data.append(df)
                        return_data.append(rf*100)
            except:
                pass
        elif stock_industry == 'Materials':
            try:
                for ticker in Health_Care:
                    df = yf.download(ticker, start=start, end=end)['Close']
                    rf =  (df.pct_change() + 1).cumprod()-1
                    if len(df) > 0:
                        download_data.append(df)
                        return_data.append(rf*100)
            except:
                pass
        elif stock_industry == 'Consumer_Discretionary':
            try:
                for ticker in Health_Care:
                    df = yf.download(ticker, start=start, end=end)['Close']
                    rf =  (df.pct_change() + 1).cumprod()-1
                    if len(df) > 0:
                        download_data.append(df)
                        return_data.append(rf*100)
            except:
                pass
        elif stock_industry ==  'Real_Estate':
            try:
                for ticker in Health_Care:
                    df = yf.download(ticker, start=start, end=end)['Close']
                    rf =  (df.pct_change() + 1).cumprod()-1
                    if len(df) > 0:
                        download_data.append(df)
                        return_data.append(rf*100)
            except:
                pass
        elif stock_industry == 'Communication_Services':
            try:
                for ticker in Health_Care:
                    df = yf.download(ticker, start=start, end=end)['Close']
                    rf =  (df.pct_change() + 1).cumprod()-1
                    if len(df) > 0:
                        download_data.append(df)
                        return_data.append(rf*100)
            except:
                pass
        elif stock_industry == 'Consumer_Staples':
            try:
                for ticker in Health_Care:
                    df = yf.download(ticker, start=start, end=end)['Close']
                    rf =  (df.pct_change() + 1).cumprod()-1
                    if len(df) > 0:
                        download_data.append(df)
                        return_data.append(rf*100)
            except:
                pass  
        elif stock_industry == 'Energy':
            try:
                for ticker in Health_Care:
                    df = yf.download(ticker, start=start, end=end)['Close']
                    rf =  (df.pct_change() + 1).cumprod()-1
                    if len(df) > 0:
                        download_data.append(df)
                        return_data.append(rf*100)
            except:
                pass    
    

    elif stock_type == 'Broad Market':
        
        try:
            for ticker in  tickers:
                df = yf.download(ticker, start=start, end=end)['Close']
                rf =  (df.pct_change() + 1).cumprod()-1
                if len(df) > 0:
                   download_data.append(df)
                   return_data.append(rf*100)

        except:
     
            pass     
    
    return pd.concat(return_data,axis=1)      
 

# Create a dropdown menu to choose the graph type
#graph_type = st.selectbox('Select Graph Type 1', ['Bar Chart', 'Line Chart'])
#return_df = get_stock(stock_type_selected,stock_industry_selected,tickers_selected_list)
#return_df['Year']  = return_df.index.year.astype(str)
#st.dataframe(return_df.head())


# Create a dropdown menu to choose the graph type
graph_type = st.selectbox('Select Graph Type 1', ['Bar Chart', 'Line Chart'])
return_df = get_stock(stock_type_selected,stock_industry_selected,tickers_selected_list)
return_df.reset_index(inplace =True)
#return_df['Year']  = return_df.index.year.astype(str)
return_df['Year'] = return_df.loc[:,'Date'].dt.year.astype(str)
stock_list =  list(set(return_df.columns).difference(['Year']))

#['S & P 500 Stocks', 'Broad Market'], stock_industry_selected
if  stock_type_selected == 'S & P 500 Stocks':
    
    #return_df.drop('Date',axis=1,inplace=True)
    return_df.reset_index(drop=True, inplace=True)
    #stock_list =  list(set(return_df.columns).difference('Year'))
    #d = return_df.drop('Year',axis=1).mean().reset_index().rename(columns= {'index':'Stock',0:'Mean_Return'}).sort_values(by='Mean_Return',ascending=False)
    #d = return_df[list(stock_industry_selected) + ['Year']].groupby('Year').mean().reset_index().melt(id_vars ='Year',value_vars=list(stock_industry_selected))
    d = return_df[stock_list + ['Year']].groupby('Year').mean().reset_index().melt(id_vars ='Year',value_vars= stock_list)
else:
    #tickers_selected_list = tickers_selected
    fig=return_df[stock_list].plot(color_discrete_sequence=px.colors.qualitative.Set1,title= f"Mean Return Between {start} to {end}")



# Create a function to generate the graph
def generate_graph(graph_type):
    if graph_type == 'Bar Chart':
        
        if stock_type_selected == 'S & P 500 Stocks':
            #fig = px.bar(d, x="Stock", y="Mean_Return", orientation='v',title= f"Mean Return Between {start} to {end}", color="Stock",color_discrete_sequence=px.colors.qualitative.Set1)
            fig = px.bar(d, x="Year", y="value", orientation='v',title= f"Mean Return Between {start} to {end}", color="Ticker",color_discrete_sequence=px.colors.qualitative.Set1, barmode="group")
            fig.update_layout(yaxis_title="Mean Return (%)")            
        
        else:
            fig = px.bar(d, x="Year", y="value", orientation='v',title= f"Mean Return Between {start} to {end}", color="Ticker",color_discrete_sequence=px.colors.qualitative.Set1, barmode="group")
            fig.update_layout(yaxis_title="Mean Return (%)")

    elif graph_type == 'Line Chart':
        fig=return_df[stock_list].plot(color_discrete_sequence=px.colors.qualitative.Set1,title= f"Mean Return Between {start} to {end}")
        fig.update_layout(yaxis_title="Daily Return (%)")
        fig.update_xaxes(tickangle=45)

    return fig

# Create a Streamlit app
st.title('Graph App')
st.write('Select a graph type to display:')
graph_type_selected = st.selectbox('Select Graph Type 2', ['Bar Chart', 'Line Chart'])
fig = generate_graph(graph_type_selected)
st.plotly_chart(fig, use_container_width=True)




# Create a Streamlit app
#st.title('Returns Chart')
#st.write(f'{tickers_selected_list + ['Year']}')
#graph_type_selected = st.selectbox('Select Graph Type 2', ['Bar Chart', 'Line Chart', 'Scatter Plot'])
#fig = generate_graph(graph_type_selected)

#d = get_stock(stock_type_selected,stock_industry_selected).mean().reset_index().rename(columns= {'index':'Stock',0:'Mean_Return'}).sort_values(by='Mean_Return',ascending=False)
#fig = px.bar(d, x="Stock", y="Mean_Return", orientation='v',title= f"Mean Return Between {start} to {end}", color="Stock",color_discrete_sequence=px.colors.qualitative.Set1)
#fig.update_layout(yaxis_title="Mean Return (%)")
#st.plotly_chart(fig, use_container_width=True)
# Format y-axis as percentage
#fig.update_yaxes(tickformat=".0%")
#st.plotly_chart(fig, use_container_width=True)
#st.dataframe(d.rename(columns={'value':'Mean Return %'}))
#st.dataframe(return_df.head())
st.dataframe(d)
#fig.show()