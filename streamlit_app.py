import streamlit as st

# ===== CONFIGURAÇÃO DO SITE =====
st.set_page_config(
    page_title="BetVisão",
    layout="wide",
)

# ===== ESTILO (tema claro/escuro automático) =====
with open("style.css", "w") as f:
    f.write("""
:root {
    --primary-color: #00FF9D;
    --secondary-color: #1C1C1C;
    --accent-color: #0077FF;
}
""")

# ===== MENU LATERAL =====
st.sidebar.title("📊 BetVisão • Dashboard")

menu = st.sidebar.radio("Navegar para:", [
    "🏠 Início",
    "📈 Análise de Jogos",
    "📉 Safe Bets (mais seguras)",
    "🔥 High Risk Bets (arriscadas)",
    "🔧 Configurações"
])

# ===== PÁGINAS =====
if menu == "🏠 Início":
    st.title("Bem-vindo ao BetVisão 👀⚽")
    st.write("Seu dashboard inteligente para insights e previsões.")

elif menu == "📈 Análise de Jogos":
    st.title("📈 Análise de Jogos")
    st.write("Aqui vai mostrar gráficos, tendências e estatísticas.")

elif menu == "📉 Safe Bets (mais seguras)":
    st.title("📉 Sugestões de Apostas Seguras")
    st.write("⚠️ Ainda em desenvolvimento.")

elif menu == "🔥 High Risk Bets (arriscadas)":
    st.title("🔥 Apostas Arriscadas")
    st.write("Aposte por sua conta e risco 😉")

elif menu == "🔧 Configurações":
    st.title("⚙️ Configurações")
    st.write("Personalização futura: tema, planos premium, etc.")

st.sidebar.info("💡 Versão inicial — em construção")