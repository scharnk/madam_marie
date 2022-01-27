import streamlit as st
# from streamlit_option_menu import option_menu
import pandas as pd
import os
from dotenv import load_dotenv
from alpha_vantage.timeseries import TimeSeries
import pandas_bokeh
from bokeh.plotting import figure, show
from PIL import Image


################################ GET DATA ######################################

project_folder = os.path.expanduser('~/code/GitHub/madam_marie')
load_dotenv(os.path.join(project_folder,'.env'))
key = os.getenv("API_KEY")
ts = TimeSeries(key, output_format='pandas')

############################### STREAMLIT ######################################
# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")

header = st.container()
body = st.container()
# features = st.container()
sidebar = st.sidebar.container()

with header:
    st.title('Fortune Teller Tarot Reader')
    img = Image.open("banner_image_cropped.jpg")
    st.image(img)
    st.text('- Card descriptions scraped from BiddyTarot.com')
    st.text('- App deployed using Heroku')
    st.text('- Tarot card images taken from Wikimedia')

# major_
arcana = [
             "Fool",
             "The Magician",
             "High Priestess",
             "The Empress",
             "The Emperor",
             "Hierophant",
             "Lovers",
             "Chariot",
             "Strength",
             "Hermit",
             "Wheel of Fortune",
             "Justice",
             "Hanged Man",
             "Death",
             "Temperance",
             "Devil",
             "Tower",
             "Star",
             "Moon",
             "Sun",
             "Judgement",
             "World",
#              ]
# minor_arcana = [
                    'Ace of Cups',
                    'Two of Cups',
                    'Three of Cups',
                    'Four of Cups',
                    'Five of Cups',
                    'Six of Cups',
                    'Seven of Cups',
                    'Eight of Cups',
                    'Nine of Cups',
                    'Ten of Cups',
                    'Page of Cups',
                    'Knight of Cups',
                    'Queen of Cups',
                    'King of Cups',
                    'Ace of Swords',
                    'Two of Swords',
                    'Three of Swords',
                    'Four of Swords',
                    'Five of Swords',
                    'Six of Swords',
                    'Seven of Swords',
                    'Eight of Swords',
                    'Nine of Swords',
                    'Ten of Swords',
                    'Page of Swords',
                    'Knight of Swords',
                    'Queen of Swords',
                    'King of Swords',
                    'Ace of Pentacles',
                    'Two of Pentacles',
                    'Three of Pentacles',
                    'Four of Pentacles',
                    'Five of Pentacles',
                    'Six of Pentacles',
                    'Seven of Pentacles',
                    'Eight of Pentacles',
                    'Nine of Pentacles',
                    'Ten of Pentacles',
                    'Page of Pentacles',
                    'Knight of Pentacles',
                    'Queen of Pentacles',
                    'King of Pentacles',
                    'Ace of Wands',
                    'Two of Wands',
                    'Three of Wands',
                    'Four of Wands',
                    'Five of Wands',
                    'Six of Wands',
                    'Seven of Wands',
                    'Eight of Wands',
                    'Nine of Wands',
                    'Ten of Wands',
                    'Page of Wands',
                    'Knight of Wands',
                    'Queen of Wands',
                    'King of Wands'
                    ]

