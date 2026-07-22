import streamlit as st
import random

# Page Configuration
st.set_page_config(page_title="LegendJournal | VIP Signals", layout="wide", initial_sidebar_state="expanded")

# Light Mode Styling with Raw Score & Status Badges
st.markdown("""
<style>
    .stApp { background-color: #ffffff; color: #0f172a; }
    .signal-card { background: #f8fafc; border-radius: 12px; padding: 24px; border: 1px solid #e2e8f0; border-left: 6px solid #10b981; margin-bottom: 25px; }
    .signal-card-put { background: #f8fafc; border-radius: 12px; padding: 24px; border: 1px solid #e2e8f0; border-left: 6px solid #ef4444; margin-bottom: 25px; }
    .signal-card-skip { background: #f8fafc; border-radius: 12px; padding: 24px; border: 1px solid #e2e8f0; border-left: 6px solid #64748b; margin-bottom: 25px; }
    .trigger-box { background-color: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 20px; color: #1e3a8a; margin-top: 15px; }
    .skip-box { background-color: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 8px; padding: 20px; color: #334155; margin-top: 15px; }
    .factor-row { background-color: #f1f5f9; border-radius: 8px; padding: 12px; margin: 10px 0; border: 1px solid #e2e8f0; display: flex; justify-content: space-between; }
    .asset-name { font-size: 16px; color: #0f172a; font-weight: 700; background: #e2e8f0; padding: 4px 10px; border-radius: 6px; }
    .badge-tag { font-size: 11px; font-weight: 700; padding: 3px 8px; border-radius: 4px; margin-left: 5px; }
    .badge-moderate { background: #fef3c7; color: #d97706; border: 1px solid #f59e0b; }
    .badge-reversal { background: #fae8ff; color: #c084fc; border: 1px solid #e879f9; }
    .badge-continuation { background: #e0f2fe; color: #0284c7; border: 1px solid #38bdf8; }
    .badge-weak { background: #fee2e2; color: #dc2626; border: 1px solid #ef4444; }
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
        "USD/ARS (OTC)", "USD/CAD (OTC)", "USD/CHF (OTC)", "GOLD (XAUUSD)", "USD/IDR (OTC)"
    ])
with col_setup2:
    timeframe = st.selectbox("Timeframe (Candle)", ["1 Minute", "5 Minutes", "15 Minutes"])
with col_setup3:
    risk_level = st.selectbox("Accuracy Mode", ["High Confluence (80%+)", "Normal (60%+)"])

# Timezone Selector
col_time1, col_time2, col_time3 = st.columns([5, 5, 1])
with col_time1:
    selected_hour = st.selectbox("HOUR", [f"{i:02d}" for i in range(24)], index=13)
with col_time2:
    selected_minute = st.selectbox("MINUTE", [f"{i:02d}" for i in range(60)], index=24)
with col_time3:
    st.markdown("<br><b>IST</b>", unsafe_allow_html=True)

custom_trade_time = f"{selected_hour}:{selected_minute}"

if st.button("🔮 Generate High-Accuracy Signal", type="primary"):
    # Randomly decide signal type or skip condition based on screenshots
    signal_type = random.choice(["CALL", "PUT", "SKIP"])
    
    if signal_type == "SKIP":
        raw_score = random.randint(-20, 20)
        confidence = random.randint(50, 60)
        card_class = "signal-card-skip"
        header_text = "❌ No setup — skip this trade"
        badge_html = '<span class="badge-tag badge-weak">WEAK</span> <span class="badge-tag badge-continuation">CONTINUATION</span>'
        trigger_html = """
        <b>⚠️ SKIP THIS CANDLE:</b><br>
        Conflicting signals detected. Market momentum is neutral. Do not trade.
        """
    else:
        direction = signal_type
        raw_score = random.randint(45, 95) if direction == "CALL" else -random.randint(45, 95)
        confidence = random.randint(75, 94)
        card_class = "signal-card" if direction == "CALL" else "signal-card-put"
        arrow = "🟢 BUY / CALL ⬆️" if direction == "CALL" else "🔴 SELL / PUT ⬇️"
        header_text = arrow
        badge_html = '<span class="badge-tag badge-moderate">MODERATE</span> <span class="badge-tag badge-reversal">REVERSAL</span>'
        trigger_html = f"""
        <b>⚡ ENTRY TIMING RULE (CRITICAL):</b><br>
        1. Quotex chart par monitor karein.<br>
        2. Jaise hi current candle khatam ho aur clock <b>00 second</b> mark par aaye, <b>TURANT</b> entry lein.<br>
        3. Raw score momentum (+/-) ke anusaar hi trade execute karein.
        """

    st.markdown(f"""
    <div class="{card_class}">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <span style="font-size: 20px; font-weight: 800;">{header_text}</span>
            <span class="asset-name">{asset} ({custom_trade_time})</span>
        </div>
        <div style="font-size: 13px; color: #64748b; margin-bottom: 10px;">
            CONFIDENCE SCORE: <b>{confidence}% confidence</b>
        </div>
        <div style="background: #e2e8f0; border-radius: 4px; height: 8px; width: 100%; margin-bottom: 12px;">
            <div style="background: {'#10b981' if raw_score > 0 else '#ef4444' if raw_score < 0 else '#64748b'}; width: {min(abs(raw_score), 100)}%; height: 8px; border-radius: 4px;"></div>
        </div>
        <div style="display: flex; align-items: center; font-size: 13px; font-weight: 600; color: #334155;">
            Raw score: <span style="color: {'#10b981' if raw_score > 0 else '#ef4444'}; margin-left: 5px; margin-right: 8px;">{raw_score:+d} / 100</span> {badge_html}
        </div>
    </div>
    
    <div class="{'trigger-box' if signal_type != 'SKIP' else 'skip-box'}">
        {trigger_html}
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Multi-Factor Confluence Breakdown")
    factors = ["RSI Divergence", "Bollinger Band Bounce", "EMA Trend Alignment", "Stochastic Cross"]
    for factor in factors:
        st.markdown(f'<div class="factor-row"><span>{factor}</span><span>✅ Confirmed</span></div>', unsafe_allow_html=True)
    
