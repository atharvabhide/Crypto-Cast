import utils.basic_info as basic_info
import utils.home as home
import utils.prediction as prediction
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Crypto Cast",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="auto",)

st.markdown("<center><h1 Style='overflow: visible; padding-bottom: 50px; padding-top: 0px;'>Crypto Cast</h1></center>", unsafe_allow_html=True)

selected = option_menu(
        menu_title=None,
        options=["Home", "Basic Info", "Prediction"],
        icons=['house', 'info', 'book'],
        default_index=0,
        orientation = "horizontal",
        styles={
        "container": {"padding": "5!important", "background-color": "gray"},
        "icon": {"color": "#2ECC71", "font-size": "25px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "light-grey"},
        "nav-link-selected": {"background-color": "#2ECC71"},
        }
)

if selected == "Home":
    home.get_home()
elif selected == "Basic Info":
    basic_info.get_basic_info()
elif selected == "Prediction":
    prediction.get_prediction()

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """

st.markdown(hide_menu_style, unsafe_allow_html=True)