arcana_image_links = [
'https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/RWS_Tarot_00_Fool.jpg/340px-RWS_Tarot_00_Fool.jpg',
'https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/RWS_Tarot_01_Magician.jpg/340px-RWS_Tarot_01_Magician.jpg',
'https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/RWS_Tarot_02_High_Priestess.jpg/440px-RWS_Tarot_02_High_Priestess.jpg',
'https://upload.wikimedia.org/wikipedia/commons/d/d2/RWS_Tarot_03_Empress.jpg',
'https://upload.wikimedia.org/wikipedia/commons/c/c3/RWS_Tarot_04_Emperor.jpg',
'https://upload.wikimedia.org/wikipedia/commons/8/8d/RWS_Tarot_05_Hierophant.jpg',
'https://upload.wikimedia.org/wikipedia/commons/3/3a/TheLovers.jpg',
'https://upload.wikimedia.org/wikipedia/commons/9/9b/RWS_Tarot_07_Chariot.jpg',
'https://upload.wikimedia.org/wikipedia/commons/f/f5/RWS_Tarot_08_Strength.jpg',
'https://upload.wikimedia.org/wikipedia/commons/4/4d/RWS_Tarot_09_Hermit.jpg',
'https://upload.wikimedia.org/wikipedia/commons/3/3c/RWS_Tarot_10_Wheel_of_Fortune.jpg',
'https://upload.wikimedia.org/wikipedia/commons/e/e0/RWS_Tarot_11_Justice.jpg',
'https://upload.wikimedia.org/wikipedia/commons/2/2b/RWS_Tarot_12_Hanged_Man.jpg',
'https://upload.wikimedia.org/wikipedia/commons/d/d7/RWS_Tarot_13_Death.jpg',
'https://upload.wikimedia.org/wikipedia/commons/f/f8/RWS_Tarot_14_Temperance.jpg',
'https://upload.wikimedia.org/wikipedia/commons/5/55/RWS_Tarot_15_Devil.jpg',
'https://upload.wikimedia.org/wikipedia/commons/5/53/RWS_Tarot_16_Tower.jpg',
'https://upload.wikimedia.org/wikipedia/commons/d/db/RWS_Tarot_17_Star.jpg',
'https://upload.wikimedia.org/wikipedia/commons/7/7f/RWS_Tarot_18_Moon.jpg',
'https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/RWS_Tarot_19_Sun.jpg/370px-RWS_Tarot_19_Sun.jpg',
'https://upload.wikimedia.org/wikipedia/commons/d/dd/RWS_Tarot_20_Judgement.jpg',
'https://upload.wikimedia.org/wikipedia/commons/f/ff/RWS_Tarot_21_World.jpg',
# minor_arcana_image_links = [
# cups, swords, pentacles, wands
# cups
'https://upload.wikimedia.org/wikipedia/commons/3/36/Cups01.jpg',
'https://upload.wikimedia.org/wikipedia/commons/f/f8/Cups02.jpg',
'https://upload.wikimedia.org/wikipedia/commons/7/7a/Cups03.jpg',
'https://upload.wikimedia.org/wikipedia/commons/3/35/Cups04.jpg',
'https://upload.wikimedia.org/wikipedia/commons/d/d7/Cups05.jpg',
'https://upload.wikimedia.org/wikipedia/commons/1/17/Cups06.jpg',
'https://upload.wikimedia.org/wikipedia/commons/a/ae/Cups07.jpg',
'https://upload.wikimedia.org/wikipedia/commons/6/60/Cups08.jpg',
'https://upload.wikimedia.org/wikipedia/commons/2/24/Cups09.jpg',
'https://upload.wikimedia.org/wikipedia/commons/8/84/Cups10.jpg',
'https://upload.wikimedia.org/wikipedia/commons/a/ad/Cups11.jpg',
'https://upload.wikimedia.org/wikipedia/commons/f/fa/Cups12.jpg',
'https://upload.wikimedia.org/wikipedia/commons/6/62/Cups13.jpg',
'https://upload.wikimedia.org/wikipedia/commons/0/04/Cups14.jpg',
# swords
'https://upload.wikimedia.org/wikipedia/commons/1/1a/Swords01.jpg',
'https://upload.wikimedia.org/wikipedia/commons/9/9e/Swords02.jpg',
'https://upload.wikimedia.org/wikipedia/commons/0/02/Swords03.jpg',
'https://upload.wikimedia.org/wikipedia/commons/b/bf/Swords04.jpg',
'https://upload.wikimedia.org/wikipedia/commons/2/23/Swords05.jpg',
'https://upload.wikimedia.org/wikipedia/commons/2/29/Swords06.jpg',
'https://upload.wikimedia.org/wikipedia/commons/3/34/Swords07.jpg',
'https://upload.wikimedia.org/wikipedia/commons/a/a7/Swords08.jpg',
'https://upload.wikimedia.org/wikipedia/commons/2/2f/Swords09.jpg',
'https://upload.wikimedia.org/wikipedia/commons/d/d4/Swords10.jpg',
'https://upload.wikimedia.org/wikipedia/commons/4/4c/Swords11.jpg',
'https://upload.wikimedia.org/wikipedia/commons/b/b0/Swords12.jpg',
'https://upload.wikimedia.org/wikipedia/commons/d/d4/Swords13.jpg',
'https://upload.wikimedia.org/wikipedia/commons/3/33/Swords14.jpg',
# pentacles
'https://upload.wikimedia.org/wikipedia/commons/f/fd/Pents01.jpg',
'https://upload.wikimedia.org/wikipedia/commons/9/9f/Pents02.jpg',
'https://upload.wikimedia.org/wikipedia/commons/4/42/Pents03.jpg',
'https://upload.wikimedia.org/wikipedia/commons/3/35/Pents04.jpg',
'https://upload.wikimedia.org/wikipedia/commons/9/96/Pents05.jpg',
'https://upload.wikimedia.org/wikipedia/commons/a/a6/Pents06.jpg',
'https://upload.wikimedia.org/wikipedia/commons/6/6a/Pents07.jpg',
'https://upload.wikimedia.org/wikipedia/commons/4/49/Pents08.jpg',
'https://upload.wikimedia.org/wikipedia/commons/f/f0/Pents09.jpg',
'https://upload.wikimedia.org/wikipedia/commons/4/42/Pents10.jpg',
'https://upload.wikimedia.org/wikipedia/commons/e/ec/Pents11.jpg',
'https://upload.wikimedia.org/wikipedia/commons/d/d5/Pents12.jpg',
'https://upload.wikimedia.org/wikipedia/commons/8/88/Pents13.jpg',
'https://upload.wikimedia.org/wikipedia/commons/1/1c/Pents14.jpg',
# wands
'https://upload.wikimedia.org/wikipedia/commons/1/11/Wands01.jpg',
'https://upload.wikimedia.org/wikipedia/commons/0/0f/Wands02.jpg',
'https://upload.wikimedia.org/wikipedia/commons/f/ff/Wands03.jpg',
'https://upload.wikimedia.org/wikipedia/commons/a/a4/Wands04.jpg',
'https://upload.wikimedia.org/wikipedia/commons/9/9d/Wands05.jpg',
'https://upload.wikimedia.org/wikipedia/commons/3/3b/Wands06.jpg',
'https://upload.wikimedia.org/wikipedia/commons/e/e4/Wands07.jpg',
'https://upload.wikimedia.org/wikipedia/commons/6/6b/Wands08.jpg',
'https://upload.wikimedia.org/wikipedia/commons/4/4d/Tarot_Nine_of_Wands.jpg',
'https://upload.wikimedia.org/wikipedia/commons/0/0b/Wands10.jpg',
'https://upload.wikimedia.org/wikipedia/commons/6/6a/Wands11.jpg',
'https://upload.wikimedia.org/wikipedia/commons/1/16/Wands12.jpg',
'https://upload.wikimedia.org/wikipedia/commons/0/0d/Wands13.jpg',
'https://upload.wikimedia.org/wikipedia/commons/c/ce/Wands14.jpg'
]

