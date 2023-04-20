import streamlit as st
import bitcoin.bit_info as bit_info
import ethereum.eth_info as eth_info
import litecoin.lite_info as lite_info
import dogecoin.doge_info as doge_info
import shibainu.shib_info as shib_info


def get_basic_info():

    with st.form(key='my_form'):
        crypto = st.selectbox('Select Cryptocurrency',
                          ['Bitcoin (BTC)', 'Ethereum (ETH)', 'Litecoin (LTC)', 'Dogecoin (DOGE)', 'Shiba Inu (SHIB)'])
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        if crypto == "Bitcoin (BTC)":
            bit_info.get_bit_info()
        if crypto == "Ethereum (ETH)":
            eth_info.get_eth_info()
        if crypto == "Litecoin (LTC)":
            lite_info.get_lite_info()
        if crypto == "Dogecoin (DOGE)":
            doge_info.get_doge_info()
        if crypto == "Shiba Inu (SHIB)":
            shib_info.get_shib_info()
