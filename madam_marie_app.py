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

arcana_keywords = [['    The Fool Upright: Beginnings, innocence, spontaneity, a free spirit',
  ' The Fool Reversed: Holding back, recklessness, risk-taking   '],
 ['    The Magician Upright: Manifestation, resourcefulness, power, inspired action',
  ' The Magician Reversed: Manipulation, poor planning, untapped talents   '],
 ['    The High Priestess Upright: Intuition, sacred knowledge, divine feminine, the subconscious mind',
  ' The High Priestess Reversed: Secrets, disconnected from intuition, withdrawal and silence   '],
 ['    The Empress Upright: Femininity, beauty, nature, nurturing, abundance',
  ' The Empress Reversed: Creative block, dependence on others   '],
 ['    The Emperor Upright: Authority, establishment, structure, a father figure',
  ' The Emperor Reversed: Domination, excessive control, lack of discipline, inflexibility   '],
 ['    The Hierophant Upright: Spiritual wisdom, religious beliefs, conformity, tradition,institutions',
  ' The Hierophant Reversed: Personal beliefs, freedom, challenging the status quo   '],
 ['    The Lovers Upright: Love, harmony, relationships, values alignment, choices',
  ' The Lovers Reversed: Self-love, disharmony, imbalance, misalignment of values   '],
 ['    The Chariot Upright: Control, willpower, success, action, determination',
  ' The Chariot Reversed: Self-discipline, opposition, lack of directionThe Chariot   '],
 ['    Strength Upright: Strength, courage, persuasion, influence, compassion',
  ' Strength Reversed: Inner strength, self-doubt, low energy, raw emotion   '],
 ['    The Hermit Upright: Soul-searching, introspection, being alone, inner guidance',
  ' The Hermit Reversed: Isolation, loneliness, withdrawal   '],
 ['    Wheel of Fortune Upright: Good luck, karma, life cycles, destiny, a turning point',
  ' Wheel of Fortune Reversed: Bad luck, resistance to change, breaking cycles   '],
 ['    Justice Upright: Justice, fairness, truth, cause and effect, law',
  ' Justice Reversed: Unfairness, lack of accountability, dishonestyJustice   '],
 ['    The Hanged Man Upright: Pause, surrender, letting go, new perspectives',
  ' The Hanged Man Reversed: Delays, resistance, stalling, indecision   '],
 ['    Death Upright: Endings, change, transformation, transition',
  ' Death Reversed: Resistance to change, personal transformation, inner purging   '],
 ['    Temperance Upright: Balance, moderation, patience, purpose',
  ' Temperance Reversed: Imbalance, excess, self-healing, re-alignment   '],
 ['    The Devil Upright: Shadow self, attachment, addiction, restriction, sexuality',
  ' The Devil Reversed: Releasing limiting beliefs, exploring dark thoughts, detachment   '],
 ['    The Tower Upright: Sudden change, upheaval, chaos, revelation, awakening',
  ' The Tower Reversed: Personal transformation, fear of change, averting disaster   '],
 ['    The Star Upright: Hope, faith, purpose, renewal, spirituality',
  ' The Star Reversed: Lack of faith, despair, self-trust, disconnection   '],
 ['    The Moon Upright: Illusion, fear, anxiety, subconscious, intuition',
  ' The Moon Reversed: Release of fear, repressed emotion, inner confusion   '],
 ['    The Sun Upright: Positivity, fun, warmth, success, vitality',
  ' The Sun Reversed: Inner child, feeling down, overly optimistic   '],
 ['    Judgement Upright: Judgement, rebirth, inner calling, absolution',
  ' Judgement Reversed: Self-doubt, inner critic, ignoring the call   '],
 ['    The World Upright: Completion, integration, accomplishment, travel',
  ' The World Reversed: Seeking personal closure, short-cuts, delays   ']]

arcana_dict = dict(zip(arcana, arcana_image_links))
# minor_arcana_dict = dict(zip(minor_arcana, minor_arcana_image_links))

with sidebar:
    st.title('Select cards')

    # list(major_arcana + minor_arcana))
    # ["Fool","The Magician","High Priestess","The Empress","The Emperor","Hierophant","Lovers","Chariot","Strength","Hermit","Wheel of Fortune","Justice","Hanged Man","Death","Temperance","Devil","Tower","Star","Moon","Sun","Judgement","World"])
    CARD1 = st.selectbox('CARD 1', list(arcana))
    CARD2 = st.selectbox('CARD 2:', list(arcana))
    CARD3 = st.selectbox('CARD 3:', list(arcana))


