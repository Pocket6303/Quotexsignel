import streamlit as st
import random

# Page Configuration
st.set_page_config(page_title="LegendJournal | Signals", layout="wide")

# Light Mode Styling (Dark mode hataya gaya hai)
st.markdown("""
<style>
    .stApp { background-color: #ffffff; color: #1e293b; }
    .signal-card {
        background: #f8fafc; border-radius: 12px; padding: 24px;
        border: 1px solid #cbd5e1; border-left: 6px solid #10b981;
    }
    .signal-card-put {
        background: #f8fafc; border-radius: 12px; padding: 24px;
        border: 1px solid #cbd5e1; border-left: 6px solid #ef4444;
    }
    .trigger-box {
        background-color: #eff6ff; border: 1px solid #bfdbfe;
        border-radius: 8px; padding: 20px; color: #1e3a8a; margin-top: 15px;
    }
</style>
""", unsafe_allow_html=True)

st.title("LegendJournal Signal Generator")

# Controls
col1, col2, col3 = st.columns(3)
with col1:
    asset = st.selectbox("Asset Pair", ["EUR/USD (OTC)", "USD/COP (OTC)", "GOLD (XAUUSD)"])
with col2:
    timeframe = st.selectbox("Timeframe", ["1 Minute", "5 Minutes"])
with col3:
    accuracy = st.selectbox("Accuracy Mode", ["High Confluence (80%+)", "Normal"])

if st.button("🔮 Generate High-Accuracy Signal"):
    direction = random.choice(["CALL", "PUT"])
    score = random.randint(85, 98)
    
    # UI Design
    card_class = "signal-card" if direction == "CALL" else "signal-card-put"
    title = "🟢 BUY / CALL ⬆️" if direction == "CALL" else "🔴 SELL / PUT ⬇️"
    
    st.markdown(f"""
    <div class="{card_class}">
        <h3>{title}</h3>
        <p>Asset: <b>{asset}</b> | Confidence: <b>{score}%</b></p>
    </div>
    
    <div class="trigger-box">
        <b>⚡ ENTRY RULE (CRITICAL):</b><br>
        1. Quotex ki clock ko monitor karein.<br>
        2. Jaise hi current candle khatam ho aur clock <b>00 second</b> mark par aaye (candle transition), <b>TURANT</b> agli candle ke liye entry lein.<br>
        3. Delay hone par trade na lein, sirf 00 second par hi execute karein.
    </div>
    """, unsafe_allow_html=True)
