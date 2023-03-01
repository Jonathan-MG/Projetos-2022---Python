# Jonathan Martins Gomes - RA: 20.00862-7
import streamlit as st

class Profile_View:
    def __init__(self) -> None:
        if "userlogged" not in st.session_state:
            st.session_state["userlogged"] = st.session_state["username"]
        current_user = (f'{st.session_state["userlogged"]}')
        
        new_user_email = st.text_input("Digite o novo endereço de email:",key="new_user_email")
        if st.button("Alterar E-mail",key="change_email_button"):
            if st.session_state["users_db"].update_user(current_user, "e-mail", new_user_email):
                st.write("Troca de e-mail realizada com sucesso!")
            else:
                st.write("Não foi possível realizar a troca de e-mail, verifique seus dados!")                
        
        new_user_password = st.text_input("Digite uma nova senha:",key="new_user_password",type='password')
        if st.button("Alterar Senha",key="change_password_button"):
            if st.session_state["users_db"].update_user(current_user, "password", new_user_password):
                st.write("Troca de senha realizada com sucesso!")
            else:
                st.write("Não foi possível realizar a troca de senha, verifique seus dados!")