arcana_dict = dict(zip(arcana, arcana_image_links))
# minor_arcana_dict = dict(zip(minor_arcana, minor_arcana_image_links))

with sidebar:
    st.title('Select cards')
    # ARCANE = st.selectbox('Arcana:', ['Major','Minor'])
    CARD1 = st.selectbox('CARD 1:', list(arcana))
    # list(major_arcana + minor_arcana))
    # ["Fool","The Magician","High Priestess","The Empress","The Emperor","Hierophant","Lovers","Chariot","Strength","Hermit","Wheel of Fortune","Justice","Hanged Man","Death","Temperance","Devil","Tower","Star","Moon","Sun","Judgement","World"])
    CARD2 = st.selectbox('CARD 2:', list(arcana))
    # CARD2 = st.selectbox('CARD 1:', card_list)
    CARD3 = st.selectbox('CARD 3:', list(arcana))

# with test:
#     st.title('Select Spread')

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


with body:
    st.header("Three Tarot Spread")
    st.text('Three card spreads can represent several different meanings, including:')
    st.caption('[Past, Present, Future]')
    st.subheader('[Mind, Body, Soul]')
    st.subheader('[Background, Problem, Advice]')


#     p = figure(title="The Highs and Lows of: '{}'".format(ticker), x_axis_type='datetime', x_axis_label='Date', y_axis_label='Value (USD)')
#     p.line(date, y, legend_label="Max / day (USD)", line_width=2)
#     p.line(date, x, color= "red", legend_label="Min / day (USD)", line_width=2)
#     st.bokeh_chart(p, use_container_width=True)


