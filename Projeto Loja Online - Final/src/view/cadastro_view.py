# Jonathan Martins Gomes - RA: 20.00862-7
import streamlit as st

def Confirma_cadastro(new_user,new_useremail,new_userpassword,new_usercpf,new_userbirth,new_username):
    if st.session_state["users_db"].add_user(new_user,
                                            new_useremail,
                                            new_userpassword,
                                            new_usercpf,
                                            new_userbirth,
                                            new_username):
        st.write("Cadastro realizado com sucesso!")
    else:
        st.write("Não foi possível realizar o cadastro, por favor, verifique seus dados.")

class Cadastro():
    def __init__(self) -> None:       
        new_username = st.text_input(label="Digite seu nome:", key="new_username")
        new_userbirth = st.text_input(label="Digite sua data de nascimento:", key="new_userbirth")
        new_usercpf = st.text_input(label="Digite seu CPF (Apenas números):", key="new_usercpf")
        new_user = st.text_input(label="Digite seu nome de usuário desejado:", key="new_user")
        new_useremail = st.text_input(label="Digite seu E-mail:", key="new_useremail")
        new_userpassword = st.text_input(label="Digite a senha desejada:",type="password", key="new_userpassword")
        
        if st.button("Cadastrar", key="botao_cadastro"):
            Confirma_cadastro(new_user,
                            new_useremail,
                            new_userpassword,
                            new_usercpf,
                            new_userbirth,
                            new_username)