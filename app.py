import streamlit as st
import pandas as pd

# Título da interface
st.title("Visualizador de Dados Online 📊")

# Campo para o usuário inserir o link
url = st.text_input("Cole aqui o link da base de dados (.csv):")

# Botão para carregar os dados
if st.button("Mostrar dados"):
    if url:
        try:
            # Tenta carregar o CSV a partir da URL
            df = pd.read_csv(url)

            st.success("✅ Dados carregados com sucesso!")
            st.write("### Primeiras linhas do DataFrame:")
            st.dataframe(df.head())  # Mostra as 5 primeiras linhas

        except Exception as e:
            st.error(f"❌ Erro ao carregar os dados: {e}")
    else:
        st.warning("⚠️ Por favor, insira o link do arquivo CSV.")
