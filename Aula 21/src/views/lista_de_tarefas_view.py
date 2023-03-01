from this import s
import streamlit as st
from controllers.tarefa_controller import TarefaController

class ListaTarefasView:
    def __init__(self, controller) -> None:
        self._controller = controller
        self._decricao_tarefa = st.text_input("Insira sua tarefa aqui...")
        self._bot_adicionar = st.button("Adicionar Tarefa",
        on_click = self.adicionar_tarefa)
    def adicionar_tarefa(self):
        self._controller.criar_nova_tarefa(self._decricao_tarefa)