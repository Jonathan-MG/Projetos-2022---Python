# Jonathan Martins Gomes - RA: 20.00862-7
import streamlit as st
from datetime import datetime

class Cart_View:
    def __init__(self) -> None:
        col1,col2,col3 = st.columns([1.5,5,2.5],gap = "small")
        with col1:
            st.write("Remover:")
            for i in range(st.session_state["carrinho"].get_Quantidade_Produtos()):
                aux = st.session_state["carrinho"].exibir_Produtos(i)
                if st.button("Remover",key = ("Remover_"+aux.get_Keyword()+str(i))):
                    st.session_state["carrinho"].remover(aux)      
        
        with col2:
            st.write("Produtos:")
            for produto in range(st.session_state["carrinho"].get_Quantidade_Produtos()):
                st.write(str(st.session_state["carrinho"].exibir_Produtos(produto)))
                st.text(" ")
        
        with col3:
            st.write("Resumo da Compra:")
            st.write("Quant. de Produtos: "+str(st.session_state["carrinho"].get_Quantidade_Produtos()))
            st.write("Valor total: R$ "+str(st.session_state["carrinho"].get_Valor_Total()))
            if st.button("Pagamento",key = ("pagamento")):
                if st.session_state["pedido"].inserir_pedido(st.session_state["userlogged"],
                                                          st.session_state["carrinho"],
                                                          datetime.today().strftime("%d/%m/%Y")):
                    st.write("Deu tudo certo, mas a próxima página ainda não existe....")
                else:
                    st.write("Não foi possível concluir seu pedido!")