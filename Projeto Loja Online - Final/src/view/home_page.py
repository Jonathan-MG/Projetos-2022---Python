# Jonathan Martins Gomes - RA: 20.00862-7
import streamlit as st
from controllers.product_controller import Product_Ctrl
from controllers.carrinho_controller import Carrinho_Ctrl
from controllers.pedido_controller import Pedido_Ctrl
from view.store_view import Store_View
from view.cart_view import Cart_View
from view.profile_view import Profile_View
from view.admin_view import Admin_View

class Home:
    def __init__(self):
        if "carrinho" not in st.session_state:
            st.session_state["carrinho"] = Carrinho_Ctrl()
        st.session_state["produtos"] = Product_Ctrl()
        st.session_state["pedido"] = Pedido_Ctrl()
        
        store,cart,profile,administration = st.tabs(["Loja","Carrinho","Perfil","Novos Produtos"])    
        with store:
            Store_View()
        with cart:
            Cart_View()
        with profile:
            Profile_View()
        with administration:
            Admin_View()
        
        hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
        st.markdown(hide_menu_style, unsafe_allow_html=True)