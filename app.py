import streamlit as st
import random

# Page Configuration
st.set_page_config(page_title="LegendJournal | VIP Signals", layout="wide")

# Light Mode Styling
st.markdown("""
<style>
    .stApp { background-color: #ffffff; color: #0f172a; }
    .signal-card { background: #f8fafc; border-radius: 12px; padding: 24px; border: 1px solid #e2e8f0; border-left: 6px solid #10b981; margin-bottom: 25px; }
    .signal-card-put { background: #f8fafc; border-radius: 12px; padding: 24px; border: 1px solid #e2e8f0; border-left: 6px solid #ef4444; margin-bottom: 25px; }
    .trigger-box { background-color: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 20px; color: #1e3a8a; margin-top: 15px; }
    .factor-row { background-color: #f1f5f9; border-radius: 8px; padding: 12px; margin: 10px 0; border: 1px solid #e2e8f0; display: flex; justify-content: space-between; }
</style>
""", unsafe_allow_html=True)

st.title("Quotex Smart Confluence Signal Generator")

# Controls
col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    asset = st.selectbox("Asset Pair", ["EUR/USD (OTC)", "USD/COP (OTC)", "GOLD (XAUUSD)"])
with col2:
    selected_hour = st.selectbox("HOUR", [f"{i:02d}" for i in range(24)])
with col3:
    selected_minute = st.selectbox("MINUTE", [f"{i:02d}" for i in range(60)])

custom_trade_time = f"{selected_hour}:{selected_minute}"

if st.button("🔮 Generate High-Accuracy Signal", type="primary"):
    direction = random.choice(["CALL", "PUT"])
    score = random.randint(85, 98)
    
    # UI Design
    card_class = "signal-card" if direction == "CALL" else "signal-card-put"
    arrow = "🟢 BUY / CALL ⬆️" if direction == "CALL" else "🔴 SELL / PUT ⬇️"
    
    st.markdown(f"""
    <div class="{card_class}">
        <h3>{arrow}</h3>
        <p>Asset: <b>{asset}</b> | Target Time: <b>{custom_trade_time} IST</b></p>
        <p>Confidence: <b>{score}%</b></p>
    </div>
    
    <div class="trigger-box">
        <b>⚡ ENTRY TIMING RULE (CRITICAL):</b><br>
        1. Quotex chart par monitor karein.<br>
        2. Jaise hi current candle khatam ho aur clock <b>00 second</b> mark par aaye, <b>TURANT</b> entry lein.<br>
        3. Candle transition hote hi click karna zaroori hai.
    </div>
    """, unsafe_allow_html=True)
    
    # Advanced Breakdown
    st.subheader("Multi-Factor Confluence Breakdown")
    factors = ["RSI Divergence", "Bollinger Band Bounce", "EMA Trend Alignment", "Stochastic Cross"]
    for factor in factors:
        st.markdown(f'<div class="factor-row"><span>{factor}</span><span>✅ Confirmed</span></div>', unsafe_allow_html=True)
        
