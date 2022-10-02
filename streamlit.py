import streamlit as st
import requests
from datetime import datetime, timedelta
import pandas as pd
from kubernetes import client, config


def getJSONData(search_input):
    search =  search_input
    config.load_kube_config()
    v1 = client.CoreV1Api()
    key = v1.read_namespaced_secret("apikey", "default")
    url = "https://www.alphavantage.co/query?apikey="+key+"&function=TIME_SERIES_DAILY&symbol="+search
    r = requests.get(url)
    if (r.status_code == 200):
        return r.json()
    else:
        st.write("Error: " + r.status_code)

def getClosingValue(search_input,date):
    stock_ticker = search_input
    payload = getJSONData(stock_ticker)
    for key1, value1 in payload.items():
        for key2, value2 in value1.items():
            if key2 == date:
                for key3, value3 in value2.items():
                    if key3 == '4. close':
                        closing_value = value3
                        return closing_value



def relative_date(reference, weekday, timevalue):
    hour, minute = divmod(timevalue, 1)
    minute *= 60
    days = reference.weekday() - weekday
    return (reference - timedelta(days=days)).replace(hour=int(hour), minute=int(minute), second=0, microsecond=0)


d = datetime.now().date()
if (d.weekday() > 4):
    date = relative_date(datetime.now(),4,5).date()
else:
    date = datetime.now().date()



# Title
st.title("Display the closing data for any stock")

# main page
st.header('Query parameters')
ticker_list = pd.read_csv('https://raw.githubusercontent.com/giselle007/streamlit/master/ticker_symbols.txt')
option = st.selectbox('Select one symbol', ticker_list)
start_date = st.date_input("Desired date", date)
if start_date.weekday() < 5:
    st.success('Desired date %s' % (start_date))
    st.write(""" ### Stock Selected: """ + option)
    closing = str(getClosingValue(option,str(start_date)))
    closing_value = closing[0:6]
    st.write(""" Closing price: $""" + closing_value )
else:
    st.error("Error: Desired date must be a weekday")
    st.write(""" ### Stock Selected: """ + option)
    closing = str(getClosingValue(option,str(start_date)))
    closing_value = closing[0:6]
    st.write(""" Closing price: $""" + closing_value )

