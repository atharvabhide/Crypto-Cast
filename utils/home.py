import streamlit as st
from requests import Session
import json
from dotenv import load_dotenv
import os
import utils.cryptographs as cryptographs
import utils.graph_color_decision as graph_color_decision

load_dotenv("./.env")
API_KEY = os.environ.get("API_KEY")

def get_home():
        with open('styles/homeview') as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
        headers = {
                'Accepts': 'application/json',
                'X-CMC_PRO_API_KEY': API_KEY,
        }
        def get_btc():
                parameters = {'slug': 'bitcoin', 'convert': 'USD'}
                session = Session()
                session.headers.update(headers)
                response = session.get(url, params=parameters)
                hour24 = json.loads(response.text)['data']['1']['quote']['USD']['percent_change_24h']
                price = json.loads(response.text)['data']['1']['quote']['USD']['price']
                marketcap = json.loads(response.text)['data']['1']['quote']['USD']['market_cap']
                marketcap_ch = json.loads(response.text)['data']['1']['quote']['USD']['market_cap_dominance']
                volume = json.loads(response.text)['data']['1']['quote']['USD']['volume_24h']
                volume_ch = json.loads(response.text)['data']['1']['quote']['USD']['volume_change_24h']
                week_per_ch = json.loads(response.text)['data']['1']['quote']['USD']['percent_change_7d']
                graph_color_decision.bit_color = week_per_ch
                cl1,col1, col2, col3,col4,g1 = st.columns([0.5,1.5,2,2,2,1.5])

                with cl1:
                        st.write(1)
                with col1:
                        st.image("images/bitcoin.png")
                with col2:
                        st.metric(label='Bitcoin BTC ', value=("$"+str(round(price, 2))), delta=str(round(hour24, 2)) + "%")
                with col3:
                        st.metric(label="Volume (24h)", value=("$"+str(round(volume, 2))), delta=str(round(volume_ch, 2)) + "%")
                with col4:
                        st.metric(label="Market Cap", value=("$"+str(round(marketcap, 2))), delta=str(round(marketcap_ch, 2)) + "%")
                with g1:
                        st.write("7 days graph")
                        cryptographs.get_btc_graph()

        def get_eth():
                parameters = {'slug': 'ethereum', 'convert': 'USD'}
                session = Session()
                session.headers.update(headers)
                response = session.get(url, params=parameters)
                hour24 = json.loads(response.text)['data']['1027']['quote']['USD']['percent_change_24h']
                price = json.loads(response.text)['data']['1027']['quote']['USD']['price']
                marketcap = json.loads(response.text)['data']['1027']['quote']['USD']['market_cap']
                marketcap_ch = json.loads(response.text)['data']['1027']['quote']['USD']['market_cap_dominance']
                volume = json.loads(response.text)['data']['1027']['quote']['USD']['volume_24h']
                volume_ch = json.loads(response.text)['data']['1027']['quote']['USD']['volume_change_24h']
                week_per_ch = json.loads(response.text)['data']['1027']['quote']['USD']['percent_change_7d']
                graph_color_decision.eth_color = week_per_ch
                cl2,col5, col6, col7,col8,g2 = st.columns([0.5,1.5,2,2,2,1.5])

                with cl2:
                        st.write(2)
                with col5:
                        st.image("images/ethereum.png")
                with col6:
                        st.metric(label="Ethereum (ETH)", value=("$"+str(round(price, 2))), delta=str(round(hour24, 2)) + "%")
                with col7:
                        st.metric(label="Volume (24h)", value=("$"+str(round(volume, 2))), delta=str(round(volume_ch, 2)) + "%")
                with col8:
                        st.metric(label="Market Cap", value=("$"+str(round(marketcap, 2))),delta=str(round(marketcap_ch, 2)) + "%")
                with g2:
                        st.write("7 days graph")
                        cryptographs.get_eth_graph()

        def get_ltc():
                parameters = {'slug': 'litecoin', 'convert': 'USD'}
                session = Session()
                session.headers.update(headers)
                response = session.get(url, params=parameters)
                hour24 = json.loads(response.text)['data']['2']['quote']['USD']['percent_change_24h']
                price = json.loads(response.text)['data']['2']['quote']['USD']['price']
                marketcap = json.loads(response.text)['data']['2']['quote']['USD']['market_cap']
                marketcap_ch = json.loads(response.text)['data']['2']['quote']['USD']['market_cap_dominance']
                volume = json.loads(response.text)['data']['2']['quote']['USD']['volume_24h']
                volume_ch = json.loads(response.text)['data']['2']['quote']['USD']['volume_change_24h']
                week_per_ch = json.loads(response.text)['data']['2']['quote']['USD']['percent_change_7d']
                graph_color_decision.ltc_color = week_per_ch
                cl6,col21, col22, col23,col24,g6 = st.columns([0.5,1.5,2,2,2,1.5])

                with cl6:
                        st.write(3)
                with col21:
                        st.image("images/litecoin.png")
                with col22:
                        st.metric(label="Litecoin (LTC)", value=("$"+str(round(price, 2))),delta=str(round(hour24, 2)) + "%")
                with col23:
                        st.metric(label="Volume (24h)", value=("$"+str(round(volume, 2))), delta=str(round(volume_ch, 2)) + "%")
                with col24:
                        st.metric(label="Market Cap", value=("$"+str(round(marketcap, 2))),delta=str(round(marketcap_ch, 2)) + "%")
                with g6:
                        st.write("7 days graph")
                        cryptographs.get_ltc_graph()

        def get_doge():
                parameters = {'slug': 'dogecoin', 'convert': 'USD'}
                session = Session()
                session.headers.update(headers)
                response = session.get(url, params=parameters)
                hour24 = json.loads(response.text)['data']['74']['quote']['USD']['percent_change_24h']
                price = json.loads(response.text)['data']['74']['quote']['USD']['price']
                marketcap = json.loads(response.text)['data']['74']['quote']['USD']['market_cap']
                marketcap_ch = json.loads(response.text)['data']['74']['quote']['USD']['market_cap_dominance']
                volume = json.loads(response.text)['data']['74']['quote']['USD']['volume_24h']
                volume_ch = json.loads(response.text)['data']['74']['quote']['USD']['volume_change_24h']
                week_per_ch = json.loads(response.text)['data']['74']['quote']['USD']['percent_change_7d']
                graph_color_decision.doge_color = week_per_ch
                cl8,col29, col30, col31,col32,g8 = st.columns([0.5,1.5,2,2,2,1.5])

                with cl8:
                        st.write(4)
                with col29:
                        st.image("images/dogecoin.png")
                with col30:
                        st.metric(label="Dogecoin (DOGE)", value=("$"+str(round(price, 2))), delta=str(round(hour24, 2)) + "%")
                with col31:
                        st.metric(label="Volume (24h)", value=("$"+str(round(volume, 2))), delta=str(round(volume_ch, 2)) + "%")
                with col32:
                        st.metric(label="Market Cap", value=("$"+str(round(marketcap, 2))),delta=str(round(marketcap_ch, 2)) + "%")
                with g8:
                        st.write("7 days graph")
                        cryptographs.get_doge_graph()

        def get_shib():
                parameters = {'slug': 'shiba-inu', 'convert': 'USD'}
                session = Session()
                session.headers.update(headers)
                response = session.get(url, params=parameters)
                hour24 = json.loads(response.text)['data']['5994']['quote']['USD']['percent_change_24h']
                price = json.loads(response.text)['data']['5994']['quote']['USD']['price']
                marketcap = json.loads(response.text)['data']['5994']['quote']['USD']['market_cap']
                marketcap_ch = json.loads(response.text)['data']['5994']['quote']['USD']['market_cap_dominance']
                volume = json.loads(response.text)['data']['5994']['quote']['USD']['volume_24h']
                volume_ch = json.loads(response.text)['data']['5994']['quote']['USD']['volume_change_24h']
                week_per_ch = json.loads(response.text)['data']['5994']['quote']['USD']['percent_change_7d']
                graph_color_decision.shib_color = week_per_ch
                cl10,col37, col38, col39,col40,g10 = st.columns([0.5,1.5,2,2,2,1.5])

                with cl10:
                        st.write(5)
                with col37:
                        st.image("images/shibacoin.png")
                with col38:
                        st.metric(label="Shiba Inu (SHIB)", value=("$"+str(round(price,5))), delta=str(round(hour24, 2)) + "%")
                with col39:
                        st.metric(label="Volume (24h)", value=("$"+str(round(volume, 2))), delta=str(round(volume_ch, 2)) + "%")
                with col40:
                        st.metric(label="Market Cap", value=("$"+str(round(marketcap, 2))),delta=str(round(marketcap_ch, 2)) + "%")
                with g10:
                        st.write("7 days graph")
                        cryptographs.get_shib_graph()
        st.write(" ")
        hide_img_fs = '''
                <style>
                button[title="View fullscreen"]{
                    visibility: hidden;}
                </style>
                '''
        st.markdown(hide_img_fs, unsafe_allow_html=True)
        get_btc()
        st.write("---------------------------")
        get_eth()
        st.write("---------------------------")
        get_ltc()
        st.write("---------------------------")
        get_doge()
        st.write("---------------------------")
        get_shib()