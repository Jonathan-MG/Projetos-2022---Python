# Jonathan Martins Gomes - RA: 20.00862-7
import streamlit as st
from view.home_page import Home
from view.login import Login

st.set_page_config(page_title="Snoteam",layout="centered",initial_sidebar_state="collapsed",menu_items=None)
if Login():
    Home()