with body:
    st.subheader("The Three Tarot Spread")
    st.text('- Three card tarot spreads can be used to represent several different meanings, including:')
    # st.subheader('')
    st.caption('- [Past, Present, Future]')
    st.caption('- [Mind, Body, Soul]')
    st.caption('- [Background, Problem, Advice]')


col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.header("{}".format(CARD1))
    st.image(arcana_dict["{}".format(CARD1)])
    st.markdown("{}".format())

    with st.expander("Upright Meaning"):
         st.write("""
            PLACEHOLDER
         """)
    with st.expander("Reversed Meaning"):
         st.write("""
            PLACEHOLDER
         """)


with col2:
    st.header("{}".format(CARD2))
    st.image(arcana_dict["{}".format(CARD2)])
    # st.image("https://upload.wikimedia.org/wikipedia/commons/1/11/Wands01.jpg")
    st.write('PLACEHOLDER')

    with st.expander("Upright Meaning"):
         st.write("""
            PLACEHOLDER
         """)
    with st.expander("Reversed Meaning"):
         st.write("""
            PLACEHOLDER
         """)

with col3:
    st.header("{}".format(CARD3))
    st.image(arcana_dict["{}".format(CARD3)])
    # st.image("https://upload.wikimedia.org/wikipedia/commons/d/de/RWS_Tarot_01_Magician.jpg")
    # st.write('Upright Magician: As a master manifestor, the Magician brings you the tools, resources and energy you need to make your dreams come true. Seriously, everything you need right now is at your fingertips. You have the spiritual (fire), physical (earth), mental (air) and emotional (water) resources to manifest your desires. And when you combine them with the energy of the spiritual and earthly realms, you will become a manifestation powerhouse! The key is to bring these tools together synergistically so that the impact of what you create is greater than the separate parts. This is alchemy at its best!Now is the perfect time to move forward on an idea that you recently conceived. The seed of potential has sprouted, and you are being called to take action and bring your intention to fruition. The skills, knowledge and capabilities you have gathered along your life path have led you to where you are now, and whether or not you know it, you are ready to turn your ideas into reality.In your quest to manifest your goals, you must establish a clear vision of what you will create (and why) before you act. It is not enough to be motivated by ego (money, status, or fame) – you need to have a soul connection to your goals and intentions. You are a powerful, creative being, and this is your opportunity to bring your Higher Self in alignment with your day-to-day actions to create the future you want most.When you are clear about your ‘what’ and your ‘why’, the Magician calls on you to take inspired action. You will need focused attention and intense concentration to bring your goals to fruition. Focus on the ONE thing that will move you towards your goal. Commitment to the task is essential, so drop any distractions that may draw your focus away from what you want to achieve. Be methodical in your planning to make sure that you stay on track and carry out your tasks.')

    with st.expander("Upright Meaning"):
         st.write("""
             Upright Magician: As a master manifestor, the Magician brings you the tools, resources and energy you need to make your dreams come true. Seriously, everything you need right now is at your fingertips. You have the spiritual (fire), physical (earth), mental (air) and emotional (water) resources to manifest your desires. And when you combine them with the energy of the spiritual and earthly realms, you will become a manifestation powerhouse! The key is to bring these tools together synergistically so that the impact of what you create is greater than the separate parts. This is alchemy at its best!Now is the perfect time to move forward on an idea that you recently conceived. The seed of potential has sprouted, and you are being called to take action and bring your intention to fruition. The skills, knowledge and capabilities you have gathered along your life path have led you to where you are now, and whether or not you know it, you are ready to turn your ideas into reality.In your quest to manifest your goals, you must establish a clear vision of what you will create (and why) before you act. It is not enough to be motivated by ego (money, status, or fame) – you need to have a soul connection to your goals and intentions. You are a powerful, creative being, and this is your opportunity to bring your Higher Self in alignment with your day-to-day actions to create the future you want most.When you are clear about your ‘what’ and your ‘why’, the Magician calls on you to take inspired action. You will need focused attention and intense concentration to bring your goals to fruition. Focus on the ONE thing that will move you towards your goal. Commitment to the task is essential, so drop any distractions that may draw your focus away from what you want to achieve. Be methodical in your planning to make sure that you stay on track and carry out your tasks.
         """)
    with st.expander("Reversed Meaning"):
         st.write("""
            PLACEHOLDER
         """)
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
