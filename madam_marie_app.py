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
sidebar = st.sidebar.beta_container()

with header:
    st.title('Fortune Teller Tarot Reader')
    st.text('Data scraped from BiddyTarot.com')
    st.text('')
    st.text('App deployed using Heroku')

with sidebar:
    st.title('Select cards')

# with test:
#     st.title('Select Spread')
#     # st.text("Type the name of a stock ticker")
#     ticker = st.text_input("(i.e. 'AARP', 'AMZN', 'MSFT', 'GOOG', etc.)", 'GOOG')
#     data, meta = ts.get_daily_adjusted(ticker, outputsize='full')
    display1 = ('Major','Minor')

# #     display1 = ('January','February','March','April','May','June','July','August','September','October','November','December')
#     options1 = list(range(len(display1)))
#     YEAR = st.selectbox('YEAR:', ['2021','2020','2019','2018','2017','2016','2015'])
#     monthh = st.selectbox('MONTH:', options1, format_func=lambda x: display1[x])
#     MONTH = monthh+1
    st.selectbox(label='Card 1', options1 = display1)
    st.selectbox(label='Card 2', options2 = display1)
    st.selectbox(label='Card 3', options3 = display1)
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
#     st.bokeh_chart(p, use_beta_container_width=True)


col1, col2, col3 = st.beta_columns(3)
# col1, col2, col3 = st.beta_columns((1,1,0.5))) also works

with col1:
    st.header("Moon")
    st.image("https://upload.wikimedia.org/wikipedia/en/7/7f/RWS_Tarot_18_Moon.jpg", width=400)
    st.text('')

with col2:
    st.header("Ace of Wands")
    st.image("https://upload.wikimedia.org/wikipedia/en/1/11/Wands01.jpg", width=400)
    st.text_input('Upright Ace of Wands: As an Ace, this Wands card brings you pure potential – this time in the spiritual, energetic realm. Ideas are flowing to you, motivating and inspiring you to pursue a new path. You are open to receiving new opportunities that align with your Higher Self. A whole world of possibility is available to you.The Ace of Wands encourages you to follow your heart and live your passion. If you feel a strong pull towards a new project or path, but are questioning whether it will work, then this card gives you a gentle nudge to pursue your passion. You can always start out small, treating the project or idea as an experiment or trial. Then, if it feels good, keep doing it; and if it doesn’t, make adjustments and try again. Let your energy, dedication and motivation be your guides.If you have been looking for a sign about whether this is the right project, then the Ace of Wands is a clear YES! The sprouting wand and the fertile landscape in the background are all positive indications that this idea has the potential to turn into something fulfilling and energising. Use your creative energy and passion to take the first steps. Even if you prefer to plan out everything before you begin down a particular path, the Ace of Wands wants you to listen to your instincts and follow your gut. If it seems like a good idea, it probably is. So, start with a few fundamentals to get things rolling, and then continue to grow and develop your ideas through more complex activities later on. The important thing is that you act now rather than spending more time planning or researching.Keep in mind, however, that the Aces represent potential but not guaranteed results. The Ace of Wands (or any Ace) is a seed that has yet to grow into something more substantial or sustainable. The opportunity on offer shows great promise, but it will be up to you to maximise it for the long term. See this card as the spark needed to fuel a massive fire, but remember that the flash itself is not enough to keep the flames burning.The Ace of Wands may appear when you have an opportunity to grow on a personal or spiritual level. You may be interested in taking a class or investing in a course so you can follow your creative spirit. For example, you might enrol in a photography class, a Tarot course, or a self-improvement program. Trust that this experience will open you up to even more possibilities.')

with col3:
    st.header("Magician")
    st.image("https://upload.wikimedia.org/wikipedia/en/d/de/RWS_Tarot_01_Magician.jpg", width=400)
    st.text_area('Upright Magician: As a master manifestor, the Magician brings you the tools, resources and energy you need to make your dreams come true. Seriously, everything you need right now is at your fingertips. You have the spiritual (fire), physical (earth), mental (air) and emotional (water) resources to manifest your desires. And when you combine them with the energy of the spiritual and earthly realms, you will become a manifestation powerhouse! The key is to bring these tools together synergistically so that the impact of what you create is greater than the separate parts. This is alchemy at its best!Now is the perfect time to move forward on an idea that you recently conceived. The seed of potential has sprouted, and you are being called to take action and bring your intention to fruition. The skills, knowledge and capabilities you have gathered along your life path have led you to where you are now, and whether or not you know it, you are ready to turn your ideas into reality.In your quest to manifest your goals, you must establish a clear vision of what you will create (and why) before you act. It is not enough to be motivated by ego (money, status, or fame) – you need to have a soul connection to your goals and intentions. You are a powerful, creative being, and this is your opportunity to bring your Higher Self in alignment with your day-to-day actions to create the future you want most.When you are clear about your ‘what’ and your ‘why’, the Magician calls on you to take inspired action. You will need focused attention and intense concentration to bring your goals to fruition. Focus on the ONE thing that will move you towards your goal. Commitment to the task is essential, so drop any distractions that may draw your focus away from what you want to achieve. Be methodical in your planning to make sure that you stay on track and carry out your tasks.')

    # c1 = st.image('https://upload.wikimedia.org/wikipedia/en/1/11/Wands01.jpg')
    # c2 = st.image('https://upload.wikimedia.org/wikipedia/en/d/de/RWS_Tarot_01_Magician.jpg')
    # c3 = st.image('https://upload.wikimedia.org/wikipedia/en/7/7f/RWS_Tarot_18_Moon.jpg')

    #
#####st.image(['https://upload.wikimedia.org/wikipedia/en/1/11/Wands01.jpg', 'https://upload.wikimedia.org/wikipedia/en/7/7f/RWS_Tarot_18_Moon.jpg', 'https://upload.wikimedia.org/wikipedia/en/d/de/RWS_Tarot_01_Magician.jpg'], width=250)
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
