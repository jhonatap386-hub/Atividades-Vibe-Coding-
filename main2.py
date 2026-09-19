
import streamlit as st

# Configura o título da página
st.title("🚨 Detector de Mensagens Negativas")
st.write("Digite a mensagem do cliente para verificar se ela precisa de atenção prioritária.")

# Lista de palavras negativas que indicam prioridade no atendimento
palavras_negativas = ["ruim", "péssimo", "pessimo", "erro", "problema", "horrível", "horrivel", "reclamação", "reclamacao", "insatisfeito"]

# Campo de texto para o usuário digitar a mensagem
mensagem = st.text_area("Mensagem do cliente", height=150, placeholder="Digite aqui a mensagem recebida...")

# Botão para disparar a verificação
if st.button("Verificar"):

    if mensagem.strip() == "":
        st.warning("Por favor, insira uma mensagem antes de verificar.")
    else:
        # Deixa a mensagem em minúsculas para comparar sem diferenciar caixa
        mensagem_lower = mensagem.lower()

        # Verifica se alguma palavra negativa está presente na mensagem
        encontrou_negativa = any(palavra in mensagem_lower for palavra in palavras_negativas)

        # Regra condicional: se achou palavra negativa, prioriza o atendimento
        if encontrou_negativa:
            st.error("🔴 PRIORIDADE ALTA: mensagem contém termos negativos. Encaminhar para suporte imediato.")
        else:
            st.success("🟢 Mensagem sem termos negativos. Atendimento padrão.")
```