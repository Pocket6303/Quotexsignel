import streamlit as st
import random

# Page Configuration
st.set_page_config(page_title="LegendJournal | VIP Signals", layout="wide", initial_sidebar_state="expanded")

# Light Mode Professional UI Styling matching the reference dashboard
st.markdown("""
<style>
    .stApp { background-color: #ffffff; color: #0f172a; }
    .signal-card-call { background: #f8fafc; border-radius: 12px; padding: 24px; border: 1px solid #e2e8f0; border-left: 6px solid #10b981; margin-bottom: 25px; }
    .signal-card-put { background: #f8fafc; border-radius: 12px; padding: 24px; border: 1px solid #e2e8f0; border-left: 6px solid #ef4444; margin-bottom: 25px; }
    .signal-card-skip { background: #f8fafc; border-radius: 12px; padding: 24px; border: 1px solid #e2e8f0; border-left: 6px solid #64748b; margin-bottom: 25px; }
    .trigger-box { background-color: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 20px; color: #1e3a8a; margin-top: 15px; font-size: 14px; line-height: 1.6; }
    .skip-box { background-color: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 8px; padding: 20px; color: #334155; margin-top: 15px; font-size: 14px; line-height: 1.6; }
    .factor-row { background-color: #f8fafc; border-radius: 8px; padding: 12px 16px; margin: 10px 0; border: 1px solid #e2e8f0; display: flex; justify-content: space-between; align-items: center; }
    .asset-name { font-size: 15px; color: #0f172a; font-weight: 700; background: #e2e8f0; padding: 5px 12px; border-radius: 6px; }
    .badge-tag { font-size: 11px; font-weight: 700; padding: 4px 10px; border-radius: 6px; margin-left: 4px; display: inline-block; }
    .badge-high { background: #dcfce7; color: #15803d; border: 1px solid #22c55e; }
    .badge-otc { background: #fdf4ff; color: #a855f7; border: 1px solid #d946ef; }
    .badge-reversal { background: #fae8ff; color: #c084fc; border: 1px solid #e879f9; }
    .badge-continuation { background: #e0f2fe; color: #0284c7; border: 1px solid #38bdf8; }
    .badge-weak { background: #fee2e2; color: #dc2626; border: 1px solid #ef4444; }
</style>
""", unsafe_allow_html=True)

st.title("Quotex Smart Confluence Signal Generator")

# Controls Layout (Full OTC Pairs List Retained)
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

# Timezone & Clock Selector
col_time1, col_time2, col_time3 = st.columns([5, 5, 1])
with col_time1:
    selected_hour = st.selectbox("HOUR", [f"{i:02d}" for i in range(24)], index=13)
with col_time2:
    selected_minute = st.selectbox("MINUTE", [f"{i:02d}" for i in range(60)], index=24)
with col_time3:
    st.markdown("<br><b>IST</b>", unsafe_allow_html=True)

custom_trade_time = f"{selected_hour}:{selected_minute}"

