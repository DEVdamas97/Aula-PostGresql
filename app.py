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
elif menu == "Atualizar":
    st.subheader("Atualizar idade")
    alunos = listar_alunos()
    if alunos:
        id_aluno = st.selectbox("Escolha o aluno", [ linha[0] for linha in alunos ])
        nova_idade = st.number_input("Nova idade", min_value=10, step=1) # o step pula de um numero a outro, no caso de 1 em 1
        if st.button("Atualizar"):
            atualizar_aluno(id_aluno, nova_idade)
            st.success(f"Idade do aluno {id_aluno} Atualizado com sucesso")
        else:
            st.info("Nenhum aluno disponivel para atualizar")

elif menu == "Deletar":
    st.subheader("Deletar aluno")
    alunos = listar_alunos()
    if alunos:
        id_aluno = st.selectbox("Escolha o id para deletar", [linha[0] for linha in alunos])
        if st.button("Deletar"):
            deletar_aluno(id_aluno)
            st.success(f"Aluno do id {id_aluno} deletado com sucesso!")
        else:
            st.info("Nenhum aluno disponivel para deletar!")