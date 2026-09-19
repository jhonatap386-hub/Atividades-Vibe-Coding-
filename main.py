import streamlit as st
import nltk
from nltk.corpus import stopwords
from collections import Counter
import re

# Baixa os dados do NLTK necessários (só baixa uma vez)
nltk.download('stopwords')

# Configura o título da página
st.title("📊 Análise de Frequência de Palavras em Avaliações")
st.write("Cole abaixo as avaliações de clientes para identificar os padrões mais comuns.")

# Campo de texto para o usuário colar as avaliações
texto = st.text_area("Avaliações dos clientes", height=200, placeholder="Cole aqui as avaliações...")

# Botão para disparar a análise
if st.button("Analisar"):

    if texto.strip() == "":
        st.warning("Por favor, insira algum texto antes de analisar.")
    else:
        # Deixa tudo minúsculo e remove pontuação
        texto_limpo = re.sub(r"[^\w\sÀ-ÿ]", "", texto.lower())

        # Separa o texto em palavras
        palavras = texto_limpo.split()

        # Remove stopwords (palavras sem valor analítico, tipo "o", "e", "de")
        stop_words = set(stopwords.words('portuguese'))
        palavras_filtradas = [p for p in palavras if p not in stop_words]

        # Conta a frequência de cada palavra
        contagem = Counter(palavras_filtradas)

        # Pega as 10 palavras mais frequentes
        top_10 = contagem.most_common(10)

        # Mostra o resultado em tabela
        st.subheader("Palavras mais frequentes")
        st.table(top_10)

        # Mostra também em gráfico de barras
        st.subheader("Gráfico de frequência")
        palavras_grafico = [item[0] for item in top_10]
        valores_grafico = [item[1] for item in top_10]
        st.bar_chart(data=dict(zip(palavras_grafico, valores_grafico)))