import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from alpha_vantage.timeseries import TimeSeries
import pandas_bokeh
from bokeh.plotting import figure, show

################################ GET DATA ######################################

project_folder = os.path.expanduser('~/code/GitHub/madam_marie')
load_dotenv(os.path.join(project_folder,'.env'))
key = os.getenv("API_KEY")
ts = TimeSeries(key, output_format='pandas')

############################### STREAMLIT ######################################
# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")

header = st.beta_container()
dataset = st.beta_container()
# features = st.beta_container()
# test = st.sidebar.beta_container()

with header:
    st.title('Fortune Teller Tarot Reader')
    st.text('Data scraped from BiddyTarot.com')
    st.text('')
    st.text('App deployed using Heroku')

# with test:
#     st.title('Select Spread')
#     # st.text("Type the name of a stock ticker")
#     ticker = st.text_input("(i.e. 'AARP', 'AMZN', 'MSFT', 'GOOG', etc.)", 'GOOG')
#     data, meta = ts.get_daily_adjusted(ticker, outputsize='full')
#     display1 = ('Major','Minor')

# #     display1 = ('January','February','March','April','May','June','July','August','September','October','November','December')
#     options1 = list(range(len(display1)))
#     YEAR = st.selectbox('YEAR:', ['2021','2020','2019','2018','2017','2016','2015'])
#     monthh = st.selectbox('MONTH:', options1, format_func=lambda x: display1[x])
#     MONTH = monthh+1

#     cols = ['open','high','low','close','adj_close','volume','divedend','split_coeff']
#     data.columns = cols
#     data['day'] = data.index.date
#     data['time'] = data.index.time

#     US_daily_market = data
#     US_daily_market.index = pd.to_datetime(US_daily_market.index, format='%Y-%m-%d')

#     US_daily_market['month'] = US_daily_market.index.month
#     US_daily_market['year'] = US_daily_market.index.year
#     US_daily_market = US_daily_market.reset_index()
#     US_daily_market = US_daily_market.loc[(US_daily_market['month'] == int(MONTH)) & (US_daily_market['year'] == int(YEAR))]

#     date = US_daily_market['day']
#     x = US_daily_market['low']
#     y = US_daily_market['high']

with dataset:
    st.header("Three Tarot Spread")
    st.text('Tarot card images taken from Wikimedia, and descriptions scraped from BiddyTarot.com')
    st.text('The three card spread can represent several different meanings including:')
    st.text('[Past, Present, Future]')
    st.text('[Mind, Body, Soul]')
    st.text('[Background, Problem, Advice]')
#     st.header("Stock Market Data For: '{}'".format(ticker))
#     st.text('Data visualization constructed with Bokeh, from hourly intraday stock data')
#     g1_col, g2_col = st.beta_columns(2)
#     p = figure(title="The Highs and Lows of: '{}'".format(ticker), x_axis_type='datetime', x_axis_label='Date', y_axis_label='Value (USD)')
#     p.line(date, y, legend_label="Max / day (USD)", line_width=2)
#     p.line(date, x, color= "red", legend_label="Min / day (USD)", line_width=2)
#     st.bokeh_chart(p, use_container_width=True)

col1, col2, col3 = st.beta_columns(3)
# col1, col2, col3 = st.beta_columns((1,1,0.5))) also works

with col1:
    st.header("Moon")
    st.image("https://upload.wikimedia.org/wikipedia/en/7/7f/RWS_Tarot_18_Moon.jpg")
    st.text('')

with col2:
    st.header("Ace of Wands")
    st.image("https://upload.wikimedia.org/wikipedia/en/1/11/Wands01.jpg")
    st.text('')

with col3:
    st.header("Magician")
    st.image("https://upload.wikimedia.org/wikipedia/en/d/de/RWS_Tarot_01_Magician.jpg")
    st.text('')

    # c1 = st.image('https://upload.wikimedia.org/wikipedia/en/1/11/Wands01.jpg')
    # c2 = st.image('https://upload.wikimedia.org/wikipedia/en/d/de/RWS_Tarot_01_Magician.jpg')
    # c3 = st.image('https://upload.wikimedia.org/wikipedia/en/7/7f/RWS_Tarot_18_Moon.jpg')

    #
st.image(['https://upload.wikimedia.org/wikipedia/en/1/11/Wands01.jpg', 'https://upload.wikimedia.org/wikipedia/en/7/7f/RWS_Tarot_18_Moon.jpg', 'https://upload.wikimedia.org/wikipedia/en/d/de/RWS_Tarot_01_Magician.jpg'], width=250)
    # st.image('https://upload.wikimedia.org/wikipedia/en/d/de/RWS_Tarot_01_Magician.jpg', width=200)
    # st.image('https://upload.wikimedia.org/wikipedia/en/7/7f/RWS_Tarot_18_Moon.jpg', width=200)
    # st.markdown("![Alt Text](https://upload.wikimedia.org/wikipedia/en/d/de/RWS_Tarot_01_Magician.jpg)")

    # Space out the maps so the first one is 2x the size of the other three
    # c1, c2, c3 = st.beta_columns((1, 1, 1))

# >>> from PIL import Image
# >>> image = Image.open('sunrise.jpg')
# >>>
# >>> st.image(image, caption='Sunrise by the mountains')

# https://en.m.wikipedia.org/wiki/The_Fool_(Tarot_card)#/media/File%3ARWS_Tarot_00_Fool.jpg
# https://en.m.wikipedia.org/wiki/The_Magician_(Tarot_card)#/media/File%3ARWS_Tarot_01_Magician.jpg
# https://en.m.wikipedia.org/wiki/Ace_of_Wands_(Tarot_card)#/media/File%3AWands01.jpg
# https://www.sacred-texts.com/tarot/pkt/img/ar01.jpg
# https://www.sacred-texts.com/tarot/pkt/img/ar02.jpg
################################################################################
# useful links:
#
# bokeh:
#   https://www.youtube.com/watch?v=tnOgrlqA0Bc
#   https://pythonforundergradengineers.com/streamlit-app-with-bokeh.html
# alpha vantage:
#   https://www.youtube.com/watch?v=WJ2t_LYb__0
# streamlit:
#   four part series, used first 2/3:
#   https://www.youtube.com/watch?v=CSv2TBA9_2E
#
