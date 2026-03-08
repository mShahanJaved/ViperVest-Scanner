import streamlit as st
from scanner import run_analysis_for_web
from streamlit_ace import st_ace
import time
import re

# 1. Page Configuration
st.set_page_config(
    page_title="ViperVest",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Advanced Aesthetic Styling (Responsive + Forced Glow)
st.markdown("""
    <style>
    /* 1. Background */
    .stApp {
        background-color: #000000 !important;
        background-image: 
            linear-gradient(rgba(255, 255, 255, 0.05) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255, 255, 255, 0.05) 1px, transparent 1px) !important;
        background-size: 30px 30px !important;
    }

    /* 2. THE GLOW IS BACK: Definitive Animation */
    @keyframes viperscan {
      0% { text-shadow: 0 0 10px rgba(255, 255, 255, 0.3); opacity: 0.9; }
      50% { text-shadow: 0 0 30px rgba(255, 255, 255, 0.9), 0 0 50px rgba(255, 255, 255, 0.3); opacity: 1; }
      100% { text-shadow: 0 0 10px rgba(255, 255, 255, 0.3); opacity: 0.9; }
    }

    #viper-title {
        font-size: clamp(40px, 8vw, 65px) !important; 
        font-weight: 800 !important;
        color: #FFFFFF !important;
        text-align: center !important;
        display: block !important;
        letter-spacing: -3px !important;
        margin-bottom: 0px !important;
        /* Forced Animation */
        animation: viperscan 3s infinite ease-in-out !important;
        -webkit-animation: viperscan 3s infinite ease-in-out !important;
    }

    .viper-sub {
        font-size: clamp(10px, 1.2vw, 12px) !important;
        text-transform: uppercase !important;
        letter-spacing: 5px !important;
        color: #666666 !important;
        text-align: center !important;
        margin-top: -10px !important;
        display: block !important;
    }

    /* 3. Responsive Metric Fixes */
    [data-testid="stMetricLabel"] {
        font-size: clamp(0.6rem, 1.5vw, 0.8rem) !important;
        text-transform: uppercase !important;
        white-space: nowrap !important;
    }
    
    [data-testid="stMetricValue"] {
        font-size: clamp(1.2rem, 3vw, 2rem) !important;
    }

    /* Clean UI */
    [data-testid="stSidebar"] { display: none !important; }
    header { visibility: hidden !important; }
    footer { visibility: hidden !important; }
    </style>
    """, unsafe_allow_html=True)

# 4. Header UI
st.markdown('<span id="viper-title">ViperVest</span>', unsafe_allow_html=True)
st.markdown('<span class="viper-sub">Advanced Static Protection</span>', unsafe_allow_html=True)

# 5. IDE-Style Input
col_l, col_m, col_r = st.columns([1, 4, 1])

with col_m:
    user_code = st_ace(
        placeholder="Paste Python code here...",
        language="python",
        theme="terminal",
        keybinding="vscode",
        font_size=14,
        min_lines=15,
        max_lines=25,
        show_gutter=True,
        auto_update=True
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("RUN SECURITY AUDIT", use_container_width=True):
        if user_code and user_code.strip() != "":
            with st.status("Analyzing code logic...", expanded=True) as status:
                report = run_analysis_for_web(user_code)
                status.update(label="Audit Complete", state="complete", expanded=False)
            
            # --- UPDATED METRIC CALCULATION (INCLUDING LOW) ---
            crit_count = len(re.findall(r"SEVERITY:\s*CRITICAL", report.upper()))
            high_count = len(re.findall(r"SEVERITY:\s*HIGH", report.upper()))
            med_count = len(re.findall(r"SEVERITY:\s*MEDIUM", report.upper()))
            low_count = len(re.findall(r"SEVERITY:\s*LOW", report.upper()))
            
            # Recalculate Score with Low findings included
            score = 100 - (crit_count * 30) - (high_count * 15) - (med_count * 5) - (low_count * 2)
            score = max(0, score)

            # 6. Responsive Dashboard
            st.markdown("### 📊 System Health Overview")
            
            # This container helps Streamlit handle the flow better
            container = st.container()
            m1, m2, m3, m4, m5 = container.columns([1, 1, 1, 1, 1.4])
            
            m1.metric("Critical", crit_count)
            m2.metric("High", high_count)
            m3.metric("Medium", med_count)
            m4.metric("Low", low_count)
            m5.metric("Security Score", f"{score}/100", 
                      delta=f"{score-100}" if score < 100 else None, 
                      delta_color="inverse")

            # 7. Final Report
            st.markdown("---")
            st.markdown("### 🛡️ Full Security Report")
            st.markdown(report)
        else:
            st.error("Please paste code to analyze.")

# Footer
st.markdown("<br><br><p style='text-align:center; color:#333; font-size:10px;'>ViperVest v1.2 | Shahan Security | UCP Lahore</p>", unsafe_allow_html=True)