col1, col2, col3 = st.columns([1, 1, 1])
# col1, col2, col3 = st.beta_columns((1,1,0.5))) also works

with col1:
    st.header("{}".format(CARD1))
    st.image(arcana_dict["{}".format(CARD1)])
    # st.image("https://upload.wikimedia.org/wikipedia/commons/7/7f/RWS_Tarot_18_Moon.jpg")
    st.markdown("The Moon represents your fears and illusions and often comes out when you are projecting fear into your present and your future, based on your past experiences. You may have a painful memory that caused emotional distress, and rather than dealing with the emotions you pushed them down deep into your subconscious. Now, these emotions are making a reappearance, and you may find yourself under their influence on a conscious or subconscious level. For example, if you had a car accident when you were young but didn’t deal with the emotions, you may get sad or anxious every time you get into the backseat of a car. To remedy this, connect with your subconscious mind and release any fears or anxieties holding you back. Hypnosis, therapy and shamanic healing can support this process. The Moon can indicate a time of uncertainty and illusion, when nothing is what it seems. Be careful of making fast decisions when The Moon appears because you may later realize you only had half the information you needed. You need to listen to and trust your intuition so you can see beyond what is in front of you. Feel into situations rather than thinking what they mean. Let go of your conscious mental blocks or negative self-talk and allow your intuition to guide you. Your dreams, intuitions and inner guidance lead you forward toward higher levels of understanding if you listen and use your judgement to help interpret the messages of the subconscious. When The Moon card appears in your Tarot reading, pay close attention to the lunar cycles and attune to its divine power using ritual, visualization or Tarot readings. Connect with the divine feminine and uncover deep intuitive insights and visions of what lies beyond everyday life. On the New Moon, set your intentions and plant the seeds of opportunity so they can grow. And on the Full Moon, honor your achievements and look at what you need to release so that new aspects of yourself can shine.")

with col2:
    st.header("{}".format(CARD2))
    st.image(arcana_dict["{}".format(CARD2)])
    # st.image("https://upload.wikimedia.org/wikipedia/commons/1/11/Wands01.jpg")
    st.write('Upright Ace of Wands: As an Ace, this Wands card brings you pure potential – this time in the spiritual, energetic realm. Ideas are flowing to you, motivating and inspiring you to pursue a new path. You are open to receiving new opportunities that align with your Higher Self. A whole world of possibility is available to you.The Ace of Wands encourages you to follow your heart and live your passion. If you feel a strong pull towards a new project or path, but are questioning whether it will work, then this card gives you a gentle nudge to pursue your passion. You can always start out small, treating the project or idea as an experiment or trial. Then, if it feels good, keep doing it; and if it doesn’t, make adjustments and try again. Let your energy, dedication and motivation be your guides.If you have been looking for a sign about whether this is the right project, then the Ace of Wands is a clear YES! The sprouting wand and the fertile landscape in the background are all positive indications that this idea has the potential to turn into something fulfilling and energising. Use your creative energy and passion to take the first steps. Even if you prefer to plan out everything before you begin down a particular path, the Ace of Wands wants you to listen to your instincts and follow your gut. If it seems like a good idea, it probably is. So, start with a few fundamentals to get things rolling, and then continue to grow and develop your ideas through more complex activities later on. The important thing is that you act now rather than spending more time planning or researching.Keep in mind, however, that the Aces represent potential but not guaranteed results. The Ace of Wands (or any Ace) is a seed that has yet to grow into something more substantial or sustainable. The opportunity on offer shows great promise, but it will be up to you to maximise it for the long term. See this card as the spark needed to fuel a massive fire, but remember that the flash itself is not enough to keep the flames burning.The Ace of Wands may appear when you have an opportunity to grow on a personal or spiritual level. You may be interested in taking a class or investing in a course so you can follow your creative spirit. For example, you might enrol in a photography class, a Tarot course, or a self-improvement program. Trust that this experience will open you up to even more possibilities.')

