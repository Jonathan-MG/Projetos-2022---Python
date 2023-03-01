# Jonathan Martins Gomes - RA: 20.00862-7
import streamlit as st

class Store_View:
    def __init__(self) -> None:
        st.subheader("Destaques")
        c1,c2,c3 = st.columns(3,gap="small")
        c4,c5,c6 = st.columns(3,gap="small")
        c7,c8,c9 = st.columns(3,gap="small")
        c10,c11,c12 = st.columns(3,gap="small")
        colunas = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12]
        
        if "colunas_aux" not in st.session_state:
            st.session_state["colunas_aux"] = 0
            
        quant_produtos = st.session_state["produtos"].get_Quantidade_Produtos()
        for st.session_state["colunas_aux"] in range(quant_produtos):
            with colunas[st.session_state["colunas_aux"]]:
                st.image(st.session_state["produtos"].get_Produto(st.session_state["colunas_aux"]).get_Imagem(), st.session_state["produtos"].get_Produto(st.session_state["colunas_aux"]).get_Descricao())
                st.write("R$ "+ str(st.session_state["produtos"].get_Produto(st.session_state["colunas_aux"]).get_Valor()))
                if st.button("Adicionar ao carrinho", key = st.session_state["produtos"].get_Produto(st.session_state["colunas_aux"]).get_Keyword()+str(st.session_state["colunas_aux"])):
                    if st.session_state["carrinho"].adicionar(st.session_state["produtos"].get_Produto(st.session_state["colunas_aux"])):
                        st.write("Produto adicionado ao carrinho!")
                    else:
                        st.write("O produto já está no carrinho!")
                        
                
