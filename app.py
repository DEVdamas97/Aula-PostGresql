import streamlit as st
from crud import criar_aluno, listar_alunos, atualizar_aluno, deletar_aluno

st.set_page_config(page_title="Gerenciamento de alunos", page_icon="💡")

st.title("Sistema de alunos com postegreSQL")

menu = st.sidebar.radio("Menu", ["Criar", "Listar", "Atualizar", "Deletar"])

if menu == "Criar":
    st.subheader("➕ criar aluno")
    nome = st.text_input("Nome")
    idade = st.number_input("Idade", min_value=14, step=1)
    if st.button("Cadastrar"):
        if nome.strip("") != "":
            criar_aluno(nome, idade)
            st.success(f"Aluno {nome} foi cadastrado com sucesso")
        else:
            st.warning("O campo nome não pode estar vazio")
elif menu == "Listar":
    st.subheader("Lista de alunos")
    alunos = listar_alunos()
    if alunos:
        st.table(alunos)
    else:
        st.info("Nenhum aluno encontrado")