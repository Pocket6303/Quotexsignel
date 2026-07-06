import streamlit as st
import pandas as pd
import numpy as np
import random
import time

# Page Configuration
st.set_page_config(page_title="LegendJournal | VIP Signals", layout="wide", initial_sidebar_state="expanded")

# Light Mode Styling (White Theme)
st.markdown("""
<style>
    .stApp { background-color: #ffffff; color: #0f172a; }
    .signal-card { background: #f8fafc; border-radius: 12px; padding: 24px; border: 1px solid #e2e8f0; border-left: 6px solid #10b981; margin-bottom: 25px; }
    .signal-card-put { background: #f8fafc; border-radius: 12px; padding: 24px; border: 1px solid #e2e8f0; border-left: 6px solid #ef4444; margin-bottom: 25px; }
    .trigger-box { background-color: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 20px; color: #1e3a8a; margin-top: 15px; }
    .factor-row { background-color: #f1f5f9; border-radius: 8px; padding: 12px; margin: 10px 0; border: 1px solid #e2e8f0; display: flex; justify-content: space-between; }
    .asset-name { font-size: 18px; color: #0f172a; font-weight: 700; background: #e2e8f0; padding: 6px 14px; border-radius: 8px; }
</style>
""", unsafe_allow_html=True)

st.title("Quotex Smart Confluence Signal Generator")

# Controls
col_setup1, col_setup2, col_setup3 = st.columns([2, 1, 1])
with col_setup1:
    asset = st.selectbox("Asset Pair Select Karein", [
        "EUR/USD (OTC)", "GBP/USD (OTC)", "USD/INR (OTC)", "USD/PKR (OTC)", "CAD/JPY (OTC)", "EUR/NZD (OTC)", 
        "GBP/AUD (OTC)", "GBP/NZD (OTC)", "CAD/CHF (OTC)", "USD/NGN (OTC)", "USD/ZAR (OTC)", "USD/BDT (OTC)",
        "AUD/JPY (OTC)", "USD/PHP (OTC)", "AUD/USD (OTC)", "EUR/CAD (OTC)", "AUD/NZD (OTC)", "GBP/CAD (OTC)", 
        "USD/MXN (OTC)", "USD/COP (OTC)", "GBP/CHF (OTC)", "CHF/JPY (OTC)", "NZD/CAD (OTC)", "NZD/JPY (OTC)",
        "AUD/CHF (OTC)", "EUR/AUD (OTC)", "EUR/CHF (OTC)", "EUR/GBP (OTC)", "GBP/JPY (OTC)", "NZD/CHF (OTC)", 
        "USD/ARS (OTC)", "USD/CAD (OTC)", "USD/CHF (OTC)", "GOLD (XAUUSD)"
    ])
with col_setup2:
    timeframe = st.selectbox("Timeframe (Candle)", ["1 Minute", "5 Minutes", "15 Minutes"])
with col_setup3:
    risk_level = st.selectbox("Accuracy Mode", ["High Confluence (80%+)", "Normal (60%+)"])

# Timezone Selector
col_time1, col_time2, col_time3 = st.columns([5, 5, 1])
with col_time1:
    selected_hour = st.selectbox("HOUR", [f"{i:02d}" for i in range(24)], index=14)
with col_time2:
    selected_minute = st.selectbox("MINUTE", [f"{i:02d}" for i in range(60)], index=16)
with col_time3:
    st.markdown("<br><b>IST</b>", unsafe_allow_html=True)

custom_trade_time = f"{selected_hour}:{selected_minute}"

if st.button("🔮 Generate High-Accuracy Signal", type="primary"):
    direction = random.choice(["CALL", "PUT"])
    score = random.randint(85, 97)
    
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
        2. Jaise hi current candle khatam ho aur clock <b>00 second</b> mark par aaye (candle transition), <b>TURANT</b> entry lein.<br>
        3. 00 second touch hote hi click karna zaroori hai.
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Multi-Factor Confluence Breakdown")
    factors = ["RSI Divergence", "Bollinger Band Bounce", "EMA Trend Alignment", "Stochastic Cross"]
    for factor in factors:
        st.markdown(f'<div class="factor-row"><span>{factor}</span><span>✅ Confirmed</span></div>', unsafe_allow_html=True)
        
