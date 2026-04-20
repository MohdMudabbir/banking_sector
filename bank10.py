import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# ================================================================
#  MONEY RAIN ANIMATION  — replaces st.balloons()
# ================================================================
def money_rain():
    """Premium fintech-style money animation (Paytm / CRED style)."""
    st.markdown("""
<div id="money-overlay" style="
  position:fixed;
  top:0; left:0; width:100vw; height:100vh;
  pointer-events:none;
  z-index:999999;
  overflow:hidden;
"></div>

<div id="success-toast" style="
  position:fixed;
  top:50%;
  left:50%;
  transform:translate(-50%,-50%) scale(0.6);
  background:linear-gradient(135deg,rgba(0,30,10,0.97),rgba(0,60,20,0.97));
  border:2px solid #00C853;
  border-radius:24px;
  padding:2rem 3rem;
  text-align:center;
  z-index:9999999;
  box-shadow:
    0 0 40px rgba(0,200,83,0.6),
    0 0 80px rgba(0,200,83,0.25),
    0 0 120px rgba(255,215,0,0.15),
    0 24px 60px rgba(0,0,0,0.5);
  opacity:0;
  transition:all 0.45s cubic-bezier(0.34,1.56,0.64,1);
" id="money-toast">
  <div style="font-size:2.8rem;margin-bottom:0.5rem;">💸</div>
  <div style="
    font-size:1.3rem;
    font-weight:800;
    background:linear-gradient(135deg,#00E676,#FFD700,#00C853);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    background-clip:text;
    letter-spacing:0.05em;
    text-shadow:none;
  ">Expense Added Successfully!</div>
  <div style="
    font-size:0.8rem;
    color:rgba(0,200,83,0.8);
    margin-top:0.5rem;
    letter-spacing:0.1em;
  ">✦ Transaction Recorded ✦</div>
</div>

<style>
@keyframes money-rise {
  0%   { transform: translateY(0)   rotate(0deg)   scale(0.6); opacity:0; }
  8%   { opacity:1; }
  85%  { opacity:1; }
  100% { transform: translateY(-110vh) rotate(var(--rot)) scale(var(--sc)); opacity:0; }
}
@keyframes toast-bg-pulse {
  0%,100% { box-shadow:
    0 0 40px rgba(0,200,83,0.6),
    0 0 80px rgba(0,200,83,0.25),
    0 0 120px rgba(255,215,0,0.15),
    0 24px 60px rgba(0,0,0,0.5);
  }
  50% { box-shadow:
    0 0 60px rgba(0,200,83,0.9),
    0 0 120px rgba(0,200,83,0.45),
    0 0 180px rgba(255,215,0,0.25),
    0 24px 60px rgba(0,0,0,0.5);
  }
}
.money-particle {
  position: absolute;
  bottom: 0;
  font-size: var(--fs);
  left: var(--lf);
  animation: money-rise var(--dur) cubic-bezier(0.25, 0.46, 0.45, 0.94) var(--delay) forwards;
  filter: drop-shadow(0 0 8px var(--glow)) drop-shadow(0 0 16px var(--glow));
  will-change: transform, opacity;
  user-select: none;
}
</style>

<script>
(function(){
  var overlay = document.getElementById('money-overlay');
  var toast   = document.getElementById('money-toast');

  // ── Show toast ──
  setTimeout(function(){
    toast.style.opacity  = '1';
    toast.style.transform = 'translate(-50%,-50%) scale(1)';
    toast.style.animation = 'toast-bg-pulse 1.4s ease-in-out infinite';
  }, 80);

  // ── Money symbols pool ──
  var symbols = [
    { sym:'₹',  glow:'#00C853' },
    { sym:'💸', glow:'#FFD700' },
    { sym:'💰', glow:'#FFD700' },
    { sym:'🪙', glow:'#FFD700' },
    { sym:'₹',  glow:'#69FF47' },
    { sym:'💵', glow:'#00C853' },
    { sym:'₹',  glow:'#FFD700' },
  ];

  var count   = 48;
  var created = 0;

  function spawnParticle(){
    if (created >= count) return;
    created++;

    var pick    = symbols[Math.floor(Math.random() * symbols.length)];
    var el      = document.createElement('span');
    var leftPct = (Math.random() * 96 + 2).toFixed(1) + '%';
    var fs      = (Math.random() * 28 + 18).toFixed(0) + 'px';
    var dur     = (Math.random() * 1.8 + 2.0).toFixed(2) + 's';
    var delay   = (Math.random() * 1.6).toFixed(2) + 's';
    var rot     = (Math.random() * 520 - 260).toFixed(0) + 'deg';
    var sc      = (Math.random() * 0.6 + 0.8).toFixed(2);

    el.className = 'money-particle';
    el.textContent = pick.sym;
    el.style.cssText = [
      '--lf:'   + leftPct,
      '--fs:'   + fs,
      '--dur:'  + dur,
      '--delay:'+ delay,
      '--rot:'  + rot,
      '--sc:'   + sc,
      '--glow:' + pick.glow,
    ].join(';');

    overlay.appendChild(el);
    setTimeout(function(){ if(el.parentNode) el.parentNode.removeChild(el); },
               (parseFloat(dur) + parseFloat(delay) + 0.3) * 1000);
  }

  // Stagger spawns over 1.8 s
  for (var i = 0; i < count; i++){
    (function(idx){ setTimeout(spawnParticle, idx * 38 + Math.random()*30); })(i);
  }

  // ── Hide toast after 3.2 s ──
  setTimeout(function(){
    toast.style.transition = 'all 0.5s cubic-bezier(0.4,0,0.2,1)';
    toast.style.opacity    = '0';
    toast.style.transform  = 'translate(-50%,-50%) scale(0.85) translateY(-30px)';
    setTimeout(function(){ if(toast.parentNode) toast.parentNode.removeChild(toast); }, 550);
  }, 3200);

  // ── Clean overlay ──
  setTimeout(function(){
    if(overlay.parentNode) overlay.parentNode.removeChild(overlay);
  }, 4500);
})();
</script>
""", unsafe_allow_html=True)

