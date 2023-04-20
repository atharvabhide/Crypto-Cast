import streamlit as st
import requests
from streamlit_lottie import st_lottie_spinner
import bitcoin.bit as bit
import dogecoin.doge as doge
import ethereum.eth as eth
import litecoin.ltc as ltc
import shibainu.shib as shib


def get_prediction():

    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_url = "https://assets1.lottiefiles.com/private_files/lf30_h4qnjuax.json"
    lottie_json = load_lottieurl(lottie_url)

    with st.form(key='my_form'):
        crypto = st.selectbox('Select Cryptocurrency',
                              ['Bitcoin (BTC)', 'Ethereum (ETH)',
                               'Litecoin (LTC)','Dogecoin (DOGE)', 'Shiba Inu (SHIB)'])
        submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        if crypto == "Bitcoin (BTC)":
            with st_lottie_spinner(lottie_json):
                bit.get_bit()
        if crypto == "Ethereum (ETH)":
            with st_lottie_spinner(lottie_json):
                eth.get_eth()
        if crypto == "Litecoin (LTC)":
            with st_lottie_spinner(lottie_json):
                ltc.get_ltc()
        if crypto == "Dogecoin (DOGE)":
            with st_lottie_spinner(lottie_json):
                doge.get_doge()
        if crypto == "Shiba Inu (SHIB)":
            with st_lottie_spinner(lottie_json):
                shib.get_shib()