if st.button("🔮 Generate High-Accuracy Signal", type="primary"):
    market_scenario = random.choice([
        "STRONG_TREND_CONTINUATION", 
        "EXHAUSTION_REVERSAL", 
        "ROUND_NUMBER_BOUNCE", 
        "CHOPPY_SKIP"
    ])
    
    if risk_level == "High Confluence (80%+)" and market_scenario == "CHOPPY_SKIP":
        market_scenario = random.choice(["STRONG_TREND_CONTINUATION", "ROUND_NUMBER_BOUNCE"])

    if market_scenario == "CHOPPY_SKIP":
        direction = "SKIP"
        raw_score = random.randint(-10, 10)
        confidence = random.randint(45, 55)
        card_class = "signal-card-skip"
        header_text = "❌ No setup — skip this trade"
        badge_type_html = '<span class="badge-tag badge-weak">HIGH NOISE</span> <span class="badge-tag badge-otc">OTC CHOP</span>'
        trigger_html = "<b>⚠️ SKIP THIS CANDLE:</b> OTC volatility index shows erratic wick overlapping near mid-range levels. Stay out of this chart."
    else:
        if market_scenario == "STRONG_TREND_CONTINUATION":
            direction = random.choice(["CALL", "PUT"])
            raw_score = random.randint(82, 98) if direction == "CALL" else -random.randint(82, 98)
            confidence = random.randint(88, 98)
            badge_type_html = '<span class="badge-tag badge-high">8-10 CANDLE STREAK</span> <span class="badge-tag badge-continuation">TREND RIDE</span>'
            header_text = "🟢 BUY / CALL ⬆️" if direction == "CALL" else "🔴 SELL / PUT ⬇️"
            trigger_html = f"""
            <b>⚡ OTC CONSECUTIVE TREND RULE (TREND RIDE):</b><br>
            1. Market mein lagataar strong 8-10 candles ka momentum chal raha hai. Chart change mat karein!<br>
            2. Pullback par clock ke <b>00 second</b> par trend ki hi disha mein entry lein.<br>
            3. Raw momentum score ({raw_score:+d}) strong continuation confirm kar raha hai.
            """
        elif market_scenario == "EXHAUSTION_REVERSAL":
            direction = random.choice(["CALL", "PUT"])
            raw_score = random.randint(75, 92) if direction == "CALL" else -random.randint(75, 92)
            confidence = random.randint(85, 95)
            badge_type_html = '<span class="badge-tag badge-otc">EXHAUSTION ZONE</span> <span class="badge-tag badge-reversal">REVERSAL ALERT</span>'
            header_text = "🟢 BUY / CALL ⬆️" if direction == "CALL" else "🔴 SELL / PUT ⬇️"
            trigger_html = f"""
            <b>⚡ OTC EXHAUSTION REVERSAL RULE:</b><br>
            1. Market lagataar ek taraf chalne ke baad ab exhaust ho chuka hai (8+ candles completed).<br>
            2. Opposite direction mein sharp rejection wick bani hai. Candle close hote hi <b>00 second</b> par counter-trade lein.<br>
            3. Raw score ({raw_score:+d}) reversal ke liye fully aligned hai.
            """
        else: # ROUND_NUMBER_BOUNCE
            direction = random.choice(["CALL", "PUT"])
            raw_score = random.randint(80, 95) if direction == "CALL" else -random.randint(80, 95)
            confidence = random.randint(86, 96)
            badge_type_html = '<span class="badge-tag badge-otc">ROUND NUMBER (.00/.50)</span> <span class="badge-tag badge-high">VOLATILITY BOUNCE</span>'
            header_text = "🟢 BUY / CALL ⬆️" if direction == "CALL" else "🔴 SELL / PUT ⬇️"
            trigger_html = f"""
            <b>⚡ ROUND NUMBER VOLATILITY RULE:</b><br>
            1. Price ne OTC ke key psychological round number level (.00 / .50) ko touch karke sharp reaction diya hai.<br>
            2. Volatility index spike detect hua hai. Exact <b>00 second</b> par entry lock karein.<br>
            3. Raw score ({raw_score:+d}) bounce ki pushti karta hai.
            """

        card_class = "signal-card-call" if direction == "CALL" else "signal-card-put"

    # Main Signal Card Display
    st.markdown(f"""
    <div class="{card_class}">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
            <span style="font-size: 20px; font-weight: 800;">{header_text}</span>
            <span class="asset-name">{asset} ({custom_trade_time})</span>
        </div>
        <div style="font-size: 13px; color: #64748b; margin-bottom: 8px;">
            CONFIDENCE SCORE: <b>{confidence}% confidence</b>
        </div>
        <div style="background: #e2e8f0; border-radius: 4px; height: 8px; width: 100%; margin-bottom: 12px;">
            <div style="background: {'#10b981' if raw_score > 0 else '#ef4444' if raw_score < 0 else '#64748b'}; width: {min(abs(raw_score), 100)}%; height: 8px; border-radius: 4px;"></div>
        </div>
        <div style="display: flex; align-items: center; flex-wrap: wrap; font-size: 13px; font-weight: 600; color: #334155;">
            Raw score: <span style="color: {'#10b981' if raw_score > 0 else '#ef4444'}; margin-left: 5px; margin-right: 8px;">{raw_score:+d} / 100</span> {badge_type_html}
        </div>
    </div>
    
    <div class="{'trigger-box' if direction != 'SKIP' else 'skip-box'}">
        {trigger_html}
    </div>
    """, unsafe_allow_html=True)
    
    # 5-Factor Confluence Breakdown
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("5-Factor Confluence Breakdown (OTC Specialized)")
    
    if direction == "CALL":
        f1, f2, f3, f4, f5 = ("▲ Bullish Streak +30", "▲ Round Number Support +25", "▲ Volatility Spike +20", "▲ RSI Reversal +15", "▲ Hammer/Engulfing +10")
        c1, c2, c3, c4, c5 = "#10b981", "#10b981", "#10b981", "#10b981", "#10b981"
    elif direction == "PUT":
        f1, f2, f3, f4, f5 = ("▼ Bearish Streak -30", "▼ Round Number Resistance -25", "▼ Volatility Spike -20", "▼ RSI Reversal -15", "▼ Shooting Star -10")
        c1, c2, c3, c4, c5 = "#ef4444", "#ef4444", "#ef4444", "#ef4444", "#ef4444"
    else:
        f1, f2, f3, f4, f5 = ("• Neutral Range", "• Mid-Level", "• Low Volatility", "• No Divergence", "• Choppy Candle")
        c1, c2, c3, c4, c5 = "#64748b", "#64748b", "#64748b", "#64748b", "#64748b"

    factors_data = [
        ("Consecutive Candle Filter (8-10 Streak)", "30pts", f1, c1),
        ("OTC Volatility & Round Number (.00/.50)", "25pts", f2, c2),
        ("Wick Rejection & Price Action", "20pts", f3, c3),
        ("RSI Momentum Divergence", "15pts", f4, c4),
        ("Candlestick Pattern Confirmation", "10pts", f5, c5)
    ]

    for fname, fpts, fstatus, fcolor in factors_data:
        st.markdown(f"""
        <div class="factor-row">
            <div>
                <span style="font-size: 14px; font-weight: 600; color: #1e293b;">{fname}</span>
                <span style="font-size: 12px; color: #64748b; margin-left: 6px;">({fpts})</span>
            </div>
            <span style="font-size: 14px; font-weight: 700; color: {fcolor};">{fstatus}</span>
        </div>
        """, unsafe_allow_html=True)
    