with col3:
    st.header("{}".format(CARD3))
    st.image(arcana_dict["{}".format(CARD3)])
    # st.image("https://upload.wikimedia.org/wikipedia/commons/d/de/RWS_Tarot_01_Magician.jpg")
    st.write('Upright Magician: As a master manifestor, the Magician brings you the tools, resources and energy you need to make your dreams come true. Seriously, everything you need right now is at your fingertips. You have the spiritual (fire), physical (earth), mental (air) and emotional (water) resources to manifest your desires. And when you combine them with the energy of the spiritual and earthly realms, you will become a manifestation powerhouse! The key is to bring these tools together synergistically so that the impact of what you create is greater than the separate parts. This is alchemy at its best!Now is the perfect time to move forward on an idea that you recently conceived. The seed of potential has sprouted, and you are being called to take action and bring your intention to fruition. The skills, knowledge and capabilities you have gathered along your life path have led you to where you are now, and whether or not you know it, you are ready to turn your ideas into reality.In your quest to manifest your goals, you must establish a clear vision of what you will create (and why) before you act. It is not enough to be motivated by ego (money, status, or fame) – you need to have a soul connection to your goals and intentions. You are a powerful, creative being, and this is your opportunity to bring your Higher Self in alignment with your day-to-day actions to create the future you want most.When you are clear about your ‘what’ and your ‘why’, the Magician calls on you to take inspired action. You will need focused attention and intense concentration to bring your goals to fruition. Focus on the ONE thing that will move you towards your goal. Commitment to the task is essential, so drop any distractions that may draw your focus away from what you want to achieve. Be methodical in your planning to make sure that you stay on track and carry out your tasks.')


    # st.image(['https://upload.wikimedia.org/wikipedia/en/1/11/Wands01.jpg', 'https://upload.wikimedia.org/wikipedia/en/7/7f/RWS_Tarot_18_Moon.jpg', 'https://upload.wikimedia.org/wikipedia/en/d/de/RWS_Tarot_01_Magician.jpg'], width=250)
    # st.image('https://upload.wikimedia.org/wikipedia/en/d/de/RWS_Tarot_01_Magician.jpg', width=200)
    # st.image('https://upload.wikimedia.org/wikipedia/en/7/7f/RWS_Tarot_18_Moon.jpg', width=200)
    # st.markdown("![Alt Text](https://upload.wikimedia.org/wikipedia/en/d/de/RWS_Tarot_01_Magician.jpg)")


# https://en.m.wikipedia.org/wiki/The_Fool_(Tarot_card)#/media/File%3ARWS_Tarot_00_Fool.jpg
# https://en.m.wikipedia.org/wiki/The_Magician_(Tarot_card)#/media/File%3ARWS_Tarot_01_Magician.jpg
# https://en.m.wikipedia.org/wiki/Ace_of_Wands_(Tarot_card)#/media/File%3AWands01.jpg
# https://www.sacred-texts.com/tarot/pkt/img/ar01.jpg
# https://www.sacred-texts.com/tarot/pkt/img/ar02.jpg

################################################################################
# NEXT STEPS:

# get list of links for images
# make dictionary of key value pairs
#   KEY: name of card
#   VALUES: upright and reversed keywords,
#       upright and reversed meanings,
#       link to images


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