# ==================== PAGE CONFIG ====================
st.set_page_config(
    page_title="🌟 Indian Banking Sector Analytics 2024",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== PREMIUM CSS DESIGN ====================
st.markdown("""
<style>
    /* Global Styles */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Premium Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Main Container with Glassmorphism */
    .main-container {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 30px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    /* Premium Header */
    .premium-header {
        background: linear-gradient(120deg, #1e3c72 0%, #2a5298 100%);
        padding: 2.5rem;
        border-radius: 30px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 20px 40px rgba(0,0,0,0.2);
        border: 1px solid rgba(255,255,255,0.1);
        position: relative;
        overflow: hidden;
    }
    
    .premium-header::before {
        content: "📊";
        position: absolute;
        right: -20px;
        bottom: -20px;
        font-size: 150px;
        opacity: 0.1;
        transform: rotate(-10deg);
    }
    
    .premium-header h1 {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .premium-header p {
        font-size: 1.2rem;
        opacity: 0.9;
        font-weight: 300;
    }
    
    /* Glassmorphism Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(10px);
        padding: 1.5rem;
        border-radius: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border: 1px solid rgba(255,255,255,0.3);
        transition: all 0.3s ease;
        height: 100%;
    }
    
    .glass-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.2);
        border: 1px solid rgba(255,255,255,0.5);
    }
    
    /* Premium Metric Cards */
    .metric-premium {
        background: linear-gradient(145deg, #ffffff, #f5f5f5);
        padding: 1.5rem;
        border-radius: 20px;
        box-shadow: 10px 10px 20px #d9d9d9, -10px -10px 20px #ffffff;
        text-align: center;
        transition: all 0.3s ease;
        border: 1px solid rgba(255,255,255,0.5);
    }
    
    .metric-premium:hover {
        transform: scale(1.05);
        box-shadow: 15px 15px 30px #d9d9d9, -15px -15px 30px #ffffff;
    }
    
    .metric-premium h3 {
        color: #2c3e50;
        font-size: 1rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.5rem;
    }
    
    .metric-premium .value {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(120deg, #1e3c72, #2a5298);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0.5rem 0;
    }
    
    .metric-premium .trend {
        font-size: 0.9rem;
        color: #27ae60;
        font-weight: 500;
    }
    
    /* Year Cards - Luxury Edition */
    .year-luxury {
        background: linear-gradient(145deg, #ffffff, #f8f9fa);
        border-radius: 20px;
        padding: 1.2rem;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.1), -5px -5px 15px rgba(255,255,255,0.8);
        text-align: center;
        transition: all 0.3s ease;
        border-left: 5px solid;
        margin-bottom: 1rem;
    }
    
    .year-luxury .year {
        font-size: 2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .year-luxury .phase {
        font-size: 1rem;
        font-weight: 600;
        color: #2c3e50;
        margin: 0.5rem 0;
    }
    
    .year-luxury .stats {
        font-size: 0.9rem;
        color: #666;
        background: rgba(102,126,234,0.1);
        padding: 0.5rem;
        border-radius: 10px;
        margin-top: 0.5rem;
    }
    
    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
        background: rgba(255,255,255,0.2);
        padding: 0.5rem;
        border-radius: 50px;
        backdrop-filter: blur(10px);
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 50px;
        padding: 0.8rem 2rem;
        font-weight: 600;
        color: #2c3e50;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea, #764ba2) !important;
        color: white !important;
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        border: none;
        padding: 0.8rem 2rem;
        border-radius: 50px;
        font-weight: 600;
        transition: all 0.3s ease;
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 30px rgba(102,126,234,0.4);
    }
    
    /* Data Editor Styling */
    .data-editor-section {
        background: linear-gradient(145deg, #ffffff, #f8f9fa);
        padding: 2rem;
        border-radius: 30px;
        box-shadow: inset 5px 5px 15px #d9d9d9, inset -5px -5px 15px #ffffff;
    }
    
    /* Divider */
    .premium-divider {
        height: 3px;
        background: linear-gradient(90deg, #667eea, #764ba2, #f093fb, #f5576c);
        margin: 2rem 0;
        border-radius: 3px;
    }
    
    /* Chart Container */
    .chart-container {
        background: white;
        padding: 1.5rem;
        border-radius: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    
    /* Success Message */
    .success-message {
        background: linear-gradient(135deg, #43e97b, #38f9d7);
        color: white;
        padding: 1rem;
        border-radius: 15px;
        text-align: center;
        font-weight: 600;
        animation: slideIn 0.5s ease;
    }
    
    @keyframes slideIn {
        from {
            transform: translateY(-20px);
            opacity: 0;
        }
        to {
            transform: translateY(0);
            opacity: 1;
        }
    }
</style>
""", unsafe_allow_html=True)

# ==================== DATA GENERATION ====================
@st.cache_data
def generate_banking_data():
    """Generate comprehensive banking data"""
    
    years = list(range(2013, 2024))
    
    # Public Sector Banks
    psb_data = {
        'Deposits': [42000, 46500, 52000, 56000, 59000, 60000, 64000, 71000, 80000, 89000, 102000],
        'Credit': [37000, 41000, 46000, 49000, 50000, 49000, 52000, 60000, 70000, 80000, 92000],
        'NPA': [3.1, 3.3, 3.5, 6.8, 8.5, 9.8, 9.2, 7.5, 5.2, 4.3, 3.6],
        'Profit': [5200, 5600, 5900, 3800, 2600, 1800, 3100, 5200, 6800, 8400, 9800]
    }
    
    # Private Sector Banks
    private_data = {
        'Deposits': [18000, 20000, 23000, 26000, 29000, 31000, 34000, 38000, 43000, 48000, 54000],
        'Credit': [16000, 18000, 20000, 22000, 24000, 26000, 28000, 32000, 37000, 42000, 47000],
        'NPA': [2.1, 2.2, 2.4, 3.8, 4.5, 5.2, 4.8, 3.9, 3.2, 2.8, 2.5],
        'Profit': [2800, 3100, 3400, 2900, 2600, 2300, 2800, 3400, 4000, 4700, 5400]
    }
    
    # Foreign Banks
    foreign_data = {
        'Deposits': [5000, 5500, 6000, 7000, 7000, 7000, 7000, 9000, 12000, 15000, 19000],
        'Credit': [5000, 5000, 6000, 7000, 8000, 8000, 9000, 10000, 13000, 16000, 19000],
        'NPA': [1.8, 1.9, 2.0, 2.5, 3.0, 3.2, 3.0, 2.5, 2.2, 2.0, 1.9],
        'Profit': [500, 500, 500, 500, 600, 400, 300, 300, 700, 1100, 1600]
    }
    
    # Overall totals
    df = pd.DataFrame({
        'Year': years,
        'PSB_Deposits': psb_data['Deposits'],
        'PSB_Credit': psb_data['Credit'],
        'PSB_NPA': psb_data['NPA'],
        'PSB_Profit': psb_data['Profit'],
        'Private_Deposits': private_data['Deposits'],
        'Private_Credit': private_data['Credit'],
        'Private_NPA': private_data['NPA'],
        'Private_Profit': private_data['Profit'],
        'Foreign_Deposits': foreign_data['Deposits'],
        'Foreign_Credit': foreign_data['Credit'],
        'Foreign_NPA': foreign_data['NPA'],
        'Foreign_Profit': foreign_data['Profit'],
        'Total_Deposits': [sum(x) for x in zip(psb_data['Deposits'], private_data['Deposits'], foreign_data['Deposits'])],
        'Total_Credit': [sum(x) for x in zip(psb_data['Credit'], private_data['Credit'], foreign_data['Credit'])],
        'Total_NPA': [round(sum(x)/3, 1) for x in zip(psb_data['NPA'], private_data['NPA'], foreign_data['NPA'])],
        'Total_Profit': [sum(x) for x in zip(psb_data['Profit'], private_data['Profit'], foreign_data['Profit'])],
        'GDP_Growth': [6.4, 7.4, 8.0, 7.1, 6.6, 6.5, 5.8, 4.2, 8.7, 7.2, 6.8]
    })
    
    return df

# Year phases with professional descriptions
YEAR_PHASES = {
    2013: {"phase": "Stability Phase", "desc": "Consistent growth with controlled NPAs", "color": "#27ae60"},
    2014: {"phase": "Expansion Era", "desc": "Credit growth accelerates", "color": "#2980b9"},
    2015: {"phase": "Peak Growth", "desc": "Highest GDP growth of the decade", "color": "#8e44ad"},
    2016: {"phase": "Stress Beginning", "desc": "NPA concerns emerge", "color": "#f39c12"},
    2017: {"phase": "Crisis Peak", "desc": "Maximum NPA pressure", "color": "#e67e22"},
    2018: {"phase": "Critical Year", "desc": "Asset quality review impact", "color": "#d35400"},
    2019: {"phase": "Reform Initiation", "desc": "PCA framework implementation", "color": "#c0392b"},
    2020: {"phase": "Pandemic Impact", "desc": "Moratorium and relief measures", "color": "#16a085"},
    2021: {"phase": "Digital Leap", "desc": "Accelerated digital adoption", "color": "#27ae60"},
    2022: {"phase": "Strong Recovery", "desc": "Profitability bounces back", "color": "#2980b9"},
    2023: {"phase": "Tech Integration", "desc": "Fintech collaboration peak", "color": "#8e44ad"}
}

# ==================== SESSION STATE ====================
if 'banking_data' not in st.session_state:
    st.session_state.banking_data = generate_banking_data()
if 'data_source' not in st.session_state:
    st.session_state.data_source = "Default Dataset"

# ==================== SIDEBAR ====================
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 2rem 1rem;">
        <div style="font-size: 4rem; margin-bottom: 1rem;">🏦</div>
        <h2 style="color: white; margin: 0;">BankSight Pro</h2>
        <p style="color: rgba(255,255,255,0.8);">Analytics Dashboard 2024</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Navigation (UPDATED with Year Comparison)
    page = st.radio(
        "📊 **Navigation**",
        ["🏠 Dashboard", 
         "📈 Trends & Charts", 
         "🏛️ Sector Analysis",
         "🔍 Year Comparison",      # <--- NEW PAGE
         "📝 Data Management"]
    )
    
    st.markdown("---")
    
    # Data Source Info
    st.info(f"📁 **Data Source:** {st.session_state.data_source}")
    
    # Year Filter
    years = st.session_state.banking_data['Year'].tolist()
    selected_years = st.select_slider(
        "📅 Select Year Range",
        options=years,
        value=(years[0], years[-1])
    )
    
    st.markdown("---")
    
    # About Section
    with st.expander("ℹ️ About"):
        st.markdown("""
        **Indian Banking Analytics**
        - Public Sector Banks
        - Private Sector Banks  
        - Foreign Banks
        
        *Data: 2013-2023*
        """)

# Filter data based on selected range
filtered_df = st.session_state.banking_data[
    (st.session_state.banking_data['Year'] >= selected_years[0]) & 
    (st.session_state.banking_data['Year'] <= selected_years[1])
]

# ==================== MAIN HEADER ====================
st.markdown("""
<div class="premium-header">
    <h1>🏦 Indian Banking Sector Analytics</h1>
    <p>Comprehensive Analysis • 2013-2023 • 3 Banking Sectors</p>
    <div style="display: flex; justify-content: center; gap: 2rem; margin-top: 1rem;">
        <span>📊 Public Sector</span>
        <span>📈 Private Sector</span>
        <span>🌍 Foreign Banks</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ==================== DASHBOARD PAGE ====================
if page == "🏠 Dashboard":
    
    # Key Metrics
    st.markdown("## 📊 Key Performance Indicators")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        latest_total_deposits = filtered_df['Total_Deposits'].iloc[-1]
        deposit_growth = ((filtered_df['Total_Deposits'].iloc[-1] / filtered_df['Total_Deposits'].iloc[0]) - 1) * 100
        st.markdown(f"""
        <div class="metric-premium">
            <h3>💰 Total Deposits</h3>
            <div class="value">₹{latest_total_deposits:,.0f} Cr</div>
            <div class="trend">↑ {deposit_growth:.1f}% since {selected_years[0]}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        latest_total_credit = filtered_df['Total_Credit'].iloc[-1]
        credit_growth = ((filtered_df['Total_Credit'].iloc[-1] / filtered_df['Total_Credit'].iloc[0]) - 1) * 100
        st.markdown(f"""
        <div class="metric-premium">
            <h3>💳 Total Credit</h3>
            <div class="value">₹{latest_total_credit:,.0f} Cr</div>
            <div class="trend">↑ {credit_growth:.1f}% growth</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        latest_npa = filtered_df['Total_NPA'].iloc[-1]
        npa_change = filtered_df['Total_NPA'].iloc[-1] - filtered_df['Total_NPA'].iloc[0]
        st.markdown(f"""
        <div class="metric-premium">
            <h3>⚠️ NPA Level</h3>
            <div class="value">{latest_npa:.1f}%</div>
            <div class="trend">{'↓' if npa_change < 0 else '↑'} {abs(npa_change):.1f}% change</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        latest_profit = filtered_df['Total_Profit'].iloc[-1]
        profit_growth = ((filtered_df['Total_Profit'].iloc[-1] / filtered_df['Total_Profit'].iloc[0]) - 1) * 100
        st.markdown(f"""
        <div class="metric-premium">
            <h3>📊 Net Profit</h3>
            <div class="value">₹{latest_profit:,.0f} Cr</div>
            <div class="trend">↑ {profit_growth:.1f}% return</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="premium-divider"></div>', unsafe_allow_html=True)
    
    # Year Cards
    st.markdown("## 📅 Year-by-Year Analysis")
    
    # Create year cards in rows of 3
    years_list = filtered_df['Year'].tolist()
    for i in range(0, len(years_list), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(years_list):
                year = years_list[i + j]
                year_data = filtered_df[filtered_df['Year'] == year].iloc[0]
                phase_info = YEAR_PHASES.get(year, {"phase": "Analysis Year", "desc": "Regular operations", "color": "#3498db"})
                
                with col:
                    st.markdown(f"""
                    <div class="year-luxury" style="border-left-color: {phase_info['color']};">
                        <div class="year">{year}</div>
                        <div class="phase">{phase_info['phase']}</div>
                        <div style="font-size: 0.9rem; color: {phase_info['color']};">{phase_info['desc']}</div>
                        <div class="stats">
                            <div>Deposits: ₹{year_data['Total_Deposits']:,.0f}Cr</div>
                            <div>Credit: ₹{year_data['Total_Credit']:,.0f}Cr</div>
                            <div>NPA: {year_data['Total_NPA']}% | Profit: ₹{year_data['Total_Profit']}Cr</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
    
    st.markdown('<div class="premium-divider"></div>', unsafe_allow_html=True)
    
    # Overview Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📈 Growth Trajectory")
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=filtered_df['Year'], 
            y=filtered_df['Total_Deposits'],
            name='Deposits',
            line=dict(color='#1e3c72', width=3),
            mode='lines+markers',
            marker=dict(size=8)
        ))
        
        fig.add_trace(go.Scatter(
            x=filtered_df['Year'], 
            y=filtered_df['Total_Credit'],
            name='Credit',
            line=dict(color='#2a5298', width=3),
            mode='lines+markers',
            marker=dict(size=8)
        ))
        
        fig.update_layout(
            title="Deposits vs Credit Over Time",
            xaxis_title="Year",
            yaxis_title="Amount (₹ Cr)",
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            height=400,
            hovermode='x unified'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 🥧 Sector Distribution (Latest Year)")
        latest_year = filtered_df['Year'].iloc[-1]
        latest_data = filtered_df[filtered_df['Year'] == latest_year].iloc[0]
        
        fig = go.Figure(data=[go.Pie(
            labels=['Public Sector', 'Private Sector', 'Foreign Banks'],
            values=[latest_data['PSB_Deposits'], latest_data['Private_Deposits'], latest_data['Foreign_Deposits']],
            hole=0.4,
            marker_colors=['#1e3c72', '#2a5298', '#3498db']
        )])
        
        fig.update_layout(
            title=f"Deposit Distribution - {latest_year}",
            height=400,
            showlegend=True,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig, use_container_width=True)

# ==================== TRENDS & CHARTS PAGE ====================
elif page == "📈 Trends & Charts":
    
    st.markdown("## 📊 Comprehensive Chart Analysis")
    
    # Chart type selector
    chart_type = st.selectbox(
        "Select Chart Type",
        ["Line Charts", "Bar Charts", "Pie Charts", "Scatter Plots", "Area Charts"]
    )
    
    if chart_type == "Line Charts":
        st.markdown("### 📈 Multi-Sector Line Chart")
        
        metric = st.selectbox(
            "Select Metric",
            ["Deposits", "Credit", "NPA", "Profit"]
        )
        
        fig = go.Figure()
        
        if metric == "Deposits":
            fig.add_trace(go.Scatter(x=filtered_df['Year'], y=filtered_df['PSB_Deposits'], 
                                    mode='lines+markers', name='Public Sector', line=dict(color='#1e3c72', width=3)))
            fig.add_trace(go.Scatter(x=filtered_df['Year'], y=filtered_df['Private_Deposits'], 
                                    mode='lines+markers', name='Private Sector', line=dict(color='#2a5298', width=3)))
            fig.add_trace(go.Scatter(x=filtered_df['Year'], y=filtered_df['Foreign_Deposits'], 
                                    mode='lines+markers', name='Foreign Banks', line=dict(color='#3498db', width=3)))
            y_title = "Deposits (₹ Cr)"
        elif metric == "Credit":
            fig.add_trace(go.Scatter(x=filtered_df['Year'], y=filtered_df['PSB_Credit'], 
                                    mode='lines+markers', name='Public Sector', line=dict(color='#1e3c72', width=3)))
            fig.add_trace(go.Scatter(x=filtered_df['Year'], y=filtered_df['Private_Credit'], 
                                    mode='lines+markers', name='Private Sector', line=dict(color='#2a5298', width=3)))
            fig.add_trace(go.Scatter(x=filtered_df['Year'], y=filtered_df['Foreign_Credit'], 
                                    mode='lines+markers', name='Foreign Banks', line=dict(color='#3498db', width=3)))
            y_title = "Credit (₹ Cr)"
        elif metric == "NPA":
            fig.add_trace(go.Scatter(x=filtered_df['Year'], y=filtered_df['PSB_NPA'], 
                                    mode='lines+markers', name='Public Sector', line=dict(color='#1e3c72', width=3)))
            fig.add_trace(go.Scatter(x=filtered_df['Year'], y=filtered_df['Private_NPA'], 
                                    mode='lines+markers', name='Private Sector', line=dict(color='#2a5298', width=3)))
            fig.add_trace(go.Scatter(x=filtered_df['Year'], y=filtered_df['Foreign_NPA'], 
                                    mode='lines+markers', name='Foreign Banks', line=dict(color='#3498db', width=3)))
            y_title = "NPA (%)"
        else:  # Profit
            fig.add_trace(go.Scatter(x=filtered_df['Year'], y=filtered_df['PSB_Profit'], 
                                    mode='lines+markers', name='Public Sector', line=dict(color='#1e3c72', width=3)))
            fig.add_trace(go.Scatter(x=filtered_df['Year'], y=filtered_df['Private_Profit'], 
                                    mode='lines+markers', name='Private Sector', line=dict(color='#2a5298', width=3)))
            fig.add_trace(go.Scatter(x=filtered_df['Year'], y=filtered_df['Foreign_Profit'], 
                                    mode='lines+markers', name='Foreign Banks', line=dict(color='#3498db', width=3)))
            y_title = "Profit (₹ Cr)"
        
        fig.update_layout(
            title=f"{metric} Comparison Across Sectors",
            xaxis_title="Year",
            yaxis_title=y_title,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            height=500,
            hovermode='x unified'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    elif chart_type == "Bar Charts":
        st.markdown("### 📊 Comparative Bar Charts")
        
        col1, col2 = st.columns(2)
        
        with col1:
            year_choice = st.selectbox("Select Year for Bar Chart", filtered_df['Year'])
            year_data = filtered_df[filtered_df['Year'] == year_choice].iloc[0]
            
            fig = go.Figure(data=[
                go.Bar(name='Public Sector', x=['Deposits', 'Credit', 'Profit'], 
                      y=[year_data['PSB_Deposits'], year_data['PSB_Credit'], year_data['PSB_Profit']],
                      marker_color='#1e3c72'),
                go.Bar(name='Private Sector', x=['Deposits', 'Credit', 'Profit'], 
                      y=[year_data['Private_Deposits'], year_data['Private_Credit'], year_data['Private_Profit']],
                      marker_color='#2a5298'),
                go.Bar(name='Foreign Banks', x=['Deposits', 'Credit', 'Profit'], 
                      y=[year_data['Foreign_Deposits'], year_data['Foreign_Credit'], year_data['Foreign_Profit']],
                      marker_color='#3498db')
            ])
            
            fig.update_layout(
                title=f"Sector Comparison - {year_choice}",
                barmode='group',
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                height=400
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            metric_bar = st.selectbox("Select Metric for Year Comparison", ["Deposits", "Credit", "Profit", "NPA"])
            
            if metric_bar == "Deposits":
                fig = go.Figure(data=[
                    go.Bar(name='Public', x=filtered_df['Year'], y=filtered_df['PSB_Deposits'], marker_color='#1e3c72'),
                    go.Bar(name='Private', x=filtered_df['Year'], y=filtered_df['Private_Deposits'], marker_color='#2a5298'),
                    go.Bar(name='Foreign', x=filtered_df['Year'], y=filtered_df['Foreign_Deposits'], marker_color='#3498db')
                ])
                y_title = "Deposits (₹ Cr)"
            elif metric_bar == "Credit":
                fig = go.Figure(data=[
                    go.Bar(name='Public', x=filtered_df['Year'], y=filtered_df['PSB_Credit'], marker_color='#1e3c72'),
                    go.Bar(name='Private', x=filtered_df['Year'], y=filtered_df['Private_Credit'], marker_color='#2a5298'),
                    go.Bar(name='Foreign', x=filtered_df['Year'], y=filtered_df['Foreign_Credit'], marker_color='#3498db')
                ])
                y_title = "Credit (₹ Cr)"
            elif metric_bar == "Profit":
                fig = go.Figure(data=[
                    go.Bar(name='Public', x=filtered_df['Year'], y=filtered_df['PSB_Profit'], marker_color='#1e3c72'),
                    go.Bar(name='Private', x=filtered_df['Year'], y=filtered_df['Private_Profit'], marker_color='#2a5298'),
                    go.Bar(name='Foreign', x=filtered_df['Year'], y=filtered_df['Foreign_Profit'], marker_color='#3498db')
                ])
                y_title = "Profit (₹ Cr)"
            else:  # NPA
                fig = go.Figure(data=[
                    go.Bar(name='Public', x=filtered_df['Year'], y=filtered_df['PSB_NPA'], marker_color='#1e3c72'),
                    go.Bar(name='Private', x=filtered_df['Year'], y=filtered_df['Private_NPA'], marker_color='#2a5298'),
                    go.Bar(name='Foreign', x=filtered_df['Year'], y=filtered_df['Foreign_NPA'], marker_color='#3498db')
                ])
                y_title = "NPA (%)"
            
            fig.update_layout(
                title=f"{metric_bar} - Yearly Comparison",
                barmode='group',
                xaxis_title="Year",
                yaxis_title=y_title,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                height=400
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    elif chart_type == "Pie Charts":
        st.markdown("### 🥧 Distribution Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            year_pie = st.selectbox("Select Year", filtered_df['Year'], key="pie_year")
            metric_pie = st.selectbox("Select Metric", ["Deposits", "Credit", "Profit"], key="pie_metric")
            
            year_data = filtered_df[filtered_df['Year'] == year_pie].iloc[0]
            
            if metric_pie == "Deposits":
                values = [year_data['PSB_Deposits'], year_data['Private_Deposits'], year_data['Foreign_Deposits']]
            elif metric_pie == "Credit":
                values = [year_data['PSB_Credit'], year_data['Private_Credit'], year_data['Foreign_Credit']]
            else:
                values = [year_data['PSB_Profit'], year_data['Private_Profit'], year_data['Foreign_Profit']]
            
            fig = go.Figure(data=[go.Pie(
                labels=['Public Sector', 'Private Sector', 'Foreign Banks'],
                values=values,
                hole=0.3,
                marker_colors=['#1e3c72', '#2a5298', '#3498db']
            )])
            
            fig.update_layout(
                title=f"{metric_pie} Distribution - {year_pie}",
                height=400,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)'
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("### 📊 NPA Distribution")
            
            fig = go.Figure()
            
            for year in filtered_df['Year'].iloc[-3:]:
                year_data = filtered_df[filtered_df['Year'] == year].iloc[0]
                fig.add_trace(go.Pie(
                    labels=['Public', 'Private', 'Foreign'],
                    values=[year_data['PSB_NPA'], year_data['Private_NPA'], year_data['Foreign_NPA']],
                    name=str(year),
                    domain=dict(row=0, col=len(fig.data))
                ))
            
            fig.update_layout(
                title="NPA Comparison - Last 3 Years",
                grid=dict(rows=1, columns=3),
                height=400,
                showlegend=True,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)'
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    elif chart_type == "Scatter Plots":
        st.markdown("### 🔍 Correlation Scatter Plots")
        
        col1, col2 = st.columns(2)
        
        with col1:
            x_axis = st.selectbox("X-Axis", ["NPA", "GDP_Growth", "Deposits", "Credit"], key="x")
            y_axis = st.selectbox("Y-Axis", ["Profit", "Credit", "Deposits", "NPA"], key="y")
            
            if x_axis == "NPA":
                x_data = filtered_df['Total_NPA']
            elif x_axis == "GDP_Growth":
                x_data = filtered_df['GDP_Growth']
            elif x_axis == "Deposits":
                x_data = filtered_df['Total_Deposits']
            else:
                x_data = filtered_df['Total_Credit']
            
            if y_axis == "Profit":
                y_data = filtered_df['Total_Profit']
            elif y_axis == "Credit":
                y_data = filtered_df['Total_Credit']
            elif y_axis == "Deposits":
                y_data = filtered_df['Total_Deposits']
            else:
                y_data = filtered_df['Total_NPA']
            
            fig = px.scatter(
                filtered_df, x=x_data, y=y_data,
                text='Year', size='Total_Profit',
                color='Year',
                title=f"{x_axis} vs {y_axis} Correlation",
                labels={'x': x_axis, 'y': y_axis}
            )
            
            fig.update_traces(textposition='top center')
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                height=500
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("### 📈 Correlation Matrix")
            
            corr_data = filtered_df[['Total_NPA', 'GDP_Growth', 'Total_Profit', 'Total_Deposits', 'Total_Credit']].corr()
            
            fig = px.imshow(
                corr_data,
                text_auto='.2f',
                aspect="auto",
                color_continuous_scale='RdBu_r',
                title="Correlation Matrix"
            )
            
            fig.update_layout(
                height=500,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)'
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    else:  # Area Charts
        st.markdown("### 📊 Area Charts - Cumulative View")
        
        metric_area = st.selectbox("Select Metric", ["Deposits", "Credit", "Profit"])
        
        fig = go.Figure()
        
        if metric_area == "Deposits":
            fig.add_trace(go.Scatter(
                x=filtered_df['Year'], y=filtered_df['PSB_Deposits'],
                fill='tozeroy', name='Public Sector',
                line=dict(color='#1e3c72', width=2)
            ))
            fig.add_trace(go.Scatter(
                x=filtered_df['Year'], y=filtered_df['Private_Deposits'],
                fill='tonexty', name='Private Sector',
                line=dict(color='#2a5298', width=2)
            ))
            fig.add_trace(go.Scatter(
                x=filtered_df['Year'], y=filtered_df['Foreign_Deposits'],
                fill='tonexty', name='Foreign Banks',
                line=dict(color='#3498db', width=2)
            ))
        elif metric_area == "Credit":
            fig.add_trace(go.Scatter(
                x=filtered_df['Year'], y=filtered_df['PSB_Credit'],
                fill='tozeroy', name='Public Sector',
                line=dict(color='#1e3c72', width=2)
            ))
            fig.add_trace(go.Scatter(
                x=filtered_df['Year'], y=filtered_df['Private_Credit'],
                fill='tonexty', name='Private Sector',
                line=dict(color='#2a5298', width=2)
            ))
            fig.add_trace(go.Scatter(
                x=filtered_df['Year'], y=filtered_df['Foreign_Credit'],
                fill='tonexty', name='Foreign Banks',
                line=dict(color='#3498db', width=2)
            ))
        else:
            fig.add_trace(go.Scatter(
                x=filtered_df['Year'], y=filtered_df['PSB_Profit'],
                fill='tozeroy', name='Public Sector',
                line=dict(color='#1e3c72', width=2)
            ))
            fig.add_trace(go.Scatter(
                x=filtered_df['Year'], y=filtered_df['Private_Profit'],
                fill='tonexty', name='Private Sector',
                line=dict(color='#2a5298', width=2)
            ))
            fig.add_trace(go.Scatter(
                x=filtered_df['Year'], y=filtered_df['Foreign_Profit'],
                fill='tonexty', name='Foreign Banks',
                line=dict(color='#3498db', width=2)
            ))
        
        fig.update_layout(
            title=f"{metric_area} - Area Chart",
            xaxis_title="Year",
            yaxis_title=f"{metric_area} (₹ Cr)",
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            height=500,
            hovermode='x unified'
        )
        
        st.plotly_chart(fig, use_container_width=True)

# ==================== SECTOR ANALYSIS PAGE ====================
elif page == "🏛️ Sector Analysis":
    
    st.markdown("## 🏦 Sector-wise Deep Dive")
    
    sector = st.selectbox(
        "Select Sector for Analysis",
        ["Public Sector Banks", "Private Sector Banks", "Foreign Banks"]
    )
    
    col1, col2, col3 = st.columns(3)
    
    if sector == "Public Sector Banks":
        prefix = "PSB"
        color = "#1e3c72"
    elif sector == "Private Sector Banks":
        prefix = "Private"
        color = "#2a5298"
    else:
        prefix = "Foreign"
        color = "#3498db"
    
    with col1:
        latest_deposits = filtered_df[f'{prefix}_Deposits'].iloc[-1]
        deposit_growth = ((filtered_df[f'{prefix}_Deposits'].iloc[-1] / filtered_df[f'{prefix}_Deposits'].iloc[0]) - 1) * 100
        st.markdown(f"""
        <div class="metric-premium">
            <h3>💰 Total Deposits</h3>
            <div class="value">₹{latest_deposits:,.0f} Cr</div>
            <div class="trend">↑ {deposit_growth:.1f}% growth</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        latest_credit = filtered_df[f'{prefix}_Credit'].iloc[-1]
        credit_growth = ((filtered_df[f'{prefix}_Credit'].iloc[-1] / filtered_df[f'{prefix}_Credit'].iloc[0]) - 1) * 100
        st.markdown(f"""
        <div class="metric-premium">
            <h3>💳 Total Credit</h3>
            <div class="value">₹{latest_credit:,.0f} Cr</div>
            <div class="trend">↑ {credit_growth:.1f}% growth</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        latest_npa = filtered_df[f'{prefix}_NPA'].iloc[-1]
        npa_change = filtered_df[f'{prefix}_NPA'].iloc[-1] - filtered_df[f'{prefix}_NPA'].iloc[0]
        st.markdown(f"""
        <div class="metric-premium">
            <h3>⚠️ NPA Level</h3>
            <div class="value">{latest_npa:.1f}%</div>
            <div class="trend">{'↓' if npa_change < 0 else '↑'} {abs(npa_change):.1f}% change</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="premium-divider"></div>', unsafe_allow_html=True)
    
    # Sector Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"### 📈 {sector} - Key Metrics")
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=filtered_df['Year'], y=filtered_df[f'{prefix}_Deposits'],
            name='Deposits', mode='lines+markers',
            line=dict(color=color, width=3)
        ))
        
        fig.add_trace(go.Scatter(
            x=filtered_df['Year'], y=filtered_df[f'{prefix}_Credit'],
            name='Credit', mode='lines+markers',
            line=dict(color='#e67e22', width=3)
        ))
        
        fig.add_trace(go.Scatter(
            x=filtered_df['Year'], y=filtered_df[f'{prefix}_Profit'],
            name='Profit', mode='lines+markers',
            line=dict(color='#27ae60', width=3)
        ))
        
        fig.update_layout(
            title="Performance Trends",
            xaxis_title="Year",
            yaxis_title="Amount (₹ Cr)",
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            height=400,
            hovermode='x unified'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown(f"### 📊 {sector} - NPA Analysis")
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=filtered_df['Year'], y=filtered_df[f'{prefix}_NPA'],
            name='NPA %',
            marker_color=color,
            marker_line_color='#2c3e50',
            marker_line_width=1.5,
            opacity=0.8
        ))
        
        fig.add_hline(y=filtered_df[f'{prefix}_NPA'].mean(), 
                     line_dash="dash", 
                     line_color="red",
                     annotation_text=f"Avg: {filtered_df[f'{prefix}_NPA'].mean():.2f}%")
        
        fig.update_layout(
            title="NPA Trend",
            xaxis_title="Year",
            yaxis_title="NPA (%)",
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Market Share Chart
    st.markdown(f"### 🥧 {sector} - Market Share Analysis")
    
    latest_year = filtered_df['Year'].iloc[-1]
    latest_data = filtered_df[filtered_df['Year'] == latest_year].iloc[0]
    
    col1, col2 = st.columns(2)
    
    with col1:
        deposit_share = (latest_data[f'{prefix}_Deposits'] / latest_data['Total_Deposits']) * 100
        credit_share = (latest_data[f'{prefix}_Credit'] / latest_data['Total_Credit']) * 100
        profit_share = (latest_data[f'{prefix}_Profit'] / latest_data['Total_Profit']) * 100
        
        fig = go.Figure(data=[go.Pie(
            labels=['Deposits', 'Credit', 'Profit'],
            values=[deposit_share, credit_share, profit_share],
            hole=0.3,
            marker_colors=[color, '#e67e22', '#27ae60']
        )])
        
        fig.update_layout(
            title=f"Share Distribution - {latest_year}",
            height=400,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Market share over time
        share_over_time = pd.DataFrame({
            'Year': filtered_df['Year'],
            'Deposit_Share': (filtered_df[f'{prefix}_Deposits'] / filtered_df['Total_Deposits']) * 100,
            'Credit_Share': (filtered_df[f'{prefix}_Credit'] / filtered_df['Total_Credit']) * 100,
            'Profit_Share': (filtered_df[f'{prefix}_Profit'] / filtered_df['Total_Profit']) * 100
        })
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=share_over_time['Year'], y=share_over_time['Deposit_Share'],
            name='Deposit Share', mode='lines+markers',
            line=dict(color=color, width=3)
        ))
        
        fig.add_trace(go.Scatter(
            x=share_over_time['Year'], y=share_over_time['Credit_Share'],
            name='Credit Share', mode='lines+markers',
            line=dict(color='#e67e22', width=3)
        ))
        
        fig.add_trace(go.Scatter(
            x=share_over_time['Year'], y=share_over_time['Profit_Share'],
            name='Profit Share', mode='lines+markers',
            line=dict(color='#27ae60', width=3)
        ))
        
        fig.update_layout(
            title="Market Share Evolution",
            xaxis_title="Year",
            yaxis_title="Share (%)",
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            height=400,
            hovermode='x unified'
        )
        
        st.plotly_chart(fig, use_container_width=True)

# ==================== YEAR COMPARISON PAGE (NEW) ====================
elif page == "🔍 Year Comparison":
    
    st.markdown("## 🔍 Compare Multiple Years")
    st.markdown("Select 2 or 3 years to compare all banking parameters side by side.")
    
    # Use full dataset, not filtered
    full_data = st.session_state.banking_data
    available_years = full_data['Year'].tolist()
    
    selected_compare_years = st.multiselect(
        "Choose years to compare (2 or 3)",
        options=available_years,
        default=[available_years[0], available_years[-1]] if len(available_years) >= 2 else available_years,
        max_selections=3
    )
    
    if len(selected_compare_years) < 2:
        st.warning("Please select at least 2 years to compare.")
    else:
        compare_df = full_data[full_data['Year'].isin(selected_compare_years)].copy().sort_values('Year')
        
        st.markdown("### 📋 Comparison Table")
        
        metrics_to_show = [
            'PSB_Deposits', 'PSB_Credit', 'PSB_NPA', 'PSB_Profit',
            'Private_Deposits', 'Private_Credit', 'Private_NPA', 'Private_Profit',
            'Foreign_Deposits', 'Foreign_Credit', 'Foreign_NPA', 'Foreign_Profit',
            'Total_Deposits', 'Total_Credit', 'Total_NPA', 'Total_Profit',
            'GDP_Growth'
        ]
        
        comparison_data = []
        for metric in metrics_to_show:
            row = {'Metric': metric.replace('_', ' ')}
            for year in selected_compare_years:
                value = compare_df[compare_df['Year'] == year][metric].values[0]
                if 'NPA' in metric or metric == 'GDP_Growth':
                    row[f'{year}'] = f"{value:.2f}%"
                else:
                    row[f'{year}'] = f"₹{value:,.0f} Cr"
            comparison_data.append(row)
        
        comparison_df = pd.DataFrame(comparison_data)
        st.dataframe(comparison_df, use_container_width=True, hide_index=True)
        
        st.markdown("### 📊 Visual Comparison")
        viz_metric = st.selectbox(
            "Select metric to visualize",
            options=metrics_to_show,
            format_func=lambda x: x.replace('_', ' ') + (' (%)' if 'NPA' in x or x=='GDP_Growth' else ' (₹ Cr)')
        )
        
        viz_data = []
        for year in selected_compare_years:
            value = compare_df[compare_df['Year'] == year][viz_metric].values[0]
            viz_data.append({'Year': year, 'Value': value})
        viz_df = pd.DataFrame(viz_data)
        
        fig = px.bar(viz_df, x='Year', y='Value', title=f"{viz_metric.replace('_', ' ')} Comparison",
                     text_auto='.2s', color='Year', color_discrete_sequence=px.colors.qualitative.Set2)
        fig.update_layout(xaxis_title="Year", yaxis_title="Value" + (" (%)" if 'NPA' in viz_metric or viz_metric=='GDP_Growth' else " (₹ Cr)"),
                          plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', height=500, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
        
        if len(selected_compare_years) == 2:
            st.markdown("### 📈 Percentage Change")
            year1, year2 = selected_compare_years[0], selected_compare_years[1]
            change_data = []
            for metric in metrics_to_show:
                val1 = compare_df[compare_df['Year'] == year1][metric].values[0]
                val2 = compare_df[compare_df['Year'] == year2][metric].values[0]
                if val1 != 0:
                    pct_change = ((val2 - val1) / val1) * 100
                else:
                    pct_change = np.nan
                change_data.append({
                    'Metric': metric.replace('_', ' '),
                    f'{year1} to {year2} Change (%)': f"{pct_change:+.2f}%" if not np.isnan(pct_change) else "N/A"
                })
            change_df = pd.DataFrame(change_data)
            st.dataframe(change_df, use_container_width=True, hide_index=True)
            
            fig_change = px.bar(change_df, x='Metric', y=f'{year1} to {year2} Change (%)',
                                title=f"Percentage Change from {year1} to {year2}",
                                color=f'{year1} to {year2} Change (%)', color_continuous_scale='RdYlGn',
                                text_auto='.2f')
            fig_change.update_layout(xaxis_tickangle=-45, plot_bgcolor='rgba(0,0,0,0)',
                                      paper_bgcolor='rgba(0,0,0,0)', height=500)
            st.plotly_chart(fig_change, use_container_width=True)
        
        elif len(selected_compare_years) == 3:
            st.markdown("### 📈 Trend Across Selected Years")
            multi_metrics = st.multiselect(
                "Select metrics to plot",
                options=metrics_to_show,
                default=['Total_Deposits', 'Total_Credit', 'Total_Profit'],
                format_func=lambda x: x.replace('_', ' ') + (' (%)' if 'NPA' in x or x=='GDP_Growth' else ' (₹ Cr)')
            )
            if multi_metrics:
                trend_data = []
                for metric in multi_metrics:
                    for year in selected_compare_years:
                        value = compare_df[compare_df['Year'] == year][metric].values[0]
                        trend_data.append({
                            'Year': year,
                            'Metric': metric.replace('_', ' '),
                            'Value': value
                        })
                trend_df = pd.DataFrame(trend_data)
                fig_trend = px.line(trend_df, x='Year', y='Value', color='Metric', markers=True,
                                    title="Trend Comparison", color_discrete_sequence=px.colors.qualitative.Set1)
                fig_trend.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', height=500)
                st.plotly_chart(fig_trend, use_container_width=True)
        
        st.markdown("### 🥧 Sector Distribution by Year")
        cols = st.columns(len(selected_compare_years))
        for i, year in enumerate(selected_compare_years):
            year_data = compare_df[compare_df['Year'] == year].iloc[0]
            with cols[i]:
                fig_pie = go.Figure(data=[go.Pie(
                    labels=['Public', 'Private', 'Foreign'],
                    values=[year_data['PSB_Deposits'], year_data['Private_Deposits'], year_data['Foreign_Deposits']],
                    hole=0.4, marker_colors=['#1e3c72', '#2a5298', '#3498db']
                )])
                fig_pie.update_layout(title=f"Deposit Distribution - {year}", height=300,
                                      plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
                st.plotly_chart(fig_pie, use_container_width=True)

# ==================== DATA MANAGEMENT PAGE ====================
elif page == "📝 Data Management":
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #1e3c72, #2a5298); padding: 2rem; border-radius: 30px; color: white; text-align: center; margin-bottom: 2rem;">
        <h2>📊 Data Management Console</h2>
        <p>View, edit, and analyze banking sector data</p>
    </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["📋 View Data", "✏️ Edit Data", "📤 Upload/Download"])
    
    with tab1:
        st.markdown("### 📋 Banking Sector Dataset (2013-2023)")
        display_df = filtered_df.copy()
        st.dataframe(
            display_df,
            use_container_width=True,
            height=400,
            column_config={
                "Year": st.column_config.NumberColumn("Year", format="%d"),
                "PSB_Deposits": st.column_config.NumberColumn("PSB Deposits", format="₹%d Cr"),
                "PSB_Credit": st.column_config.NumberColumn("PSB Credit", format="₹%d Cr"),
                "PSB_NPA": st.column_config.NumberColumn("PSB NPA", format="%.2f%%"),
                "PSB_Profit": st.column_config.NumberColumn("PSB Profit", format="₹%d Cr"),
                "Private_Deposits": st.column_config.NumberColumn("Private Deposits", format="₹%d Cr"),
                "Private_Credit": st.column_config.NumberColumn("Private Credit", format="₹%d Cr"),
                "Private_NPA": st.column_config.NumberColumn("Private NPA", format="%.2f%%"),
                "Private_Profit": st.column_config.NumberColumn("Private Profit", format="₹%d Cr"),
                "Foreign_Deposits": st.column_config.NumberColumn("Foreign Deposits", format="₹%d Cr"),
                "Foreign_Credit": st.column_config.NumberColumn("Foreign Credit", format="₹%d Cr"),
                "Foreign_NPA": st.column_config.NumberColumn("Foreign NPA", format="%.2f%%"),
                "Foreign_Profit": st.column_config.NumberColumn("Foreign Profit", format="₹%d Cr"),
                "Total_Deposits": st.column_config.NumberColumn("Total Deposits", format="₹%d Cr"),
                "Total_Credit": st.column_config.NumberColumn("Total Credit", format="₹%d Cr"),
                "Total_NPA": st.column_config.NumberColumn("Total NPA", format="%.2f%%"),
                "Total_Profit": st.column_config.NumberColumn("Total Profit", format="₹%d Cr"),
                "GDP_Growth": st.column_config.NumberColumn("GDP Growth", format="%.1f%%")
            }
        )
        
        st.markdown("### 📊 Quick Statistics")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Records", len(filtered_df))
        with col2:
            st.metric("Date Range", f"{filtered_df['Year'].min()} - {filtered_df['Year'].max()}")
        with col3:
            st.metric("Avg NPA", f"{filtered_df['Total_NPA'].mean():.2f}%")
        with col4:
            st.metric("Avg GDP Growth", f"{filtered_df['GDP_Growth'].mean():.1f}%")
    
    with tab2:
        st.markdown("### ✏️ Edit Dataset")
        st.markdown("*Make changes directly in the table below*")
        
        edited_df = st.data_editor(
            filtered_df,
            use_container_width=True,
            height=500,
            num_rows="dynamic",
            column_config={
                "Year": st.column_config.NumberColumn("Year", required=True, min_value=2000, max_value=2030),
                "PSB_Deposits": st.column_config.NumberColumn("PSB Deposits", required=True, min_value=0, format="₹%d Cr"),
                "PSB_Credit": st.column_config.NumberColumn("PSB Credit", required=True, min_value=0, format="₹%d Cr"),
                "PSB_NPA": st.column_config.NumberColumn("PSB NPA", required=True, min_value=0, max_value=20, format="%.2f%%"),
                "PSB_Profit": st.column_config.NumberColumn("PSB Profit", required=True, format="₹%d Cr"),
                "Private_Deposits": st.column_config.NumberColumn("Private Deposits", required=True, min_value=0, format="₹%d Cr"),
                "Private_Credit": st.column_config.NumberColumn("Private Credit", required=True, min_value=0, format="₹%d Cr"),
                "Private_NPA": st.column_config.NumberColumn("Private NPA", required=True, min_value=0, max_value=20, format="%.2f%%"),
                "Private_Profit": st.column_config.NumberColumn("Private Profit", required=True, format="₹%d Cr"),
                "Foreign_Deposits": st.column_config.NumberColumn("Foreign Deposits", required=True, min_value=0, format="₹%d Cr"),
                "Foreign_Credit": st.column_config.NumberColumn("Foreign Credit", required=True, min_value=0, format="₹%d Cr"),
                "Foreign_NPA": st.column_config.NumberColumn("Foreign NPA", required=True, min_value=0, max_value=20, format="%.2f%%"),
                "Foreign_Profit": st.column_config.NumberColumn("Foreign Profit", required=True, format="₹%d Cr"),
                "Total_Deposits": st.column_config.NumberColumn("Total Deposits", disabled=True),
                "Total_Credit": st.column_config.NumberColumn("Total Credit", disabled=True),
                "Total_NPA": st.column_config.NumberColumn("Total NPA", disabled=True),
                "Total_Profit": st.column_config.NumberColumn("Total Profit", disabled=True),
                "GDP_Growth": st.column_config.NumberColumn("GDP Growth", required=True, min_value=-10, max_value=20, format="%.1f%%")
            }
        )
        
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("💾 Save Changes", use_container_width=True):
                edited_df['Total_Deposits'] = edited_df['PSB_Deposits'] + edited_df['Private_Deposits'] + edited_df['Foreign_Deposits']
                edited_df['Total_Credit'] = edited_df['PSB_Credit'] + edited_df['Private_Credit'] + edited_df['Foreign_Credit']
                edited_df['Total_NPA'] = (edited_df['PSB_NPA'] + edited_df['Private_NPA'] + edited_df['Foreign_NPA']) / 3
                edited_df['Total_Profit'] = edited_df['PSB_Profit'] + edited_df['Private_Profit'] + edited_df['Foreign_Profit']
                st.session_state.banking_data = edited_df
                st.session_state.data_source = "User Modified Data"
                st.success("✅ Changes saved successfully!")
                money_rain()
        with col2:
            if st.button("🔄 Reset to Default", use_container_width=True):
                st.session_state.banking_data = generate_banking_data()
                st.session_state.data_source = "Default Dataset"
                st.success("✅ Reset to default data!")
                st.rerun()
        with col3:
            if st.button("📥 Download Current Data", use_container_width=True):
                csv = edited_df.to_csv(index=False)
                st.download_button(
                    label="Click to Download CSV",
                    data=csv,
                    file_name=f"banking_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv"
                )
    
    with tab3:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 📤 Upload New Data")
            st.markdown("Upload CSV file with same column structure")
            uploaded_file = st.file_uploader(
                "Choose a CSV file",
                type=['csv'],
                help="File must contain all required columns"
            )
            if uploaded_file is not None:
                try:
                    new_data = pd.read_csv(uploaded_file)
                    required_cols = ['Year', 'PSB_Deposits', 'PSB_Credit', 'PSB_NPA', 'PSB_Profit',
                                     'Private_Deposits', 'Private_Credit', 'Private_NPA', 'Private_Profit',
                                     'Foreign_Deposits', 'Foreign_Credit', 'Foreign_NPA', 'Foreign_Profit',
                                     'GDP_Growth']
                    if all(col in new_data.columns for col in required_cols):
                        st.success("✅ File uploaded successfully!")
                        if st.button("Process Uploaded Data"):
                            new_data['Total_Deposits'] = new_data['PSB_Deposits'] + new_data['Private_Deposits'] + new_data['Foreign_Deposits']
                            new_data['Total_Credit'] = new_data['PSB_Credit'] + new_data['Private_Credit'] + new_data['Foreign_Credit']
                            new_data['Total_NPA'] = (new_data['PSB_NPA'] + new_data['Private_NPA'] + new_data['Foreign_NPA']) / 3
                            new_data['Total_Profit'] = new_data['PSB_Profit'] + new_data['Private_Profit'] + new_data['Foreign_Profit']
                            st.session_state.banking_data = new_data
                            st.session_state.data_source = "Uploaded Dataset"
                            st.success("✅ Data processed and loaded!")
                            st.rerun()
                    else:
                        st.error("❌ Invalid file format. Please check column names.")
                except Exception as e:
                    st.error(f"❌ Error reading file: {str(e)}")
        
        with col2:
            st.markdown("### 📊 Data Export Options")
            st.markdown("Download data in different formats")
            export_format = st.selectbox("Select Format", ["CSV", "Excel", "JSON"])
            if st.button("Generate Export"):
                if export_format == "CSV":
                    csv = filtered_df.to_csv(index=False)
                    st.download_button(
                        "Download CSV",
                        data=csv,
                        file_name=f"banking_data_{datetime.now().strftime('%Y%m%d')}.csv",
                        mime="text/csv"
                    )
                elif export_format == "Excel":
                    output = pd.ExcelWriter('temp.xlsx', engine='xlsxwriter')
                    filtered_df.to_excel(output, index=False, sheet_name='Banking Data')
                    output.close()
                    with open('temp.xlsx', 'rb') as f:
                        st.download_button(
                            "Download Excel",
                            data=f,
                            file_name=f"banking_data_{datetime.now().strftime('%Y%m%d')}.xlsx",
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                        )
                else:  # JSON
                    json_str = filtered_df.to_json(orient='records', indent=2)
                    st.download_button(
                        "Download JSON",
                        data=json_str,
                        file_name=f"banking_data_{datetime.now().strftime('%Y%m%d')}.json",
                        mime="application/json"
                    )

# ==================== FOOTER ====================
st.markdown("---")
st.markdown("""
<div style="background: linear-gradient(135deg, #1e3c72, #2a5298); padding: 1.5rem; border-radius: 20px; color: white; text-align: center;">
    <p style="margin: 0; font-size: 1.1rem;">🏦 Indian Banking Sector Analytics Project 2024</p>
    <p style="margin: 0.5rem 0 0 0; opacity: 0.8; font-size: 0.9rem;">Data-driven insights for informed decision making</p>
    <p style="margin: 0.5rem 0 0 0; opacity: 0.6; font-size: 0.8rem;">Public Sector | Private Sector | Foreign Banks</p>
</div>
""", unsafe_allow_html=True)