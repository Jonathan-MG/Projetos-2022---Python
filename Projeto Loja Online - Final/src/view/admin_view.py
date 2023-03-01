# Jonathan Martins Gomes - RA: 20.00862-7
import streamlit as st
import base64

class Admin_View:
    def __init__(self) -> None:        
        new_product_name = st.text_input("Digite o nome do produto:",key="new_prod_name")               
        new_product_description = st.text_input("Digite uma descrição do produto:",key="new_prod_description")
        new_product_keyword = st.text_input("Digite a 'keyword' do produto:",key="new_prod_key")               
        new_product_value = st.text_input("Digite o valor do produto:",key="new_prod_value")
        new_product_image = st.file_uploader("Carrega uma imagem de Capa.",
                                             key="new_prod_img",
                                             accept_multiple_files=False)
        
        if st.button("Cadastrar Produto",key="new_prod_button"):
            if st.session_state["produtos"].criar_novo_produto(new_product_name,
                                                            new_product_description,
                                                            new_product_keyword,
                                                            float(new_product_value),
                                                            new_product_image):
                st.write("Produto cadastrado com sucesso no banco de dados!")
            else:
                st.write("Não foi possível realizar o cadastro, favor verificar se o produto já não existe no sistema!")