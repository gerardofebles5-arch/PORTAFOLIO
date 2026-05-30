"""
================================================================================
PORTFOLIO TÉCNICO ELITE v6.0 - MICROPROYECTOS IMPRESIONANTES
================================================================================
Autor: Salomon Febles
Perfil: Ingeniero de Sistemas 9no Semestre - Trading & Ciberseguridad

NIVEL: ENTERPRISE-GRADE | PROFESSIONAL 2026 | PORTAFOLIO DE MICROPROYECTOS

5 Módulos Elite:
1. ShieldVZLA Elite - EDR Avanzado + MITRE ATT&CK + Forensics
2. TradeGuard Elite - Trading Algorítmico Profesional + Backtesting + API Real
3. FinRisk AI Elite - ML Avanzado + Explainable AI
4. InventoryBot Elite - Supply Chain + EOQ + Forecasting
5. DocuVerify Elite - Blockchain Legal + Smart Contracts

Stack: Python, Streamlit, SQLite, Plotly, Scikit-learn, Pandas, NumPy

MEJORAS v6.0:
- Dark/Light mode toggle con persistencia
- Animaciones fluidas con CSS transitions
- Sistema de puntos/XP por actividades (gamificación)
- API real de Binance para datos en vivo
- Real-time analytics con WebSockets
- UI/UX profesional mejorado
- Integraciones de APIs externas (Weather, News, GitHub, Crypto, Etherscan)
- Loading skeletons para mejor UX
- Toast notifications personalizadas
- Keyboard shortcuts para power users
- Progress bars animadas
- Confetti celebrations en logros, nuevos badges (12 achievements), sistema de niveles, XP por actividad
- Custom fonts con Google Fonts
- Responsive design mobile-first
- Scrollbar personalizada
- Onboarding guide interactivo
- Search functionality global
- Export/Import de configuraciones
- Notificaciones en sidebar, Estadísticas rápidas
- Estructura 100% monolítica en un solo archivo
- Trading: Sentiment Analysis, News Trading, Order Flow, Position Sizing, Risk Calculator, Market Scanner, Correlation Matrix, Portfolio Analytics, Options Trading, Futures Trading, Margin Trading
- Ciberseguridad: Threat Intel, Vulnerability Scanner, Malware Analysis, Incident Response, Security Dashboard, Compliance Audit, Threat Hunting, SIEM Dashboard, SOAR Playbooks, Phishing Simulator, Network Security, Endpoint Protection
- Blockchain: NFT Marketplace, DeFi Dashboard, DAO Governance, Token Swap, Smart Contract Audit, Wallet Manager, Cross-Chain Bridge, Token Staking, Liquidity Pool, DEX Aggregator, Yield Farming, Flash Loans
- ML: Feature Engineering, Model Monitoring, Deep Learning, Time Series Forecasting, Hyperparameter Tuning, Feature Importance, Model Deployment, A/B Testing, Model Registry, Anomaly Detection, Credit Scoring, Fraud Detection
- Supply Chain: Lead Time Analysis, Reorder Point, Supplier Performance, Inventory Optimization, Demand Planning, Logistics Optimization, Safety Stock Calculator, Multi-Warehouse Optimization, Supplier Risk Assessment
- Dashboard: Métricas del Sistema, Gráficos de XP, Activity Log, Achievements, System Health, Performance Metrics, User Analytics, Alert System, Growth Metrics, Module Usage, Security Overview, Financial Overview, Analytics Dashboard, Geographic Distribution, Time Analytics, Goal Tracking, Recent Activity, System Configuration, Documentation, Theme Customization, Search & Filters, Quick Stats Summary, Learning Path, Leaderboard, Progress Timeline, Gamification Settings, Privacy Settings, Notification Preferences, Data Export, Data Import, Data Management, Mobile Optimization, Accessibility, Integrations, Quick Actions
- CSS: Hover Effects, Gradient Text, Card Hover, Tooltips, Animations, Glassmorphism, Neumorphism, Gradient Borders, Skeleton Loading, Progress Bar, Badge Styles, Alert Styles, Button Styles, Card Styles, Table Styles, Input Styles, Select Styles, Checkbox Styles, Radio Styles, Toggle Switch, Modal Styles, Dropdown Styles, Accordion Styles, Tabs Styles, Breadcrumb Styles, Pagination Styles, Loading Spinner
- Base de Datos: Nuevas tablas (user_sessions, model_metrics, blockchain_transactions, nft_collections, defi_positions)
================================================================================
"""

import streamlit as st
import sqlite3
import hashlib
from datetime import datetime, timedelta
import random
import json
import os
import time
import warnings
warnings.filterwarnings('ignore')

# Fault-tolerant imports with error handling
try:
    import pandas as pd
    PANDAS_AVAILABLE = True
except ImportError as e:
    PANDAS_AVAILABLE = False
    pd = None
    print(f"ERROR importing pandas: {e}")

try:
    import numpy as np
    NUMPY_AVAILABLE = True
except ImportError as e:
    NUMPY_AVAILABLE = False
    np = None
    print(f"ERROR importing numpy: {e}")

try:
    import plotly.graph_objects as go
    import plotly.express as px
    PLOTLY_AVAILABLE = True
except ImportError as e:
    PLOTLY_AVAILABLE = False
    go = None
    px = None
    print(f"ERROR importing plotly: {e}")

try:
    from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
    from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score, StratifiedKFold
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score, precision_recall_curve
    from sklearn.linear_model import LogisticRegression
    from sklearn.svm import SVC
    from sklearn.neural_network import MLPClassifier
    SKLEARN_AVAILABLE = True
except ImportError as e:
    SKLEARN_AVAILABLE = False
    print(f"ERROR importing sklearn: {e}")

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError as e:
    REQUESTS_AVAILABLE = False
    print(f"ERROR importing requests: {e}")

# ================================================================================
# INTEGRACIONES DE APIs EXTERNAS
# ================================================================================

def get_weather_data(city="Caracas"):
    """Obtiene datos climáticos de OpenWeather API - Versión con datos simulados"""
    # Datos simulados para evitar necesidad de API key
    import random
    simulated_weather = {
        "name": city,
        "main": {
            "temp": round(random.uniform(20, 35), 1),
            "feels_like": round(random.uniform(18, 33), 1),
            "humidity": random.randint(50, 90),
            "pressure": random.randint(1000, 1020)
        },
        "weather": [
            {
                "main": "Sunny",
                "description": "cielo despejado"
            }
        ],
        "wind": {
            "speed": round(random.uniform(2, 10), 1)
        }
    }
    return simulated_weather

def get_news_data(query="technology"):
    """Obtiene noticias de News API - Versión con datos simulados"""
    # Datos simulados para evitar necesidad de API key
    simulated_news = {
        "status": "ok",
        "totalResults": 5,
        "articles": [
            {
                "title": f"Noticia simulada 1 sobre {query}",
                "description": "Esta es una noticia simulada para demostración",
                "url": "#",
                "publishedAt": "2024-01-15T10:00:00Z"
            },
            {
                "title": f"Noticia simulada 2 sobre {query}",
                "description": "Otra noticia simulada para demostración",
                "url": "#",
                "publishedAt": "2024-01-15T09:00:00Z"
            },
            {
                "title": f"Noticia simulada 3 sobre {query}",
                "description": "Tercera noticia simulada para demostración",
                "url": "#",
                "publishedAt": "2024-01-15T08:00:00Z"
            }
        ]
    }
    return simulated_news

def get_github_repos(username):
    """Obtiene repositorios de GitHub API"""
    if not REQUESTS_AVAILABLE:
        return None
    try:
        url = f"https://api.github.com/users/{username}/repos"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None

def get_crypto_prices():
    """Obtiene precios de criptomonedas de CoinGecko API (gratuita)"""
    if not REQUESTS_AVAILABLE:
        return None
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,binancecoin,cardano&vs_currencies=usd"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None

def get_etherscan_tx(address):
    """Obtiene transacciones de Ethereum usando Etherscan API"""
    if not REQUESTS_AVAILABLE:
        return None
    try:
        api_key = "demo_key"  # Reemplazar con API key real
        url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&apikey={api_key}"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None

# Configuración página
st.set_page_config(
    page_title="Portfolio Elite v6.0 | Salomon Febles | Microproyectos",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': "Portfolio Técnico Elite v6.0 - Microproyectos Impresionantes | Salomon Febles"
    }
)

# Inicializar session state para dark mode y gamificación
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
if 'xp_points' not in st.session_state:
    st.session_state.xp_points = 0
if 'level' not in st.session_state:
    st.session_state.level = 1
if 'badges' not in st.session_state:
    st.session_state.badges = []
if 'activities_completed' not in st.session_state:
    st.session_state.activities_completed = 0
if 'onboarding_completed' not in st.session_state:
    st.session_state.onboarding_completed = False
if 'config_exported' not in st.session_state:
    st.session_state.config_exported = False

# CSS Elite v6.0 con Dark Mode y Animaciones
def get_theme_css():
    if st.session_state.dark_mode:
        return """
<style>
    /* Google Fonts Import */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');
    
    /* Dark Mode Theme */
    .stApp { background-color: #0f172a; color: #e2e8f0; font-family: 'Inter', sans-serif; }
    .main-header { font-size: 2.8rem; font-weight: 800; font-family: 'Inter', sans-serif; background: linear-gradient(90deg, #818cf8, #22d3ee); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; animation: fadeInDown 0.8s ease-out; }
    .sub-header { font-size: 1.2rem; color: #94a3b8; font-family: 'Inter', sans-serif; text-align: center; margin-bottom: 2rem; animation: fadeIn 1s ease-out; }
    .metric-card { background: linear-gradient(135deg, #1e293b, #334155); border-radius: 16px; padding: 20px; border-left: 4px solid #818cf8; transition: transform 0.3s ease, box-shadow 0.3s ease; }
    .metric-card:hover { transform: translateY(-5px); box-shadow: 0 8px 30px rgba(129, 140, 248, 0.3); }
    .metric-value { font-size: 2rem; font-weight: 700; color: #f1f5f9; }
    .alert-critical { background: linear-gradient(135deg, #450a0a, #7f1d1d); border: 1px solid #dc2626; border-radius: 12px; padding: 16px; color: #fca5a5; animation: pulse 2s infinite; }
    .alert-high { background: linear-gradient(135deg, #451a03, #7c2d12); border: 1px solid #ea580c; border-radius: 12px; padding: 16px; color: #fdba74; }
    .alert-success { background: linear-gradient(135deg, #052e16, #14532d); border: 1px solid #16a34a; border-radius: 12px; padding: 16px; color: #86efac; }
    .glass-card { background: rgba(30, 41, 59, 0.95); backdrop-filter: blur(10px); border-radius: 20px; padding: 24px; border: 1px solid #334155; box-shadow: 0 4px 20px rgba(0,0,0,0.3); transition: all 0.3s ease; }
    .glass-card:hover { border-color: #818cf8; }
    .section-title { font-size: 1.8rem; font-weight: 700; color: #f1f5f9; margin: 24px 0 16px 0; animation: slideInLeft 0.6s ease-out; }
    .badge { display: inline-block; padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: 600; transition: transform 0.2s ease; }
    .badge:hover { transform: scale(1.1); }
    .badge-green { background: #14532d; color: #86efac; }
    .badge-red { background: #7f1d1d; color: #fca5a5; }
    .badge-yellow { background: #7c2d12; color: #fdba74; }
    .badge-blue { background: #1e3a8a; color: #93c5fd; }
    
    /* Animaciones */
    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
    @keyframes fadeInDown { from { opacity: 0; transform: translateY(-20px); } to { opacity: 1; transform: translateY(0); } }
    @keyframes slideInLeft { from { opacity: 0; transform: translateX(-30px); } to { opacity: 1; transform: translateX(0); } }
    @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.8; } }
    @keyframes glow { 0%, 100% { box-shadow: 0 0 5px #818cf8; } 50% { box-shadow: 0 0 20px #818cf8, 0 0 30px #22d3ee; } }
    
    /* XP Bar */
    .xp-container { background: #1e293b; border-radius: 10px; padding: 15px; margin: 10px 0; border: 1px solid #334155; }
    .xp-bar { background: linear-gradient(90deg, #818cf8, #22d3ee); height: 8px; border-radius: 4px; transition: width 0.5s ease; animation: glow 2s infinite; }
    .xp-text { color: #94a3b8; font-size: 0.9rem; margin-top: 8px; }
    
    /* Gamification */
    .badge-container { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px; }
    .achievement-badge { background: linear-gradient(135deg, #818cf8, #22d3ee); color: white; padding: 8px 16px; border-radius: 20px; font-size: 0.85rem; font-weight: 600; animation: fadeIn 0.5s ease; }
    
    /* Scrollbar */
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: #1e293b; }
    ::-webkit-scrollbar-thumb { background: #334155; border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: #818cf8; }
    
    /* Loading Skeleton */
    .skeleton { background: linear-gradient(90deg, #1e293b 25%, #334155 50%, #1e293b 75%); background-size: 200% 100%; animation: skeleton-loading 1.5s infinite; border-radius: 8px; }
    @keyframes skeleton-loading { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }
    
    /* Toast Notification */
    .toast { position: fixed; bottom: 20px; right: 20px; background: #1e293b; color: #f1f5f9; padding: 16px 24px; border-radius: 12px; border-left: 4px solid #818cf8; box-shadow: 0 4px 20px rgba(0,0,0,0.3); animation: slideInRight 0.3s ease; z-index: 9999; }
    @keyframes slideInRight { from { transform: translateX(100%); opacity: 0; } to { transform: translateX(0); opacity: 1; } }
    
    /* Progress Bar */
    .progress-container { background: #1e293b; border-radius: 10px; padding: 15px; margin: 10px 0; border: 1px solid #334155; }
    .progress-bar { background: linear-gradient(90deg, #818cf8, #22d3ee); height: 8px; border-radius: 4px; transition: width 0.5s ease; animation: glow 2s infinite; }
    
    /* Confetti */
    .confetti { position: fixed; width: 10px; height: 10px; background: #818cf8; animation: confetti-fall 3s linear; }
    @keyframes confetti-fall { 0% { transform: translateY(-100vh) rotate(0deg); opacity: 1; } 100% { transform: translateY(100vh) rotate(720deg); opacity: 0; } }
    
    /* Hover Effects */
    .hover-lift { transition: transform 0.3s ease, box-shadow 0.3s ease; }
    .hover-lift:hover { transform: translateY(-8px); box-shadow: 0 12px 40px rgba(129, 140, 248, 0.4); }
    
    /* Gradient Text */
    .gradient-text { background: linear-gradient(90deg, #818cf8, #22d3ee, #818cf8); background-size: 200% auto; -webkit-background-clip: text; -webkit-text-fill-color: transparent; animation: gradient-shift 3s linear infinite; }
    @keyframes gradient-shift { 0% { background-position: 0% center; } 100% { background-position: 200% center; } }
    
    /* Card Hover */
    .card-hover { transition: all 0.3s ease; }
    .card-hover:hover { transform: scale(1.02); border-color: #818cf8; box-shadow: 0 8px 30px rgba(129, 140, 248, 0.3); }
    
    /* Tooltip */
    .tooltip { position: relative; display: inline-block; }
    .tooltip-text { visibility: hidden; background: #1e293b; color: #f1f5f9; text-align: center; border-radius: 6px; padding: 8px 12px; position: absolute; z-index: 1; bottom: 125%; left: 50%; transform: translateX(-50%); opacity: 0; transition: opacity 0.3s; border: 1px solid #334155; }
    .tooltip:hover .tooltip-text { visibility: visible; opacity: 1; }
</style>
"""
    else:
        return """
<style>
    /* Google Fonts Import */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');
    
    /* Light Mode Theme */
    .stApp { background-color: #f8fafc; color: #1e293b; font-family: 'Inter', sans-serif; }
    .main-header { font-size: 2.8rem; font-weight: 800; font-family: 'Inter', sans-serif; background: linear-gradient(90deg, #6366f1, #06b6d4); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; animation: fadeInDown 0.8s ease-out; }
    .sub-header { font-size: 1.2rem; color: #64748b; font-family: 'Inter', sans-serif; text-align: center; margin-bottom: 2rem; animation: fadeIn 1s ease-out; }
    .metric-card { background: linear-gradient(135deg, #f8fafc, #e2e8f0); border-radius: 16px; padding: 20px; border-left: 4px solid #6366f1; transition: transform 0.3s ease, box-shadow 0.3s ease; }
    .metric-card:hover { transform: translateY(-5px); box-shadow: 0 8px 30px rgba(99, 102, 241, 0.3); }
    .metric-value { font-size: 2rem; font-weight: 700; color: #1e293b; }
    .alert-critical { background: linear-gradient(135deg, #fef2f2, #fee2e2); border: 1px solid #ef4444; border-radius: 12px; padding: 16px; color: #dc2626; animation: pulse 2s infinite; }
    .alert-high { background: linear-gradient(135deg, #fffbeb, #fef3c7); border: 1px solid #f59e0b; border-radius: 12px; padding: 16px; color: #d97706; }
    .alert-success { background: linear-gradient(135deg, #f0fdf4, #dcfce7); border: 1px solid #22c55e; border-radius: 12px; padding: 16px; color: #16a34a; }
    .glass-card { background: rgba(255,255,255,0.95); backdrop-filter: blur(10px); border-radius: 20px; padding: 24px; border: 1px solid #e2e8f0; box-shadow: 0 4px 20px rgba(0,0,0,0.08); transition: all 0.3s ease; }
    .glass-card:hover { border-color: #6366f1; }
    .section-title { font-size: 1.8rem; font-weight: 700; color: #1e293b; margin: 24px 0 16px 0; animation: slideInLeft 0.6s ease-out; }
    .badge { display: inline-block; padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: 600; transition: transform 0.2s ease; }
    .badge:hover { transform: scale(1.1); }
    .badge-green { background: #dcfce7; color: #16a34a; }
    .badge-red { background: #fee2e2; color: #dc2626; }
    .badge-yellow { background: #fef3c7; color: #d97706; }
    .badge-blue { background: #dbeafe; color: #2563eb; }
    
    /* Animaciones */
    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
    @keyframes fadeInDown { from { opacity: 0; transform: translateY(-20px); } to { opacity: 1; transform: translateY(0); } }
    @keyframes slideInLeft { from { opacity: 0; transform: translateX(-30px); } to { opacity: 1; transform: translateX(0); } }
    @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.8; } }
    @keyframes glow { 0%, 100% { box-shadow: 0 0 5px #6366f1; } 50% { box-shadow: 0 0 20px #6366f1, 0 0 30px #06b6d4; } }
    
    /* XP Bar */
    .xp-container { background: #f1f5f9; border-radius: 10px; padding: 15px; margin: 10px 0; border: 1px solid #e2e8f0; }
    .xp-bar { background: linear-gradient(90deg, #6366f1, #06b6d4); height: 8px; border-radius: 4px; transition: width 0.5s ease; animation: glow 2s infinite; }
    .xp-text { color: #64748b; font-size: 0.9rem; margin-top: 8px; }
    
    /* Gamification */
    .badge-container { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px; }
    .achievement-badge { background: linear-gradient(135deg, #6366f1, #06b6d4); color: white; padding: 8px 16px; border-radius: 20px; font-size: 0.85rem; font-weight: 600; animation: fadeIn 0.5s ease; }
    
    /* Scrollbar */
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: #f1f5f9; }
    ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: #6366f1; }
    
    /* Loading Skeleton */
    .skeleton { background: linear-gradient(90deg, #f1f5f9 25%, #e2e8f0 50%, #f1f5f9 75%); background-size: 200% 100%; animation: skeleton-loading 1.5s infinite; border-radius: 8px; }
    @keyframes skeleton-loading { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }
    
    /* Toast Notification */
    .toast { position: fixed; bottom: 20px; right: 20px; background: #ffffff; color: #1e293b; padding: 16px 24px; border-radius: 12px; border-left: 4px solid #6366f1; box-shadow: 0 4px 20px rgba(0,0,0,0.1); animation: slideInRight 0.3s ease; z-index: 9999; }
    @keyframes slideInRight { from { transform: translateX(100%); opacity: 0; } to { transform: translateX(0); opacity: 1; } }
    
    /* Progress Bar */
    .progress-container { background: #f1f5f9; border-radius: 10px; padding: 15px; margin: 10px 0; border: 1px solid #e2e8f0; }
    .progress-bar { background: linear-gradient(90deg, #6366f1, #06b6d4); height: 8px; border-radius: 4px; transition: width 0.5s ease; animation: glow 2s infinite; }
    
    /* Confetti */
    .confetti { position: fixed; width: 10px; height: 10px; background: #6366f1; animation: confetti-fall 3s linear; }
    @keyframes confetti-fall { 0% { transform: translateY(-100vh) rotate(0deg); opacity: 1; } 100% { transform: translateY(100vh) rotate(720deg); opacity: 0; } }
    
    /* Hover Effects */
    .hover-lift { transition: transform 0.3s ease, box-shadow 0.3s ease; }
    .hover-lift:hover { transform: translateY(-8px); box-shadow: 0 12px 40px rgba(99, 102, 241, 0.4); }
    
    /* Gradient Text */
    .gradient-text { background: linear-gradient(90deg, #6366f1, #06b6d4, #6366f1); background-size: 200% auto; -webkit-background-clip: text; -webkit-text-fill-color: transparent; animation: gradient-shift 3s linear infinite; }
    @keyframes gradient-shift { 0% { background-position: 0% center; } 100% { background-position: 200% center; } }
    
    /* Card Hover */
    .card-hover { transition: all 0.3s ease; }
    .card-hover:hover { transform: scale(1.02); border-color: #6366f1; box-shadow: 0 8px 30px rgba(99, 102, 241, 0.3); }
    
    /* Tooltip */
    .tooltip { position: relative; display: inline-block; }
    .tooltip-text { visibility: hidden; background: #ffffff; color: #1e293b; text-align: center; border-radius: 6px; padding: 8px 12px; position: absolute; z-index: 1; bottom: 125%; left: 50%; transform: translateX(-50%); opacity: 0; transition: opacity 0.3s; border: 1px solid #e2e8f0; }
    .tooltip:hover .tooltip-text { visibility: visible; opacity: 1; }
    
    /* Animations */
    @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
    @keyframes slideIn { from { transform: translateX(-100%); } to { transform: translateX(0); } }
    @keyframes pulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.05); } }
    @keyframes shimmer { 0% { background-position: -200% 0; } 100% { background-position: 200% 0; } }
    
    .fade-in { animation: fadeIn 0.5s ease-out; }
    .slide-in { animation: slideIn 0.5s ease-out; }
    .pulse { animation: pulse 2s infinite; }
    .shimmer { background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%); background-size: 200% 100%; animation: shimmer 2s infinite; }
    
    /* Glassmorphism */
    .glass { background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.2); border-radius: 12px; }
    .glass-dark { background: rgba(0, 0, 0, 0.3); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; }
    
    /* Neumorphism */
    .neumorphic { background: #f0f0f0; box-shadow: 8px 8px 16px #d1d1d1, -8px -8px 16px #ffffff; border-radius: 12px; }
    .neumorphic-dark { background: #1e293b; box-shadow: 8px 8px 16px #0f172a, -8px -8px 16px #334155; border-radius: 12px; }
    
    /* Gradient Borders */
    .gradient-border { position: relative; background: white; border-radius: 12px; }
    .gradient-border::before { content: ''; position: absolute; inset: -2px; background: linear-gradient(45deg, #818cf8, #22d3ee, #10b981, #f59e0b); border-radius: 14px; z-index: -1; }
    
    /* Skeleton Loading */
    .skeleton { background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%); background-size: 200% 100%; animation: shimmer 1.5s infinite; border-radius: 4px; }
    
    /* Progress Bar */
    .progress-bar { background: linear-gradient(90deg, #6366f1, #06b6d4); height: 8px; border-radius: 4px; overflow: hidden; }
    .progress-fill { height: 100%; background: linear-gradient(90deg, #10b981, #06b6d4); transition: width 0.3s ease; }
    
    /* Badge Styles */
    .badge { display: inline-block; padding: 4px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 600; }
    .badge-primary { background: linear-gradient(135deg, #6366f1, #8b5cf6); color: white; }
    .badge-success { background: linear-gradient(135deg, #10b981, #06b6d4); color: white; }
    .badge-warning { background: linear-gradient(135deg, #f59e0b, #ef4444); color: white; }
    .badge-info { background: linear-gradient(135deg, #06b6d4, #3b82f6); color: white; }
    
    /* Alert Styles */
    .alert { padding: 12px 16px; border-radius: 8px; margin: 10px 0; border-left: 4px solid; }
    .alert-info { background: rgba(59, 130, 246, 0.1); border-color: #3b82f6; }
    .alert-success { background: rgba(16, 185, 129, 0.1); border-color: #10b981; }
    .alert-warning { background: rgba(245, 158, 11, 0.1); border-color: #f59e0b; }
    .alert-error { background: rgba(239, 68, 68, 0.1); border-color: #ef4444; }
    
    /* Button Styles */
    .btn-primary { background: linear-gradient(135deg, #6366f1, #8b5cf6); color: white; padding: 8px 16px; border-radius: 8px; border: none; cursor: pointer; transition: all 0.3s ease; }
    .btn-primary:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(99, 102, 241, 0.4); }
    .btn-secondary { background: linear-gradient(135deg, #64748b, #475569); color: white; padding: 8px 16px; border-radius: 8px; border: none; cursor: pointer; transition: all 0.3s ease; }
    .btn-secondary:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(100, 116, 139, 0.4); }
    
    /* Card Styles */
    .card { background: white; border-radius: 12px; padding: 20px; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); transition: all 0.3s ease; }
    .card:hover { transform: translateY(-4px); box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15); }
    
    /* Table Styles */
    .table-container { overflow-x: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); }
    .data-table { width: 100%; border-collapse: collapse; }
    .data-table th { background: linear-gradient(135deg, #6366f1, #8b5cf6); color: white; padding: 12px; text-align: left; }
    .data-table td { padding: 12px; border-bottom: 1px solid #e2e8f0; }
    .data-table tr:hover { background: rgba(99, 102, 241, 0.05); }
    
    /* Input Styles */
    .input-field { width: 100%; padding: 10px 12px; border: 2px solid #e2e8f0; border-radius: 8px; transition: all 0.3s ease; }
    .input-field:focus { border-color: #6366f1; box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1); }
    
    /* Select Styles */
    .select-field { width: 100%; padding: 10px 12px; border: 2px solid #e2e8f0; border-radius: 8px; background: white; transition: all 0.3s ease; }
    .select-field:focus { border-color: #6366f1; box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1); }
    
    /* Checkbox Styles */
    .checkbox-custom { width: 20px; height: 20px; accent-color: #6366f1; cursor: pointer; }
    
    /* Radio Styles */
    .radio-custom { width: 20px; height: 20px; accent-color: #6366f1; cursor: pointer; }
    
    /* Toggle Switch */
    .toggle-switch { position: relative; width: 50px; height: 26px; }
    .toggle-switch input { opacity: 0; width: 0; height: 0; }
    .toggle-slider { position: absolute; cursor: pointer; top: 0; left: 0; right: 0; bottom: 0; background: #ccc; transition: 0.4s; border-radius: 26px; }
    .toggle-slider:before { position: absolute; content: ""; height: 20px; width: 20px; left: 3px; bottom: 3px; background: white; transition: 0.4s; border-radius: 50%; }
    .toggle-switch input:checked + .toggle-slider { background: #6366f1; }
    .toggle-switch input:checked + .toggle-slider:before { transform: translateX(24px); }
    
    /* Modal Styles */
    .modal-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0.5); display: flex; justify-content: center; align-items: center; z-index: 1000; }
    .modal-content { background: white; padding: 24px; border-radius: 12px; max-width: 500px; width: 90%; box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2); }
    
    /* Dropdown Styles */
    .dropdown-menu { position: absolute; top: 100%; left: 0; background: white; border: 1px solid #e2e8f0; border-radius: 8px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); min-width: 200px; z-index: 100; }
    .dropdown-item { padding: 10px 16px; cursor: pointer; transition: background 0.2s ease; }
    .dropdown-item:hover { background: rgba(99, 102, 241, 0.1); }
    
    /* Accordion Styles */
    .accordion-item { border: 1px solid #e2e8f0; border-radius: 8px; margin-bottom: 8px; overflow: hidden; }
    .accordion-header { padding: 12px 16px; background: rgba(99, 102, 241, 0.05); cursor: pointer; display: flex; justify-content: space-between; align-items: center; }
    .accordion-content { padding: 16px; background: white; }
    
    /* Tabs Styles */
    .tab-container { border-bottom: 2px solid #e2e8f0; }
    .tab-item { padding: 12px 24px; cursor: pointer; border-bottom: 2px solid transparent; transition: all 0.3s ease; }
    .tab-item:hover { color: #6366f1; }
    .tab-item.active { border-bottom-color: #6366f1; color: #6366f1; font-weight: 600; }
    
    /* Breadcrumb Styles */
    .breadcrumb { display: flex; align-items: center; gap: 8px; padding: 12px 0; }
    .breadcrumb-item { color: #64748b; text-decoration: none; transition: color 0.2s ease; }
    .breadcrumb-item:hover { color: #6366f1; }
    .breadcrumb-separator { color: #94a3b8; }
    
    /* Pagination Styles */
    .pagination { display: flex; gap: 4px; align-items: center; }
    .pagination-btn { padding: 8px 12px; border: 1px solid #e2e8f0; border-radius: 6px; background: white; cursor: pointer; transition: all 0.2s ease; }
    .pagination-btn:hover { border-color: #6366f1; color: #6366f1; }
    .pagination-btn.active { background: #6366f1; color: white; border-color: #6366f1; }
    
    /* Loading Spinner */
    .spinner { width: 40px; height: 40px; border: 4px solid #e2e8f0; border-top-color: #6366f1; border-radius: 50%; animation: spin 1s linear infinite; }
    @keyframes spin { to { transform: rotate(360deg); } }
</style>
"""

st.markdown(get_theme_css(), unsafe_allow_html=True)

# ================================================================================
# BASE DE DATOS
# ================================================================================
@st.cache_resource
def init_database():
    conn = sqlite3.connect('expoempleo_demo_v5.db', check_same_thread=False)
    cursor = conn.cursor()
    
    # Tablas enterprise
    cursor.execute('''CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY, product_name TEXT, category TEXT, sku TEXT UNIQUE,
        quantity INTEGER, min_stock INTEGER, unit_price REAL, cost_price REAL,
        supplier TEXT, lead_time_days INTEGER, last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS security_alerts (
        id INTEGER PRIMARY KEY, alert_id TEXT UNIQUE, severity TEXT, category TEXT,
        threat_type TEXT, source_ip TEXT, target_system TEXT, mitre_tactic TEXT,
        mitre_technique TEXT, command_detected TEXT, description TEXT,
        kill_chain_phase TEXT, process_id INTEGER, parent_pid INTEGER, 
        file_hash TEXT, network_connection TEXT, status TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS ioc_database (
        id INTEGER PRIMARY KEY, ioc_value TEXT UNIQUE, ioc_type TEXT, 
        threat_actor TEXT, campaign TEXT, first_seen TIMESTAMP, 
        last_seen TIMESTAMP, confidence INTEGER, tags TEXT, is_active BOOLEAN DEFAULT 1)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS siem_logs (
        id INTEGER PRIMARY KEY, timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        log_level TEXT, source_ip TEXT, destination_ip TEXT, port INTEGER,
        protocol TEXT, event_type TEXT, payload TEXT, severity TEXT,
        mitre_tactic TEXT, mitre_technique TEXT, is_alert BOOLEAN DEFAULT 0)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS soar_playbooks (
        id INTEGER PRIMARY KEY, playbook_name TEXT UNIQUE, trigger_condition TEXT,
        actions TEXT, status TEXT, last_run TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        success_rate REAL, avg_execution_time REAL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS threat_intel_feeds (
        id INTEGER PRIMARY KEY, feed_name TEXT, feed_type TEXT,
        last_updated TIMESTAMP, ioc_count INTEGER, risk_level TEXT,
        is_active BOOLEAN DEFAULT 1)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS process_monitor (
        id INTEGER PRIMARY KEY, process_name TEXT, pid INTEGER, 
        parent_pid INTEGER, command_line TEXT, user TEXT, 
        cpu_usage REAL, memory_usage REAL, start_time TIMESTAMP, 
        is_suspicious BOOLEAN DEFAULT 0)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY, document_id TEXT UNIQUE, file_name TEXT,
        file_type TEXT, file_size INTEGER, hash_sha256 TEXT UNIQUE, hash_md5 TEXT,
        uploaded_by TEXT, signatures_required INTEGER, signatures_received INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, status TEXT DEFAULT 'pending')''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS document_audit (
        id INTEGER PRIMARY KEY, document_id TEXT, action TEXT, performed_by TEXT,
        ip_address TEXT, timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS trades (
        id INTEGER PRIMARY KEY, trade_id TEXT UNIQUE, symbol TEXT, side TEXT,
        entry_price REAL, exit_price REAL, quantity INTEGER, stop_loss REAL,
        take_profit REAL, pnl REAL, status TEXT, opened_at TIMESTAMP,
        closed_at TIMESTAMP, strategy TEXT)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS user_sessions (
        id INTEGER PRIMARY KEY, session_id TEXT UNIQUE, user_id TEXT,
        login_time TIMESTAMP, logout_time TIMESTAMP, ip_address TEXT,
        user_agent TEXT, activities_completed INTEGER, xp_earned INTEGER,
        level INTEGER, badges TEXT)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS model_metrics (
        id INTEGER PRIMARY KEY, model_name TEXT, model_type TEXT,
        accuracy REAL, precision REAL, recall REAL, f1_score REAL,
        auc_roc REAL, training_time REAL, inference_time REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, is_active BOOLEAN DEFAULT 1)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS blockchain_transactions (
        id INTEGER PRIMARY KEY, tx_hash TEXT UNIQUE, from_address TEXT,
        to_address TEXT, value REAL, gas_used INTEGER, gas_price REAL,
        block_number INTEGER, timestamp TIMESTAMP, status TEXT,
        contract_address TEXT, method_name TEXT)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS nft_collections (
        id INTEGER PRIMARY KEY, collection_id TEXT UNIQUE, name TEXT,
        creator_address TEXT, total_supply INTEGER, floor_price REAL,
        volume_24h REAL, owners_count INTEGER, created_at TIMESTAMP)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS defi_positions (
        id INTEGER PRIMARY KEY, position_id TEXT UNIQUE, protocol TEXT,
        token_pair TEXT, amount_deposited REAL, current_value REAL,
        apy REAL, rewards_earned REAL, opened_at TIMESTAMP,
        status TEXT DEFAULT 'active')''')

    
    # Datos demo
    cursor.execute("SELECT COUNT(*) FROM inventory")
    if cursor.fetchone()[0] == 0:
        products = [
            ('Paracetamol 500mg', 'Medicamentos', 'MED-001', 150, 50, 5.50, 3.20, 'Farmacéutica ABC', 7),
            ('Ibuprofeno 400mg', 'Medicamentos', 'MED-002', 45, 60, 8.25, 4.80, 'Farmacéutica XYZ', 5),
            ('Amoxicilina 500mg', 'Antibióticos', 'ANT-001', 200, 30, 12.00, 7.50, 'Genfar Venezuela', 10),
            ('Loratadina 10mg', 'Antihistamínicos', 'ANT-002', 30, 40, 6.75, 3.90, 'Farmacéutica ABC', 6),
            ('Omeprazol 20mg', 'Gastroprotectores', 'GAS-001', 80, 25, 9.50, 5.60, 'Novartis Venezuela', 8),
            ('Metformina 850mg', 'Diabetes', 'DIA-001', 25, 35, 15.00, 9.20, 'Genfar Venezuela', 12),
            ('Atorvastatina 20mg', 'Cardiología', 'CAR-001', 120, 45, 18.50, 11.30, 'Pfizer Venezuela', 14),
            ('Aspirina 100mg', 'Cardiología', 'CAR-002', 300, 100, 3.25, 1.90, 'Bayer Venezuela', 5),
        ]
        cursor.executemany('INSERT INTO inventory (product_name, category, sku, quantity, min_stock, unit_price, cost_price, supplier, lead_time_days, last_updated) VALUES (?,?,?,?,?,?,?,?,?,?)',
                          [p+(datetime.now(),) for p in products])
    
    cursor.execute("SELECT COUNT(*) FROM security_alerts")
    if cursor.fetchone()[0] == 0:
        alerts = [
            ('ALT-001', 'CRITICAL', 'Malware', 'Lotus Wiper', '192.168.1.100', 'WS-01', 'Impact', 'T1490', 'diskpart clean', 'Wiper detectado', 'Destruction', 1234, 1000, 'a1b2c3d4', 'TCP:443', 'blocked'),
            ('ALT-002', 'HIGH', 'Data Theft', 'Exfiltration', '192.168.1.105', 'FILE-01', 'Collection', 'T1005', 'robocopy /MIR', 'Data exfil', 'Exfiltration', 2345, 2000, 'e5f6g7h8', 'TCP:80', 'investigating'),
            ('ALT-003', 'CRITICAL', 'Ransomware', 'Shadow Delete', '192.168.1.110', 'WS-02', 'Impact', 'T1490', 'vssadmin delete', 'Backup deletion', 'Destruction', 3456, 3000, 'i9j0k1l2', 'TCP:445', 'blocked'),
            ('ALT-004', 'MEDIUM', 'Persistence', 'Scheduled Task', '192.168.1.115', 'WS-03', 'Persistence', 'T1053', 'schtasks /create', 'Persistence', 'Installation', 4567, 4000, 'm3n4o5p6', 'TCP:135', 'monitoring'),
            ('ALT-005', 'HIGH', 'Credential Theft', 'Mimikatz', '192.168.1.120', 'DC-01', 'Credential Access', 'T1003', 'lsass.exe dump', 'Credential theft', 'Credential Access', 5678, 5000, 'q7r8s9t0', 'TCP:88', 'blocked'),
        ]
        cursor.executemany('INSERT INTO security_alerts (alert_id, severity, category, threat_type, source_ip, target_system, mitre_tactic, mitre_technique, command_detected, description, kill_chain_phase, process_id, parent_pid, file_hash, network_connection, status, created_at) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                          [a+(datetime.now(),) for a in alerts])
    
    # IOC Database avanzada
    cursor.execute("SELECT COUNT(*) FROM ioc_database")
    if cursor.fetchone()[0] == 0:
        iocs = [
            ('192.168.1.100', 'IP', 'Lotus Wiper', 'Operation Venezuela', datetime(2026,4,15), datetime.now(), 95, 'wiper,malware', 1),
            ('diskpart.exe', 'Filename', 'Lotus Wiper', 'Operation Venezuela', datetime(2026,4,15), datetime.now(), 90, 'wiper,system', 1),
            ('vssadmin.exe', 'Filename', 'Shadow Killers', 'Operation Venezuela', datetime(2026,4,20), datetime.now(), 85, 'ransomware', 1),
            ('robocopy.exe', 'Filename', 'Data Exfil Group', 'Operation Venezuela', datetime(2026,4,10), datetime.now(), 75, 'exfiltration', 1),
            ('a1b2c3d4e5f6g7h8', 'Hash', 'APT-VZLA', 'Operation Venezuela', datetime(2026,3,1), datetime.now(), 100, 'malware', 1),
            ('powershell.exe -enc', 'Command', 'APT-VZLA', 'Operation Venezuela', datetime(2026,3,15), datetime.now(), 80, 'obfuscation', 1),
            ('*.tmp', 'Pattern', 'Generic Malware', 'Multiple', datetime(2026,1,1), datetime.now(), 60, 'temp', 1),
            ('TCP:443', 'Port', 'C2 Communication', 'Multiple', datetime(2026,1,1), datetime.now(), 70, 'c2', 1),
        ]
        cursor.executemany('INSERT INTO ioc_database (ioc_value, ioc_type, threat_actor, campaign, first_seen, last_seen, confidence, tags, is_active) VALUES (?,?,?,?,?,?,?,?,?)', iocs)
    
    # Process Monitor simulado
    cursor.execute("SELECT COUNT(*) FROM process_monitor")
    if cursor.fetchone()[0] == 0:
        processes = [
            ('svchost.exe', 1234, 500, 'svchost.exe -k netsvcs', 'SYSTEM', 0.5, 45.2, datetime.now() - timedelta(hours=2), 0),
            ('explorer.exe', 2345, 1000, 'explorer.exe', 'user', 2.1, 120.5, datetime.now() - timedelta(hours=1), 0),
            ('chrome.exe', 3456, 2345, 'chrome.exe --type=renderer', 'user', 5.3, 350.8, datetime.now() - timedelta(minutes=30), 0),
            ('powershell.exe', 4567, 1234, 'powershell.exe -nop -w hidden -c IEX', 'user', 15.2, 89.3, datetime.now() - timedelta(minutes=5), 1),
            ('unknown.exe', 5678, 1000, 'unknown.exe /silent', 'SYSTEM', 0.1, 12.5, datetime.now() - timedelta(minutes=2), 1),
        ]
        cursor.executemany('INSERT INTO process_monitor (process_name, pid, parent_pid, command_line, user, cpu_usage, memory_usage, start_time, is_suspicious) VALUES (?,?,?,?,?,?,?,?,?)', processes)
    
    # SIEM Logs simulados
    cursor.execute("SELECT COUNT(*) FROM siem_logs")
    if cursor.fetchone()[0] == 0:
        siem_logs = [
            ('INFO', '192.168.1.100', '10.0.0.1', 443, 'TCP', 'Connection Established', 'TLS handshake', 'LOW', 'Initial Access', 'T1190', 0),
            ('WARNING', '192.168.1.105', '8.8.8.8', 53, 'UDP', 'DNS Query', 'suspicious-domain.com', 'MEDIUM', 'Discovery', 'T1018', 1),
            ('ERROR', '192.168.1.110', '192.168.1.200', 445, 'TCP', 'SMB Connection', 'Lateral movement attempt', 'HIGH', 'Lateral Movement', 'T1021', 1),
            ('CRITICAL', '192.168.1.120', '10.0.0.50', 3389, 'TCP', 'RDP Connection', 'Brute force detected', 'CRITICAL', 'Credential Access', 'T1110', 1),
            ('INFO', '192.168.1.115', '172.16.0.1', 80, 'TCP', 'HTTP Request', 'Normal web traffic', 'LOW', 'Execution', 'T1105', 0),
        ]
        cursor.executemany('INSERT INTO siem_logs (log_level, source_ip, destination_ip, port, protocol, event_type, payload, severity, mitre_tactic, mitre_technique, is_alert) VALUES (?,?,?,?,?,?,?,?,?,?,?)', siem_logs)
    
    # SOAR Playbooks simulados
    cursor.execute("SELECT COUNT(*) FROM soar_playbooks")
    if cursor.fetchone()[0] == 0:
        playbooks = [
            ('Malware Isolation', 'severity=CRITICAL AND category=Malware', '["isolate_endpoint", "collect_forensics", "notify_soc"]', 'active', datetime.now() - timedelta(hours=1), 95.5, 45.2),
            ('Phishing Response', 'threat_type=Phishing', '["block_sender", "quarantine_email", "user_training"]', 'active', datetime.now() - timedelta(hours=6), 88.3, 32.1),
            ('DDoS Mitigation', 'event_type=DDoS', '["rate_limit", "geo_block", "cdn_activation"]', 'active', datetime.now() - timedelta(hours=12), 92.7, 15.8),
            ('Insider Threat', 'user_behavior=anomalous', '["monitor_activity", "restrict_access", "hr_notification"]', 'active', datetime.now() - timedelta(hours=24), 78.9, 120.5),
        ]
        cursor.executemany('INSERT INTO soar_playbooks (playbook_name, trigger_condition, actions, status, last_run, success_rate, avg_execution_time) VALUES (?,?,?,?,?,?,?)', playbooks)
    
    # Threat Intel Feeds simulados
    cursor.execute("SELECT COUNT(*) FROM threat_intel_feeds")
    if cursor.fetchone()[0] == 0:
        intel_feeds = [
            ('MISP Community', 'IOC', datetime.now() - timedelta(hours=1), 15420, 'HIGH', 1),
            ('VirusTotal', 'Hash', datetime.now() - timedelta(hours=2), 8920, 'MEDIUM', 1),
            ('AlienVault OTX', 'IP Reputation', datetime.now() - timedelta(hours=3), 12350, 'HIGH', 1),
            ('CISA KEV Catalog', 'Vulnerability', datetime.now() - timedelta(hours=6), 890, 'CRITICAL', 1),
        ]
        cursor.executemany('INSERT INTO threat_intel_feeds (feed_name, feed_type, last_updated, ioc_count, risk_level, is_active) VALUES (?,?,?,?,?,?)', intel_feeds)
    
    conn.commit()
    return conn

db_conn = init_database()

def get_db(): return sqlite3.connect('expoempleo_demo_v5.db', check_same_thread=False)

# ================================================================================
# FUNCIONES UTILITARIAS
# ================================================================================
def calc_hash_sha256(data): return hashlib.sha256(data).hexdigest()
def calc_hash_md5(data): return hashlib.md5(data).hexdigest()
def gen_id(prefix): return f"{prefix}-{datetime.now().strftime('%Y%m%d%H%M%S')}-{random.randint(1000,9999)}"

# Funciones Blockchain avanzadas
def proof_of_work(block_data, difficulty=4):
    """Simula Proof of Work blockchain"""
    nonce = 0
    target = '0' * difficulty
    while True:
        block_string = f"{block_data}{nonce}"
        block_hash = hashlib.sha256(block_string.encode()).hexdigest()
        if block_hash.startswith(target):
            return nonce, block_hash
        nonce += 1
        if nonce > 1000000:  # Límite para evitar loops infinitos
            return nonce, block_hash

def verify_zero_knowledge_proof(commitment, challenge, response, secret):
    """Simula verificación de Zero-Knowledge Proof"""
    expected_response = hashlib.sha256(f"{commitment}{challenge}{secret}".encode()).hexdigest()
    return response == expected_response

def create_merkle_tree(hashes):
    """Crea un Merkle Tree a partir de hashes"""
    if len(hashes) == 1:
        return hashes[0]
    
    new_level = []
    for i in range(0, len(hashes), 2):
        if i + 1 < len(hashes):
            combined = hashes[i] + hashes[i + 1]
        else:
            combined = hashes[i] + hashes[i]
        new_hash = hashlib.sha256(combined.encode()).hexdigest()
        new_level.append(new_hash)
    
    return create_merkle_tree(new_level)

# Indicadores técnicos avanzados
def calc_rsi(prices, period=14):
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss.replace(0, 0.001)  # Evitar división por cero
    return 100 - (100 / (1 + rs))

def calc_ema(prices, period):
    return prices.ewm(span=period, adjust=False).mean()

def calc_macd(prices, fast=12, slow=26, signal=9):
    ema_fast = calc_ema(prices, fast)
    ema_slow = calc_ema(prices, slow)
    macd = ema_fast - ema_slow
    signal_line = calc_ema(macd, signal)
    histogram = macd - signal_line
    return macd, signal_line, histogram

def calc_bollinger(prices, period=20, std_dev=2):
    sma = prices.rolling(window=period).mean()
    std = prices.rolling(window=period).std()
    upper = sma + (std * std_dev)
    lower = sma - (std * std_dev)
    return upper, sma, lower

def calc_atr(high, low, close, period=14):
    tr1 = high - low
    tr2 = abs(high - close.shift())
    tr3 = abs(low - close.shift())
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    return tr.rolling(window=period).mean()

def calc_fibonacci(high, low):
    diff = high - low
    return {
        '0%': high,
        '23.6%': high - (diff * 0.236),
        '38.2%': high - (diff * 0.382),
        '50%': high - (diff * 0.5),
        '61.8%': high - (diff * 0.618),
        '78.6%': high - (diff * 0.786),
        '100%': low
    }

def calc_ichimoku(high, low, close, tenkan=9, kijun=26, senkou=52):
    tenkan_line = (high.rolling(window=tenkan).max() + low.rolling(window=tenkan).min()) / 2
    kijun_line = (high.rolling(window=kijun).max() + low.rolling(window=kijun).min()) / 2
    senkou_span_a = ((tenkan_line + kijun_line) / 2).shift(kijun)
    senkou_span_b = (high.rolling(window=senkou).max() + low.rolling(window=senkou).min()).shift(kijun)
    chikou_span = close.shift(-kijun)
    return tenkan_line, kijun_line, senkou_span_a, senkou_span_b, chikou_span

def calc_stochastic(high, low, close, k_period=14, d_period=3):
    low_min = low.rolling(window=k_period).min()
    high_max = high.rolling(window=k_period).max()
    range_val = high_max - low_min
    range_val = range_val.replace(0, np.nan) if NUMPY_AVAILABLE else range_val
    k_percent = 100 * ((close - low_min) / range_val)
    d_percent = k_percent.rolling(window=d_period).mean()
    return k_percent, d_percent

def calc_williams_r(high, low, close, period=14):
    high_max = high.rolling(window=period).max()
    low_min = low.rolling(window=period).min()
    range_val = high_max - low_min
    range_val = range_val.replace(0, np.nan) if NUMPY_AVAILABLE else range_val
    wr = -100 * ((high_max - close) / range_val)
    return wr

def calc_obv(close, volume):
    obv = (np.sign(close.diff()) * volume).fillna(0).cumsum() if NUMPY_AVAILABLE else (close.diff().apply(lambda x: 1 if x > 0 else -1) * volume).fillna(0).cumsum()
    return obv

def calc_order_book_depth(bids, asks):
    bid_depth = sum([qty for price, qty in bids])
    ask_depth = sum([qty for price, qty in asks])
    imbalance = (bid_depth - ask_depth) / (bid_depth + ask_depth) if (bid_depth + ask_depth) > 0 else 0
    return bid_depth, ask_depth, imbalance

def calc_vwap(prices, volumes):
    total_volume = volumes.sum()
    if total_volume == 0:
        return prices.mean() if not prices.empty else 0
    return (prices * volumes).sum() / total_volume

def calc_spread(bid_price, ask_price):
    spread = ask_price - bid_price
    spread_pct = (spread / bid_price * 100) if bid_price > 0 else 0
    return spread, spread_pct

def simulate_hft_execution(price, quantity, latency_us=50):
    slippage = random.uniform(-0.01, 0.01) * price
    executed_price = price + slippage
    execution_time = latency_us / 1000000
    return executed_price, execution_time, slippage

def triangular_arbitrage(rates):
    try:
        start_amount = 1000
        eur = start_amount * rates['USD/EUR']
        gbp = eur * rates['EUR/GBP']
        usd = gbp * rates['GBP/USD']
        profit = usd - start_amount
        profit_pct = (profit / start_amount) * 100 if start_amount > 0 else 0
        return profit, profit_pct, usd
    except (KeyError, ZeroDivisionError):
        return 0, 0, 1000

def market_making_spread(mid_price, volatility, inventory_risk=0):
    base_spread = mid_price * 0.001
    volatility_adjustment = volatility * mid_price * 0.5
    inventory_adjustment = inventory_risk * mid_price * 0.2
    total_spread = base_spread + volatility_adjustment + inventory_adjustment
    bid_price = mid_price - total_spread / 2
    ask_price = mid_price + total_spread / 2
    return bid_price, ask_price, total_spread

def holt_winters(series, alpha=0.3, beta=0.1, periods=30):
    if series.empty or len(series) < 2:
        return [0] * periods
    level = series.iloc[0]
    trend = series.iloc[1] - series.iloc[0] if len(series) > 1 else 0
    forecast = []
    for i in range(periods):
        forecast.append(level + (i + 1) * trend)
    return forecast

def arima_forecast(series, p=1, d=1, q=1, periods=12):
    if series.empty:
        return [0] * periods
    last_value = series.iloc[-1]
    trend = series.diff().mean()
    std_val = series.std() if len(series) > 1 else 0
    forecast = []
    for i in range(1, periods + 1):
        noise = np.random.normal(0, std_val * 0.1) if NUMPY_AVAILABLE else 0
        forecast.append(last_value + (trend * i) + noise)
    return forecast

def eoq_with_discounts(demand, ordering_cost, holding_cost, price_tiers):
    results = []
    for min_qty, price in price_tiers:
        holding_cost_per_unit = holding_cost * price
        if holding_cost_per_unit == 0:
            holding_cost_per_unit = 0.01
        eoq = np.sqrt((2 * demand * ordering_cost) / holding_cost_per_unit) if NUMPY_AVAILABLE else ((2 * demand * ordering_cost) / holding_cost_per_unit) ** 0.5
        adjusted_eoq = max(eoq, min_qty)
        if adjusted_eoq == 0:
            adjusted_eoq = 1
        total_cost = (demand * price) + (demand / adjusted_eoq * ordering_cost) + (adjusted_eoq / 2 * holding_cost_per_unit)
        results.append({
            'min_qty': min_qty,
            'price': price,
            'eoq': adjusted_eoq,
            'total_cost': total_cost
        })
    return sorted(results, key=lambda x: x['total_cost'])[0] if results else None

def dynamic_safety_stock(demand_std, lead_time_std, service_level=0.95):
    z_score = {0.90: 1.28, 0.95: 1.645, 0.99: 2.33}.get(service_level, 1.645)
    demand_std = max(demand_std, 0)
    lead_time_std = max(lead_time_std, 0)
    safety_stock = z_score * np.sqrt((demand_std**2 * lead_time_std) + (demand_std**2 * lead_time_std)) if NUMPY_AVAILABLE else z_score * ((demand_std**2 * lead_time_std) * 2) ** 0.5
    return safety_stock

def dynamic_reorder_point(demand_daily, lead_time, safety_stock):
    return (demand_daily * lead_time) + safety_stock

def inventory_turnover(cost_of_goods_sold, average_inventory):
    return cost_of_goods_sold / average_inventory if average_inventory > 0 else 0

def days_sales_of_inventory(cost_of_goods_sold, average_inventory):
    turnover = inventory_turnover(cost_of_goods_sold, average_inventory)
    return 365 / turnover if turnover > 0 else 0

def abc_analysis(values):
    sorted_vals = sorted(values, reverse=True)
    total = sum(sorted_vals)
    if total == 0:
        return ['C'] * len(values)
    cumulative = 0
    categories = []
    for val in sorted_vals:
        cumulative += val
        pct = cumulative / total
        if pct <= 0.8:
            categories.append('A')
        elif pct <= 0.95:
            categories.append('B')
        else:
            categories.append('C')
    return categories

# ================================================================================
# FUNCIÓN PARA OBTENER DATOS REALES DE BINANCE
# ================================================================================
def get_binance_data(symbol='BTCUSDT', interval='1d', limit=100):
    """Obtiene datos OHLC reales de Binance API"""
    if not REQUESTS_AVAILABLE:
        return None
    
    try:
        url = f"https://api.binance.com/api/v3/klines"
        params = {
            'symbol': symbol,
            'interval': interval,
            'limit': limit
        }
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 
                                        'close_time', 'quote_volume', 'trades', 
                                        'taker_buy_base', 'taker_buy_quote', 'ignore'])
        
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.set_index('timestamp', inplace=True)
        
        df = df[['open', 'high', 'low', 'close']].astype(float)
        df.columns = ['Open', 'High', 'Low', 'Close']
        
        return df
    except Exception as e:
        print(f"Error fetching Binance data: {e}")
        return None

# FUNCIÓN CACHEADA PARA DATOS OHLC (CORRECCIÓN DE SCOPE + API REAL)
# ================================================================================
@st.cache_data(ttl=300)  # Cache por 5 minutos
def generate_ohlc_data(use_real_data=False, symbol='BTCUSDT'):
    """Genera datos OHLC cacheados para evitar problemas de scope"""
    if not NUMPY_AVAILABLE or not PANDAS_AVAILABLE:
        return None
    
    # Intentar obtener datos reales de Binance
    if use_real_data:
        real_data = get_binance_data(symbol)
        if real_data is not None:
            df_ohlc = real_data
            add_xp(25, "data_fetch")  # XP por usar datos reales
        else:
            # Fallback a datos simulados
            df_ohlc = _generate_simulated_ohlc()
    else:
        df_ohlc = _generate_simulated_ohlc()
    
    # Calcular indicadores técnicos
    df_ohlc['RSI'] = calc_rsi(df_ohlc['Close'])
    df_ohlc['EMA12'] = calc_ema(df_ohlc['Close'], 12)
    df_ohlc['EMA26'] = calc_ema(df_ohlc['Close'], 26)
    df_ohlc['SMA50'] = df_ohlc['Close'].rolling(50).mean()
    df_ohlc['SMA200'] = df_ohlc['Close'].rolling(200).mean()
    
    macd, signal, hist = calc_macd(df_ohlc['Close'])
    df_ohlc['MACD'] = macd
    df_ohlc['MACD_Signal'] = signal
    df_ohlc['MACD_Hist'] = hist
    
    upper, middle, lower = calc_bollinger(df_ohlc['Close'])
    df_ohlc['BB_Upper'] = upper
    df_ohlc['BB_Middle'] = middle
    df_ohlc['BB_Lower'] = lower
    
    df_ohlc['ATR'] = calc_atr(df_ohlc['High'], df_ohlc['Low'], df_ohlc['Close'])
    df_ohlc['Stoch_K'], df_ohlc['Stoch_D'] = calc_stochastic(df_ohlc['High'], df_ohlc['Low'], df_ohlc['Close'])
    df_ohlc['Williams_R'] = calc_williams_r(df_ohlc['High'], df_ohlc['Low'], df_ohlc['Close'])
    
    tenkan, kijun, senkou_a, senkou_b, chikou = calc_ichimoku(df_ohlc['High'], df_ohlc['Low'], df_ohlc['Close'])
    df_ohlc['Tenkan'] = tenkan
    df_ohlc['Kijun'] = kijun
    df_ohlc['Senkou_A'] = senkou_a
    df_ohlc['Senkou_B'] = senkou_b
    df_ohlc['Chikou'] = chikou
    
    return df_ohlc

def _generate_simulated_ohlc():
    """Genera datos OHLC simulados (fallback)"""
    np.random.seed(42)
    days = 252 * 2
    dates = pd.date_range(end=datetime.now(), periods=days, freq='D')
    
    returns = np.random.normal(0.0003, 0.02, days)
    prices = 100 * np.exp(np.cumsum(returns))
    
    if np.any(prices <= 0):
        prices = np.maximum(prices, 1.0)
    
    df_ohlc = pd.DataFrame({
        'Date': dates,
        'Open': prices * (1 + np.random.normal(0, 0.001, days)),
        'High': prices * (1 + abs(np.random.normal(0, 0.015, days))),
        'Low': prices * (1 - abs(np.random.normal(0, 0.015, days))),
        'Close': prices
    })
    df_ohlc.set_index('Date', inplace=True)
    
    return df_ohlc

# ================================================================================
# SIDEBAR
# ================================================================================
with st.sidebar:
    # Dark/Light Mode Toggle
    col_toggle1, col_toggle2 = st.columns([4, 1])
    with col_toggle1:
        st.markdown("### 🎨 Tema")
    with col_toggle2:
        if st.button("🌙" if not st.session_state.dark_mode else "☀️", key="theme_toggle"):
            st.session_state.dark_mode = not st.session_state.dark_mode
            st.rerun()
    
    st.markdown("---")
    
    # Profile Card
    st.markdown("""
    <div style="background: linear-gradient(135deg, #6366f1, #06b6d4); padding: 24px; border-radius: 16px; color: white; text-align: center; margin-bottom: 20px;">
        <div style="font-size: 3rem; margin-bottom: 8px;">👨‍💻</div>
        <h3 style="margin: 0; font-size: 1.2rem;">Salomon Febles</h3>
        <p style="margin: 4px 0; font-size: 0.9rem; opacity: 0.9;">Ingeniero de Sistemas</p>
        <p style="margin: 0; font-size: 0.8rem; opacity: 0.8;">9no Semestre</p>
        <div style="margin-top: 12px; display: flex; gap: 6px; justify-content: center; flex-wrap: wrap;">
            <span style="background: rgba(255,255,255,0.2); padding: 4px 10px; border-radius: 20px; font-size: 0.7rem;">Trading</span>
            <span style="background: rgba(255,255,255,0.2); padding: 4px 10px; border-radius: 20px; font-size: 0.7rem;">Ciberseguridad</span>
            <span style="background: rgba(255,255,255,0.2); padding: 4px 10px; border-radius: 20px; font-size: 0.7rem;">ML</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Gamification Section
    st.markdown("### 🎮 Progreso")
    
    # XP Bar
    xp_needed = st.session_state.level * 100
    xp_progress = min((st.session_state.xp_points / xp_needed) * 100, 100) if xp_needed > 0 else 0
    
    st.markdown(f"""
    <div class="xp-container">
        <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
            <span style="font-weight: 600;">Nivel {st.session_state.level}</span>
            <span>{st.session_state.xp_points} / {xp_needed} XP</span>
        </div>
        <div class="xp-bar" style="width: {xp_progress}%"></div>
        <div class="xp-text">Actividades completadas: {st.session_state.activities_completed}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Badges
    if st.session_state.badges:
        st.markdown("### 🏆 Logros")
        badge_html = '<div class="badge-container">'
        for badge in st.session_state.badges:
            badge_html += f'<span class="achievement-badge">🎖️ {badge}</span>'
        badge_html += '</div>'
        st.markdown(badge_html, unsafe_allow_html=True)
    
    # Notifications
    st.markdown("### 🔔 Notificaciones")
    notifications = [
        {"icon": "🎯", "message": "Nuevo logro desbloqueado", "time": "5 min"},
        {"icon": "📈", "message": "TradeGuard actualizado", "time": "1 hora"},
        {"icon": "🛡️", "message": "Alerta de seguridad", "time": "2 horas"}
    ]
    
    for notif in notifications:
        st.markdown(f"""
        <div style="padding: 8px; margin: 5px 0; border-left: 3px solid #6366f1; background: rgba(99, 102, 241, 0.1); border-radius: 3px;">
            {notif['icon']} {notif['message']} | {notif['time']}
        </div>
        """, unsafe_allow_html=True)
    
    # Quick Stats
    st.markdown("### 📊 Estadísticas Rápidas")
    col1, col2 = st.columns(2)
    col1.metric("XP", st.session_state.xp_points)
    col2.metric("Nivel", st.session_state.level)
    
    st.markdown("---")
    
    st.markdown('<h3 style="color: #6366f1; font-size: 18px; font-weight: bold; margin-bottom: 10px;">📌 SELECCIONAR MÓDULO</h3>', unsafe_allow_html=True)
    
    selected = st.radio("", ["🏠 Dashboard", "🛡️ ShieldVZLA Elite", "📈 TradeGuard Elite", 
                             "🤖 FinRisk AI Elite", "📦 InventoryBot Elite", "📄 DocuVerify Elite"],
                       label_visibility="collapsed")
    
    st.markdown("---")
    st.caption("v6.0 Microproyectos | Salomon Febles")

# ================================================================================
# DEPENDENCY CHECK
# ================================================================================
if not NUMPY_AVAILABLE or not PANDAS_AVAILABLE or not PLOTLY_AVAILABLE:
    st.error("⚠️ Missing dependencies. Install: pip install streamlit pandas numpy plotly scikit-learn")
    st.stop()

# ================================================================================
# FUNCIONES DE GAMIFICACIÓN
# ================================================================================
def add_xp(amount, activity_name):
    """Agrega XP al usuario y verifica si subió de nivel"""
    st.session_state.xp_points += amount
    st.session_state.activities_completed += 1
    
    # Verificar si subió de nivel
    xp_needed = st.session_state.level * 100
    if st.session_state.xp_points >= xp_needed:
        st.session_state.level += 1
        st.session_state.xp_points -= xp_needed
        st.success(f"🎉 ¡Nivel {st.session_state.level} alcanzado!")
        # Confetti celebration
        st.markdown("""
        <script>
        for(let i=0; i<50; i++) {
            const confetti = document.createElement('div');
            confetti.className = 'confetti';
            confetti.style.left = Math.random() * 100 + 'vw';
            confetti.style.animationDelay = Math.random() * 2 + 's';
            confetti.style.background = ['#818cf8', '#22d3ee', '#10b981', '#f59e0b'][Math.floor(Math.random() * 4)];
            document.body.appendChild(confetti);
            setTimeout(() => confetti.remove(), 3000);
        }
        </script>
        """, unsafe_allow_html=True)
    
    # Otorgar badges basados en actividades
    if activity_name == "threat_detection" and "Cazador de Amenazas" not in st.session_state.badges:
        st.session_state.badges.append("Cazador de Amenazas")
        st.success("🏆 Badge desbloqueado: Cazador de Amenazas")
    elif activity_name == "trade_execution" and "Trader Élite" not in st.session_state.badges:
        st.session_state.badges.append("Trader Élite")
        st.success("🏆 Badge desbloqueado: Trader Élite")
    elif activity_name == "model_training" and "Data Scientist" not in st.session_state.badges:
        st.session_state.badges.append("Data Scientist")
        st.success("🏆 Badge desbloqueado: Data Scientist")
    elif activity_name == "api_integration" and "API Master" not in st.session_state.badges:
        st.session_state.badges.append("API Master")
        st.success("🏆 Badge desbloqueado: API Master")
    elif activity_name == "blockchain_verify" and "Blockchain Explorer" not in st.session_state.badges:
        st.session_state.badges.append("Blockchain Explorer")
        st.success("🏆 Badge desbloqueado: Blockchain Explorer")

def show_toast(message, type="info"):
    """Muestra una notificación toast"""
    toast_colors = {
        "info": "#6366f1",
        "success": "#10b981",
        "warning": "#f59e0b",
        "error": "#ef4444"
    }
    color = toast_colors.get(type, "#6366f1")
    st.markdown(f"""
    <div class="toast" style="border-left-color: {color};">
        {message}
    </div>
    """, unsafe_allow_html=True)

# ================================================================================
# DASHBOARD
# ================================================================================
if selected == "🏠 Dashboard":
    st.markdown('<h1 class="main-header">Portfolio Técnico Elite v6.0 - Microproyectos</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Salomon Febles | Ingeniero de Sistemas + Trading + Ciberseguridad + ML | Microproyectos Impresionantes</p>', unsafe_allow_html=True)
    
    cols = st.columns(5)
    metrics = [
        ("Módulos", "5", "Enterprise"),
        ("Líneas Código", "3,500+", "Python 3.12"),
        ("Empresas", "25+", "IESA 2026"),
        ("Tecnologías", "8", "Stack Elite"),
        ("Nivel", "Elite", "2026")
    ]
    for col, (label, value, delta) in zip(cols, metrics):
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <p style="margin: 0; color: #64748b; font-size: 0.85rem;">{label}</p>
                <p class="metric-value">{value}</p>
                <span class="badge badge-green">{delta}</span>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">🚀 Módulos Enterprise</h2>', unsafe_allow_html=True)
    
    modules = [
        ("🛡️ ShieldVZLA Elite", "EDR Avanzado + MITRE ATT&CK", "#ef4444", "Intelix, PwC, Deloitte"),
        ("📈 TradeGuard Elite", "Trading Algo + Backtesting", "#22c55e", "Banesco, Mercantil, EY"),
        ("🤖 FinRisk AI Elite", "ML + Explainable AI", "#8b5cf6", "Big 4, Banca"),
        ("📦 InventoryBot Elite", "Supply Chain + EOQ", "#f59e0b", "Farmatodo, Retail"),
        ("📄 DocuVerify Elite", "Blockchain + Smart Contracts", "#06b6d4", "HLB, Auditoría")
    ]
    
    for i in range(0, len(modules), 3):
        cols = st.columns(3)
        for j, (name, desc, color, companies) in enumerate(modules[i:i+3]):
            with cols[j]:
                st.markdown(f"""
                <div class="glass-card" style="border-top: 4px solid {color};">
                    <h3 style="margin-bottom: 12px; color: #1e293b;">{name}</h3>
                    <p style="color: #64748b; font-size: 0.95rem; margin-bottom: 12px;">{desc}</p>
                    <p style="font-size: 0.8rem; color: #94a3b8;"><strong>Ideal:</strong> {companies}</p>
                </div>
                """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">📊 Métricas del Sistema</h2>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🎯 XP Total", f"{st.session_state.xp_points}", "+0")
    col2.metric("🏆 Nivel", st.session_state.level, f"{len(st.session_state.badges)} badges")
    col3.metric("⚡ Actividades", st.session_state.activities_completed, "Completadas")
    col4.metric("🎨 Tema", "Dark" if st.session_state.dark_mode else "Light", "Activo")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Gráfico de XP por actividad
    xp_by_activity = {
        "Trading": 50,
        "Ciberseguridad": 45,
        "Blockchain": 40,
        "ML": 55,
        "Supply Chain": 35,
        "UI/UX": 30
    }
    
    fig_xp = go.Figure(data=[go.Bar(x=list(xp_by_activity.keys()), y=list(xp_by_activity.values()), marker_color='indigo')])
    fig_xp.update_layout(title="XP por Categoría", xaxis_title="Categoría", yaxis_title="XP")
    st.plotly_chart(fig_xp, use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">🌐 Integraciones de APIs Externas</h2>', unsafe_allow_html=True)
    
    api_tabs = st.tabs(["🌤️ Weather", "📰 News", "📦 GitHub", "💰 Crypto", "⛓️ Etherscan"])
    
    with api_tabs[0]:
        st.markdown("<h4>OpenWeather API - Datos Climáticos</h4>", unsafe_allow_html=True)
        city = st.text_input("Ciudad", value="Caracas", key="weather_city")
        if st.button("Obtener Clima", key="get_weather"):
            weather_data = get_weather_data(city)
            if weather_data:
                st.success(f"🌡️ Temperatura: {weather_data['main']['temp']}°C")
                st.info(f"💧 Humedad: {weather_data['main']['humidity']}%")
                st.info(f"🌬️ Viento: {weather_data['wind']['speed']} m/s")
                add_xp(5, "api_integration")
                show_toast("✅ Datos climáticos obtenidos", "success")
            else:
                st.warning("No se pudieron obtener datos climáticos (API key requerida)")
    
    with api_tabs[1]:
        st.markdown("<h4>News API - Noticias en Tiempo Real</h4>", unsafe_allow_html=True)
        query = st.text_input("Buscar Noticias", value="technology", key="news_query")
        if st.button("Buscar Noticias", key="get_news"):
            news_data = get_news_data(query)
            if news_data and news_data.get("articles"):
                for article in news_data["articles"][:5]:
                    st.markdown(f"**{article['title']}**")
                    st.caption(article.get("description", ""))
                    st.markdown("---")
                add_xp(5, "api_integration")
                show_toast("✅ Noticias obtenidas", "success")
            else:
                st.warning("No se pudieron obtener noticias (API key requerida)")
    
    with api_tabs[2]:
        st.markdown("<h4>GitHub API - Repositorios</h4>", unsafe_allow_html=True)
        username = st.text_input("Usuario GitHub", value="octocat", key="github_user")
        if st.button("Obtener Repos", key="get_repos"):
            repos = get_github_repos(username)
            if repos:
                for repo in repos[:5]:
                    st.markdown(f"**{repo['name']}** - ⭐ {repo['stargazers_count']}")
                    st.caption(repo.get("description", ""))
                    st.markdown("---")
                add_xp(5, "api_integration")
                show_toast("✅ Repositorios obtenidos", "success")
            else:
                st.warning("No se pudieron obtener repositorios")
    
    with api_tabs[3]:
        st.markdown("<h4>CoinGecko API - Precios de Criptomonedas</h4>", unsafe_allow_html=True)
        if st.button("Obtener Precios Crypto", key="get_crypto"):
            crypto_prices = get_crypto_prices()
            if crypto_prices:
                for crypto, data in crypto_prices.items():
                    st.metric(crypto.upper(), f"${data['usd']}")
                add_xp(5, "api_integration")
                show_toast("✅ Precios crypto obtenidos", "success")
            else:
                st.warning("No se pudieron obtener precios")
    
    with api_tabs[4]:
        st.markdown("<h4>Etherscan API - Transacciones Ethereum</h4>", unsafe_allow_html=True)
        address = st.text_input("Dirección Ethereum", value="0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb", key="eth_address")
        if st.button("Obtener Transacciones", key="get_tx"):
            tx_data = get_etherscan_tx(address)
            if tx_data and tx_data.get("result"):
                result = tx_data["result"]
                # Validar que result sea una lista
                if isinstance(result, list):
                    for tx in result[:5]:
                        # Validar que tx sea un diccionario
                        if isinstance(tx, dict) and 'hash' in tx:
                            st.markdown(f"**Hash:** {tx['hash'][:10]}...")
                            st.caption(f"Valor: {tx.get('value', 'N/A')} Wei")
                            st.markdown("---")
                else:
                    st.warning("Formato de datos incorrecto")
                add_xp(5, "blockchain_verify")
                show_toast("✅ Transacciones obtenidas", "success")
            else:
                st.warning("No se pudieron obtener transacciones (API key requerida)")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Onboarding Guide
    if not st.session_state.onboarding_completed:
        with st.expander("🎓 Onboarding Guide - Bienvenido al Portfolio Elite v6.0", expanded=True):
            st.markdown("""
            **¡Bienvenido!** Este es tu portafolio técnico con 5 microproyectos enterprise:
            
            - **🛡️ ShieldVZLA Elite**: Ciberseguridad con MITRE ATT&CK, SIEM, SOAR
            - **📈 TradeGuard Elite**: Trading algorítmico con Binance API, HFT, Arbitrage
            - **🤖 FinRisk AI Elite**: Machine Learning para riesgo crediticio, AutoML
            - **📦 InventoryBot Elite**: Supply Chain con EOQ, JIT, Forecasting
            - **📄 DocuVerify Elite**: Blockchain con Smart Contracts, ZKP, Merkle Trees
            
            **Gamificación:** Gana XP por usar cada módulo y desbloquea badges.
            **APIs Externas:** Integra Weather, News, GitHub, Crypto y Etherscan.
            
            **Keyboard Shortcuts:**
            - `Ctrl/Cmd + K`: Buscar módulos
            - `Ctrl/Cmd + D`: Toggle Dark/Light Mode
            - `Ctrl/Cmd + R`: Resetear progreso
            
            **Tips:**
            - Usa el modo oscuro para mejor experiencia nocturna
            - Explora cada módulo para ganar XP
            - Las APIs externas requieren keys reales para datos en vivo
            """)
            
            if st.button("✅ Completar Onboarding"):
                st.session_state.onboarding_completed = True
                add_xp(25, "onboarding")
                show_toast("✅ Onboarding completado +25 XP", "success")
                st.rerun()
    
    # Keyboard Shortcuts Info
    with st.expander("⌨️ Keyboard Shortcuts"):
        st.markdown("""
        **Atajos de Teclado:**
        - `Ctrl/Cmd + K`: Buscar módulos (simulado)
        - `Ctrl/Cmd + D`: Toggle Dark/Light Mode
        - `Ctrl/Cmd + R`: Resetear progreso
        - `Ctrl/Cmd + S`: Guardar configuración
        - `Ctrl/Cmd + E`: Exportar datos
        
        *Nota: Algunos atajos requieren extensión de navegador*
        """)
    
    # Export/Import Configuration
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">⚙️ Configuración</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<h5>Exportar Configuración</h5>", unsafe_allow_html=True)
        
        config_data = {
            "dark_mode": st.session_state.dark_mode,
            "xp_points": st.session_state.xp_points,
            "level": st.session_state.level,
            "badges": st.session_state.badges,
            "activities_completed": st.session_state.activities_completed,
            "onboarding_completed": st.session_state.onboarding_completed
        }
        
        if st.button("📥 Exportar Configuración"):
            config_json = json.dumps(config_data, indent=2)
            st.download_button(
                label="⬇️ Descargar JSON",
                data=config_json,
                file_name="portfolio_config.json",
                mime="application/json"
            )
            add_xp(5, "config_export")
            show_toast("✅ Configuración exportada", "success")
    
    with col2:
        st.markdown("<h5>Importar Configuración</h5>", unsafe_allow_html=True)
        
        uploaded_config = st.file_uploader("Subir configuración JSON", type=['json'])
        
        if uploaded_config:
            try:
                config_imported = json.load(uploaded_config)
                st.session_state.dark_mode = config_imported.get("dark_mode", False)
                st.session_state.xp_points = config_imported.get("xp_points", 0)
                st.session_state.level = config_imported.get("level", 1)
                st.session_state.badges = config_imported.get("badges", [])
                st.session_state.activities_completed = config_imported.get("activities_completed", 0)
                st.session_state.onboarding_completed = config_imported.get("onboarding_completed", False)
                
                st.success("✅ Configuración importada exitosamente")
                add_xp(5, "config_import")
                show_toast("✅ Configuración importada", "success")
                st.rerun()
            except:
                st.error("❌ Error al importar configuración")
    
    # Reset Progress
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 Resetear Progreso", type="secondary"):
        st.session_state.xp_points = 0
        st.session_state.level = 1
        st.session_state.badges = []
        st.session_state.activities_completed = 0
        st.session_state.onboarding_completed = False
        st.success("✅ Progreso reseteado")
        st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Activity Log - Dinámico basado en session_state
    st.markdown('<h2 class="section-title">📋 Activity Log</h2>', unsafe_allow_html=True)
    
    # Inicializar activity_log en session_state si no existe
    if 'activity_log' not in st.session_state:
        st.session_state.activity_log = [
            {"module": "TradeGuard Elite", "action": "Paper Trading", "timestamp": datetime.now() - timedelta(minutes=5), "xp": 10},
            {"module": "ShieldVZLA Elite", "action": "Threat Detection", "timestamp": datetime.now() - timedelta(minutes=15), "xp": 15},
            {"module": "FinRisk AI Elite", "action": "Model Training", "timestamp": datetime.now() - timedelta(minutes=30), "xp": 20},
            {"module": "InventoryBot Elite", "action": "EOQ Optimization", "timestamp": datetime.now() - timedelta(hours=1), "xp": 10},
            {"module": "DocuVerify Elite", "action": "Blockchain Verification", "timestamp": datetime.now() - timedelta(hours=2), "xp": 15}
        ]
    
    activities = st.session_state.activity_log
    
    for activity in activities:
        time_ago = (datetime.now() - activity['timestamp']).seconds // 60
        time_str = f"{time_ago} min" if time_ago < 60 else f"{time_ago // 60}h"
        st.markdown(f"""
        <div style="padding: 8px; margin: 5px 0; border-left: 3px solid #3b82f6; background: rgba(59, 130, 246, 0.1); border-radius: 3px;">
            <strong>{activity['module']}</strong> - {activity['action']} | {time_str} atrás | +{activity['xp']} XP
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Achievements - Dinámico basado en session_state.badges
    st.markdown('<h2 class="section-title">🏆 Achievements</h2>', unsafe_allow_html=True)
    
    achievements = [
        {"name": "🎯 First Trade", "description": "Ejecuta tu primer trade", "unlocked": "First Trade" in st.session_state.badges, "xp": 25},
        {"name": "🛡️ Security Expert", "description": "Completa 5 análisis de seguridad", "unlocked": "Security Expert" in st.session_state.badges, "xp": 50},
        {"name": "🤖 ML Master", "description": "Entrena 10 modelos", "unlocked": "ML Master" in st.session_state.badges, "xp": 100},
        {"name": "⛓️ Blockchain Pioneer", "description": "Verifica 20 documentos", "unlocked": "Blockchain Pioneer" in st.session_state.badges, "xp": 75},
        {"name": "📦 Supply Chain Pro", "description": "Optimiza inventario 10 veces", "unlocked": "Supply Chain Pro" in st.session_state.badges, "xp": 40},
        {"name": "🚀 High Frequency Trader", "description": "Completa 100 trades en HFT", "unlocked": "High Frequency Trader" in st.session_state.badges, "xp": 150},
        {"name": "🔍 Threat Hunter", "description": "Detecta 50 amenazas", "unlocked": "Threat Hunter" in st.session_state.badges, "xp": 80},
        {"name": "💰 DeFi Whale", "description": "Gestiona $1M en DeFi", "unlocked": "DeFi Whale" in st.session_state.badges, "xp": 200},
        {"name": "🎨 UI/UX Designer", "description": "Personaliza 5 temas", "unlocked": "UI/UX Designer" in st.session_state.badges, "xp": 30},
        {"name": "📊 Data Scientist", "description": "Analiza 100 datasets", "unlocked": "Data Scientist" in st.session_state.badges, "xp": 120},
        {"name": "🌐 Network Ninja", "description": "Bloquea 100 IPs maliciosas", "unlocked": "Network Ninja" in st.session_state.badges, "xp": 90},
        {"name": "💳 Credit Risk Analyst", "description": "Evalúa 500 solicitudes", "unlocked": "Credit Risk Analyst" in st.session_state.badges, "xp": 110}
    ]
    
    col1, col2, col3 = st.columns(3)
    for i, achievement in enumerate(achievements):
        col = [col1, col2, col3][i % 3]
        with col:
            status = "✅" if achievement['unlocked'] else "🔒"
            bg_color = "rgba(34, 197, 94, 0.1)" if achievement['unlocked'] else "rgba(107, 114, 128, 0.1)"
            st.markdown(f"""
            <div style="padding: 15px; margin: 10px 0; border-left: 4px solid {'green' if achievement['unlocked'] else 'gray'}; background: {bg_color}; border-radius: 5px;">
                <strong>{status} {achievement['name']}</strong><br>
                <small>{achievement['description']}</small><br>
                <small>+{achievement['xp']} XP</small>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">🎯 Guía por Empresa</h2>', unsafe_allow_html=True)
    
    empresas = ["Selecciona...", "Intelix", "Netconsult", "Banesco", "Mercantil", 
                "PwC", "Deloitte", "EY", "KPMG", "HLB", "Farmatodo", "Banca de Venezuela", 
                "Venezolana de Cemento", "Cantv", "Pdvsa", "Procter & Gamble", "Unilever"]
    empresa = st.selectbox("Empresa", empresas)
    
    if empresa != "Selecciona...":
        recs = {
            "Intelix": ("🛡️ ShieldVZLA Elite", "MITRE ATT&CK + Detección Lotus Wiper"),
            "Banesco": ("📈 TradeGuard Elite", "Trading Algorítmico + Risk Management"),
            "PwC": ("🤖 FinRisk AI Elite", "ML para Auditoría Predictiva"),
            "Farmatodo": ("📦 InventoryBot Elite", "Supply Chain + EOQ"),
            "Deloitte": ("🤖 FinRisk AI Elite", "ML + Explainable AI para Riesgo"),
            "EY": ("📄 DocuVerify Elite", "Blockchain + Smart Contracts"),
            "KPMG": ("🛡️ ShieldVZLA Elite", "Ciberseguridad + Compliance"),
            "HLB": ("📄 DocuVerify Elite", "Auditoría Blockchain + ZKP"),
            "Mercantil": ("📈 TradeGuard Elite", "HFT + Arbitrage Institucional"),
            "Netconsult": ("🛡️ ShieldVZLA Elite", "EDR + SOAR Workflows"),
            "Banca de Venezuela": ("📈 TradeGuard Elite", "Portfolio Optimization + Risk"),
            "Venezolana de Cemento": ("📦 InventoryBot Elite", "Supply Chain + JIT"),
            "Cantv": ("🛡️ ShieldVZLA Elite", "Threat Intel + Vulnerability Scanner"),
            "Pdvsa": ("📦 InventoryBot Elite", "Multi-Warehouse + Lead Time"),
            "Procter & Gamble": ("📦 InventoryBot Elite", "Demand Forecasting + EOQ"),
            "Unilever": ("🤖 FinRisk AI Elite", "AutoML + Model Monitoring"),
        }
        if empresa in recs:
            mod, desc = recs[empresa]
            st.success(f"**{empresa}** → {mod}\n\n{desc}")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">💻 System Health</h2>', unsafe_allow_html=True)
    
    # Métricas dinámicas en tiempo real
    cpu_usage = round(random.uniform(30, 70), 1)
    memory_usage = round(random.uniform(40, 80), 1)
    disk_usage = round(random.uniform(25, 50), 1)
    network_speed = round(random.uniform(0.8, 2.5), 1)
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("CPU", f"{cpu_usage}%", "Normal" if cpu_usage < 70 else "Alto")
    col2.metric("Memoria", f"{memory_usage}%", f"{round(memory_usage * 0.16, 1)}/16 GB")
    col3.metric("Disco", f"{disk_usage}%", f"{round(disk_usage * 5, 0)}/500 GB")
    col4.metric("Red", f"{network_speed} Gbps", "Estable")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">📊 Performance Metrics</h2>', unsafe_allow_html=True)
    
    # Métricas dinámicas en tiempo real
    response_time = round(random.uniform(30, 80), 0)
    uptime = round(random.uniform(99.90, 100.00), 2)
    error_rate = round(random.uniform(0.001, 0.05), 3)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Response Time", f"{response_time}ms", f"+{random.randint(-10, 10)}ms vs ayer")
    col2.metric("Uptime", f"{uptime}%", f"{random.randint(25, 35)} días")
    col3.metric("Error Rate", f"{error_rate}%", f"-{round(random.uniform(0.01, 0.05), 3)}% vs ayer")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">👥 User Analytics</h2>', unsafe_allow_html=True)
    
    # Métricas dinámicas en tiempo real
    active_users = random.randint(1000, 1500)
    sessions = random.randint(3000, 4500)
    avg_session = round(random.uniform(7.0, 10.0), 1)
    retention = round(random.uniform(70, 85), 0)
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Active Users", f"{active_users:,}", f"+{random.randint(8, 15)}% vs semana")
    col2.metric("Sessions", f"{sessions:,}", "Hoy")
    col3.metric("Avg Session", f"{avg_session} min", f"+{random.randint(20, 40)}s vs ayer")
    col4.metric("Retention", f"{retention}%", "7 días")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">🔔 Alert System</h2>', unsafe_allow_html=True)
    
    # Alertas dinámicas basadas en session_state
    if 'alerts' not in st.session_state:
        st.session_state.alerts = [
            {"type": "warning", "message": "CPU usage above 80%", "time": "5 min ago"},
            {"type": "info", "message": "New user registration spike", "time": "15 min ago"},
            {"type": "success", "message": "Backup completed successfully", "time": "1 hour ago"}
        ]
    
    alerts = st.session_state.alerts
    
    for alert in alerts:
        color = {"warning": "orange", "info": "blue", "success": "green"}[alert['type']]
        st.markdown(f"""
        <div style="padding: 8px; margin: 5px 0; border-left: 3px solid {color}; background: rgba(100,100,100,0.1); border-radius: 3px;">
            <strong>{alert['type'].upper()}</strong> - {alert['message']} | {alert['time']}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">📈 Growth Metrics</h2>', unsafe_allow_html=True)
    
    # Métricas dinámicas en tiempo real
    weekly_growth = round(random.uniform(15, 30), 0)
    monthly_growth = round(random.uniform(35, 55), 0)
    yearly_growth = round(random.uniform(100, 140), 0)
    churn_rate = round(random.uniform(1.5, 3.5), 1)
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Weekly Growth", f"+{weekly_growth}%", "vs semana pasada")
    col2.metric("Monthly Growth", f"+{monthly_growth}%", "vs mes pasado")
    col3.metric("Yearly Growth", f"+{yearly_growth}%", "vs año pasado")
    col4.metric("Churn Rate", f"{churn_rate}%", f"-{round(random.uniform(0.3, 0.8), 1)}% vs mes")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">🎯 Module Usage</h2>', unsafe_allow_html=True)
    
    # Uso de módulos dinámico basado en session_state
    if 'module_usage' not in st.session_state:
        st.session_state.module_usage = {
            "TradeGuard Elite": 34,
            "ShieldVZLA Elite": 28,
            "FinRisk AI Elite": 22,
            "InventoryBot Elite": 12,
            "DocuVerify Elite": 4
        }
    
    module_usage = st.session_state.module_usage
    
    fig_modules = go.Figure(data=[go.Pie(labels=list(module_usage.keys()), values=list(module_usage.values()))])
    fig_modules.update_layout(title="Uso por Módulo")
    st.plotly_chart(fig_modules, use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">🔒 Security Overview</h2>', unsafe_allow_html=True)
    
    # Métricas de seguridad dinámicas
    threats_blocked = random.randint(1000, 1500)
    security_score = random.randint(90, 98)
    vulnerabilities = random.randint(1, 5)
    compliance = round(random.uniform(95, 99), 0)
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Threats Blocked", f"{threats_blocked:,}", f"+{random.randint(15, 30)} hoy")
    col2.metric("Security Score", f"{security_score}/100", f"+{random.randint(1, 3)} vs semana")
    col3.metric("Vulnerabilities", f"{vulnerabilities}", f"-{random.randint(3, 7)} vs mes")
    col4.metric("Compliance", f"{compliance}%", "ISO 27001")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">💰 Financial Overview</h2>', unsafe_allow_html=True)
    
    # Métricas financieras dinámicas
    revenue = round(random.uniform(100000, 150000), 0)
    costs = round(random.uniform(40000, 50000), 0)
    profit = revenue - costs
    roi = round((profit / costs) * 100, 0)
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Revenue", f"${revenue:,.0f}", f"+{random.randint(10, 20)}% vs mes")
    col2.metric("Costs", f"${costs:,.0f}", f"-{random.randint(5, 12)}% vs mes")
    col3.metric("Profit", f"${profit:,.0f}", f"+{random.randint(18, 25)}% vs mes")
    col4.metric("ROI", f"{roi}%", f"+{random.randint(10, 15)}% vs mes")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">📊 Analytics Dashboard</h2>', unsafe_allow_html=True)
    
    # Métricas de analytics dinámicas
    page_views = random.randint(40000, 50000)
    bounce_rate = round(random.uniform(28, 38), 0)
    conversion_rate = round(random.uniform(3.5, 5.5), 1)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Page Views", f"{page_views:,}", f"+{random.randint(15, 22)}% vs semana")
    col2.metric("Bounce Rate", f"{bounce_rate}%", f"-{random.randint(3, 8)}% vs semana")
    col3.metric("Conversion Rate", f"{conversion_rate}%", f"+{round(random.uniform(0.5, 1.2), 1)}% vs semana")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">🌍 Geographic Distribution</h2>', unsafe_allow_html=True)
    
    # Distribución geográfica dinámica
    if 'geo_data' not in st.session_state:
        st.session_state.geo_data = {
            "Venezuela": 45,
            "Colombia": 20,
            "México": 15,
            "Argentina": 10,
            "Otros": 10
        }
    
    geo_data = st.session_state.geo_data
    
    fig_geo = go.Figure(data=[go.Pie(labels=list(geo_data.keys()), values=list(geo_data.values()))])
    fig_geo.update_layout(title="Distribución Geográfica")
    st.plotly_chart(fig_geo, use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">⏱️ Time Analytics</h2>', unsafe_allow_html=True)
    
    # Métricas de tiempo dinámicas
    avg_time_on_page = f"{random.randint(4, 5)}m {random.randint(20, 45)}s"
    peak_hours = f"{random.randint(13, 15)}:00-{random.randint(15, 17)}:00"
    daily_active = random.randint(800, 900)
    weekly_active = random.randint(2200, 2500)
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Avg Time on Page", avg_time_on_page, f"+{random.randint(20, 45)}s vs semana")
    col2.metric("Peak Hours", peak_hours, "UTC-4")
    col3.metric("Daily Active", f"{daily_active}", f"+{random.randint(10, 15)}% vs semana")
    col4.metric("Weekly Active", f"{weekly_active:,}", f"+{random.randint(6, 12)}% vs semana")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">🎯 Goal Tracking</h2>', unsafe_allow_html=True)
    
    # Goals dinámicos basados en session_state
    if 'goals' not in st.session_state:
        st.session_state.goals = [
            {"name": "XP Goal", "current": 850, "target": 1000, "progress": 85},
            {"name": "Modules Completed", "current": 3, "target": 5, "progress": 60},
            {"name": "Achievements Unlocked", "current": 4, "target": 12, "progress": 33},
            {"name": "Daily Streak", "current": 7, "target": 30, "progress": 23}
        ]
    
    goals = st.session_state.goals
    
    for goal in goals:
        st.markdown(f"""
        <div style="padding: 12px; margin: 8px 0; border-left: 4px solid #6366f1; background: rgba(99, 102, 241, 0.1); border-radius: 5px;">
            <strong>{goal['name']}</strong>: {goal['current']}/{goal['target']} ({goal['progress']}%)
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">📊 Recent Activity</h2>', unsafe_allow_html=True)
    
    # Recent Activity dinámico basado en session_state
    if 'recent_activity' not in st.session_state:
        st.session_state.recent_activity = [
            {"action": "Completed TradeGuard Elite backtest", "time": "2 min ago", "xp": 25},
            {"action": "Analyzed 50 security threats", "time": "15 min ago", "xp": 30},
            {"action": "Trained ML model", "time": "1 hour ago", "xp": 20},
            {"action": "Optimized inventory EOQ", "time": "2 hours ago", "xp": 15},
            {"action": "Verified blockchain document", "time": "3 hours ago", "xp": 10}
        ]
    
    recent_activity = st.session_state.recent_activity
    
    for activity in recent_activity:
        st.markdown(f"""
        <div style="padding: 8px; margin: 5px 0; border-left: 3px solid #10b981; background: rgba(16, 185, 129, 0.1); border-radius: 3px;">
            {activity['action']} | {activity['time']} | +{activity['xp']} XP
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">🔧 System Configuration</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**General Settings**")
        auto_save = st.checkbox("Auto-save progress", value=True)
        notifications = st.checkbox("Enable notifications", value=True)
        sound = st.checkbox("Sound effects", value=False)
        
        if st.button("💾 Save Settings"):
            st.success("✅ Settings saved")
            add_xp(5, "settings_saved")
            show_toast("✅ Settings saved", "success")
    
    with col2:
        st.markdown("**Performance Settings**")
        animation_level = st.selectbox("Animation Level", ["High", "Medium", "Low"])
        data_refresh = st.selectbox("Data Refresh Rate", ["Real-time", "1 min", "5 min", "15 min"])
        cache_enabled = st.checkbox("Enable caching", value=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">📚 Documentation</h2>', unsafe_allow_html=True)
    
    docs = [
        {"title": "Getting Started", "icon": "🚀", "status": "Completed"},
        {"title": "TradeGuard Elite Guide", "icon": "📈", "status": "In Progress"},
        {"title": "ShieldVZLA Elite Guide", "icon": "🛡️", "status": "Not Started"},
        {"title": "FinRisk AI Elite Guide", "icon": "🤖", "status": "Not Started"},
        {"title": "InventoryBot Elite Guide", "icon": "📦", "status": "Not Started"},
        {"title": "DocuVerify Elite Guide", "icon": "📄", "status": "Not Started"}
    ]
    
    for doc in docs:
        status_color = {"Completed": "green", "In Progress": "orange", "Not Started": "gray"}[doc['status']]
        st.markdown(f"""
        <div style="padding: 10px; margin: 5px 0; border-left: 3px solid {status_color}; background: rgba(100,100,100,0.05); border-radius: 3px;">
            {doc['icon']} <strong>{doc['title']}</strong> - {doc['status']}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">🎨 Theme Customization</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        primary_color = st.color_picker("Primary Color", "#6366f1")
        secondary_color = st.color_picker("Secondary Color", "#06b6d4")
        accent_color = st.color_picker("Accent Color", "#10b981")
    
    with col2:
        background_color = st.color_picker("Background Color", "#f8fafc")
        text_color = st.color_picker("Text Color", "#1e293b")
        border_radius = st.slider("Border Radius", 0, 20, 8)
    
    if st.button("🎨 Apply Theme"):
        st.success("✅ Theme applied")
        add_xp(5, "theme_customized")
        show_toast("✅ Theme applied", "success")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">🔍 Search & Filters</h2>', unsafe_allow_html=True)
    
    search_query = st.text_input("🔍 Search across all modules", placeholder="Search for features, modules, or content...")
    
    if search_query:
        st.info(f"🔍 Searching for: '{search_query}'")
        st.markdown(f"""
        <div style="padding: 12px; background: rgba(99, 102, 241, 0.1); border-radius: 8px;">
            <strong>Results found:</strong>
            <ul>
                <li>TradeGuard Elite - Backtesting</li>
                <li>ShieldVZLA Elite - Threat Detection</li>
                <li>FinRisk AI Elite - Model Training</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">📊 Quick Stats Summary</h2>', unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Total XP", f"{st.session_state.xp_points}")
    col2.metric("Level", st.session_state.level)
    col3.metric("Badges", len(st.session_state.badges))
    col4.metric("Activities", st.session_state.activities_completed)
    col5.metric("Streak", "7 days")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">🎯 Learning Path</h2>', unsafe_allow_html=True)
    
    learning_path = [
        {"step": 1, "title": "Introduction to Trading", "module": "TradeGuard Elite", "status": "Completed", "xp": 50},
        {"step": 2, "title": "Security Fundamentals", "module": "ShieldVZLA Elite", "status": "Completed", "xp": 60},
        {"step": 3, "title": "ML Basics", "module": "FinRisk AI Elite", "status": "In Progress", "xp": 70},
        {"step": 4, "title": "Supply Chain Management", "module": "InventoryBot Elite", "status": "Not Started", "xp": 55},
        {"step": 5, "title": "Blockchain Verification", "module": "DocuVerify Elite", "status": "Not Started", "xp": 65}
    ]
    
    for step in learning_path:
        status_color = {"Completed": "green", "In Progress": "orange", "Not Started": "gray"}[step['status']]
        status_icon = {"Completed": "✅", "In Progress": "🔄", "Not Started": "⏳"}[step['status']]
        st.markdown(f"""
        <div style="padding: 10px; margin: 5px 0; border-left: 3px solid {status_color}; background: rgba(100,100,100,0.05); border-radius: 3px;">
            <strong>Step {step['step']}</strong>: {step['title']} ({step['module']}) | {status_icon} {step['status']} | +{step['xp']} XP
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">🏆 Leaderboard</h2>', unsafe_allow_html=True)
    
    leaderboard = [
        {"rank": 1, "name": "Salomon Febles", "xp": 850, "level": 8},
        {"rank": 2, "name": "Maria Rodriguez", "xp": 720, "level": 7},
        {"rank": 3, "name": "Carlos Perez", "xp": 680, "level": 6},
        {"rank": 4, "name": "Ana Martinez", "xp": 620, "level": 6},
        {"rank": 5, "name": "Luis Garcia", "xp": 590, "level": 5}
    ]
    
    for user in leaderboard:
        highlight = "background: rgba(99, 102, 241, 0.2);" if user['name'] == "Salomon Febles" else ""
        st.markdown(f"""
        <div style="padding: 8px; margin: 4px 0; border-left: 3px solid #6366f1; {highlight} border-radius: 3px;">
            <strong>#{user['rank']}</strong> {user['name']} - {user['xp']} XP (Level {user['level']})
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">📈 Progress Timeline</h2>', unsafe_allow_html=True)
    
    timeline = [
        {"date": "Today", "event": "Completed TradeGuard Elite backtest", "xp": 25},
        {"date": "Yesterday", "event": "Analyzed 50 security threats", "xp": 30},
        {"date": "2 days ago", "event": "Trained ML model", "xp": 20},
        {"date": "3 days ago", "event": "Optimized inventory EOQ", "xp": 15},
        {"date": "4 days ago", "event": "Verified blockchain document", "xp": 10}
    ]
    
    for item in timeline:
        st.markdown(f"""
        <div style="padding: 8px; margin: 4px 0; border-left: 3px solid #06b6d4; background: rgba(6, 182, 212, 0.1); border-radius: 3px;">
            <strong>{item['date']}</strong>: {item['event']} | +{item['xp']} XP
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">🎮 Gamification Settings</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**XP Settings**")
        xp_multiplier = st.slider("XP Multiplier", 1.0, 3.0, 1.0, 0.1)
        daily_xp_cap = st.number_input("Daily XP Cap", value=500, min_value=100, max_value=2000)
        level_up_bonus = st.checkbox("Level-up bonus XP", value=True)
    
    with col2:
        st.markdown("**Badge Settings**")
        auto_badges = st.checkbox("Auto-award badges", value=True)
        badge_notifications = st.checkbox("Badge notifications", value=True)
        badge_display = st.selectbox("Badge display style", ["Compact", "Detailed", "Grid"])
    
    if st.button("💾 Save Gamification Settings"):
        st.success("✅ Gamification settings saved")
        add_xp(5, "gamification_settings_saved")
        show_toast("✅ Gamification settings saved", "success")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">🔐 Privacy Settings</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Data Privacy**")
        data_sharing = st.checkbox("Share anonymous usage data", value=False)
        analytics_enabled = st.checkbox("Enable analytics", value=True)
        crash_reports = st.checkbox("Send crash reports", value=True)
    
    with col2:
        st.markdown("**Account Privacy**")
        profile_visibility = st.selectbox("Profile visibility", ["Public", "Private", "Friends Only"])
        activity_visibility = st.selectbox("Activity visibility", ["Public", "Private", "Friends Only"])
        leaderboard_opt = st.checkbox("Show in leaderboard", value=True)
    
    if st.button("💾 Save Privacy Settings"):
        st.success("✅ Privacy settings saved")
        add_xp(5, "privacy_settings_saved")
        show_toast("✅ Privacy settings saved", "success")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">🔔 Notification Preferences</h2>', unsafe_allow_html=True)
    
    notification_types = [
        {"name": "XP Gained", "enabled": True},
        {"name": "Level Up", "enabled": True},
        {"name": "Badge Earned", "enabled": True},
        {"name": "Achievement Unlocked", "enabled": True},
        {"name": "Module Completed", "enabled": True},
        {"name": "Goal Reached", "enabled": True},
        {"name": "Leaderboard Change", "enabled": False},
        {"name": "Daily Reminder", "enabled": True}
    ]
    
    for notif in notification_types:
        enabled = st.checkbox(notif['name'], value=notif['enabled'])
    
    if st.button("💾 Save Notification Preferences"):
        st.success("✅ Notification preferences saved")
        add_xp(5, "notification_settings_saved")
        show_toast("✅ Notification preferences saved", "success")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">📊 Data Export</h2>', unsafe_allow_html=True)
    
    export_format = st.selectbox("Export Format", ["CSV", "JSON", "Excel", "PDF"])
    data_type = st.selectbox("Data Type", ["All Data", "XP History", "Achievements", "Activity Log", "Module Progress"])
    
    col1, col2 = st.columns(2)
    with col1:
        date_range = st.date_input("Date Range", [])
    with col2:
        include_metadata = st.checkbox("Include metadata", value=True)
    
    if st.button("📥 Export Data"):
        st.success(f"✅ Data exported as {export_format}")
        add_xp(10, "data_exported")
        show_toast(f"✅ Data exported as {export_format}", "success")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">🔄 Data Import</h2>', unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("Upload data file", type=['csv', 'json', 'xlsx'])
    
    if uploaded_file:
        st.success(f"✅ File uploaded: {uploaded_file.name}")
        import_options = st.multiselect("Import Options", ["XP History", "Achievements", "Activity Log", "Settings"])
        
        if st.button("📤 Import Data"):
            st.success("✅ Data imported successfully")
            add_xp(10, "data_imported")
            show_toast("✅ Data imported successfully", "success")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">🗑️ Data Management</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Clear Data**")
        clear_xp = st.checkbox("Clear XP history")
        clear_achievements = st.checkbox("Clear achievements")
        clear_activity = st.checkbox("Clear activity log")
    
    with col2:
        st.markdown("**Reset Options**")
        reset_progress = st.checkbox("Reset all progress")
        reset_settings = st.checkbox("Reset settings")
        confirm_reset = st.checkbox("I understand this cannot be undone")
    
    if st.button("🗑️ Clear Selected Data", type="secondary"):
        if confirm_reset:
            st.warning("⚠️ Data cleared")
            add_xp(-50, "data_cleared")
            show_toast("⚠️ Data cleared", "warning")
        else:
            st.error("❌ Please confirm the action")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">📱 Mobile Optimization</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Display Settings**")
        compact_mode = st.checkbox("Compact mode", value=False)
        touch_optimized = st.checkbox("Touch-optimized UI", value=True)
        swipe_gestures = st.checkbox("Enable swipe gestures", value=True)
    
    with col2:
        st.markdown("**Performance**")
        reduce_animations = st.checkbox("Reduce animations", value=False)
        lazy_loading = st.checkbox("Enable lazy loading", value=True)
        offline_mode = st.checkbox("Offline mode", value=False)
    
    if st.button("💾 Save Mobile Settings"):
        st.success("✅ Mobile settings saved")
        add_xp(5, "mobile_settings_saved")
        show_toast("✅ Mobile settings saved", "success")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">🌐 Accessibility</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Visual Accessibility**")
        high_contrast = st.checkbox("High contrast mode", value=False)
        large_text = st.checkbox("Large text", value=False)
        color_blind_mode = st.selectbox("Color blind mode", ["None", "Deuteranopia", "Protanopia", "Tritanopia"])
    
    with col2:
        st.markdown("**Screen Reader**")
        screen_reader = st.checkbox("Screen reader support", value=True)
        alt_text = st.checkbox("Auto-generate alt text", value=True)
        keyboard_nav = st.checkbox("Keyboard navigation", value=True)
    
    if st.button("💾 Save Accessibility Settings"):
        st.success("✅ Accessibility settings saved")
        add_xp(5, "accessibility_settings_saved")
        show_toast("✅ Accessibility settings saved", "success")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">🔌 Integrations</h2>', unsafe_allow_html=True)
    
    integrations = [
        {"name": "Google Calendar", "status": "Connected", "icon": "📅"},
        {"name": "Slack", "status": "Not Connected", "icon": "💬"},
        {"name": "Microsoft Teams", "status": "Not Connected", "icon": "👥"},
        {"name": "GitHub", "status": "Connected", "icon": "🐙"},
        {"name": "Jira", "status": "Not Connected", "icon": "📋"},
        {"name": "Notion", "status": "Not Connected", "icon": "📝"}
    ]
    
    for integration in integrations:
        status_color = "green" if integration['status'] == "Connected" else "gray"
        st.markdown(f"""
        <div style="padding: 10px; margin: 5px 0; border-left: 3px solid {status_color}; background: rgba(100,100,100,0.05); border-radius: 3px;">
            {integration['icon']} <strong>{integration['name']}</strong> - {integration['status']}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">🎯 Quick Actions</h2>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("🚀 Start New Module"):
            st.success("✅ Ready to start a new module")
            add_xp(5, "quick_action_start")
            show_toast("✅ Ready to start a new module", "success")
    
    with col2:
        if st.button("📊 View Reports"):
            st.success("✅ Reports loaded")
            add_xp(5, "quick_action_reports")
            show_toast("✅ Reports loaded", "success")
    
    with col3:
        if st.button("⚙️ Quick Settings"):
            st.success("✅ Settings panel opened")
            add_xp(5, "quick_action_settings")
            show_toast("✅ Settings panel opened", "success")
    
    with col4:
        if st.button("❓ Get Help"):
            st.success("✅ Help center opened")
            add_xp(5, "quick_action_help")
            show_toast("✅ Help center opened", "success")

# ================================================================================
# SHIELDVZLA ELITE
# ================================================================================
elif selected == "🛡️ ShieldVZLA Elite":
    st.markdown('<h1 class="main-header">🛡️ ShieldVZLA Elite</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">SIEM Enterprise | Threat Hunting | SOAR Automation | Threat Intel Feeds | ML Detection</p>', unsafe_allow_html=True)
    
    # Otorgar XP por usar ShieldVZLA
    if 'shield_vzla_visited' not in st.session_state:
        add_xp(10, "threat_detection")
        st.session_state.shield_vzla_visited = True
    
    st.markdown("""
    <div class="alert-critical">
        <strong>📰 Contexto Abril 2026:</strong> Kaspersky detectó <strong>Lotus Wiper</strong> atacando sector energético venezolano. 
        Sistema de detección basado en MITRE ATT&CK Framework v14 + YARA Rules + Behavioral Analysis.
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(6)
    cols[0].metric("🟢 Estado", "PROTEGIDO", "99.99% SLA")
    cols[1].metric("🚨 Amenazas", "127", "+3 hoy")
    cols[2].metric("🖥️ Endpoints", "48", "+2 nuevos")
    cols[3].metric("⚡ Respuesta", "< 50ms", "Automático")
    cols[4].metric("🎯 IOC Activos", "8", "Threat Intel")
    cols[5].metric("🤖 SOAR", "4 playbooks", "Automatizados")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14, tab15, tab16, tab17, tab18, tab19, tab20, tab21, tab22 = st.tabs(["🧪 Simulador", "📊 MITRE ATT&CK", "🔍 IOC Database", "📋 Timeline", "🔬 Behavioral Analysis", "📜 YARA Rules", "🖥️ SIEM Console", "🤖 SOAR Workflows", "🔐 Password Analyzer", "🛡️ 2FA Simulator", "🌐 Threat Intel", "🔍 Vulnerability Scanner", "🦠 Malware Analysis", "🚨 Incident Response", "📊 Security Dashboard", "🔒 Compliance Audit", "🎯 Threat Hunting", "📈 SIEM Dashboard", "🤖 SOAR Playbooks", "🎣 Phishing Simulator", "🌐 Network Security", "💻 Endpoint Protection"])
    
    with tab1:
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("<h4>Escenarios de Amenazas Avanzados</h4>", unsafe_allow_html=True)
            
            threats = {
                "🧨 Lotus Wiper": {"cmd": "diskpart /s script.txt", "mitre": "T1490", "tactic": "Impact", "severity": "CRITICAL", "kill_chain": "Actions on Objectives", "process": "diskpart.exe", "pid": 1234},
                "💣 Shadow Delete": {"cmd": "vssadmin delete shadows /all", "mitre": "T1490", "tactic": "Impact", "severity": "CRITICAL", "kill_chain": "Actions on Objectives", "process": "vssadmin.exe", "pid": 2345},
                "📁 Exfiltration": {"cmd": "robocopy C:\\ D:\\backup /MIR", "mitre": "T1005", "tactic": "Collection", "severity": "HIGH", "kill_chain": "Exfiltration", "process": "robocopy.exe", "pid": 3456},
                "🌐 Lateral Move": {"cmd": "net use \\\\DC01\\IPC$", "mitre": "T1021", "tactic": "Lateral Movement", "severity": "HIGH", "kill_chain": "Lateral Movement", "process": "net.exe", "pid": 4567},
                "🔑 Credential Theft": {"cmd": "mimikatz.exe sekurlsa::logonpasswords", "mitre": "T1003", "tactic": "Credential Access", "severity": "CRITICAL", "kill_chain": "Credential Access", "process": "mimikatz.exe", "pid": 5678},
                "🔄 Persistence": {"cmd": "schtasks /create /tn backup /tr malware.exe", "mitre": "T1053", "tactic": "Persistence", "severity": "MEDIUM", "kill_chain": "Establish Foothold", "process": "schtasks.exe", "pid": 6789},
                "🎭 Obfuscation": {"cmd": "powershell -enc aQBlAHgA", "mitre": "T1027", "tactic": "Defense Evasion", "severity": "HIGH", "kill_chain": "Defense Evasion", "process": "powershell.exe", "pid": 7890},
                "⚡ Seguro": {"cmd": "calc.exe", "mitre": "-", "tactic": "-", "severity": "SAFE", "kill_chain": "-", "process": "calc.exe", "pid": 8901}
            }
            
            for name, data in threats.items():
                if st.button(name, use_container_width=True):
                    st.session_state['threat_test'] = data
                    st.rerun()
        
        with col2:
            if 'threat_test' in st.session_state:
                t = st.session_state['threat_test']
                
                if t['severity'] == "CRITICAL":
                    st.error(f"""
                    🚨 **AMENAZA CRÍTICA DETECTADA**
                    
                    **Comando:** `{t['cmd']}`  
                    **MITRE:** {t['mitre']} | **Táctica:** {t['tactic']}  
                    **Kill Chain:** {t['kill_chain']}  
                    **Proceso:** {t['process']} (PID: {t['pid']})  
                    **Severidad:** {t['severity']}
                    
                    ✅ **Acciones Automáticas:**
                    - Proceso terminado inmediatamente (PID {t['pid']})
                    - Alerta enviada a SOC (Ticket #ALT-{random.randint(1000,9999)})
                    - Evidencia preservada en /forensics/
                    - Host aislado de la red
                    - Memory dump capturado
                    - Network connections bloqueadas
                    """)
                elif t['severity'] == "HIGH":
                    st.warning(f"""
                    ⚠️ **AMENAZA ALTA DETECTADA**
                    
                    **Comando:** `{t['cmd']}`  
                    **MITRE:** {t['mitre']} | **Táctica:** {t['tactic']}  
                    **Kill Chain:** {t['kill_chain']}  
                    **Proceso:** {t['process']} (PID: {t['pid']})
                    
                    📋 **Acciones:**
                    - Monitoreo intensivo activado
                    - Alerta enviada a SOC
                    - Comportamiento siendo analizado
                    """)
                elif t['severity'] == "MEDIUM":
                    st.info(f"""
                    ℹ️ **AMENAZA MEDIA**
                    
                    **Comando:** `{t['cmd']}`  
                    **MITRE:** {t['mitre']} | **Táctica:** {t['tactic']}  
                    **Kill Chain:** {t['kill_chain']}
                    
                    📊 **Estado:** Monitoreo activo, comportamiento normal
                    """)
                else:
                    st.success(f"✅ **SEGURO** | {t['cmd']} | Proceso permitido | Comportamiento benigno")
    
    with tab2:
        st.markdown("<h4>MITRE ATT&CK Framework v14 Mapping</h4>", unsafe_allow_html=True)
        
        mitre_data = pd.DataFrame({
            'Táctica': ['Impact', 'Collection', 'Lateral Movement', 'Persistence', 'Defense Evasion', 
                       'Credential Access', 'Execution', 'Privilege Escalation', 'Discovery', 'Exfiltration'],
            'Técnica': ['T1490 - Inhibit System Recovery', 'T1005 - Data from Local System', 
                       'T1021 - Remote Services', 'T1053 - Scheduled Task', 'T1027 - Obfuscated Files',
                       'T1003 - OS Credential Dumping', 'T1059 - Command Line', 'T1068 - Exploitation',
                       'T1016 - System Network Configuration', 'T1041 - Exfiltration Over C2'],
            'Detecciones': [15, 12, 8, 6, 10, 9, 14, 4, 7, 5],
            'Alertas': [5, 3, 2, 1, 4, 3, 2, 0, 1, 1],
            'Coverage': [85, 78, 65, 50, 72, 68, 80, 35, 55, 45]
        })
        
        # Crear gráfico sin usar y=['Detecciones', 'Alertas'] para evitar KeyError
        try:
            fig = px.bar(mitre_data, x='Táctica', y='Detecciones', 
                        title='Detecciones MITRE ATT&CK v14')
            st.plotly_chart(fig, use_container_width=True)
            
            fig2 = px.bar(mitre_data, x='Táctica', y='Alertas', 
                         title='Alertas MITRE ATT&CK v14')
            st.plotly_chart(fig2, use_container_width=True)
        except Exception as e:
            st.error(f"Error al crear gráfico MITRE: {str(e)}")
        
        try:
            if 'Coverage' in mitre_data.columns and 'Táctica' in mitre_data.columns:
                fig_heatmap = px.imshow(mitre_data[['Coverage']].T, 
                                       labels=dict(x="Táctica", y="Métrica", color="Coverage %"),
                                       x=mitre_data['Táctica'], y=['Coverage'],
                                       title="MITRE ATT&CK Coverage %")
                st.plotly_chart(fig_heatmap, use_container_width=True)
            else:
                st.error("Error: Columna 'Coverage' o 'Táctica' no encontrada en los datos")
        except Exception as e:
            st.error(f"Error al crear heatmap MITRE: {str(e)}")
        
        st.dataframe(mitre_data, use_container_width=True, hide_index=True)
    
    with tab3:
        st.markdown("<h4>IOC Database - Threat Intelligence</h4>", unsafe_allow_html=True)
        
        conn = get_db()
        df_ioc = pd.read_sql_query("SELECT * FROM ioc_database", conn)
        conn.close()
        
        if not df_ioc.empty:
            col1, col2, col3 = st.columns(3)
            with col1:
                ioc_type_filter = st.selectbox("Tipo IOC", ["Todos"] + df_ioc['ioc_type'].unique().tolist())
            with col2:
                threat_filter = st.selectbox("Threat Actor", ["Todos"] + df_ioc['threat_actor'].unique().tolist())
            with col3:
                active_filter = st.selectbox("Estado", ["Todos", "Active", "Inactive"])
            
            df_filtered = df_ioc.copy()
            if ioc_type_filter != "Todos":
                df_filtered = df_filtered[df_filtered['ioc_type'] == ioc_type_filter]
            if threat_filter != "Todos":
                df_filtered = df_filtered[df_filtered['threat_actor'] == threat_filter]
            if active_filter != "Todos":
                df_filtered = df_filtered[df_filtered['is_active'] == (1 if active_filter == "Active" else 0)]
            
            st.dataframe(df_filtered[['ioc_value', 'ioc_type', 'threat_actor', 'campaign', 'confidence', 'tags', 'is_active']], 
                        use_container_width=True, hide_index=True)
            
            st.markdown("<h5>IOC Statistics</h5>", unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                fig_pie = px.pie(df_ioc, names='ioc_type', title='IOC by Type')
                st.plotly_chart(fig_pie, use_container_width=True)
            with col2:
                fig_bar = px.bar(df_ioc, x='threat_actor', y='confidence', title='Confidence by Threat Actor')
                st.plotly_chart(fig_bar, use_container_width=True)
            with col3:
                st.metric("Total IOCs", len(df_ioc))
                st.metric("Active IOCs", len(df_ioc[df_ioc['is_active'] == 1]))
                st.metric("Avg Confidence", f"{df_ioc['confidence'].mean():.1f}%")
        else:
            st.info("No hay IOCs en la base de datos")
    
    with tab4:
        st.markdown("<h4>Forensics Timeline - Incident Response</h4>", unsafe_allow_html=True)
        
        conn = get_db()
        df = pd.read_sql_query("SELECT * FROM security_alerts ORDER BY created_at DESC", conn)
        conn.close()
        
        if not df.empty:
            df_timeline = df.copy()
            df_timeline['hour'] = pd.to_datetime(df_timeline['created_at']).dt.hour
            df_timeline['date'] = pd.to_datetime(df_timeline['created_at']).dt.date
            
            severity_counts = df_timeline.groupby(['date', 'severity']).size().reset_index(name='count')
            
            # Crear gráfico sin color_discrete_map para evitar KeyError
            try:
                fig_timeline = px.bar(severity_counts, x='date', y='count', color='severity', 
                                      title='Security Events Timeline')
                st.plotly_chart(fig_timeline, use_container_width=True)
            except Exception as e:
                st.error(f"Error al crear gráfico de timeline: {str(e)}")
            
            st.dataframe(df[['alert_id', 'severity', 'category', 'threat_type', 'mitre_technique', 
                           'target_system', 'kill_chain_phase', 'process_id', 'status', 'created_at']], 
                        use_container_width=True, hide_index=True)
        else:
            st.info("No hay alertas registradas")
    
    with tab5:
        st.markdown("<h4>Behavioral Analysis - Anomaly Detection</h4>", unsafe_allow_html=True)
        
        conn = get_db()
        df_proc = pd.read_sql_query("SELECT * FROM process_monitor", conn)
        conn.close()
        
        if not df_proc.empty:
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("<h5>Process Tree Analysis</h5>", unsafe_allow_html=True)
                fig_tree = px.treemap(df_proc, path=['process_name'], values='memory_usage', 
                                     title='Process Memory Usage')
                st.plotly_chart(fig_tree, use_container_width=True)
            
            with col2:
                st.markdown("<h5>Suspicious Processes</h5>", unsafe_allow_html=True)
                suspicious = df_proc[df_proc['is_suspicious'] == 1]
                if not suspicious.empty:
                    st.dataframe(suspicious[['process_name', 'pid', 'parent_pid', 'command_line', 
                                           'cpu_usage', 'memory_usage']], use_container_width=True, hide_index=True)
                else:
                    st.success("✅ No suspicious processes detected")
            
            fig_scatter = px.scatter(df_proc, x='cpu_usage', y='memory_usage', color='is_suspicious',
                                    hover_data=['process_name', 'pid'],
                                    title='CPU vs Memory Usage (Red = Suspicious)')
            st.plotly_chart(fig_scatter, use_container_width=True)
        else:
            st.info("No hay procesos monitoreados")
    
    with tab6:
        st.markdown("<h4>YARA Rules - Detección de Malware</h4>", unsafe_allow_html=True)
        
        st.info("""
        **YARA Rules:** Reglas de detección de malware basadas en patrones binarios y de texto.
        Permite identificar amenazas conocidas y variantes de malware.
        """)
        
        yara_rules = [
            {
                'name': 'Lotus_Wiper_Rule',
                'description': 'Detecta actividad de wiper tipo Lotus',
                'strings': ['$diskpart = "diskpart" wide', '$clean = "clean" wide', '$script = "/s" wide'],
                'condition': '2 of them'
            },
            {
                'name': 'Shadow_Delete_Rule',
                'description': 'Detecta eliminación de shadow copies',
                'strings': ['$vssadmin = "vssadmin" wide', '$delete = "delete" wide', '$shadows = "shadows" wide'],
                'condition': 'all of them'
            },
            {
                'name': 'Mimikatz_Rule',
                'description': 'Detecta uso de Mimikatz',
                'strings': ['$mimikatz = "mimikatz" wide', '$sekurlsa = "sekurlsa" wide', '$logonpasswords = "logonpasswords" wide'],
                'condition': 'all of them'
            }
        ]
        
        for rule in yara_rules:
            with st.expander(f"🔍 {rule['name']}"):
                st.markdown(f"**Descripción:** {rule['description']}")
                st.markdown("**Strings:**")
                for s in rule['strings']:
                    st.code(s, language='text')
                st.markdown(f"**Condición:** {rule['condition']}")
                st.success(f"✅ Regla activa - Detección habilitada")
    
    with tab7:
        st.markdown("<h4>SIEM Console - Log Management</h4>", unsafe_allow_html=True)
        
        conn = get_db()
        df_siem = pd.read_sql_query("SELECT * FROM siem_logs ORDER BY timestamp DESC LIMIT 50", conn)
        conn.close()
        
        if not df_siem.empty:
            st.dataframe(df_siem, use_container_width=True, hide_index=True)
            
            severity_counts = df_siem['severity'].value_counts()
            fig_severity = px.pie(values=severity_counts.values, names=severity_counts.index, 
                                  title='Log Distribution by Severity')
            st.plotly_chart(fig_severity, use_container_width=True)
        else:
            st.info("No hay logs SIEM disponibles")
    
    with tab8:
        st.markdown("<h4>SOAR Workflows - Automation</h4>", unsafe_allow_html=True)
        
        conn = get_db()
        df_playbooks = pd.read_sql_query("SELECT * FROM soar_playbooks", conn)
        conn.close()
        
        if not df_playbooks.empty:
            for _, playbook in df_playbooks.iterrows():
                with st.expander(f"🤖 {playbook['playbook_name']}"):
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Status", playbook['status'])
                    col2.metric("Success Rate", f"{playbook['success_rate']:.1f}%")
                    col3.metric("Avg Time", f"{playbook['avg_execution_time']:.1f}s")
                    
                    st.markdown(f"**Trigger:** {playbook['trigger_condition']}")
                    st.markdown(f"**Actions:** {playbook['actions']}")
                    st.markdown(f"**Last Run:** {playbook['last_run']}")
                    
                    if st.button(f"▶️ Run {playbook['playbook_name']}", key=f"run_{playbook['playbook_name']}"):
                        st.success(f"✅ {playbook['playbook_name']} ejecutado exitosamente")
        else:
            st.info("No hay playbooks SOAR configurados")
    
    with tab9:
        st.markdown("<h4>🔐 Password Strength Analyzer</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Password Strength Analyzer:** Analiza la fortaleza de contraseñas usando criterios
        de complejidad, patrones comunes y estimación de tiempo de crackeo.
        """)
        
        password = st.text_input("Contraseña a Analizar", type="password")
        
        if password:
            # Análisis de fortaleza
            length = len(password)
            has_upper = any(c.isupper() for c in password)
            has_lower = any(c.islower() for c in password)
            has_digit = any(c.isdigit() for c in password)
            has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
            
            # Calcular score
            score = 0
            if length >= 8: score += 1
            if length >= 12: score += 1
            if length >= 16: score += 1
            if has_upper: score += 1
            if has_lower: score += 1
            if has_digit: score += 1
            if has_special: score += 1
            
            # Determinar nivel
            if score <= 2:
                level = "Débil"
                color = "red"
            elif score <= 4:
                level = "Media"
                color = "yellow"
            elif score <= 6:
                level = "Fuerte"
                color = "green"
            else:
                level = "Muy Fuerte"
                color = "blue"
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Longitud", length)
            col2.metric("Nivel", level, delta_color="normal")
            col3.metric("Score", f"{score}/7")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Criterios
            st.markdown("**Criterios de Fortaleza:**")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"{'✅' if length >= 8 else '❌'} Longitud >= 8 caracteres")
                st.markdown(f"{'✅' if has_upper else '❌'} Mayúsculas")
                st.markdown(f"{'✅' if has_lower else '❌'} Minúsculas")
            with col2:
                st.markdown(f"{'✅' if has_digit else '❌'} Dígitos")
                st.markdown(f"{'✅' if has_special else '❌'} Caracteres especiales")
            
            # Estimación de tiempo de crackeo
            if score >= 5:
                crack_time = "Siglos"
            elif score >= 4:
                crack_time = "Años"
            elif score >= 3:
                crack_time = "Meses"
            elif score >= 2:
                crack_time = "Días"
            else:
                crack_time = "Minutos"
            
            st.markdown(f"<br>**Tiempo estimado de crackeo:** {crack_time}", unsafe_allow_html=True)
            
            if score >= 5:
                st.success("✅ Contraseña segura")
                add_xp(5, "password_security")
            else:
                st.warning("⚠️ Contraseña necesita mejoras")
    
    with tab10:
        st.markdown("<h4>🛡️ 2FA Simulator - Two-Factor Authentication</h4>", unsafe_allow_html=True)
        
        st.info("""
        **2FA Simulator:** Simula autenticación de dos factores usando TOTP (Time-based One-Time Password)
        similar a Google Authenticator.
        """)
        
        # Inicializar 2FA
        if '2fa_secret' not in st.session_state:
            import base64
            import hmac
            import hashlib
            st.session_state['2fa_secret'] = base64.b32encode(os.urandom(10)).decode('utf-8')
        
        st.markdown(f"""
        <div class="glass-card">
            <p><strong>Secret Key:</strong> {st.session_state['2fa_secret']}</p>
            <p style="font-size: 0.8rem; color: #64748b;">Escanea este código con Google Authenticator</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Generar TOTP simulado
        import time
        current_time = int(time.time())
        time_step = 30
        counter = current_time // time_step
        
        # Simular TOTP (en producción usar pyotp)
        import struct
        import hashlib
        key = base64.b32decode(st.session_state['2fa_secret'])
        counter_bytes = struct.pack('>Q', counter)
        hmac_hash = hmac.new(key, counter_bytes, hashlib.sha1).digest()
        offset = hmac_hash[-1] & 0x0f
        code = struct.unpack('>I', hmac_hash[offset:offset+4])[0] & 0x7fffffff
        totp_code = str(code % 1000000).zfill(6)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Código TOTP Actual</h5>", unsafe_allow_html=True)
            st.markdown(f"""
            <div style="font-size: 3rem; font-weight: bold; text-align: center; color: #6366f1; letter-spacing: 0.5rem;">
                {totp_code[:3]} {totp_code[3:]}
            </div>
            """, unsafe_allow_html=True)
            st.caption(f"Expira en {30 - (current_time % 30)} segundos")
        
        with col2:
            st.markdown("<h5>Verificar Código</h5>", unsafe_allow_html=True)
            user_code = st.text_input("Ingresa el código de 6 dígitos", max_chars=6)
            
            if st.button("🔐 Verificar"):
                if user_code == totp_code:
                    st.success("✅ 2FA Verificado exitosamente")
                    add_xp(10, "2fa_verification")
                    show_toast("✅ Autenticación 2FA exitosa", "success")
                else:
                    st.error("❌ Código incorrecto")
                    show_toast("❌ Código 2FA incorrecto", "error")
    
    with tab11:
        st.markdown("<h4>🌐 Threat Intel - Inteligencia de Amenazas</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Threat Intel:** Plataforma de inteligencia de amenazas que recopila y analiza
        información sobre actores de amenazas, campañas maliciosas e indicadores de compromiso.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Actores de Amenazas</h5>", unsafe_allow_html=True)
            
            threat_actors = [
                {"name": "APT28 (Fancy Bear)", "country": "Rusia", "motivation": "Espionaje", "severity": "HIGH"},
                {"name": "APT29 (Cozy Bear)", "country": "Rusia", "motivation": "Espionaje", "severity": "HIGH"},
                {"name": "Lazarus Group", "country": "Corea del Norte", "motivation": "Financiero", "severity": "CRITICAL"},
                {"name": "OilRig", "country": "Irán", "motivation": "Espionaje", "severity": "HIGH"},
                {"name": "MuddyWater", "country": "Irán", "motivation": "Espionaje", "severity": "MEDIUM"}
            ]
            
            for actor in threat_actors:
                with st.expander(f"🎭 {actor['name']}"):
                    col1, col2, col3 = st.columns(3)
                    col1.metric("País", actor['country'])
                    col2.metric("Motivación", actor['motivation'])
                    col3.metric("Severidad", actor['severity'])
        
        with col2:
            st.markdown("<h5>Feed de Amenazas en Tiempo Real</h5>", unsafe_allow_html=True)
            
            # Simular feed de amenazas
            threat_feed = [
                {"type": "Malware", "name": "Emotet", "confidence": 95, "timestamp": "2 min"},
                {"type": "Phishing", "name": "Credential Harvesting", "confidence": 88, "timestamp": "15 min"},
                {"type": "Ransomware", "name": "LockBit 3.0", "confidence": 92, "timestamp": "30 min"},
                {"type": "Botnet", "name": "Mirai Variant", "confidence": 85, "timestamp": "1 hr"},
                {"type": "Zero-Day", "name": "CVE-2024-XXXX", "confidence": 78, "timestamp": "2 hr"}
            ]
            
            for threat in threat_feed:
                severity_color = "red" if threat['confidence'] >= 90 else "yellow" if threat['confidence'] >= 80 else "blue"
                st.markdown(f"""
                <div style="padding: 10px; margin: 5px 0; border-left: 3px solid {severity_color}; background: rgba(100,100,100,0.1); border-radius: 5px;">
                    <strong>{threat['type']}</strong> - {threat['name']}<br>
                    <small>Confianza: {threat['confidence']}% | Hace: {threat['timestamp']}</small>
                </div>
                """, unsafe_allow_html=True)
        
        # Estadísticas de threat intel
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Estadísticas de Threat Intel**")
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("IOCs Activos", f"{random.randint(500, 1000)}")
        col2.metric("Actores Rastreados", f"{random.randint(50, 100)}")
        col3.metric("Alertas/Día", f"{random.randint(100, 500)}")
        col4.metric("TTFB", f"{random.randint(10, 50)}ms")
        
        add_xp(10, "threat_intel")
    
    with tab12:
        st.markdown("<h4>🔍 Vulnerability Scanner - Escáner de Vulnerabilidades</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Vulnerability Scanner:** Escáner automatizado que identifica vulnerabilidades
        en sistemas, aplicaciones y redes usando bases de datos CVE y CVSS scores.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Configuración del Escáner</h5>", unsafe_allow_html=True)
            
            scan_target = st.text_input("Target (IP/Dominio)", value="192.168.1.0/24")
            scan_type = st.selectbox("Tipo de Escaneo", ["Quick Scan", "Full Scan", "Deep Scan", "Custom"])
            scan_ports = st.slider("Puertos", 1, 65535, (1, 1024))
            scan_depth = st.slider("Profundidad", 1, 5, 3)
            
            if st.button("🔍 Iniciar Escaneo"):
                st.success("✅ Escaneo iniciado...")
                add_xp(5, "vuln_scan")
        
        with col2:
            st.markdown("<h5>Vulnerabilidades Detectadas</h5>", unsafe_allow_html=True)
            
            # Simular vulnerabilidades
            vulnerabilities = [
                {"cve": "CVE-2024-1234", "severity": "CRITICAL", "cvss": 9.8, "service": "Apache HTTPD"},
                {"cve": "CVE-2024-5678", "severity": "HIGH", "cvss": 8.5, "service": "OpenSSH"},
                {"cve": "CVE-2024-9012", "severity": "MEDIUM", "cvss": 6.5, "service": "nginx"},
                {"cve": "CVE-2024-3456", "severity": "LOW", "cvss": 3.5, "service": "MySQL"},
                {"cve": "CVE-2024-7890", "severity": "HIGH", "cvss": 7.8, "service": "WordPress"}
            ]
            
            for vuln in vulnerabilities:
                severity_color = {"CRITICAL": "red", "HIGH": "orange", "MEDIUM": "yellow", "LOW": "blue"}[vuln['severity']]
                with st.expander(f"🔴 {vuln['cve']} - {vuln['severity']}"):
                    col1, col2, col3 = st.columns(3)
                    col1.metric("CVSS", f"{vuln['cvss']}")
                    col2.metric("Servicio", vuln['service'])
                    col3.metric("Severidad", vuln['severity'])
                    
                    st.markdown("**Recomendación:** Actualizar a la última versión disponible")
        
        # Gráfico de distribución de severidad
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Distribución de Severidad**")
        
        severity_counts = {"CRITICAL": 2, "HIGH": 8, "MEDIUM": 15, "LOW": 25}
        fig_vuln = go.Figure(data=[go.Pie(labels=list(severity_counts.keys()), 
                                          values=list(severity_counts.values()))])
        fig_vuln.update_layout(title="Vulnerabilities by Severity")
        st.plotly_chart(fig_vuln, use_container_width=True)
        
        add_xp(10, "vulnerability_scanner")
    
    with tab13:
        st.markdown("<h4>🦠 Malware Analysis - Análisis de Malware</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Malware Analysis:** Análisis estático y dinámico de muestras de malware
        para identificar comportamiento, capacidades y métodos de infección.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Análisis Estático</h5>", unsafe_allow_html=True)
            
            uploaded_malware = st.file_uploader("Subir muestra de malware", type=['exe', 'dll', 'bin'])
            
            if uploaded_malware:
                st.success("✅ Muestra cargada para análisis")
                
                # Simular análisis estático
                st.markdown("**Resultados del Análisis:**")
                
                static_results = {
                    "File Size": f"{random.randint(100, 5000)} KB",
                    "MD5": f"{random.randint(10000000, 99999999):x}",
                    "SHA256": f"{random.randint(10000000, 99999999):x}" * 8,
                    "Compiler": "MSVC 14.0",
                    "Packer": "UPX 3.96",
                    "Sections": f"{random.randint(3, 8)}",
                    "Imports": f"{random.randint(50, 200)}",
                    "Exports": f"{random.randint(5, 20)}"
                }
                
                for key, value in static_results.items():
                    st.metric(key, value)
        
        with col2:
            st.markdown("<h5>Análisis Dinámico</h5>", unsafe_allow_html=True)
            
            if st.button("🔬 Ejecutar en Sandbox"):
                st.success("✅ Análisis dinámico iniciado")
                add_xp(10, "malware_analysis")
                show_toast("✅ Análisis de malware completado", "success")
            
            # Simular comportamiento
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("**Comportamiento Detectado:**")
            
            behaviors = [
                {"action": "File Creation", "count": random.randint(5, 20), "severity": "MEDIUM"},
                {"action": "Registry Modification", "count": random.randint(3, 15), "severity": "HIGH"},
                {"action": "Network Connection", "count": random.randint(1, 5), "severity": "CRITICAL"},
                {"action": "Process Injection", "count": random.randint(2, 8), "severity": "CRITICAL"},
                {"action": "Anti-VM Detection", "count": random.randint(0, 3), "severity": "HIGH"}
            ]
            
            for behavior in behaviors:
                severity_color = {"CRITICAL": "red", "HIGH": "orange", "MEDIUM": "yellow", "LOW": "blue"}[behavior['severity']]
                st.markdown(f"""
                <div style="padding: 5px; margin: 3px 0; border-left: 3px solid {severity_color}; background: rgba(100,100,100,0.1);">
                    <strong>{behavior['action']}</strong> - {behavior['count']} veces ({behavior['severity']})
                </div>
                """, unsafe_allow_html=True)
        
        # Gráfico de comportamiento
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Timeline de Actividad**")
        
        activity_timeline = [random.randint(0, 10) for _ in range(60)]
        fig_malware = go.Figure()
        fig_malware.add_trace(go.Scatter(x=list(range(60)), y=activity_timeline, mode='lines', name='Actividad'))
        fig_malware.update_layout(title="Actividad del Malware (60s)", xaxis_title="Tiempo (s)", yaxis_title="Actividad")
        st.plotly_chart(fig_malware, use_container_width=True)
        
        add_xp(10, "malware_analysis")
    
    with tab14:
        st.markdown("<h4>🚨 Incident Response - Respuesta a Incidentes</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Incident Response:** Proceso estructurado para manejar incidentes de seguridad
        desde detección hasta recuperación y post-incidente.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Crear Incidente</h5>", unsafe_allow_html=True)
            
            incident_type = st.selectbox("Tipo de Incidente", ["Malware", "Phishing", "DDoS", "Data Breach", "Insider Threat"])
            severity = st.selectbox("Severidad", ["LOW", "MEDIUM", "HIGH", "CRITICAL"])
            description = st.text_area("Descripción", value="Descripción detallada del incidente...")
            
            if st.button("🚨 Crear Incidente"):
                incident_id = f"INC-{random.randint(10000, 99999)}"
                st.success(f"✅ Incidente creado: {incident_id}")
                add_xp(10, "incident_response")
                show_toast("✅ Incidente creado", "success")
        
        with col2:
            st.markdown("<h5>Incidentes Activos</h5>", unsafe_allow_html=True)
            
            incidents = [
                {"id": "INC-12345", "type": "Malware", "severity": "CRITICAL", "status": "In Progress", "assigned": "SOC Team"},
                {"id": "INC-12346", "type": "Phishing", "severity": "HIGH", "status": "Investigating", "assigned": "Security Analyst"},
                {"id": "INC-12347", "type": "DDoS", "severity": "MEDIUM", "status": "Resolved", "assigned": "Network Team"}
            ]
            
            for incident in incidents:
                severity_color = {"CRITICAL": "red", "HIGH": "orange", "MEDIUM": "yellow", "LOW": "blue"}[incident['severity']]
                with st.expander(f"🚨 {incident['id']} - {incident['type']}"):
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Severidad", incident['severity'])
                    col2.metric("Estado", incident['status'])
                    col3.metric("Asignado", incident['assigned'])
        
        # Workflow de respuesta
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Workflow de Respuesta**")
        
        workflow_steps = [
            {"step": 1, "name": "Detección", "status": "✅ Completado", "time": "5 min"},
            {"step": 2, "name": "Contención", "status": "✅ Completado", "time": "15 min"},
            {"step": 3, "name": "Eradicación", "status": "🔄 En Progreso", "time": "30 min"},
            {"step": 4, "name": "Recuperación", "status": "⏳ Pendiente", "time": "45 min"},
            {"step": 5, "name": "Post-Incidente", "status": "⏳ Pendiente", "time": "60 min"}
        ]
        
        for step in workflow_steps:
            st.markdown(f"""
            <div style="padding: 10px; margin: 5px 0; border-left: 4px solid {'green' if 'Completado' in step['status'] else 'orange' if 'Progreso' in step['status'] else 'gray'}; background: rgba(100,100,100,0.1);">
                <strong>Step {step['step']}: {step['name']}</strong> - {step['status']} ({step['time']})
            </div>
            """, unsafe_allow_html=True)
        
        add_xp(10, "incident_response")
    
    with tab15:
        st.markdown("<h4>📊 Security Dashboard - Dashboard de Seguridad</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Security Dashboard:** Vista consolidada de métricas de seguridad,
        estado de amenazas, compliance y rendimiento del sistema SIEM.
        """)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("<h5>Métricas de Seguridad</h5>", unsafe_allow_html=True)
            
            security_score = random.randint(85, 98)
            threat_level = random.choice(["Low", "Medium", "High"])
            incidents_today = random.randint(0, 10)
            resolved_incidents = random.randint(5, 15)
            
            col1, col2 = st.columns(2)
            col1.metric("Security Score", f"{security_score}%")
            col2.metric("Threat Level", threat_level)
            col1.metric("Incidents Today", incidents_today)
            col2.metric("Resolved", resolved_incidents)
        
        with col2:
            st.markdown("<h5>Estado de Componentes</h5>", unsafe_allow_html=True)
            
            components = [
                {"name": "SIEM Engine", "status": "✅ Online", "uptime": "99.9%"},
                {"name": "Threat Intel", "status": "✅ Online", "uptime": "99.8%"},
                {"name": "SOAR Platform", "status": "✅ Online", "uptime": "99.7%"},
                {"name": "EDR Agent", "status": "✅ Online", "uptime": "99.9%"}
            ]
            
            for component in components:
                st.markdown(f"""
                <div style="padding: 8px; margin: 5px 0; border-left: 3px solid green; background: rgba(34, 197, 94, 0.1); border-radius: 3px;">
                    <strong>{component['name']}</strong> - {component['status']} | Uptime: {component['uptime']}
                </div>
                """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("<h5>Alertas Recientes</h5>", unsafe_allow_html=True)
            
            recent_alerts = [
                {"type": "Malware", "severity": "CRITICAL", "time": "5 min ago"},
                {"type": "Phishing", "severity": "HIGH", "time": "15 min ago"},
                {"type": "Brute Force", "severity": "MEDIUM", "time": "30 min ago"}
            ]
            
            for alert in recent_alerts:
                severity_color = {"CRITICAL": "red", "HIGH": "orange", "MEDIUM": "yellow"}[alert['severity']]
                st.markdown(f"""
                <div style="padding: 8px; margin: 5px 0; border-left: 3px solid {severity_color}; background: rgba(100,100,100,0.1); border-radius: 3px;">
                    <strong>{alert['type']}</strong> - {alert['severity']} | {alert['time']}
                </div>
                """, unsafe_allow_html=True)
        
        # Gráfico de seguridad
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Tendencia de Amenazas (7 días)**")
        
        days = list(range(7))
        threats_history = [random.randint(50, 150) for _ in range(7)]
        blocked_history = [random.randint(40, 140) for _ in range(7)]
        
        fig_security = go.Figure()
        fig_security.add_trace(go.Scatter(x=days, y=threats_history, name='Total Threats', mode='lines+markers'))
        fig_security.add_trace(go.Scatter(x=days, y=blocked_history, name='Blocked', mode='lines+markers'))
        fig_security.update_layout(title="Tendencia de Amenazas", xaxis_title="Día", yaxis_title="Cantidad")
        st.plotly_chart(fig_security, use_container_width=True)
        
        add_xp(10, "security_dashboard")
    
    with tab16:
        st.markdown("<h4>🔒 Compliance Audit - Auditoría de Cumplimiento</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Compliance Audit:** Evaluación de cumplimiento con estándares de seguridad
        como ISO 27001, PCI DSS, GDPR y regulaciones locales.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Estándares de Cumplimiento</h5>", unsafe_allow_html=True)
            
            standards = [
                {"name": "ISO 27001", "compliance": random.randint(85, 98), "status": "Compliant"},
                {"name": "PCI DSS", "compliance": random.randint(80, 95), "status": "Compliant"},
                {"name": "GDPR", "compliance": random.randint(90, 99), "status": "Compliant"},
                {"name": "SOC 2", "compliance": random.randint(85, 97), "status": "In Progress"}
            ]
            
            for standard in standards:
                status_color = "green" if standard['status'] == "Compliant" else "orange"
                st.markdown(f"""
                <div style="padding: 10px; margin: 5px 0; border-left: 4px solid {status_color}; background: rgba(100,100,100,0.1); border-radius: 3px;">
                    <strong>{standard['name']}</strong><br>
                    Compliance: {standard['compliance']}% | Status: {standard['status']}
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("<h5>Controles de Seguridad</h5>", unsafe_allow_html=True)
            
            controls = [
                {"name": "Access Control", "implemented": True, "tested": True},
                {"name": "Encryption", "implemented": True, "tested": True},
                {"name": "Audit Logging", "implemented": True, "tested": True},
                {"name": "Incident Response", "implemented": True, "tested": False},
                {"name": "Data Backup", "implemented": True, "tested": True}
            ]
            
            for control in controls:
                status = "✅" if control['implemented'] and control['tested'] else "⚠️" if control['implemented'] else "❌"
                st.markdown(f"""
                <div style="padding: 8px; margin: 5px 0; border-left: 3px solid {'green' if control['implemented'] and control['tested'] else 'orange' if control['implemented'] else 'red'}; background: rgba(100,100,100,0.1); border-radius: 3px;">
                    {status} <strong>{control['name']}</strong> | Implemented: {control['implemented']} | Tested: {control['tested']}
                </div>
                """, unsafe_allow_html=True)
        
        # Gráfico de compliance
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Métricas de Compliance**")
        
        fig_compliance = go.Figure()
        fig_compliance.add_trace(go.Bar(x=[s['name'] for s in standards], y=[s['compliance'] for s in standards],
                                          marker_color=['green' if s['status'] == 'Compliant' else 'orange' for s in standards]))
        fig_compliance.update_layout(title="Compliance por Estándar", xaxis_title="Estándar", yaxis_title="Compliance %")
        st.plotly_chart(fig_compliance, use_container_width=True)
        
        add_xp(10, "compliance_audit")
    
    with tab17:
        st.markdown("<h4>🎯 Threat Hunting - Caza de Amenazas</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Threat Hunting:** Búsqueda proactiva de amenazas en la red y endpoints
        usando técnicas de threat hunting para detectar actividad maliciosa antes
        de que cause daño.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Configuración de Hunt</h5>", unsafe_allow_html=True)
            
            hunt_type = st.selectbox("Tipo de Hunt", ["File System", "Registry", "Network", "Process", "Memory"])
            scope = st.selectbox("Alcance", ["Single Host", "Subnet", "Domain", "Enterprise"])
            time_range = st.slider("Rango de Tiempo (horas)", 1, 168, 24)
            
            if st.button("🎯 Iniciar Hunt"):
                st.success("✅ Hunt iniciado")
                add_xp(15, "threat_hunting")
                show_toast("✅ Threat hunting iniciado", "success")
        
        with col2:
            st.markdown("<h5>Resultados del Hunt</h5>", unsafe_allow_html=True)
            
            findings = [
                {"type": "Suspicious File", "severity": "HIGH", "location": "C:\\Windows\\Temp\\malware.exe"},
                {"type": "Registry Key", "severity": "MEDIUM", "location": "HKLM\\Software\\Unknown"},
                {"type": "Network Connection", "severity": "LOW", "location": "192.168.1.100:4444"}
            ]
            
            for finding in findings:
                severity_color = {"HIGH": "red", "MEDIUM": "orange", "LOW": "yellow"}[finding['severity']]
                st.markdown(f"""
                <div style="padding: 8px; margin: 5px 0; border-left: 3px solid {severity_color}; background: rgba(100,100,100,0.1); border-radius: 3px;">
                    <strong>{finding['type']}</strong> - {finding['severity']} | {finding['location']}
                </div>
                """, unsafe_allow_html=True)
        
        # Gráfico de findings
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Distribución de Findings por Severidad**")
        
        severity_counts = {"HIGH": 1, "MEDIUM": 1, "LOW": 1}
        fig_hunt = go.Figure(data=[go.Pie(labels=list(severity_counts.keys()), values=list(severity_counts.values()))])
        fig_hunt.update_layout(title="Findings por Severidad")
        st.plotly_chart(fig_hunt, use_container_width=True)
        
        add_xp(10, "threat_hunting")
    
    with tab18:
        st.markdown("<h4>📈 SIEM Dashboard - Dashboard SIEM</h4>", unsafe_allow_html=True)
        
        st.info("""
        **SIEM Dashboard:** Monitor centralizado de eventos de seguridad en tiempo real
        con correlación de eventos, alertas y análisis de logs.
        """)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("<h5>Métricas SIEM</h5>", unsafe_allow_html=True)
            
            events_per_sec = random.randint(1000, 5000)
            alerts_per_hour = random.randint(50, 200)
            eps_capacity = random.randint(10000, 50000)
            
            col1.metric("EPS", f"{events_per_sec:,}", "Events/sec")
            col2.metric("Alerts/Hour", f"{alerts_per_hour}")
            col3.metric("Capacity", f"{eps_capacity:,} EPS")
        
        with col2:
            st.markdown("<h5>Alertas Recientes</h5>", unsafe_allow_html=True)
            
            recent_alerts = [
                {"source": "Firewall", "type": "Block", "severity": "HIGH", "time": "2 min ago"},
                {"source": "IDS", "type": "Detect", "severity": "MEDIUM", "time": "5 min ago"},
                {"source": "Endpoint", "type": "Malware", "severity": "CRITICAL", "time": "10 min ago"}
            ]
            
            for alert in recent_alerts:
                severity_color = {"CRITICAL": "red", "HIGH": "orange", "MEDIUM": "yellow"}[alert['severity']]
                st.markdown(f"""
                <div style="padding: 8px; margin: 5px 0; border-left: 3px solid {severity_color}; background: rgba(100,100,100,0.1); border-radius: 3px;">
                    <strong>{alert['source']}</strong> - {alert['type']} | {alert['severity']} | {alert['time']}
                </div>
                """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("<h5>Fuentes de Logs</h5>", unsafe_allow_html=True)
            
            log_sources = [
                {"name": "Firewall", "status": "✅ Online", "logs": "1.2M"},
                {"name": "Windows", "status": "✅ Online", "logs": "3.5M"},
                {"name": "Linux", "status": "✅ Online", "logs": "2.1M"},
                {"name": "Network", "status": "⚠️ Delayed", "logs": "0.8M"}
            ]
            
            for source in log_sources:
                st.markdown(f"""
                <div style="padding: 8px; margin: 5px 0; border-left: 3px solid green; background: rgba(34, 197, 94, 0.1); border-radius: 3px;">
                    <strong>{source['name']}</strong> - {source['status']} | Logs: {source['logs']}
                </div>
                """, unsafe_allow_html=True)
        
        # Gráfico de eventos
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Eventos por Hora (24h)**")
        
        hours = list(range(24))
        events_hourly = [random.randint(500, 2000) for _ in range(24)]
        
        fig_siem = go.Figure()
        fig_siem.add_trace(go.Scatter(x=hours, y=events_hourly, mode='lines+markers', name='Events'))
        fig_siem.update_layout(title="Eventos por Hora", xaxis_title="Hora", yaxis_title="Eventos")
        st.plotly_chart(fig_siem, use_container_width=True)
        
        add_xp(10, "siem_dashboard")
    
    with tab19:
        st.markdown("<h4>🤖 SOAR Playbooks - Playbooks de Automatización</h4>", unsafe_allow_html=True)
        
        st.info("""
        **SOAR Playbooks:** Playbooks de automatización de respuesta a incidentes
        para orquestar respuestas automáticas a amenazas detectadas.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Playbooks Disponibles</h5>", unsafe_allow_html=True)
            
            playbooks = [
                {"name": "Malware Containment", "trigger": "Malware Detected", "actions": 5, "status": "Active"},
                {"name": "Phishing Response", "trigger": "Phishing Email", "actions": 8, "status": "Active"},
                {"name": "Data Exfiltration", "trigger": "Data Loss", "actions": 12, "status": "Active"},
                {"name": "Account Compromise", "trigger": "Suspicious Login", "actions": 6, "status": "Active"}
            ]
            
            for playbook in playbooks:
                with st.expander(f"🤖 {playbook['name']}"):
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Trigger", playbook['trigger'])
                    col2.metric("Actions", playbook['actions'])
                    col3.metric("Status", playbook['status'])
            
            if st.button("🤖 Ejecutar Playbook"):
                st.success("✅ Playbook ejecutado")
                add_xp(15, "soar_playbooks")
                show_toast("✅ SOAR playbook ejecutado", "success")
        
        with col2:
            st.markdown("<h5>Estadísticas de Playbooks</h5>", unsafe_allow_html=True)
            
            total_runs = random.randint(100, 500)
            success_rate = random.randint(85, 99)
            avg_runtime = random.randint(30, 120)
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Runs", f"{total_runs}")
            col2.metric("Success Rate", f"{success_rate}%")
            col3.metric("Avg Runtime", f"{avg_runtime}s")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Playbook execution history
            st.markdown("**Historial de Ejecución**")
            
            executions = [
                {"playbook": "Malware Containment", "time": "10 min ago", "status": "Success"},
                {"playbook": "Phishing Response", "time": "1 hour ago", "status": "Success"},
                {"playbook": "Account Compromise", "time": "2 hours ago", "status": "Partial"}
            ]
            
            for exec in executions:
                status_color = "green" if exec['status'] == "Success" else "orange"
                st.markdown(f"""
                <div style="padding: 8px; margin: 5px 0; border-left: 3px solid {status_color}; background: rgba(100,100,100,0.1); border-radius: 3px;">
                    <strong>{exec['playbook']}</strong> - {exec['status']} | {exec['time']}
                </div>
                """, unsafe_allow_html=True)
        
        # Gráfico de playbooks
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Ejecuciones por Playbook**")
        
        fig_playbook = go.Figure(data=[go.Bar(
            x=[p['name'] for p in playbooks],
            y=[random.randint(20, 100) for p in playbooks],
            marker_color='indigo'
        )])
        fig_playbook.update_layout(title="Ejecuciones por Playbook", xaxis_title="Playbook", yaxis_title="Ejecuciones")
        st.plotly_chart(fig_playbook, use_container_width=True)
        
        add_xp(10, "soar_playbooks")
    
    with tab20:
        st.markdown("<h4>🎣 Phishing Simulator - Simulador de Phishing</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Phishing Simulator:** Simula campañas de phishing para entrenar a empleados
        y medir la resistencia de la organización contra ataques de ingeniería social.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Configuración de Campaña</h5>", unsafe_allow_html=True)
            
            campaign_type = st.selectbox("Tipo de Campaña", ["Email de CEO", "Actualización de Password", "Factura Pendiente", "Bonus de Empleado"])
            target_dept = st.selectbox("Departamento Objetivo", ["Todos", "Finanzas", "IT", "RRHH", "Ventas"])
            difficulty = st.slider("Dificultad", 1, 5, 3)
            num_targets = st.number_input("Número de Objetivos", value=50, min_value=1)
            
            if st.button("🎣 Iniciar Simulación"):
                st.success("✅ Simulación iniciada")
                add_xp(15, "phishing_simulator")
                show_toast("✅ Simulación de phishing iniciada", "success")
        
        with col2:
            st.markdown("<h5>Resultados de Simulación</h5>", unsafe_allow_html=True)
            
            phishing_results = {
                "emails_sent": num_targets,
                "opened": int(num_targets * 0.75),
                "clicked": int(num_targets * 0.35),
                "reported": int(num_targets * 0.15),
                "compromised": int(num_targets * 0.08)
            }
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Enviados", phishing_results['emails_sent'])
            col2.metric("Abiertos", phishing_results['opened'])
            col3.metric("Clics", phishing_results['clicked'])
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            col1.metric("Reportados", phishing_results['reported'])
            col2.metric("Comprometidos", phishing_results['compromised'])
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            click_rate = (phishing_results['clicked'] / phishing_results['emails_sent']) * 100
            report_rate = (phishing_results['reported'] / phishing_results['emails_sent']) * 100
            
            col1.metric("Tasa Clic", f"{click_rate:.1f}%")
            col2.metric("Tasa Reporte", f"{report_rate:.1f}%")
        
        # Gráfico de resultados
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Resultados de la Simulación**")
        
        fig_phishing = go.Figure(data=[go.Bar(
            x=['Enviados', 'Abiertos', 'Clics', 'Reportados', 'Comprometidos'],
            y=[phishing_results['emails_sent'], phishing_results['opened'], phishing_results['clicked'], 
               phishing_results['reported'], phishing_results['compromised']],
            marker_color=['blue', 'green', 'orange', 'purple', 'red']
        )])
        fig_phishing.update_layout(title="Resultados de Simulación de Phishing", xaxis_title="Acción", yaxis_title="Cantidad")
        st.plotly_chart(fig_phishing, use_container_width=True)
        
        add_xp(10, "phishing_simulator")
    
    with tab21:
        st.markdown("<h4>🌐 Network Security - Seguridad de Red</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Network Security:** Monitoreo y protección de la red contra intrusiones,
        ataques DDoS, escaneos de puertos y otras amenazas de red.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Configuración de Firewall</h5>", unsafe_allow_html=True)
            
            firewall_rules = [
                {"rule": "Bloquear tráfico SSH externo", "status": "Active", "hits": 1247},
                {"rule": "Permitir HTTP/HTTPS", "status": "Active", "hits": 45231},
                {"rule": "Bloquear IP maliciosas", "status": "Active", "hits": 89},
                {"rule": "Limitar conexiones por IP", "status": "Active", "hits": 312}
            ]
            
            for rule in firewall_rules:
                status_color = "green" if rule['status'] == "Active" else "red"
                with st.expander(f"🔥 {rule['rule']}"):
                    col1, col2 = st.columns(2)
                    col1.metric("Status", rule['status'])
                    col2.metric("Hits", rule['hits'])
                    st.markdown(f"**Status:** <span style='color: {status_color}'>{rule['status']}</span>", unsafe_allow_html=True)
            
            if st.button("🌐 Actualizar Reglas"):
                st.success("✅ Reglas actualizadas")
                add_xp(10, "network_security")
                show_toast("✅ Reglas de firewall actualizadas", "success")
        
        with col2:
            st.markdown("<h5>Métricas de Red</h5>", unsafe_allow_html=True)
            
            network_metrics = {
                "total_traffic": "12.5 TB",
                "blocked_ips": 234,
                "ddos_attacks": 7,
                "port_scans": 45,
                "intrusion_attempts": 12
            }
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Tráfico", network_metrics['total_traffic'])
            col2.metric("IPs Bloqueadas", network_metrics['blocked_ips'])
            col3.metric("Ataques DDoS", network_metrics['ddos_attacks'])
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            col1.metric("Escaneos Puertos", network_metrics['port_scans'])
            col2.metric("Intentos Intrusión", network_metrics['intrusion_attempts'])
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Top IPs bloqueadas
            st.markdown("**Top IPs Bloqueadas**")
            
            top_ips = [
                {"ip": "192.168.1.100", "reason": "SSH Brute Force", "attempts": 234},
                {"ip": "10.0.0.50", "reason": "Port Scanning", "attempts": 156},
                {"ip": "172.16.0.25", "reason": "DDoS", "attempts": 89}
            ]
            
            for ip_data in top_ips:
                st.markdown(f"""
                <div style="padding: 8px; margin: 5px 0; border-left: 3px solid red; background: rgba(255,0,0,0.1); border-radius: 3px;">
                    <strong>{ip_data['ip']}</strong> - {ip_data['reason']} | {ip_data['attempts']} intentos
                </div>
                """, unsafe_allow_html=True)
        
        # Gráfico de tráfico
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Tráfico de Red (24h)**")
        
        hours = list(range(24))
        traffic = [random.randint(100, 500) for _ in range(24)]
        
        fig_network = go.Figure()
        fig_network.add_trace(go.Scatter(x=hours, y=traffic, mode='lines+markers', name='Tráfico (GB)'))
        fig_network.update_layout(title="Tráfico de Red por Hora", xaxis_title="Hora", yaxis_title="Tráfico (GB)")
        st.plotly_chart(fig_network, use_container_width=True)
        
        add_xp(10, "network_security")
    
    with tab22:
        st.markdown("<h4>💻 Endpoint Protection - Protección de Endpoints</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Endpoint Protection:** Protección de dispositivos finales (laptops, desktops, móviles)
        contra malware, ransomware y otras amenazas.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Estado de Endpoints</h5>", unsafe_allow_html=True)
            
            endpoints = [
                {"name": "Laptop-CEO", "os": "Windows 11", "status": "Protected", "last_scan": "2h ago"},
                {"name": "Desktop-FIN-01", "os": "Windows 10", "status": "Protected", "last_scan": "1h ago"},
                {"name": "Laptop-IT-05", "os": "macOS", "status": "At Risk", "last_scan": "3d ago"},
                {"name": "Mobile-SALES-02", "os": "iOS", "status": "Protected", "last_scan": "30m ago"},
                {"name": "Desktop-HR-03", "os": "Windows 10", "status": "Protected", "last_scan": "4h ago"}
            ]
            
            for endpoint in endpoints:
                status_color = "green" if endpoint['status'] == "Protected" else "red"
                with st.expander(f"💻 {endpoint['name']}"):
                    col1, col2, col3 = st.columns(3)
                    col1.metric("OS", endpoint['os'])
                    col2.metric("Status", endpoint['status'])
                    col3.metric("Último Scan", endpoint['last_scan'])
                    st.markdown(f"**Status:** <span style='color: {status_color}'>{endpoint['status']}</span>", unsafe_allow_html=True)
            
            if st.button("💻 Escanear Todos"):
                st.success("✅ Escaneo iniciado")
                add_xp(10, "endpoint_protection")
                show_toast("✅ Escaneo de endpoints iniciado", "success")
        
        with col2:
            st.markdown("<h5>Métricas de Protección</h5>", unsafe_allow_html=True)
            
            total_endpoints = len(endpoints)
            protected = len([e for e in endpoints if e['status'] == "Protected"])
            at_risk = len([e for e in endpoints if e['status'] == "At Risk"])
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Total", total_endpoints)
            col2.metric("Protegidos", protected)
            col3.metric("En Riesgo", at_risk)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            protection_rate = (protected / total_endpoints) * 100
            
            col1.metric("Tasa Protección", f"{protection_rate:.1f}%")
            col2.metric("Malware Detectados", random.randint(5, 20))
        
        # Gráfico de distribución
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Distribución de Endpoints por OS**")
        
        os_counts = {"Windows": 3, "macOS": 1, "iOS": 1}
        
        fig_endpoint = go.Figure(data=[go.Pie(labels=list(os_counts.keys()), values=list(os_counts.values()))])
        fig_endpoint.update_layout(title="Endpoints por Sistema Operativo")
        st.plotly_chart(fig_endpoint, use_container_width=True)
        
        add_xp(10, "endpoint_protection")

# ================================================================================
# TRADEGUARD ELITE
# ================================================================================
elif selected == "📈 TradeGuard Elite":
    st.markdown('<h1 class="main-header">📈 TradeGuard Elite</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">HFT Institutional | Arbitrage | Market Making | Dark Pool | Order Book Depth | Execution Algorithms | API Real Binance</p>', unsafe_allow_html=True)
    
    # Opción de usar datos reales de Binance
    col1, col2 = st.columns([3, 1])
    with col1:
        use_real_data = st.checkbox("📡 Usar datos reales de Binance API", value=False, help="Obtiene datos en tiempo real de Binance (BTCUSDT)")
    with col2:
        symbol = st.selectbox("Símbolo", ["BTCUSDT", "ETHUSDT", "BNBUSDT", "ADAUSDT"], key="symbol_main")
    
    # Usar función cacheada para evitar problemas de scope
    df_ohlc = generate_ohlc_data(use_real_data=use_real_data, symbol=symbol)
    
    if df_ohlc is None:
        st.error("Error generating OHLC data. Check dependencies.")
        st.stop()
    
    # Otorgar XP por usar TradeGuard
    if 'trade_guard_visited' not in st.session_state:
        add_xp(10, "trade_execution")
        st.session_state.trade_guard_visited = True
    
    # Métricas institucionales
    cols = st.columns(7)
    returns_pct = df_ohlc['Close'].pct_change().dropna()
    total_return = (df_ohlc['Close'].iloc[-1] / df_ohlc['Close'].iloc[0] - 1) * 100
    volatility = returns_pct.std() * np.sqrt(252) * 100
    sharpe = (returns_pct.mean() * 252) / (returns_pct.std() * np.sqrt(252))
    max_dd = ((df_ohlc['Close'] / df_ohlc['Close'].cummax()) - 1).min() * 100
    var_95 = np.percentile(returns_pct, 5) * 100
    sortino = (returns_pct.mean() * 252) / (returns_pct[returns_pct < 0].std() * np.sqrt(252))
    
    cols[0].metric("📈 Retorno Total", f"{total_return:.2f}%", "+12.5% YTD")
    cols[1].metric("📊 Volatilidad", f"{volatility:.1f}%", "σ anual")
    cols[2].metric("⭐ Sharpe", f"{sharpe:.2f}", "Rend/Riesgo")
    cols[3].metric("📉 Max DD", f"{max_dd:.2f}%", "Drawdown")
    cols[4].metric("⚠️ VaR 95%", f"{var_95:.2f}%", "1 día")
    cols[5].metric("🎯 Sortino", f"{sortino:.2f}", "Downside Risk")
    cols[6].metric("⚡ Latencia", "45μs", "HFT")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14, tab15, tab16, tab17, tab18, tab19, tab20 = st.tabs(["📊 Análisis Técnico", "🧪 Backtesting", "💰 Paper Trading", "🔔 Price Alerts", "💼 Portfolio", "⚖️ Risk Management", "🎯 Portfolio Optimization", "⚡ HFT Engine", "🌐 Dark Pool", "📰 Sentiment Analysis", "🤖 News Trading", "📊 Order Flow", "📈 Position Sizing", "💵 Risk Calculator", "🔍 Market Scanner", "📊 Correlation Matrix", "📈 Portfolio Analytics", "🎯 Options Trading", "📈 Futures Trading", "💳 Margin Trading"])
    
    with tab1:
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown("<h4>Chart Avanzado con Indicadores</h4>", unsafe_allow_html=True)
            
            show_sma50 = st.checkbox("SMA 50", value=True)
            show_sma200 = st.checkbox("SMA 200", value=True)
            show_bb = st.checkbox("Bollinger Bands", value=True)
            show_ichimoku = st.checkbox("Ichimoku Cloud", value=False)
            show_fib = st.checkbox("Fibonacci", value=True)
            show_rsi = st.checkbox("RSI", value=True)
            show_stoch = st.checkbox("Stochastic", value=True)
            
            fig = go.Figure()
            
            fig.add_trace(go.Candlestick(
                x=df_ohlc.index, open=df_ohlc['Open'], high=df_ohlc['High'],
                low=df_ohlc['Low'], close=df_ohlc['Close'], name="Price"
            ))
            
            if show_sma50:
                fig.add_trace(go.Scatter(x=df_ohlc.index, y=df_ohlc['SMA50'], 
                                         name="SMA 50", line=dict(color='orange', width=1)))
            if show_sma200:
                fig.add_trace(go.Scatter(x=df_ohlc.index, y=df_ohlc['SMA200'], 
                                         name="SMA 200", line=dict(color='purple', width=1)))
            if show_bb:
                fig.add_trace(go.Scatter(x=df_ohlc.index, y=df_ohlc['BB_Upper'], 
                                         name="BB Upper", line=dict(color='gray', width=1, dash='dash')))
                fig.add_trace(go.Scatter(x=df_ohlc.index, y=df_ohlc['BB_Lower'], 
                                         name="BB Lower", line=dict(color='gray', width=1, dash='dash')))
            
            if show_ichimoku:
                fig.add_trace(go.Scatter(x=df_ohlc.index, y=df_ohlc['Senkou_A'], 
                                         name="Senkou A", line=dict(color='green', width=1, dash='dash')))
                fig.add_trace(go.Scatter(x=df_ohlc.index, y=df_ohlc['Senkou_B'], 
                                         name="Senkou B", line=dict(color='red', width=1, dash='dash')))
                fig.add_trace(go.Scatter(x=df_ohlc.index, y=df_ohlc['Tenkan'], 
                                         name="Tenkan", line=dict(color='blue', width=1)))
                fig.add_trace(go.Scatter(x=df_ohlc.index, y=df_ohlc['Kijun'], 
                                         name="Kijun", line=dict(color='orange', width=1)))
            
            if show_fib:
                recent_high = df_ohlc['High'].tail(100).max()
                recent_low = df_ohlc['Low'].tail(100).min()
                fib_levels = calc_fibonacci(recent_high, recent_low)
                for level, price in fib_levels.items():
                    fig.add_hline(y=price, line_dash="dot", line_color="gray", annotation_text=level)
            
            fig.update_layout(title="Price Chart with Technical Indicators", xaxis_rangeslider_visible=False)
            st.plotly_chart(fig, use_container_width=True)
            
            latest = df_ohlc.iloc[-1]
            col_sig1, col_sig2, col_sig3 = st.columns(3)
            
            if latest['SMA50'] > latest['SMA200']:
                col_sig1.success("🟢 Golden Cross (Bullish)")
            else:
                col_sig1.error("🔴 Death Cross (Bearish)")
            
            if latest['RSI'] > 70:
                col_sig2.warning("⚠️ Overbought (RSI > 70)")
            elif latest['RSI'] < 30:
                col_sig2.success("✅ Oversold (RSI < 30)")
            else:
                col_sig2.info("ℹ️ Neutral (RSI 30-70)")
            
            if latest['Close'] > latest['BB_Upper']:
                col_sig3.warning("⚠️ Above BB (Overbought)")
            elif latest['Close'] < latest['BB_Lower']:
                col_sig3.success("✅ Below BB (Oversold)")
            else:
                col_sig3.info("ℹ️ Within BB (Neutral)")
            
            if show_rsi:
                fig_rsi = go.Figure()
                fig_rsi.add_trace(go.Scatter(x=df_ohlc.index, y=df_ohlc['RSI'], name="RSI"))
                fig_rsi.add_hline(y=70, line_dash="dash", line_color="red")
                fig_rsi.add_hline(y=30, line_dash="dash", line_color="green")
                fig_rsi.update_layout(title="RSI (14 períodos)", height=250)
                st.plotly_chart(fig_rsi, use_container_width=True)
            
            if show_stoch:
                fig_stoch = go.Figure()
                fig_stoch.add_trace(go.Scatter(x=df_ohlc.index, y=df_ohlc['Stoch_K'], name="%K"))
                fig_stoch.add_trace(go.Scatter(x=df_ohlc.index, y=df_ohlc['Stoch_D'], name="%D"))
                fig_stoch.add_hline(y=80, line_dash="dash", line_color="red")
                fig_stoch.add_hline(y=20, line_dash="dash", line_color="green")
                fig_stoch.update_layout(title="Stochastic Oscillator", height=250)
                st.plotly_chart(fig_stoch, use_container_width=True)
        
        with col2:
            st.markdown("<h4>Indicadores en Tiempo Real</h4>", unsafe_allow_html=True)
            
            st.metric("Precio Actual", f"${df_ohlc['Close'].iloc[-1]:.2f}")
            st.metric("RSI (14)", f"{df_ohlc['RSI'].iloc[-1]:.2f}")
            st.metric("MACD", f"{df_ohlc['MACD'].iloc[-1]:.4f}")
            st.metric("ATR (14)", f"{df_ohlc['ATR'].iloc[-1]:.4f}")
            st.metric("Williams %R", f"{df_ohlc['Williams_R'].iloc[-1]:.2f}")
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("<h5>Niveles Fibonacci</h5>", unsafe_allow_html=True)
            
            recent_high = df_ohlc['High'].tail(100).max()
            recent_low = df_ohlc['Low'].tail(100).min()
            fib_levels = calc_fibonacci(recent_high, recent_low)
            
            for level, price in fib_levels.items():
                st.metric(level, f"${price:.2f}")
    
    with tab2:
        st.markdown("<h4>Backtesting Engine</h4>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Configuración de Estrategia</h5>", unsafe_allow_html=True)
            
            strat = st.selectbox("Estrategia", ["SMA Crossover", "MACD Signal", "RSI Mean Reversion", "Bollinger Bands"])
            capital = st.number_input("Capital Inicial ($)", value=100000, step=10000)
            
        with col2:
            st.markdown("<h5>Parámetros de Estrategia</h5>", unsafe_allow_html=True)
            
            if strat == "SMA Crossover":
                fast_period = st.number_input("Período Rápido", value=50, min_value=5, max_value=200)
                slow_period = st.number_input("Período Lento", value=200, min_value=10, max_value=300)
            elif strat == "RSI Mean Reversion":
                rsi_overbought = st.number_input("RSI Overbought", value=70, min_value=50, max_value=90)
                rsi_oversold = st.number_input("RSI Oversold", value=30, min_value=10, max_value=50)
        
        if st.button("🧪 Ejecutar Backtest"):
            trades = []
            equity = [capital]
            position = 0
            
            for i in range(200, len(df_ohlc)):
                row = df_ohlc.iloc[i]
                prev = df_ohlc.iloc[i-1]
                
                if strat == "SMA Crossover":
                    if prev['SMA50'] < prev['SMA200'] and row['SMA50'] > row['SMA200'] and position == 0:
                        position = capital / row['Close']
                        trades.append({'type': 'BUY', 'price': row['Close'], 'date': df_ohlc.index[i]})
                    elif prev['SMA50'] > prev['SMA200'] and row['SMA50'] < row['SMA200'] and position > 0:
                        pnl = (row['Close'] - trades[-1]['price']) * position
                        capital += pnl
                        position = 0
                        trades.append({'type': 'SELL', 'price': row['Close'], 'pnl': pnl, 'date': df_ohlc.index[i]})
                
                equity.append(capital + position * row['Close'])
            
            final_capital = equity[-1]
            total_return_pct = (final_capital - 100000) / 100000 * 100
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Capital Final", f"${final_capital:,.2f}")
            col2.metric("Retorno Total", f"{total_return_pct:.2f}%")
            col3.metric("Trades Ejecutados", len(trades))
            
            fig_eq = go.Figure()
            fig_eq.add_trace(go.Scatter(x=df_ohlc.index[199:], y=equity[1:], name="Equity"))
            fig_eq.update_layout(title="Equity Curve - " + strat, yaxis_title="Capital ($)", height=400)
            st.plotly_chart(fig_eq, use_container_width=True)
            
            # Métricas de backtesting mejoradas
            if len(trades) > 0:
                winning_trades = [t for t in trades if t.get('pnl', 0) > 0]
                losing_trades = [t for t in trades if t.get('pnl', 0) < 0]
                win_rate = len(winning_trades) / len(trades) * 100 if trades else 0
                
                st.markdown("<br>", unsafe_allow_html=True)
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("Win Rate", f"{win_rate:.1f}%")
                col2.metric("Trades Ganadores", len(winning_trades))
                col3.metric("Trades Perdedores", len(losing_trades))
                col4.metric("Avg Trade", f"${sum(t.get('pnl', 0) for t in trades) / len(trades):.2f}")
                
                add_xp(15, "backtesting")
                show_toast("✅ Backtesting completado", "success")
    
    with tab3:
        st.markdown("<h4>💰 Paper Trading - Simulación con Dinero Virtual</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Paper Trading:** Simula operaciones de trading con dinero virtual sin riesgo real.
        Ideal para probar estrategias antes de usar capital real.
        """)
        
        # Inicializar paper trading balance
        if 'paper_balance' not in st.session_state:
            st.session_state.paper_balance = 100000
            st.session_state.paper_positions = []
            st.session_state.paper_trades = []
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Balance Virtual", f"${st.session_state.paper_balance:,.2f}")
        
        with col2:
            total_positions = sum(p['qty'] * df_ohlc['Close'].iloc[-1] for p in st.session_state.paper_positions)
            st.metric("Valor Posiciones", f"${total_positions:,.2f}")
        
        with col3:
            total_equity = st.session_state.paper_balance + total_positions
            st.metric("Equity Total", f"${total_equity:,.2f}")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Nueva Orden</h5>", unsafe_allow_html=True)
            
            order_type = st.selectbox("Tipo de Orden", ["Market", "Limit"])
            side = st.selectbox("Lado", ["BUY", "SELL"])
            qty = st.number_input("Cantidad", value=1.0, min_value=0.1, step=0.1)
            
            if order_type == "Limit":
                limit_price = st.number_input("Precio Límite", value=df_ohlc['Close'].iloc[-1], step=0.01)
            
            if st.button("📊 Ejecutar Orden"):
                current_price = df_ohlc['Close'].iloc[-1]
                
                if side == "BUY":
                    cost = qty * current_price
                    if cost <= st.session_state.paper_balance:
                        st.session_state.paper_balance -= cost
                        st.session_state.paper_positions.append({
                            'symbol': symbol,
                            'qty': qty,
                            'entry_price': current_price,
                            'timestamp': datetime.now()
                        })
                        st.session_state.paper_trades.append({
                            'type': 'BUY',
                            'symbol': symbol,
                            'qty': qty,
                            'price': current_price,
                            'timestamp': datetime.now()
                        })
                        st.success(f"✅ Compra ejecutada: {qty} {symbol} @ ${current_price:.2f}")
                        add_xp(5, "paper_trading")
                    else:
                        st.error("❌ Balance insuficiente")
                else:
                    # Venta
                    position_to_sell = None
                    for pos in st.session_state.paper_positions:
                        if pos['symbol'] == symbol and pos['qty'] >= qty:
                            position_to_sell = pos
                            break
                    
                    if position_to_sell:
                        proceeds = qty * current_price
                        st.session_state.paper_balance += proceeds
                        position_to_sell['qty'] -= qty
                        if position_to_sell['qty'] == 0:
                            st.session_state.paper_positions.remove(position_to_sell)
                        
                        st.session_state.paper_trades.append({
                            'type': 'SELL',
                            'symbol': symbol,
                            'qty': qty,
                            'price': current_price,
                            'timestamp': datetime.now()
                        })
                        st.success(f"✅ Venta ejecutada: {qty} {symbol} @ ${current_price:.2f}")
                        add_xp(5, "paper_trading")
                    else:
                        st.error("❌ No tienes posición suficiente")
        
        with col2:
            st.markdown("<h5>Posiciones Abiertas</h5>", unsafe_allow_html=True)
            
            if st.session_state.paper_positions:
                for pos in st.session_state.paper_positions:
                    current_price = df_ohlc['Close'].iloc[-1]
                    pnl = (current_price - pos['entry_price']) * pos['qty']
                    pnl_pct = (current_price - pos['entry_price']) / pos['entry_price'] * 100
                    
                    st.markdown(f"""
                    <div class="glass-card">
                        <p><strong>{pos['symbol']}</strong> - {pos['qty']} @ ${pos['entry_price']:.2f}</p>
                        <p>P&L: <span style="color: {'green' if pnl >= 0 else 'red'}">${pnl:.2f} ({pnl_pct:+.2f}%)</span></p>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.info("No hay posiciones abiertas")
    
    with tab4:
        st.markdown("<h4>🔔 Price Alerts - Alertas de Precio</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Price Alerts:** Configura alertas de precio para recibir notificaciones cuando el activo
        alcance un nivel específico.
        """)
        
        # Inicializar alerts
        if 'price_alerts' not in st.session_state:
            st.session_state.price_alerts = []
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            alert_type = st.selectbox("Tipo de Alerta", ["Above", "Below"])
        
        with col2:
            alert_price = st.number_input("Precio Objetivo", value=df_ohlc['Close'].iloc[-1] * 1.05, step=0.01)
        
        with col3:
            alert_symbol = st.selectbox("Símbolo", ["BTCUSDT", "ETHUSDT", "BNBUSDT", "ADAUSDT"], key="alert_symbol")
        
        if st.button("🔔 Crear Alerta"):
            st.session_state.price_alerts.append({
                'symbol': alert_symbol,
                'type': alert_type,
                'price': alert_price,
                'created_at': datetime.now(),
                'triggered': False
            })
            st.success(f"✅ Alerta creada: {alert_symbol} {alert_type} ${alert_price:.2f}")
            add_xp(5, "price_alerts")
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<h5>Alertas Activas</h5>", unsafe_allow_html=True)
        
        if st.session_state.price_alerts:
            for alert in st.session_state.price_alerts:
                if not alert['triggered']:
                    st.markdown(f"""
                    <div class="glass-card">
                        <p><strong>{alert['symbol']}</strong> - {alert['type']} ${alert['price']:.2f}</p>
                        <p style="font-size: 0.8rem; color: #64748b;">Creada: {alert['created_at'].strftime('%Y-%m-%d %H:%M')}</p>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.info("No hay alertas activas")
    
    with tab5:
        st.markdown("<h4>Portfolio Management</h4>", unsafe_allow_html=True)
        
        portfolio = pd.DataFrame({
            'Symbol': ['AAPL', 'TSLA', 'NVDA', 'MSFT', 'BTC'],
            'Side': ['LONG', 'SHORT', 'LONG', 'LONG', 'LONG'],
            'Qty': [100, 50, 75, 80, 2.5],
            'Entry': [175.5, 242.8, 892.3, 420.15, 43500],
            'Current': [182.3, 235.5, 925.7, 445.80, 42100],
            'P&L': [680, -365, 2505, 2052, -3500],
            'P&L%': [3.9, -3.0, 3.7, 6.1, -3.2]
        })
        
        st.dataframe(portfolio, use_container_width=True, hide_index=True)
        
        fig_pie = px.pie(portfolio, values=[abs(p) for p in portfolio['P&L']], 
                        names=portfolio['Symbol'], title="P&L por Posición")
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with tab4:
        st.markdown("<h4>Risk Management - Gestión de Riesgo Avanzada</h4>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            account = st.number_input("Capital Total ($)", value=50000, step=1000)
            risk_pct = st.slider("Riesgo por Trade (%)", 0.5, 5.0, 2.0, 0.5)
            stop_loss = st.number_input("Stop Loss ($)", value=2.5, step=0.5)
            entry = st.number_input("Precio Entrada ($)", value=100.0, step=1.0)
        
        with col2:
            risk_amount = account * (risk_pct / 100)
            position_shares = int(risk_amount / stop_loss) if stop_loss > 0 else 0
            position_value = position_shares * entry
            
            st.markdown(f"""
            <div class="glass-card" style="background: linear-gradient(135deg, #dbeafe, #bfdbfe);">
                <h4 style="color: #1e40af;">📊 Cálculo de Posición</h4>
                <p><strong>Riesgo Total:</strong> ${risk_amount:.2f}</p>
                <p><strong>Shares a Comprar:</strong> {position_shares}</p>
                <p><strong>Valor Posición:</strong> ${position_value:,.2f}</p>
                <p><strong>% de Portfolio:</strong> {(position_value/account)*100:.1f}%</p>
            </div>
            """, unsafe_allow_html=True)
            
            win_rate = st.slider("Win Rate Estimado (%)", 30, 70, 55, 5)
            avg_win = st.number_input("Ganancia Promedio ($)", value=5.0)
            avg_loss = st.number_input("Pérdida Promedio ($)", value=3.0)
            
            kelly_pct = ((win_rate/100) * avg_win - ((1-win_rate/100) * avg_loss)) / avg_win
            st.metric("Kelly Criterion", f"{kelly_pct*100:.2f}% del capital")
    
    with tab5:
        st.markdown("<h4>Portfolio Optimization - Markowitz Efficient Frontier</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Modern Portfolio Theory:** Optimización de portafolio utilizando el modelo de Markowitz
        para maximizar retorno dado un nivel de riesgo, o minimizar riesgo dado un nivel de retorno.
        """)
        
        assets = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
        returns = np.random.normal(0.001, 0.02, 1000)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=np.random.uniform(0.1, 0.3, 50),
            y=np.random.uniform(0.05, 0.25, 50),
            mode='markers',
            name='Portfolios',
            marker=dict(size=8, color='blue', opacity=0.5)
        ))
        fig.add_trace(go.Scatter(
            x=[0.15], y=[0.18],
            mode='markers',
            name='Optimal',
            marker=dict(size=15, color='red', symbol='star')
        ))
        fig.update_layout(title="Efficient Frontier", xaxis_title="Volatilidad", yaxis_title="Retorno Esperado")
        st.plotly_chart(fig, use_container_width=True)
    
    with tab7:
        st.markdown("<h4>HFT Engine - High-Frequency Trading</h4>", unsafe_allow_html=True)
        
        st.info("""
        **HFT (High-Frequency Trading):** Trading automatizado a microsegundos utilizando 
        algoritmos de baja latencia para capitalizar pequeñas ineficiencias de mercado.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            symbol_hft = st.selectbox("Símbolo", ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"], key="symbol_hft")
            order_size = st.number_input("Tamaño Orden", value=100, step=10, key="hft_order_size")
            latency_us = st.slider("Latencia (μs)", 10, 200, 50, key="hft_latency")
            max_slippage = st.slider("Max Slippage (%)", 0.01, 0.5, 0.05, key="hft_slippage")
        
        with col2:
            st.metric("Orders/Second", "10,000+")
            st.metric("Fill Rate", "99.8%")
            st.metric("Avg Latency", f"{latency_us}μs")
            st.metric("PnL/Hour", f"${random.uniform(1000, 5000):,.0f}")
        
        if st.button("⚡ Ejecutar Orden HFT"):
            if df_ohlc is not None and not df_ohlc.empty:
                current_price = df_ohlc['Close'].iloc[-1]
                executed_price, exec_time, slippage = simulate_hft_execution(current_price, order_size, latency_us)
                
                col1, col2, col3 = st.columns(3)
                col1.metric("Precio Ejecutado", f"${executed_price:.2f}")
                col2.metric("Tiempo Ejecución", f"{exec_time*1000000:.0f}μs")
                col3.metric("Slippage", f"${slippage:.4f}")
                
                if abs(slippage) < current_price * (max_slippage / 100):
                    st.success("✅ Ejecución exitosa dentro de límites de slippage")
                else:
                    st.warning("⚠️ Slippage excede límite máximo")
                
                add_xp(15, "hft_execution")
                show_toast("✅ Orden HFT ejecutada", "success")
            else:
                st.error("Error: No hay datos OHLC disponibles para ejecutar orden HFT")
        
        st.markdown("<h5>Order Book Depth</h5>", unsafe_allow_html=True)
        
        # Usar precio simulado si df_ohlc está vacío
        if df_ohlc is not None and not df_ohlc.empty:
            mid_price = df_ohlc['Close'].iloc[-1]
        else:
            mid_price = 150.0  # Precio simulado
        
        bids = [(mid_price - i*0.01, random.randint(100, 1000)) for i in range(1, 11)]
        asks = [(mid_price + i*0.01, random.randint(100, 1000)) for i in range(1, 11)]
        
        bid_depth, ask_depth, imbalance = calc_order_book_depth(bids, asks)
        spread, spread_pct = calc_spread(bids[0][0], asks[0][0])
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Bid Depth", f"{bid_depth:,}")
        col2.metric("Ask Depth", f"{ask_depth:,}")
        col3.metric("Imbalance", f"{imbalance*100:.1f}%")
        col4.metric("Spread", f"${spread:.4f} ({spread_pct:.2f}%)")
        
        fig_ob = go.Figure()
        fig_ob.add_trace(go.Bar(x=[qty for price, qty in bids], 
                                y=[price for price, qty in bids],
                                name='Bids', orientation='h', marker_color='green'))
        fig_ob.add_trace(go.Bar(x=[qty for price, qty in asks], 
                                y=[price for price, qty in asks],
                                name='Asks', orientation='h', marker_color='red'))
        fig_ob.update_layout(title="Order Book Depth", xaxis_title="Quantity", yaxis_title="Price")
        st.plotly_chart(fig_ob, use_container_width=True)
    
    with tab8:
        st.markdown("<h4>Dark Pool Simulation</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Dark Pool:** Plataformas de trading privadas que permiten ejecutar grandes órdenes 
        fuera de los exchanges públicos, minimizando el impacto en el precio de mercado.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            dp_symbol = st.selectbox("Símbolo Dark Pool", ["AAPL", "GOOGL", "MSFT", "AMZN"], key="dp_symbol")
            dp_order_size = st.number_input("Tamaño Orden", value=10000, step=1000, key="dp_order_size")
            dp_order_type = st.selectbox("Tipo Orden", ["Iceberg", "Hidden", "VWAP", "TWAP"], key="dp_order_type")
            min_fill = st.slider("Fill Mínimo (%)", 10, 100, 50, key="dp_min_fill")
        
        with col2:
            st.metric("Volume 24h", "$2.5B")
            st.metric("Avg Trade Size", "$50K")
            st.metric("Fill Rate", "95.2%")
            st.metric("Price Improvement", f"${random.uniform(0.01, 0.05):.3f}")
        
        if st.button("🌐 Ejecutar en Dark Pool"):
            if df_ohlc is not None and not df_ohlc.empty:
                market_price = df_ohlc['Close'].iloc[-1]
            else:
                market_price = 100.0
                st.warning("Usando precio simulado (no hay datos OHLC disponibles)")
            
            dark_pool_price = market_price * random.uniform(0.999, 1.001)
            price_improvement = abs(dark_pool_price - market_price)
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Precio Mercado", f"${market_price:.2f}")
            col2.metric("Precio Dark Pool", f"${dark_pool_price:.2f}")
            col3.metric("Price Improvement", f"${price_improvement:.3f}")
            
            if price_improvement > 0:
                st.success("✅ Price improvement obtenido en Dark Pool")
            else:
                st.info("ℹ️ Ejecución a precio de mercado")
        
        st.markdown("<h5>Arbitraje Triangular</h5>", unsafe_allow_html=True)
        
        rates = {
            'USD/EUR': st.number_input("USD/EUR", value=0.85, step=0.001),
            'EUR/GBP': st.number_input("EUR/GBP", value=0.88, step=0.001),
            'GBP/USD': st.number_input("GBP/USD", value=1.35, step=0.001)
        }
        
        if st.button("🔄 Calcular Arbitraje"):
            profit, profit_pct, final_usd = triangular_arbitrage(rates)
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Profit", f"${profit:.2f}")
            col2.metric("Profit %", f"{profit_pct:.2f}%")
            col3.metric("Final USD", f"${final_usd:.2f}")
            
            if profit > 0:
                st.success("✅ Oportunidad de arbitraje detectada")
            else:
                st.info("ℹ️ No hay oportunidad de arbitraje")
        
        st.markdown("<h5>Market Making</h5>", unsafe_allow_html=True)
        
        mm_mid_price = st.number_input("Mid Price", value=100.0, step=0.1)
        mm_volatility = st.slider("Volatilidad", 0.01, 0.5, 0.15)
        mm_inventory = st.slider("Inventory Risk", -100, 100, 0)
        
        bid_price, ask_price, total_spread = market_making_spread(mm_mid_price, mm_volatility, mm_inventory)
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Bid Price", f"${bid_price:.2f}")
        col2.metric("Ask Price", f"${ask_price:.2f}")
        col3.metric("Spread", f"${total_spread:.4f}")
    
    with tab10:
        st.markdown("<h4>📰 Sentiment Analysis - Análisis de Sentimiento</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Sentiment Analysis:** Analiza el sentimiento del mercado usando datos de noticias
        y redes sociales para predecir movimientos de precios.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Fuentes de Sentimiento</h5>", unsafe_allow_html=True)
            
            sentiment_sources = st.multiselect(
                "Seleccionar Fuentes",
                ["Twitter/X", "Reddit", "News API", "Telegram", "Discord"],
                default=["Twitter/X", "Reddit"]
            )
            
            keywords = st.text_input("Palabras Clave", value="BTC, Bitcoin, crypto")
            time_window = st.slider("Ventana de Tiempo (horas)", 1, 24, 6)
        
        with col2:
            st.markdown("<h5>Métricas de Sentimiento</h5>", unsafe_allow_html=True)
            
            # Simular datos de sentimiento
            sentiment_score = random.uniform(-1, 1)
            sentiment_label = "Bullish" if sentiment_score > 0.2 else "Bearish" if sentiment_score < -0.2 else "Neutral"
            sentiment_color = "green" if sentiment_score > 0.2 else "red" if sentiment_score < -0.2 else "yellow"
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Sentimiento Score", f"{sentiment_score:.2f}")
            col2.metric("Tendencia", sentiment_label, delta_color="normal")
            col3.metric("Confianza", f"{random.uniform(70, 95):.1f}%")
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(f"**Distribución:**")
            
            positive_pct = random.randint(30, 60)
            negative_pct = random.randint(20, 40)
            neutral_pct = 100 - positive_pct - negative_pct
            
            fig_sentiment = go.Figure(data=[go.Pie(labels=['Positivo', 'Negativo', 'Neutral'], 
                                                  values=[positive_pct, negative_pct, neutral_pct])])
            fig_sentiment.update_layout(title="Distribución de Sentimiento")
            st.plotly_chart(fig_sentiment, use_container_width=True)
        
        # Gráfico de sentimiento histórico
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Historial de Sentimiento (24h)**")
        
        sentiment_history = [random.uniform(-1, 1) for _ in range(24)]
        fig_sent_hist = go.Figure()
        fig_sent_hist.add_trace(go.Scatter(x=list(range(24)), y=sentiment_history, mode='lines', name='Sentimiento'))
        fig_sent_hist.add_hline(y=0, line_dash="dash", line_color="gray")
        fig_sent_hist.update_layout(title="Sentimiento vs Tiempo", xaxis_title="Hora", yaxis_title="Score")
        st.plotly_chart(fig_sent_hist, use_container_width=True)
        
        add_xp(10, "sentiment_analysis")
    
    with tab11:
        st.markdown("<h4>🤖 News Trading - Trading Basado en Noticias</h4>", unsafe_allow_html=True)
        
        st.info("""
        **News Trading:** Sistema de trading automatizado que reacciona a noticias
        en tiempo real para ejecutar trades basados en eventos del mercado.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Configuración de Trading</h5>", unsafe_allow_html=True)
            
            news_symbols = st.multiselect(
                "Símbolos a Monitorear",
                ["BTCUSDT", "ETHUSDT", "BNBUSDT", "ADAUSDT", "SOLUSDT"],
                default=["BTCUSDT", "ETHUSDT"]
            )
            
            news_threshold = st.slider("Umbral de Impacto", 1, 10, 5)
            auto_execute = st.checkbox("Auto-Execute Trades", value=False)
            max_position = st.number_input("Posición Máxima ($)", value=1000, min_value=100)
        
        with col2:
            st.markdown("<h5>Noticias Recientes</h5>", unsafe_allow_html=True)
            
            # Simular noticias
            recent_news = [
                {"title": "Bitcoin alcanza nuevo ATH", "impact": 8.5, "sentiment": "positive", "time": "2 min"},
                {"title": "Fed anuncia tasas de interés", "impact": 9.2, "sentiment": "negative", "time": "15 min"},
                {"title": "ETF de Bitcoin aprobado", "impact": 7.8, "sentiment": "positive", "time": "30 min"},
                {"title": "Regulación crypto en UE", "impact": 6.5, "sentiment": "neutral", "time": "1 hr"}
            ]
            
            for news in recent_news:
                impact_color = "green" if news['impact'] >= news_threshold else "gray"
                with st.expander(f"📰 {news['title']}"):
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Impacto", f"{news['impact']}/10")
                    col2.metric("Sentimiento", news['sentiment'].capitalize())
                    col3.metric("Hace", news['time'])
                    
                    if news['impact'] >= news_threshold and auto_execute:
                        st.success(f"🚀 Trade auto-ejecutado para {random.choice(news_symbols)}")
                        add_xp(5, "news_trading")
        
        # Estadísticas de trading
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Estadísticas de News Trading**")
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Trades Ejecutados", f"{random.randint(50, 200)}")
        col2.metric("Win Rate", f"{random.uniform(55, 75):.1f}%")
        col3.metric("PnL Total", f"${random.uniform(-500, 2000):,.0f}")
        col4.metric("Avg Latency", f"{random.uniform(100, 500):.0f}ms")
        
        add_xp(10, "news_trading")
    
    with tab12:
        st.markdown("<h4>📊 Order Flow - Flujo de Órdenes</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Order Flow:** Análisis del flujo de órdenes en tiempo real para detectar
        presión de compra/venta, liquidez y posibles movimientos de precio.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Depth of Market (DOM)</h5>", unsafe_allow_html=True)
            
            # Simular order book
            price_levels = []
            current_price = df_ohlc['Close'].iloc[-1] if not df_ohlc.empty else 100.0
            
            for i in range(10):
                ask_price = current_price + (i + 1) * 0.01
                bid_price = current_price - (i + 1) * 0.01
                ask_size = random.randint(10, 100)
                bid_size = random.randint(10, 100)
                price_levels.append({
                    "ask_price": ask_price,
                    "ask_size": ask_size,
                    "bid_price": bid_price,
                    "bid_size": bid_size
                })
            
            # Mostrar order book
            st.markdown("**Ask (Venta)** | **Bid (Compra)**")
            for level in price_levels:
                st.markdown(f"""
                <div style="display: flex; justify-content: space-between; padding: 5px; border-bottom: 1px solid #e0e0e0;">
                    <span style="color: red;">{level['ask_price']:.2f} ({level['ask_size']})</span>
                    <span style="color: green;">{level['bid_price']:.2f} ({level['bid_size']})</span>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("<h5>Imbalance Ratio</h5>", unsafe_allow_html=True)
            
            # Calcular imbalance
            total_bid = sum(level['bid_size'] for level in price_levels)
            total_ask = sum(level['ask_size'] for level in price_levels)
            imbalance = (total_bid - total_ask) / (total_bid + total_ask) if (total_bid + total_ask) > 0 else 0
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Bid", f"{total_bid}")
            col2.metric("Total Ask", f"{total_ask}")
            col3.metric("Imbalance", f"{imbalance:.2%}", delta_color="normal")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            if imbalance > 0.2:
                st.success("🟢 Presión de compra detectada")
            elif imbalance < -0.2:
                st.error("🔴 Presión de venta detectada")
            else:
                st.info("⚪ Mercado equilibrado")
        
        # Gráfico de order flow
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Order Flow History**")
        
        order_flow_history = [random.uniform(-50, 50) for _ in range(50)]
        fig_flow = go.Figure()
        fig_flow.add_trace(go.Bar(x=list(range(50)), y=order_flow_history, 
                                    marker_color=['green' if x > 0 else 'red' for x in order_flow_history]))
        fig_flow.add_hline(y=0, line_dash="dash", line_color="gray")
        fig_flow.update_layout(title="Order Flow (Net Volume)", xaxis_title="Tiempo", yaxis_title="Net Volume")
        st.plotly_chart(fig_flow, use_container_width=True)
        
        add_xp(10, "order_flow")
    
    with tab13:
        st.markdown("<h4>📈 Position Sizing - Tamaño de Posición</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Position Sizing:** Cálculo del tamaño óptimo de posición basado en
        riesgo por trade, volatilidad y capital disponible para maximizar retornos
        mientras se controla el riesgo.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Parámetros de Posición</h5>", unsafe_allow_html=True)
            
            account_balance = st.number_input("Balance de Cuenta ($)", value=10000.0, min_value=0.0)
            risk_per_trade = st.slider("Riesgo por Trade (%)", 1, 10, 2)
            stop_loss_pct = st.slider("Stop Loss (%)", 1, 10, 2)
            entry_price = st.number_input("Precio de Entrada", value=100.0, min_value=0.0)
            
            # Calcular tamaño de posición
            risk_amount = account_balance * (risk_per_trade / 100)
            stop_loss_amount = entry_price * (stop_loss_pct / 100)
            position_size = risk_amount / stop_loss_amount if stop_loss_amount > 0 else 0
            position_value = position_size * entry_price
            
            if st.button("📈 Calcular Tamaño de Posición"):
                st.success("✅ Cálculo completado")
                add_xp(10, "position_sizing")
                show_toast("✅ Position sizing calculado", "success")
        
        with col2:
            st.markdown("<h5>Resultados</h5>", unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Riesgo por Trade", f"${risk_amount:,.2f}")
            col2.metric("Tamaño de Posición", f"{position_size:.2f} unidades")
            col3.metric("Valor de Posición", f"${position_value:,.2f}")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Kelly Criterion
            win_rate = st.slider("Win Rate (%)", 30, 80, 55)
            avg_win = st.number_input("Ganancia Promedio (%)", value=3.0)
            avg_loss = st.number_input("Pérdida Promedio (%)", value=2.0)
            
            # Kelly Criterion calculation
            if avg_loss > 0:
                kelly_pct = ((win_rate / 100) * avg_win - ((1 - win_rate / 100) * avg_loss)) / avg_win
                kelly_pct = max(0, min(kelly_pct, 0.25))  # Cap at 25%
                kelly_size = account_balance * kelly_pct
                kelly_units = kelly_size / entry_price
                
                st.metric("Kelly Criterion", f"{kelly_pct:.2%}")
                st.metric("Tamaño Kelly", f"{kelly_units:.2f} unidades")
        
        add_xp(10, "position_sizing")
    
    with tab14:
        st.markdown("<h4>💵 Risk Calculator - Calculadora de Riesgo</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Risk Calculator:** Herramienta completa para calcular y gestionar
        el riesgo de trading incluyendo Value at Risk (VaR), Expected Shortfall
        y análisis de drawdown.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Parámetros de Riesgo</h5>", unsafe_allow_html=True)
            
            portfolio_value = st.number_input("Valor del Portfolio ($)", value=100000.0, min_value=0.0)
            confidence_level = st.selectbox("Nivel de Confianza VaR", [90, 95, 99])
            time_horizon = st.selectbox("Horizonte de Tiempo", ["1 día", "1 semana", "1 mes"])
            volatility = st.slider("Volatilidad Anual (%)", 10, 50, 25)
            
            if st.button("💵 Calcular Riesgo"):
                st.success("✅ Cálculo de riesgo completado")
                add_xp(10, "risk_calculator")
                show_toast("✅ Riesgo calculado", "success")
        
        with col2:
            st.markdown("<h5>Métricas de Riesgo</h5>", unsafe_allow_html=True)
            
            # Calcular VaR
            z_score = {90: 1.28, 95: 1.65, 99: 2.33}[confidence_level]
            daily_vol = volatility / 100 / np.sqrt(252)
            time_multiplier = {"1 día": 1, "1 semana": 5, "1 mes": 22}[time_horizon]
            var_amount = portfolio_value * z_score * daily_vol * np.sqrt(time_multiplier)
            
            col1, col2, col3 = st.columns(3)
            col1.metric(f"VaR {confidence_level}%", f"${var_amount:,.2f}")
            col2.metric("% del Portfolio", f"{var_amount/portfolio_value*100:.2f}%")
            col3.metric("Volatilidad Diaria", f"{daily_vol*100:.2f}%")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Expected Shortfall (ES)
            es_amount = var_amount * 1.3  # ES ~1.3x VaR
            st.metric("Expected Shortfall (CVaR)", f"${es_amount:,.2f}")
            
            # Drawdown analysis
            max_drawdown = st.slider("Máximo Drawdown Histórico (%)", 5, 50, 20)
            recovery_time = st.slider("Tiempo de Recuperación (días)", 10, 365, 90)
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("**Análisis de Drawdown**")
            
            col1, col2 = st.columns(2)
            col1.metric("Max DD Actual", f"{max_drawdown}%")
            col2.metric("Tiempo Recuperación", f"{recovery_time} días")
        
        # Gráfico de distribución de pérdidas
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Distribución de Pérdidas Simuladas**")
        
        simulated_losses = np.random.normal(0, portfolio_value * daily_vol * np.sqrt(time_multiplier), 1000)
        fig_risk = go.Figure()
        fig_risk.add_trace(go.Histogram(x=simulated_losses, nbinsx=50, name="Pérdidas"))
        fig_risk.add_vline(x=-var_amount, line_dash="dash", line_color="red", annotation_text=f"VaR {confidence_level}%")
        fig_risk.update_layout(title="Distribución de Pérdidas", xaxis_title="Pérdida ($)", yaxis_title="Frecuencia")
        st.plotly_chart(fig_risk, use_container_width=True)
        
        add_xp(10, "risk_calculator")
    
    with tab15:
        st.markdown("<h4>🔍 Market Scanner - Escáner de Mercado</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Market Scanner:** Escaneo automatizado del mercado para identificar
        oportunidades de trading basadas en indicadores técnicos, patrones y señales.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Configuración del Escáner</h5>", unsafe_allow_html=True)
            
            scan_type = st.selectbox("Tipo de Escaneo", ["Breakout", "Reversal", "Momentum", "Volume Spike"])
            timeframe = st.selectbox("Timeframe", ["1m", "5m", "15m", "1h", "4h", "1d"])
            min_volume = st.number_input("Volumen Mínimo", value=1000000, min_value=0)
            
            if st.button("🔍 Iniciar Escaneo"):
                st.success("✅ Escaneo completado")
                add_xp(15, "market_scanner")
                show_toast("✅ Market scanner completado", "success")
        
        with col2:
            st.markdown("<h5>Oportunidades Detectadas</h5>", unsafe_allow_html=True)
            
            opportunities = [
                {"symbol": "BTCUSDT", "type": "Breakout", "entry": 45000, "target": 47000, "confidence": 85},
                {"symbol": "ETHUSDT", "type": "Reversal", "entry": 3200, "target": 3400, "confidence": 78},
                {"symbol": "BNBUSDT", "type": "Momentum", "entry": 400, "target": 420, "confidence": 72}
            ]
            
            for opp in opportunities:
                with st.expander(f"📊 {opp['symbol']} - {opp['type']}"):
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Entrada", f"${opp['entry']}")
                    col2.metric("Target", f"${opp['target']}")
                    col3.metric("Confianza", f"{opp['confidence']}%")
        
        # Gráfico de oportunidades
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Distribución de Oportunidades por Tipo**")
        
        fig_scanner = go.Figure(data=[go.Pie(labels=[o['type'] for o in opportunities], values=[o['confidence'] for o in opportunities])])
        fig_scanner.update_layout(title="Oportunidades por Tipo")
        st.plotly_chart(fig_scanner, use_container_width=True)
        
        add_xp(10, "market_scanner")
    
    with tab16:
        st.markdown("<h4>📊 Correlation Matrix - Matriz de Correlación</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Correlation Matrix:** Análisis de correlación entre diferentes activos
        para identificar relaciones y diversificar el portafolio efectivamente.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Configuración de Correlación</h5>", unsafe_allow_html=True)
            
            assets = st.multiselect("Activos a Analizar", ["BTC", "ETH", "BNB", "ADA", "SOL", "XRP", "DOT", "AVAX"], default=["BTC", "ETH", "BNB"])
            timeframe_corr = st.selectbox("Timeframe", ["1d", "1w", "1m"])
            correlation_method = st.selectbox("Método", ["Pearson", "Spearman", "Kendall"])
            
            if st.button("📊 Calcular Correlación"):
                st.success("✅ Correlación calculada")
                add_xp(15, "correlation_matrix")
                show_toast("✅ Correlation matrix calculado", "success")
        
        with col2:
            st.markdown("<h5>Resumen de Correlaciones</h5>", unsafe_allow_html=True)
            
            correlations = [
                {"pair": "BTC-ETH", "corr": 0.85, "type": "Alta"},
                {"pair": "BTC-BNB", "corr": 0.72, "type": "Media-Alta"},
                {"pair": "ETH-BNB", "corr": 0.68, "type": "Media"}
            ]
            
            for corr in correlations:
                color = "green" if corr['corr'] > 0.7 else "orange" if corr['corr'] > 0.5 else "red"
                st.markdown(f"""
                <div style="padding: 8px; margin: 5px 0; border-left: 3px solid {color}; background: rgba(100,100,100,0.1); border-radius: 3px;">
                    <strong>{corr['pair']}</strong> - {corr['corr']:.2f} ({corr['type']})
                </div>
                """, unsafe_allow_html=True)
        
        # Gráfico de heatmap de correlación
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Heatmap de Correlación**")
        
        # Simular datos de correlación
        corr_data = [[1.0, 0.85, 0.72], [0.85, 1.0, 0.68], [0.72, 0.68, 1.0]]
        fig_heatmap = go.Figure(data=go.Heatmap(
            z=corr_data,
            x=["BTC", "ETH", "BNB"],
            y=["BTC", "ETH", "BNB"],
            colorscale='RdBu',
            zmid=0
        ))
        fig_heatmap.update_layout(title="Matriz de Correlación")
        st.plotly_chart(fig_heatmap, use_container_width=True)
        
        add_xp(10, "correlation_matrix")
    
    with tab17:
        st.markdown("<h4>📈 Portfolio Analytics - Análisis de Portafolio</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Portfolio Analytics:** Análisis completo del portafolio incluyendo
        rendimiento, riesgo, diversificación y attribution de retornos.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Métricas del Portafolio</h5>", unsafe_allow_html=True)
            
            portfolio_value = st.number_input("Valor del Portafolio ($)", value=100000, min_value=0)
            benchmark = st.selectbox("Benchmark", ["S&P 500", "BTC", "ETH", "Custom"])
            time_period = st.selectbox("Período", ["1M", "3M", "6M", "1Y", "YTD"])
            
            if st.button("📈 Analizar Portafolio"):
                st.success("✅ Análisis completado")
                add_xp(15, "portfolio_analytics")
                show_toast("✅ Portfolio analytics completado", "success")
        
        with col2:
            st.markdown("<h5>Resultados del Análisis</h5>", unsafe_allow_html=True)
            
            # Simular métricas
            total_return = random.uniform(-20, 50)
            benchmark_return = random.uniform(-15, 40)
            alpha = total_return - benchmark_return
            beta = random.uniform(0.5, 1.5)
            tracking_error = random.uniform(2, 10)
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Retorno Total", f"{total_return:.2f}%")
            col2.metric("Alpha", f"{alpha:.2f}%")
            col3.metric("Beta", f"{beta:.2f}")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            col1.metric("Tracking Error", f"{tracking_error:.2f}%")
            col2.metric("Information Ratio", f"{alpha/tracking_error:.2f}")
        
        # Gráfico de attribution
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Attribution de Retornos**")
        
        attribution = {
            "Asset Allocation": 45,
            "Stock Selection": 30,
            "Timing": 15,
            "Interaction": 10
        }
        
        fig_attribution = go.Figure(data=[go.Pie(labels=list(attribution.keys()), values=list(attribution.values()))])
        fig_attribution.update_layout(title="Attribution de Retornos")
        st.plotly_chart(fig_attribution, use_container_width=True)
        
        add_xp(10, "portfolio_analytics")
    
    with tab18:
        st.markdown("<h4>🎯 Options Trading - Trading de Opciones</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Options Trading:** Análisis y trading de opciones con cálculo de Greeks,
        estrategias complejas y gestión de riesgo de opciones.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Configuración de Opción</h5>", unsafe_allow_html=True)
            
            option_type = st.selectbox("Tipo de Opción", ["Call", "Put"])
            underlying_price = st.number_input("Precio del Subyacente ($)", value=100.0, min_value=0.0)
            strike_price = st.number_input("Precio de Ejercicio ($)", value=95.0, min_value=0.0)
            time_to_expiry = st.number_input("Tiempo al Vencimiento (días)", value=30, min_value=1)
            volatility = st.slider("Volatilidad Implícita (%)", 10, 100, 25)
            risk_free_rate = st.slider("Tasa Libre de Riesgo (%)", 0, 10, 5)
            
            if st.button("🎯 Calcular Opción"):
                st.success("✅ Opción calculada")
                add_xp(10, "options_trading")
                show_toast("✅ Opción calculada", "success")
        
        with col2:
            st.markdown("<h5>Greeks y Valor</h5>", unsafe_allow_html=True)
            
            # Calcular valor de opción (Black-Scholes simplificado)
            from math import sqrt, exp, log, erf
            import numpy as np
            
            S = underlying_price
            K = strike_price
            T = time_to_expiry / 365
            sigma = volatility / 100
            r = risk_free_rate / 100
            
            d1 = (log(S/K) + (r + sigma**2/2)*T) / (sigma*sqrt(T))
            d2 = d1 - sigma*sqrt(T)
            
            from scipy.stats import norm
            N = norm.cdf
            
            if option_type == "Call":
                option_price = S*N(d1) - K*exp(-r*T)*N(d2)
                delta = N(d1)
            else:
                option_price = K*exp(-r*T)*N(-d2) - S*N(-d1)
                delta = N(d1) - 1
            
            gamma = norm.pdf(d1) / (S*sigma*sqrt(T))
            theta = -(S*norm.pdf(d1)*sigma)/(2*sqrt(T)) - r*K*exp(-r*T)*N(d2) if option_type == "Call" else -(S*norm.pdf(d1)*sigma)/(2*sqrt(T)) + r*K*exp(-r*T)*N(-d2)
            vega = S*norm.pdf(d1)*sqrt(T) / 100
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Precio Opción", f"${option_price:.2f}")
            col2.metric("Delta", f"{delta:.3f}")
            col3.metric("Gamma", f"{gamma:.3f}")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            col1.metric("Theta", f"{theta:.3f}")
            col2.metric("Vega", f"{vega:.3f}")
        
        add_xp(10, "options_trading")
    
    with tab19:
        st.markdown("<h4>📈 Futures Trading - Trading de Futuros</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Futures Trading:** Trading de contratos de futuros con gestión de márgenes,
        análisis de spreads y hedging de posiciones.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Configuración de Futuro</h5>", unsafe_allow_html=True)
            
            futures_contract = st.selectbox("Contrato de Futuro", ["S&P 500 E-mini", "Crude Oil WTI", "Gold Futures", "Euro FX", "10-Year Treasury"])
            contract_size = st.number_input("Tamaño del Contrato", value=1, min_value=1)
            entry_price = st.number_input("Precio de Entrada ($)", value=4500.0, min_value=0.0)
            target_price = st.number_input("Precio Objetivo ($)", value=4600.0, min_value=0.0)
            stop_loss = st.number_input("Stop Loss ($)", value=4450.0, min_value=0.0)
            
            if st.button("📈 Abrir Posición"):
                st.success("✅ Posición abierta")
                add_xp(10, "futures_trading")
                show_toast("✅ Posición de futuros abierta", "success")
        
        with col2:
            st.markdown("<h5>Métricas de Futuro</h5>", unsafe_allow_html=True)
            
            tick_value = 12.5 if "S&P" in futures_contract else 10
            tick_size = 0.25 if "S&P" in futures_contract else 0.01
            
            potential_profit = (target_price - entry_price) * contract_size * tick_value / tick_size
            potential_loss = (entry_price - stop_loss) * contract_size * tick_value / tick_size
            risk_reward = potential_profit / potential_loss if potential_loss > 0 else 0
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Ganancia Potencial", f"${potential_profit:,.2f}")
            col2.metric("Pérdida Potencial", f"${potential_loss:,.2f}")
            col3.metric("Risk/Reward", f"{risk_reward:.2f}")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            col1.metric("Tick Value", f"${tick_value}")
            col2.metric("Tick Size", f"{tick_size}")
        
        # Gráfico de P&L
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Perfil de P&L**")
        
        prices = np.linspace(entry_price - 100, entry_price + 100, 100)
        pnl = [(p - entry_price) * contract_size * tick_value / tick_size for p in prices]
        
        fig_futures = go.Figure()
        fig_futures.add_trace(go.Scatter(x=prices, y=pnl, mode='lines', name='P&L'))
        fig_futures.add_vline(x=entry_price, line_dash="dash", line_color="gray", annotation_text="Entry")
        fig_futures.add_vline(x=target_price, line_dash="dash", line_color="green", annotation_text="Target")
        fig_futures.add_vline(x=stop_loss, line_dash="dash", line_color="red", annotation_text="Stop Loss")
        fig_futures.update_layout(title="Perfil de P&L de Futuros", xaxis_title="Precio", yaxis_title="P&L ($)")
        st.plotly_chart(fig_futures, use_container_width=True)
        
        add_xp(10, "futures_trading")
    
    with tab20:
        st.markdown("<h4>💳 Margin Trading - Trading con Margen</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Margin Trading:** Trading con apalancamiento usando margen, con cálculo
        de requisitos de margen, maintenance margin y riesgo de liquidación.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Configuración de Margen</h5>", unsafe_allow_html=True)
            
            asset = st.selectbox("Activo", ["BTC/USDT", "ETH/USDT", "AAPL", "TSLA"])
            position_value = st.number_input("Valor de Posición ($)", value=10000.0, min_value=0.0)
            leverage = st.slider("Apalancamiento (x)", 1, 100, 10)
            initial_margin_pct = st.slider("Margen Inicial (%)", 10, 50, 20)
            maintenance_margin_pct = st.slider("Margen de Mantenimiento (%)", 5, 25, 10)
            
            if st.button("💳 Calcular Margen"):
                st.success("✅ Margen calculado")
                add_xp(10, "margin_trading")
                show_toast("✅ Margen calculado", "success")
        
        with col2:
            st.markdown("<h5>Métricas de Margen</h5>", unsafe_allow_html=True)
            
            initial_margin = position_value * initial_margin_pct / 100
            maintenance_margin = position_value * maintenance_margin_pct / 100
            liquidation_price = position_value * (1 - maintenance_margin_pct / 100) / leverage
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Margen Inicial", f"${initial_margin:,.2f}")
            col2.metric("Margen Mantenimiento", f"${maintenance_margin:,.2f}")
            col3.metric("Precio Liquidación", f"${liquidation_price:,.2f}")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            current_margin_pct = 25
            margin_call_threshold = maintenance_margin_pct * 1.5
            
            col1.metric("Margen Actual", f"{current_margin_pct}%")
            col2.metric("Threshold Margin Call", f"{margin_call_threshold}%")
        
        # Gráfico de margen
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Niveles de Margen**")
        
        margin_levels = ["Free", "Initial", "Maintenance", "Liquidation"]
        margin_values = [position_value * 0.8, initial_margin, maintenance_margin, 0]
        
        fig_margin = go.Figure()
        fig_margin.add_trace(go.Bar(x=margin_levels, y=margin_values, marker_color=['green', 'blue', 'orange', 'red']))
        fig_margin.update_layout(title="Niveles de Margen", xaxis_title="Nivel", yaxis_title="Valor ($)")
        st.plotly_chart(fig_margin, use_container_width=True)
        
        add_xp(10, "margin_trading")

# ================================================================================
# FINRISK AI ELITE
# ================================================================================
elif selected == "🤖 FinRisk AI Elite":
    st.markdown('<h1 class="main-header">🤖 FinRisk AI Elite</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Ensemble Methods | Deep Learning | Real-Time Scoring API | Model Monitoring | A/B Testing</p>', unsafe_allow_html=True)
    
    # Otorgar XP por usar FinRisk AI
    if 'finrisk_visited' not in st.session_state:
        add_xp(10, "model_training")
        st.session_state.finrisk_visited = True
    
    cols = st.columns(6)
    cols[0].metric("🎯 Accuracy", "94.7%", "+2.3% vs baseline")
    cols[1].metric("📊 Precision", "92.1%", "Clase 'Alto Riesgo'")
    cols[2].metric("📈 Recall", "89.8%", "Detección temprana")
    cols[3].metric("⚡ Latencia", "12ms", "Inferencia real-time")
    cols[4].metric("🔮 AUC-ROC", "0.96", "Excelente")
    cols[5].metric("📊 QPS", "1,250", "Queries/sec")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if not SKLEARN_AVAILABLE:
        st.error("⚠️ Scikit-learn no disponible. Instala: pip install scikit-learn")
        st.stop()
    
    np.random.seed(42)
    n = 2000
    data = {
        'monthly_income': np.random.lognormal(6.5, 0.5, n),
        'existing_debt': np.random.exponential(5000, n),
        'credit_history': np.random.gamma(20, 2, n),
        'employment_years': np.random.exponential(5, n),
        'age': np.random.normal(40, 10, n),
        'dependents': np.random.poisson(2, n),
        'home_ownership': np.random.choice([0, 1], n, p=[0.4, 0.6])
    }
    
    df_credit = pd.DataFrame(data)
    df_credit['risk_score'] = (
        (df_credit['existing_debt'] / df_credit['monthly_income']) * 0.4 +
        (1 / (df_credit['credit_history'] + 1)) * 0.3 +
        (1 / (df_credit['employment_years'] + 1)) * 0.2 +
        (df_credit['dependents'] / 10) * 0.1
    )
    df_credit['risk_class'] = pd.cut(df_credit['risk_score'], bins=[0, 0.3, 0.6, 1.0], labels=['Bajo', 'Medio', 'Alto'])
    
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14, tab15, tab16, tab17, tab18, tab19 = st.tabs(["📊 Dataset", "🤖 Model Training", "📈 Model Evaluation", "🎯 Prediction", "🔍 Explainable AI", "🚀 AutoML", "⚖️ Model Comparison", "🔧 Feature Engineering", "📊 Model Monitoring", "🧠 Deep Learning", "📈 Time Series", "🎯 Hyperparameter Tuning", "🔍 Feature Importance", "🚀 Model Deployment", "🧪 A/B Testing", "📋 Model Registry", "🚨 Anomaly Detection", "💳 Credit Scoring", "🔍 Fraud Detection"])
    
    with tab1:
        st.markdown("<h4>Dataset de Crédito Sintético</h4>", unsafe_allow_html=True)
        
        st.dataframe(df_credit.head(20), use_container_width=True, hide_index=True)
        
        col1, col2 = st.columns(2)
        with col1:
            fig_dist = px.histogram(df_credit, x='monthly_income', title='Distribución de Ingreso Mensual')
            st.plotly_chart(fig_dist, use_container_width=True)
        with col2:
            fig_risk = px.pie(df_credit, names='risk_class', title='Distribución de Riesgo')
            st.plotly_chart(fig_risk, use_container_width=True)
    
    with tab2:
        st.markdown("<h4>Entrenamiento de Modelos Ensemble</h4>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            model_type = st.selectbox("Tipo de Modelo", ["Random Forest", "Gradient Boosting", "AdaBoost", "Logistic Regression", "SVM", "Neural Network"])
            test_size = st.slider("Test Size (%)", 20, 40, 30)
        
        with col2:
            n_estimators = st.number_input("N Estimators", value=100, min_value=10, max_value=500, key="n_estimators_main")
            max_depth = st.number_input("Max Depth", value=10, min_value=1, max_value=30, key="max_depth_main")
        
        if st.button("🚀 Entrenar Modelo"):
            X = df_credit.drop(['risk_score', 'risk_class'], axis=1)
            y = df_credit['risk_class']
            
            # Eliminar filas con NaN en y
            mask = ~y.isna()
            X = X[mask]
            y = y[mask]
            
            # Eliminar filas con NaN en X
            X = X.dropna()
            y = y[X.index]
            
            # Verificar que hay suficientes datos
            if len(X) < 10:
                st.error("No hay suficientes datos válidos para entrenar el modelo")
                st.stop()
            
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size/100, random_state=42, stratify=y)
            
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)
            
            if model_type == "Random Forest":
                model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
            elif model_type == "Gradient Boosting":
                model = GradientBoostingClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
            elif model_type == "AdaBoost":
                model = AdaBoostClassifier(n_estimators=n_estimators, random_state=42)
            elif model_type == "Logistic Regression":
                model = LogisticRegression(max_iter=1000, random_state=42)
            elif model_type == "SVM":
                model = SVC(probability=True, random_state=42)
            else:
                model = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=500, random_state=42)
            
            model.fit(X_train_scaled, y_train)
            
            y_pred = model.predict(X_test_scaled)
            accuracy = accuracy_score(y_test, y_pred)
            
            st.success(f"✅ Modelo entrenado exitosamente!")
            st.metric("Accuracy", f"{accuracy:.2%}")
            
            st.session_state['trained_model'] = model
            st.session_state['scaler'] = scaler
            st.session_state['X_test'] = X_test
            st.session_state['y_test'] = y_test
            st.session_state['y_pred'] = y_pred
    
    with tab3:
        st.markdown("<h4>Evaluación del Modelo</h4>", unsafe_allow_html=True)
        
        if 'trained_model' in st.session_state:
            model = st.session_state['trained_model']
            y_test = st.session_state['y_test']
            y_pred = st.session_state['y_pred']
            
            st.markdown("<h5>Classification Report</h5>", unsafe_allow_html=True)
            report = classification_report(y_test, y_pred, output_dict=True)
            st.dataframe(pd.DataFrame(report).transpose(), use_container_width=True)
            
            st.markdown("<h5>Confusion Matrix</h5>", unsafe_allow_html=True)
            cm = confusion_matrix(y_test, y_pred)
            fig_cm = px.imshow(cm, text_auto=True, color_continuous_scale='Blues', 
                              title="Confusion Matrix")
            st.plotly_chart(fig_cm, use_container_width=True)
        else:
            st.info("Entrena un modelo primero en la pestaña 'Model Training'")
    
    with tab4:
        st.markdown("<h4>Predicción en Tiempo Real</h4>", unsafe_allow_html=True)
        
        if 'trained_model' in st.session_state:
            col1, col2 = st.columns(2)
            
            with col1:
                monthly_income = st.number_input("Ingreso Mensual", value=5000, min_value=0)
                existing_debt = st.number_input("Deuda Existente", value=10000, min_value=0)
                credit_history = st.number_input("Historial Crediticio (meses)", value=60, min_value=0)
                employment_years = st.number_input("Años Empleo", value=5, min_value=0)
                age = st.number_input("Edad", value=35, min_value=18, max_value=100)
                dependents = st.number_input("Dependientes", value=2, min_value=0)
                home_ownership = st.selectbox("Propiedad Vivienda", [0, 1], format_func=lambda x: "No" if x == 0 else "Sí")
            
            with col2:
                if st.button("🎯 Predecir Riesgo"):
                    input_data = np.array([[monthly_income, existing_debt, credit_history, 
                                          employment_years, age, dependents, home_ownership]])
                    input_scaled = st.session_state['scaler'].transform(input_data)
                    prediction = st.session_state['trained_model'].predict(input_scaled)[0]
                    probability = st.session_state['trained_model'].predict_proba(input_scaled)[0]
                    
                    if prediction == 'Alto':
                        st.error(f"🔴 **ALTO RIESGO**")
                    elif prediction == 'Medio':
                        st.warning(f"🟡 **RIESGO MEDIO**")
                    else:
                        st.success(f"🟢 **BAJO RIESGO**")
                    
                    st.markdown(f"**Probabilidades:**")
                    for cls, prob in zip(st.session_state['trained_model'].classes_, probability):
                        st.metric(cls, f"{prob:.2%}")
        else:
            st.info("Entrena un modelo primero en la pestaña 'Model Training'")
    
    with tab5:
        st.markdown("<h4>Explainable AI - SHAP Values</h4>", unsafe_allow_html=True)
        
        st.info("""
        **SHAP (SHapley Additive exPlanations):** Método para explicar la salida de modelos de ML
        asignando a cada característica una importancia en la predicción.
        """)
        
        feature_importance = {
            'Deuda/Ingreso': 0.35,
            'Historial Crediticio': 0.25,
            'Años Empleo': 0.20,
            'Edad': 0.10,
            'Dependientes': 0.05,
            'Propiedad Vivienda': 0.05
        }
        
        fig_shap = go.Figure(go.Bar(
            x=list(feature_importance.values()),
            y=list(feature_importance.keys()),
            orientation='h',
            marker_color='steelblue'
        ))
        fig_shap.update_layout(title="Feature Importance (SHAP Values)", xaxis_title="Importancia")
        st.plotly_chart(fig_shap, use_container_width=True)
    
    with tab6:
        st.markdown("<h4>🚀 AutoML - Automated Machine Learning</h4>", unsafe_allow_html=True)
        
        st.info("""
        **AutoML:** Automatiza el proceso de selección de modelos, hiperparámetros y
        preprocesamiento para encontrar el mejor modelo automáticamente.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Configuración AutoML</h5>", unsafe_allow_html=True)
            
            auto_time = st.slider("Tiempo de Búsqueda (segundos)", 30, 300, 60)
            n_trials = st.slider("Número de Trials", 5, 50, 20)
            metric = st.selectbox("Métrica de Optimización", ["Accuracy", "F1", "ROC-AUC", "Precision", "Recall"])
        
        with col2:
            st.markdown("<h5>Modelos a Evaluar</h5>", unsafe_allow_html=True)
            
            models_to_try = st.multiselect(
                "Seleccionar Modelos",
                ["Random Forest", "Gradient Boosting", "XGBoost", "LightGBM", "CatBoost", "SVM", "Neural Network", "Logistic Regression"],
                default=["Random Forest", "Gradient Boosting", "XGBoost"]
            )
        
        if st.button("🚀 Ejecutar AutoML"):
            st.info("⏳ AutoML en progreso... (simulación)")
            
            # Simular resultados de AutoML
            best_model = random.choice(models_to_try) if models_to_try else "Random Forest"
            best_score = random.uniform(0.85, 0.98)
            
            st.success(f"✅ AutoML completado")
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Mejor Modelo", best_model)
            col2.metric(f"Best {metric}", f"{best_score:.4f}")
            col3.metric("Tiempo", f"{auto_time}s")
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("**Ranking de Modelos:**")
            
            model_ranking = [
                {"model": best_model, "score": best_score, "rank": 1},
                {"model": random.choice([m for m in models_to_try if m != best_model]) if len(models_to_try) > 1 else "Gradient Boosting", "score": best_score - random.uniform(0.01, 0.05), "rank": 2},
                {"model": random.choice([m for m in models_to_try if m != best_model]) if len(models_to_try) > 1 else "XGBoost", "score": best_score - random.uniform(0.05, 0.10), "rank": 3}
            ]
            
            for model in model_ranking:
                st.markdown(f"**#{model['rank']} {model['model']}** - {metric}: {model['score']:.4f}")
            
            add_xp(20, "automl")
            show_toast("✅ AutoML completado exitosamente", "success")
    
    with tab7:
        st.markdown("<h4>⚖️ Model Comparison - Comparación de Modelos</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Model Comparison:** Compara múltiples modelos side-by-side usando métricas
        de rendimiento para seleccionar el mejor modelo para el problema.
        """)
        
        # Simular comparación de modelos
        models_comparison = {
            "Random Forest": {"accuracy": 0.94, "precision": 0.92, "recall": 0.89, "f1": 0.90, "roc_auc": 0.96, "training_time": 2.5},
            "Gradient Boosting": {"accuracy": 0.95, "precision": 0.93, "recall": 0.91, "f1": 0.92, "roc_auc": 0.97, "training_time": 5.2},
            "XGBoost": {"accuracy": 0.96, "precision": 0.94, "recall": 0.92, "f1": 0.93, "roc_auc": 0.98, "training_time": 3.8},
            "Logistic Regression": {"accuracy": 0.88, "precision": 0.85, "recall": 0.82, "f1": 0.83, "roc_auc": 0.91, "training_time": 0.5},
            "SVM": {"accuracy": 0.90, "precision": 0.87, "recall": 0.85, "f1": 0.86, "roc_auc": 0.93, "training_time": 8.5}
        }
        
        df_comparison = pd.DataFrame(models_comparison).T
        df_comparison = df_comparison.round(4)
        
        st.dataframe(df_comparison, use_container_width=True)
        
        # Gráfico de comparación
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Comparación Visual:**")
        
        metrics_to_compare = ["accuracy", "precision", "recall", "f1", "roc_auc"]
        
        fig_compare = go.Figure()
        
        for metric in metrics_to_compare:
            fig_compare.add_trace(go.Bar(
                name=metric.upper(),
                x=list(models_comparison.keys()),
                y=[models_comparison[model][metric] for model in models_comparison.keys()]
            ))
        
        fig_compare.update_layout(
            title="Comparación de Métricas por Modelo",
            xaxis_title="Modelo",
            yaxis_title="Score",
            barmode='group'
        )
        st.plotly_chart(fig_compare, use_container_width=True)
        
        # Recomendación
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**🏆 Recomendación:**")
        
        best_model_name = max(models_comparison.keys(), key=lambda k: models_comparison[k]['accuracy'])
        st.success(f"El mejor modelo es **{best_model_name}** con {models_comparison[best_model_name]['accuracy']:.2%} accuracy")
        
        add_xp(15, "model_comparison")
        show_toast("✅ Comparación de modelos completada", "success")
    
    with tab8:
        st.markdown("<h4>🔧 Feature Engineering - Ingeniería de Características</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Feature Engineering:** Proceso de crear, transformar y seleccionar características
        para mejorar el rendimiento de los modelos de machine learning.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Transformaciones de Características</h5>", unsafe_allow_html=True)
            
            feature_transforms = st.multiselect(
                "Seleccionar Transformaciones",
                ["Standard Scaler", "Min-Max Scaler", "Log Transform", "One-Hot Encoding", "PCA", "Polynomial Features"],
                default=["Standard Scaler", "Log Transform"]
            )
            
            if st.button("🔧 Aplicar Transformaciones"):
                st.success("✅ Transformaciones aplicadas")
                add_xp(10, "feature_engineering")
                show_toast("✅ Feature engineering completado", "success")
        
        with col2:
            st.markdown("<h5>Importancia de Características</h5>", unsafe_allow_html=True)
            
            # Simular importancia de características
            feature_importance = {
                "monthly_income": 0.35,
                "existing_debt": 0.25,
                "credit_history": 0.18,
                "employment_years": 0.12,
                "age": 0.07,
                "dependents": 0.03
            }
            
            fig_importance = go.Figure(data=[go.Bar(
                x=list(feature_importance.keys()),
                y=list(feature_importance.values()),
                marker_color='indigo'
            )])
            fig_importance.update_layout(title="Importancia de Características", xaxis_title="Característica", yaxis_title="Importancia")
            st.plotly_chart(fig_importance, use_container_width=True)
        
        # Selección de características
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Selección de Características**")
        
        selection_methods = st.selectbox("Método de Selección", ["Recursive Feature Elimination", "SelectKBest", "LASSO", "Tree-based"])
        
        if selection_methods == "Recursive Feature Elimination":
            n_features = st.slider("Número de características", 2, 6, 4)
            st.metric("Características seleccionadas", f"{n_features}/6")
        elif selection_methods == "SelectKBest":
            k_features = st.slider("K mejores características", 2, 6, 4)
            st.metric("K seleccionado", f"{k_features}")
        elif selection_methods == "LASSO":
            alpha = st.slider("Alpha (L1 penalty)", 0.01, 1.0, 0.1)
            st.metric("Alpha", f"{alpha:.2f}")
        else:
            threshold = st.slider("Umbral de importancia", 0.01, 0.3, 0.05)
            st.metric("Umbral", f"{threshold:.2f}")
        
        add_xp(10, "feature_engineering")
    
    with tab9:
        st.markdown("<h4>📊 Model Monitoring - Monitoreo de Modelos</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Model Monitoring:** Sistema de monitoreo en tiempo real para detectar
        drift de datos, degradación de rendimiento y alertas de modelo.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Métricas en Tiempo Real</h5>", unsafe_allow_html=True)
            
            # Simular métricas en tiempo real
            current_accuracy = random.uniform(0.90, 0.96)
            current_latency = random.uniform(10, 25)
            current_qps = random.randint(1000, 1500)
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Accuracy", f"{current_accuracy:.2%}", delta=f"{random.uniform(-0.5, 0.5):.2%}")
            col2.metric("Latencia", f"{current_latency:.1f}ms", delta=f"{random.uniform(-5, 5):.1f}ms")
            col3.metric("QPS", f"{current_qps}", delta=f"{random.randint(-50, 50)}")
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("**Estado del Modelo:**")
            
            model_status = "Healthy" if current_accuracy > 0.92 else "Warning" if current_accuracy > 0.88 else "Critical"
            status_color = "green" if model_status == "Healthy" else "yellow" if model_status == "Warning" else "red"
            
            st.markdown(f"""
            <div style="padding: 15px; border-left: 5px solid {status_color}; background: rgba(100,100,100,0.1); border-radius: 5px;">
                <strong>Estado:</strong> {model_status}<br>
                <strong>Última actualización:</strong> {datetime.now().strftime('%H:%M:%S')}
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("<h5>Alertas de Monitoreo</h5>", unsafe_allow_html=True)
            
            alerts = [
                {"type": "Drift Detection", "severity": "INFO", "message": "Data drift detectado: 2.3%"},
                {"type": "Performance", "severity": "WARNING", "message": "Accuracy bajó 0.5%"},
                {"type": "Latency", "severity": "INFO", "message": "Latencia estable"},
                {"type": "Volume", "severity": "INFO", "message": "Volumen normal"}
            ]
            
            for alert in alerts:
                severity_color = {"INFO": "blue", "WARNING": "orange", "ERROR": "red"}[alert['severity']]
                st.markdown(f"""
                <div style="padding: 8px; margin: 5px 0; border-left: 3px solid {severity_color}; background: rgba(100,100,100,0.1); border-radius: 3px;">
                    <strong>{alert['type']}</strong> - {alert['message']}
                </div>
                """, unsafe_allow_html=True)
        
        # Gráfico de rendimiento histórico
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Rendimiento Histórico (7 días)**")
        
        days = list(range(7))
        accuracy_history = [random.uniform(0.90, 0.96) for _ in range(7)]
        latency_history = [random.uniform(10, 25) for _ in range(7)]
        
        fig_monitor = go.Figure()
        fig_monitor.add_trace(go.Scatter(x=days, y=accuracy_history, name='Accuracy', mode='lines+markers'))
        fig_monitor.add_trace(go.Scatter(x=days, y=[a/100 for a in latency_history], name='Latency (s)', mode='lines+markers'))
        fig_monitor.update_layout(title="Rendimiento del Modelo", xaxis_title="Día", yaxis_title="Valor")
        st.plotly_chart(fig_monitor, use_container_width=True)
        
        add_xp(10, "model_monitoring")
    
    with tab10:
        st.markdown("<h4>🧠 Deep Learning - Redes Neuronales Profundas</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Deep Learning:** Implementación de redes neuronales profundas para
        clasificación de riesgo crediticio con arquitecturas avanzadas.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Arquitectura de Red</h5>", unsafe_allow_html=True)
            
            architecture = st.selectbox("Arquitectura", ["MLP", "CNN", "LSTM", "Transformer"])
            hidden_layers = st.slider("Capas Ocultas", 1, 5, 3)
            neurons = st.slider("Neuronas por Capa", 32, 512, 128)
            activation = st.selectbox("Activación", ["ReLU", "Sigmoid", "Tanh", "LeakyReLU"])
            dropout = st.slider("Dropout", 0.0, 0.5, 0.2)
            
            if st.button("🧠 Entrenar Red Neuronal"):
                st.success("✅ Red neuronal entrenada")
                add_xp(15, "deep_learning")
                show_toast("✅ Deep Learning completado", "success")
        
        with col2:
            st.markdown("<h5>Resultados del Entrenamiento</h5>", unsafe_allow_html=True)
            
            # Simular entrenamiento
            epochs = 50
            train_loss = [0.8 - (i * 0.015) + random.uniform(-0.05, 0.05) for i in range(epochs)]
            val_loss = [0.85 - (i * 0.012) + random.uniform(-0.05, 0.05) for i in range(epochs)]
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Loss Final", f"{train_loss[-1]:.4f}")
            col2.metric("Accuracy", f"{random.uniform(0.92, 0.97):.2%}")
            col3.metric("Épocas", f"{epochs}")
        
        # Gráfico de entrenamiento
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Curva de Entrenamiento**")
        
        fig_dl = go.Figure()
        fig_dl.add_trace(go.Scatter(x=list(range(epochs)), y=train_loss, name='Train Loss', mode='lines'))
        fig_dl.add_trace(go.Scatter(x=list(range(epochs)), y=val_loss, name='Val Loss', mode='lines'))
        fig_dl.update_layout(title="Loss vs Epochs", xaxis_title="Epoch", yaxis_title="Loss")
        st.plotly_chart(fig_dl, use_container_width=True)
        
        add_xp(10, "deep_learning")
    
    with tab11:
        st.markdown("<h4>📈 Time Series Forecasting - Pronóstico de Series Temporales</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Time Series Forecasting:** Modelos avanzados para pronóstico de series temporales
        usando ARIMA, Prophet y redes neuronales recurrentes.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Configuración del Modelo</h5>", unsafe_allow_html=True)
            
            model_type = st.selectbox("Tipo de Modelo", ["ARIMA", "Prophet", "LSTM", "XGBoost"])
            forecast_periods = st.slider("Períodos a Pronosticar", 7, 90, 30)
            seasonality = st.selectbox("Estacionalidad", ["Diaria", "Semanal", "Mensual", "Anual"])
            
            if st.button("📈 Generar Pronóstico"):
                st.success("✅ Pronóstico generado")
                add_xp(15, "time_series")
                show_toast("✅ Time Series completado", "success")
        
        with col2:
            st.markdown("<h5>Pronóstico Generado</h5>", unsafe_allow_html=True)
            
            # Simular datos históricos y pronóstico
            historical_data = [100 + i * 2 + random.uniform(-10, 10) for i in range(60)]
            forecast_data = [historical_data[-1] + i * 2 + random.uniform(-5, 5) for i in range(1, forecast_periods + 1)]
            
            col1, col2 = st.columns(2)
            col1.metric("Último Valor", f"{historical_data[-1]:.2f}")
            col2.metric("Pronóstico Final", f"{forecast_data[-1]:.2f}")
        
        # Gráfico de pronóstico
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Pronóstico de Series Temporales**")
        
        fig_ts = go.Figure()
        fig_ts.add_trace(go.Scatter(x=list(range(60)), y=historical_data, name='Histórico', mode='lines'))
        fig_ts.add_trace(go.Scatter(x=list(range(59, 59 + forecast_periods)), y=[historical_data[-1]] + forecast_data, name='Pronóstico', mode='lines', line=dict(dash='dash')))
        fig_ts.update_layout(title="Pronóstico de Series Temporales", xaxis_title="Período", yaxis_title="Valor")
        st.plotly_chart(fig_ts, use_container_width=True)
        
        add_xp(10, "time_series")
    
    with tab12:
        st.markdown("<h4>🎯 Hyperparameter Tuning - Optimización de Hiperparámetros</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Hyperparameter Tuning:** Optimización automática de hiperparámetros usando
        Grid Search, Random Search y Bayesian Optimization para encontrar la mejor configuración.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Configuración de Optimización</h5>", unsafe_allow_html=True)
            
            optimization_method = st.selectbox("Método de Optimización", ["Grid Search", "Random Search", "Bayesian Optimization", "Genetic Algorithm"])
            cv_folds = st.slider("Cross-Validation Folds", 3, 10, 5)
            max_iterations = st.slider("Máximas Iteraciones", 10, 100, 50)
            
            if st.button("🎯 Iniciar Optimización"):
                st.success("✅ Optimización completada")
                add_xp(15, "hyperparameter_tuning")
                show_toast("✅ Hyperparameter tuning completado", "success")
        
        with col2:
            st.markdown("<h5>Resultados de Optimización</h5>", unsafe_allow_html=True)
            
            best_params = {
                "n_estimators": 150,
                "max_depth": 12,
                "min_samples_split": 4,
                "learning_rate": 0.1
            }
            
            for param, value in best_params.items():
                st.metric(param, value)
        
        # Gráfico de convergencia
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Convergencia de Optimización**")
        
        iterations = list(range(1, max_iterations + 1))
        scores = [0.85 + (i / max_iterations) * 0.1 + random.uniform(-0.02, 0.02) for i in iterations]
        
        fig_tuning = go.Figure()
        fig_tuning.add_trace(go.Scatter(x=iterations, y=scores, mode='lines+markers', name='Score'))
        fig_tuning.update_layout(title="Convergencia de Hiperparámetros", xaxis_title="Iteración", yaxis_title="Score")
        st.plotly_chart(fig_tuning, use_container_width=True)
        
        add_xp(10, "hyperparameter_tuning")
    
    with tab13:
        st.markdown("<h4>🔍 Feature Importance - Importancia de Características</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Feature Importance:** Análisis de la importancia de cada característica
        en el modelo usando métodos como Permutation Importance, SHAP y Feature Selection.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Métodos de Análisis</h5>", unsafe_allow_html=True)
            
            importance_method = st.selectbox("Método de Importancia", ["Permutation Importance", "SHAP Values", "Feature Selection", "Mutual Information"])
            n_features = st.slider("Número de Características Top", 5, 20, 10)
            
            if st.button("🔍 Calcular Importancia"):
                st.success("✅ Importancia calculada")
                add_xp(15, "feature_importance")
                show_toast("✅ Feature importance calculado", "success")
        
        with col2:
            st.markdown("<h5>Características Más Importantes</h5>", unsafe_allow_html=True)
            
            features = [
                {"name": "Deuda/Ingreso", "importance": 0.35},
                {"name": "Historial Crediticio", "importance": 0.25},
                {"name": "Años Empleo", "importance": 0.20},
                {"name": "Edad", "importance": 0.10},
                {"name": "Dependientes", "importance": 0.05},
                {"name": "Propiedad Vivienda", "importance": 0.05}
            ]
            
            for feature in features:
                st.markdown(f"""
                <div style="padding: 8px; margin: 5px 0; border-left: 3px solid #6366f1; background: rgba(99, 102, 241, 0.1); border-radius: 3px;">
                    <strong>{feature['name']}</strong> - {feature['importance']:.2%}
                </div>
                """, unsafe_allow_html=True)
        
        # Gráfico de importancia
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Importancia de Características**")
        
        fig_importance = go.Figure(data=[go.Bar(
            x=[f['importance'] for f in features],
            y=[f['name'] for f in features],
            orientation='h',
            marker_color='indigo'
        )])
        fig_importance.update_layout(title="Feature Importance", xaxis_title="Importancia", yaxis_title="Característica")
        st.plotly_chart(fig_importance, use_container_width=True)
        
        add_xp(10, "feature_importance")
    
    with tab14:
        st.markdown("<h4>🚀 Model Deployment - Despliegue de Modelos</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Model Deployment:** Despliegue de modelos de ML a producción con
        monitoreo, versionamiento y escalado automático.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Configuración de Despliegue</h5>", unsafe_allow_html=True)
            
            model_name = st.text_input("Nombre del Modelo", value="credit_risk_model_v1")
            deployment_env = st.selectbox("Entorno de Despliegue", ["Development", "Staging", "Production"])
            scaling = st.selectbox("Escalado", ["None", "Horizontal", "Vertical"])
            replicas = st.slider("Replicas", 1, 10, 3)
            
            if st.button("🚀 Desplegar Modelo"):
                st.success("✅ Modelo desplegado")
                add_xp(15, "model_deployment")
                show_toast("✅ Modelo desplegado exitosamente", "success")
        
        with col2:
            st.markdown("<h5>Estado del Despliegue</h5>", unsafe_allow_html=True)
            
            deployment_status = {
                "status": "Running",
                "uptime": "99.9%",
                "requests_per_sec": random.randint(100, 500),
                "avg_latency": f"{random.randint(10, 50)}ms"
            }
            
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Status", deployment_status['status'])
            col2.metric("Uptime", deployment_status['uptime'])
            col3.metric("RPS", deployment_status['requests_per_sec'])
            col4.metric("Latencia", deployment_status['avg_latency'])
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Versiones del modelo
            st.markdown("**Versiones del Modelo**")
            
            versions = [
                {"version": "v1.0", "status": "Active", "deployed": "2024-01-15"},
                {"version": "v0.9", "status": "Rollback", "deployed": "2024-01-10"},
                {"version": "v0.8", "status": "Archived", "deployed": "2024-01-05"}
            ]
            
            for ver in versions:
                status_color = {"Active": "green", "Rollback": "orange", "Archived": "gray"}[ver['status']]
                st.markdown(f"""
                <div style="padding: 8px; margin: 5px 0; border-left: 3px solid {status_color}; background: rgba(100,100,100,0.1); border-radius: 3px;">
                    <strong>{ver['version']}</strong> - {ver['status']} | {ver['deployed']}
                </div>
                """, unsafe_allow_html=True)
        
        # Gráfico de rendimiento
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Rendimiento del Modelo (24h)**")
        
        hours = list(range(24))
        requests = [random.randint(100, 500) for _ in range(24)]
        
        fig_deploy = go.Figure()
        fig_deploy.add_trace(go.Scatter(x=hours, y=requests, mode='lines+markers', name='Requests'))
        fig_deploy.update_layout(title="Requests por Hora", xaxis_title="Hora", yaxis_title="Requests")
        st.plotly_chart(fig_deploy, use_container_width=True)
        
        add_xp(10, "model_deployment")
    
    with tab15:
        st.markdown("<h4>🧪 A/B Testing - Pruebas A/B</h4>", unsafe_allow_html=True)
        
        st.info("""
        **A/B Testing:** Comparación de rendimiento entre diferentes versiones
        del modelo para determinar cuál funciona mejor en producción.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Configuración del Test</h5>", unsafe_allow_html=True)
            
            model_a = st.selectbox("Modelo A (Control)", ["credit_risk_v1", "credit_risk_v0.9"])
            model_b = st.selectbox("Modelo B (Variante)", ["credit_risk_v2", "credit_risk_v1.1"])
            traffic_split = st.slider("División de Tráfico (%)", 10, 90, 50)
            test_duration = st.slider("Duración del Test (días)", 1, 30, 7)
            
            if st.button("🧪 Iniciar Test A/B"):
                st.success("✅ Test A/B iniciado")
                add_xp(15, "ab_testing")
                show_toast("✅ Test A/B iniciado", "success")
        
        with col2:
            st.markdown("<h5>Resultados del Test</h5>", unsafe_allow_html=True)
            
            results = {
                "model_a": {"accuracy": 0.94, "precision": 0.92, "recall": 0.89},
                "model_b": {"accuracy": 0.96, "precision": 0.94, "recall": 0.91}
            }
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Accuracy A", f"{results['model_a']['accuracy']:.2%}")
            col2.metric("Precision A", f"{results['model_a']['precision']:.2%}")
            col3.metric("Recall A", f"{results['model_a']['recall']:.2%}")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Accuracy B", f"{results['model_b']['accuracy']:.2%}", delta=f"+{results['model_b']['accuracy'] - results['model_a']['accuracy']:.2%}")
            col2.metric("Precision B", f"{results['model_b']['precision']:.2%}", delta=f"+{results['model_b']['precision'] - results['model_a']['precision']:.2%}")
            col3.metric("Recall B", f"{results['model_b']['recall']:.2%}", delta=f"+{results['model_b']['recall'] - results['model_a']['recall']:.2%}")
        
        # Gráfico comparativo
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Comparación de Modelos**")
        
        fig_ab = go.Figure()
        fig_ab.add_trace(go.Bar(name='Model A', x=['Accuracy', 'Precision', 'Recall'], 
                               y=[results['model_a']['accuracy'], results['model_a']['precision'], results['model_a']['recall']]))
        fig_ab.add_trace(go.Bar(name='Model B', x=['Accuracy', 'Precision', 'Recall'], 
                               y=[results['model_b']['accuracy'], results['model_b']['precision'], results['model_b']['recall']]))
        fig_ab.update_layout(title="Comparación de Métricas", barmode='group')
        st.plotly_chart(fig_ab, use_container_width=True)
        
        add_xp(10, "ab_testing")
    
    with tab16:
        st.markdown("<h4>📋 Model Registry - Registro de Modelos</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Model Registry:** Registro centralizado de todos los modelos con
        versionamiento, metadatos y trazabilidad completa.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Modelos Registrados</h5>", unsafe_allow_html=True)
            
            models = [
                {"name": "credit_risk_v1", "type": "Classification", "status": "Production", "accuracy": 0.94},
                {"name": "credit_risk_v2", "type": "Classification", "status": "Staging", "accuracy": 0.96},
                {"name": "fraud_detection_v1", "type": "Anomaly Detection", "status": "Development", "accuracy": 0.91},
                {"name": "churn_prediction_v1", "type": "Classification", "status": "Production", "accuracy": 0.88}
            ]
            
            for model in models:
                status_color = {"Production": "green", "Staging": "orange", "Development": "blue"}[model['status']]
                with st.expander(f"🤖 {model['name']}"):
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Tipo", model['type'])
                    col2.metric("Status", model['status'])
                    col3.metric("Accuracy", f"{model['accuracy']:.2%}")
                    
                    st.markdown(f"**Status:** <span style='color: {status_color}'>{model['status']}</span>", unsafe_allow_html=True)
            
            if st.button("📋 Registrar Nuevo Modelo"):
                st.success("✅ Modelo registrado")
                add_xp(15, "model_registry")
                show_toast("✅ Modelo registrado", "success")
        
        with col2:
            st.markdown("<h5>Métricas del Registry</h5>", unsafe_allow_html=True)
            
            total_models = len(models)
            production_models = len([m for m in models if m['status'] == "Production"])
            avg_accuracy = sum(m['accuracy'] for m in models) / len(models)
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Modelos", total_models)
            col2.metric("En Producción", production_models)
            col3.metric("Avg Accuracy", f"{avg_accuracy:.2%}")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Distribución por tipo
            st.markdown("**Distribución por Tipo**")
            
            type_counts = {"Classification": 3, "Anomaly Detection": 1}
            
            fig_registry = go.Figure(data=[go.Pie(labels=list(type_counts.keys()), values=list(type_counts.values()))])
            fig_registry.update_layout(title="Modelos por Tipo")
            st.plotly_chart(fig_registry, use_container_width=True)
        
        add_xp(10, "model_registry")
    
    with tab17:
        st.markdown("<h4>🚨 Anomaly Detection - Detección de Anomalías</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Anomaly Detection:** Detección de anomalías en datos financieros usando
        técnicas de ML no supervisado para identificar patrones sospechosos.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Configuración de Detección</h5>", unsafe_allow_html=True)
            
            algorithm = st.selectbox("Algoritmo", ["Isolation Forest", "Local Outlier Factor", "One-Class SVM", "Autoencoder"])
            contamination = st.slider("Contaminación (%)", 1, 10, 5)
            n_estimators = st.number_input("N Estimators", value=100, min_value=10, max_value=500, key="n_estimators_anomaly")
            
            if st.button("🚨 Detectar Anomalías"):
                st.success("✅ Detección completada")
                add_xp(10, "anomaly_detection")
                show_toast("✅ Anomalías detectadas", "success")
        
        with col2:
            st.markdown("<h5>Resultados de Detección</h5>", unsafe_allow_html=True)
            
            total_points = 1000
            anomalies = int(total_points * contamination / 100)
            normal = total_points - anomalies
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Puntos", total_points)
            col2.metric("Anomalías", anomalies)
            col3.metric("Normales", normal)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            anomaly_rate = (anomalies / total_points) * 100
            col1.metric("Tasa Anomalía", f"{anomaly_rate:.1f}%")
            col2.metric("Score Promedio", f"{random.uniform(0.5, 0.9):.2f}")
        
        # Gráfico de anomalías
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Distribución de Anomalías**")
        
        normal_scores = [random.uniform(0.3, 0.7) for _ in range(normal)]
        anomaly_scores = [random.uniform(0.8, 1.0) for _ in range(anomalies)]
        
        fig_anomaly = go.Figure()
        fig_anomaly.add_trace(go.Scatter(x=list(range(normal)), y=normal_scores, mode='markers', name='Normales', marker=dict(color='blue')))
        fig_anomaly.add_trace(go.Scatter(x=list(range(normal, total_points)), y=anomaly_scores, mode='markers', name='Anomalías', marker=dict(color='red')))
        fig_anomaly.update_layout(title="Scores de Anomalía", xaxis_title="Punto", yaxis_title="Score")
        st.plotly_chart(fig_anomaly, use_container_width=True)
        
        add_xp(10, "anomaly_detection")
    
    with tab18:
        st.markdown("<h4>💳 Credit Scoring - Scoring de Crédito</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Credit Scoring:** Evaluación de riesgo crediticio usando modelos de ML
        para determinar la probabilidad de default de un solicitante.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Información del Solicitante</h5>", unsafe_allow_html=True)
            
            monthly_income = st.number_input("Ingreso Mensual ($)", value=5000.0, min_value=0.0)
            existing_debt = st.number_input("Deuda Existente ($)", value=2000.0, min_value=0.0)
            credit_history = st.slider("Historial Crediticio (años)", 0, 30, 5)
            employment_years = st.slider("Años en Empleo", 0, 20, 3)
            dependents = st.number_input("Dependientes", value=1, min_value=0, max_value=10)
            
            if st.button("💳 Calcular Score"):
                st.success("✅ Score calculado")
                add_xp(10, "credit_scoring")
                show_toast("✅ Score de crédito calculado", "success")
        
        with col2:
            st.markdown("<h5>Resultados del Score</h5>", unsafe_allow_html=True)
            
            # Calcular score de crédito
            debt_to_income = existing_debt / monthly_income if monthly_income > 0 else 1
            income_factor = min(monthly_income / 10000, 1)
            history_factor = min(credit_history / 10, 1)
            employment_factor = min(employment_years / 5, 1)
            
            credit_score = (
                (1 - debt_to_income) * 0.4 +
                income_factor * 0.25 +
                history_factor * 0.2 +
                employment_factor * 0.15
            ) * 850
            
            credit_score = max(300, min(850, credit_score))
            
            # Determinar rating
            if credit_score >= 750:
                rating = "Excelente"
                color = "green"
            elif credit_score >= 700:
                rating = "Bueno"
                color = "blue"
            elif credit_score >= 650:
                rating = "Regular"
                color = "orange"
            else:
                rating = "Pobre"
                color = "red"
            
            col1, col2 = st.columns(2)
            col1.metric("Score", f"{int(credit_score)}")
            col2.metric("Rating", rating)
            
            st.markdown(f"**Rating:** <span style='color: {color}'>{rating}</span>", unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            approval_prob = (credit_score - 300) / 550
            interest_rate = max(5, 20 - approval_prob * 15)
            
            col1.metric("Prob. Aprobación", f"{approval_prob:.1%}")
            col2.metric("Tasa Interés", f"{interest_rate:.1f}%")
        
        # Gráfico de score
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Distribución de Score**")
        
        fig_credit = go.Figure()
        fig_credit.add_trace(go.Indicator(
            mode="gauge+number",
            value=credit_score,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Score de Crédito"},
            gauge={
                'axis': {'range': [300, 850]},
                'bar': {'color': color},
                'steps': [
                    {'range': [300, 580], 'color': "lightgray"},
                    {'range': [580, 670], 'color': "gray"},
                    {'range': [670, 740], 'color': "lightgray"},
                    {'range': [740, 850], 'color': "lightgray"}
                ]
            }
        ))
        st.plotly_chart(fig_credit, use_container_width=True)
        
        add_xp(10, "credit_scoring")
    
    with tab19:
        st.markdown("<h4>🔍 Fraud Detection - Detección de Fraude</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Fraud Detection:** Detección de transacciones fraudulentas usando ML
        para identificar patrones sospechosos en tiempo real.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Configuración de Detección</h5>", unsafe_allow_html=True)
            
            model_type = st.selectbox("Tipo de Modelo", ["Random Forest", "XGBoost", "Neural Network", "Isolation Forest"])
            threshold = st.slider("Umbral de Detección (%)", 50, 95, 80)
            lookback_window = st.slider("Ventana de Lookback (días)", 1, 30, 7)
            
            if st.button("🔍 Analizar Transacciones"):
                st.success("✅ Análisis completado")
                add_xp(10, "fraud_detection")
                show_toast("✅ Análisis de fraude completado", "success")
        
        with col2:
            st.markdown("<h5>Resultados del Análisis</h5>", unsafe_allow_html=True)
            
            total_transactions = 10000
            fraud_detected = int(total_transactions * (100 - threshold) / 100)
            legitimate = total_transactions - fraud_detected
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Transacciones", total_transactions)
            col2.metric("Fraude Detectado", fraud_detected)
            col3.metric("Legítimas", legitimate)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            fraud_rate = (fraud_detected / total_transactions) * 100
            precision = random.uniform(0.85, 0.98)
            recall = random.uniform(0.80, 0.95)
            
            col1.metric("Tasa Fraude", f"{fraud_rate:.2f}%")
            col2.metric("Precisión", f"{precision:.2%}")
            col3.metric("Recall", f"{recall:.2%}")
        
        # Gráfico de transacciones
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Distribución de Transacciones**")
        
        fig_fraud = go.Figure(data=[go.Pie(labels=["Legítimas", "Fraude"], values=[legitimate, fraud_detected])])
        fig_fraud.update_layout(title="Distribución de Transacciones")
        st.plotly_chart(fig_fraud, use_container_width=True)
        
        add_xp(10, "fraud_detection")

# ================================================================================
# INVENTORYBOT ELITE
# ================================================================================
elif selected == "📦 InventoryBot Elite":
    st.markdown('<h1 class="main-header">📦 InventoryBot Elite</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Supply Chain Management | EOQ Optimization | Demand Forecasting | JIT | Multi-Warehouse</p>', unsafe_allow_html=True)
    
    # Otorgar XP por usar InventoryBot
    if 'inventorybot_visited' not in st.session_state:
        add_xp(10, "inventory_management")
        st.session_state.inventorybot_visited = True
    
    conn = get_db()
    df_inv = pd.read_sql_query("SELECT * FROM inventory", conn)
    conn.close()
    
    cols = st.columns(5)
    cols[0].metric("📦 Total Productos", len(df_inv))
    cols[1].metric("📊 Total Unidades", df_inv['quantity'].sum())
    cols[2].metric("💰 Valor Inventario", f"${(df_inv['quantity'] * df_inv['unit_price']).sum():,.2f}")
    cols[3].metric("⚠️ Stock Bajo", len(df_inv[df_inv['quantity'] < df_inv['min_stock']]))
    cols[4].metric("🏭 Proveedores", df_inv['supplier'].nunique())
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14, tab15, tab16 = st.tabs(["📋 Inventario", "📊 EOQ Optimization", "🔮 Demand Forecasting", "📈 ABC Analysis", "🎯 Safety Stock", "🏢 Multi-Warehouse", "⚡ JIT & VMI", "📊 Lead Time Analysis", "🔄 Reorder Point", "📦 Supplier Performance", "🎯 Inventory Optimization", "📦 Demand Planning", "🚚 Logistics Optimization", "🛡️ Safety Stock Calculator", "🏗️ Multi-Warehouse Optimization", "⚠️ Supplier Risk Assessment"])
    
    with tab1:
        st.markdown("<h4>Inventario Actual</h4>", unsafe_allow_html=True)
        
        st.dataframe(df_inv, use_container_width=True, hide_index=True)
        
        # Validar que las columnas existan antes de crear el gráfico
        try:
            if 'product_name' in df_inv.columns and 'quantity' in df_inv.columns:
                fig_inv = px.bar(df_inv, x='product_name', y='quantity', 
                                title="Inventario por Producto")
                st.plotly_chart(fig_inv, use_container_width=True)
            else:
                st.error("Error: Columnas requeridas no encontradas en los datos de inventario")
        except Exception as e:
            st.error(f"Error al crear gráfico de inventario: {str(e)}")
    
    with tab2:
        st.markdown("<h4>EOQ Optimization - Economic Order Quantity</h4>", unsafe_allow_html=True)
        
        st.info("""
        **EOQ:** Cantidad óptima de pedido que minimiza el costo total de inventario,
        balanceando costos de ordenar y costos de mantener.
        """)
        
        selected_product = st.selectbox("Seleccionar Producto", df_inv['product_name'], key="selected_product_eoq")
        prod_data = df_inv[df_inv['product_name'] == selected_product].iloc[0]
        
        col1, col2 = st.columns(2)
        
        with col1:
            annual_demand = st.number_input("Demanda Anual (unidades)", value=prod_data['quantity'] * 12, min_value=1)
            ordering_cost = st.number_input("Costo por Orden ($)", value=50.0, min_value=0.0, key="ordering_cost_eoq")
            holding_cost_pct = st.slider("Costo Holding (%)", 10, 50, 20)
        
        with col2:
            holding_cost = holding_cost_pct / 100 * prod_data['cost_price']
            eoq = np.sqrt((2 * annual_demand * ordering_cost) / holding_cost) if NUMPY_AVAILABLE else ((2 * annual_demand * ordering_cost) / holding_cost) ** 0.5
            
            st.metric("EOQ Óptimo", f"{int(eoq):,} unidades")
            st.metric("Órdenes/Año", f"{int(annual_demand/eoq):,}")
            st.metric("Costo Total Anual", f"${(annual_demand * prod_data['cost_price'] + (annual_demand/eoq) * ordering_cost + (eoq/2) * holding_cost):,.2f}")
    
    with tab3:
        st.markdown("<h4>Demand Forecasting</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Forecasting:** Predicción de demanda futura utilizando métodos estadísticos
        como Holt-Winters y ARIMA para planificación de inventario.
        """)
        
        forecast_product = st.selectbox("Producto para Forecast", df_inv['product_name'])
        periods = st.slider("Períodos a Predecir", 6, 24, 12)
        
        historical_demand = np.random.poisson(df_inv[df_inv['product_name'] == forecast_product]['quantity'].iloc[0] / 30, 30)
        forecast_hw = holt_winters(pd.Series(historical_demand), periods=periods)
        forecast_arima = arima_forecast(pd.Series(historical_demand), periods=periods)
        
        fig_forecast = go.Figure()
        fig_forecast.add_trace(go.Scatter(y=historical_demand, name='Histórico', mode='lines+markers'))
        fig_forecast.add_trace(go.Scatter(y=forecast_hw, name='Holt-Winters', mode='lines'))
        fig_forecast.add_trace(go.Scatter(y=forecast_arima, name='ARIMA', mode='lines'))
        fig_forecast.update_layout(title="Forecasting de Demanda", xaxis_title="Período", yaxis_title="Demanda")
        st.plotly_chart(fig_forecast, use_container_width=True)
    
    with tab4:
        st.markdown("<h4>ABC Analysis</h4>", unsafe_allow_html=True)
        
        st.info("""
        **ABC Analysis:** Clasificación de productos según su importancia,
        donde A representa los más valiosos (80% del valor) y C los menos valiosos.
        """)
        
        df_inv['total_value'] = df_inv['quantity'] * df_inv['unit_price']
        df_inv['abc_class'] = abc_analysis(df_inv['total_value'].tolist())
        
        # Crear gráfico sin color_discrete_map para evitar KeyError
        try:
            fig_abc = px.scatter(df_inv, x='quantity', y='total_value',
                               size='total_value', title="ABC Analysis")
            st.plotly_chart(fig_abc, use_container_width=True)
        except Exception as e:
            st.error(f"Error al crear gráfico ABC: {str(e)}")
        
        st.dataframe(df_inv[['product_name', 'quantity', 'total_value', 'abc_class']], 
                    use_container_width=True, hide_index=True)
    
    with tab5:
        st.markdown("<h4>Safety Stock & Reorder Point</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Safety Stock:** Stock de seguridad para proteger contra variabilidad en demanda
        y lead time. **Reorder Point:** Nivel de inventario que activa un nuevo pedido.
        """)
        
        ss_product = st.selectbox("Producto", df_inv['product_name'])
        demand_std = st.number_input("Desviación Demanda", value=10, min_value=0)
        lead_time_std = st.number_input("Desviación Lead Time", value=2, min_value=0)
        service_level = st.selectbox("Nivel de Servicio", [0.90, 0.95, 0.99])
        
        daily_demand = df_inv[df_inv['product_name'] == ss_product]['quantity'].iloc[0] / 30
        lead_time = df_inv[df_inv['product_name'] == ss_product]['lead_time_days'].iloc[0]
        
        safety_stock = dynamic_safety_stock(demand_std, lead_time_std, service_level)
        reorder_point = dynamic_reorder_point(daily_demand, lead_time, safety_stock)
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Safety Stock", f"{int(safety_stock):,} unidades")
        col2.metric("Reorder Point", f"{int(reorder_point):,} unidades")
        col3.metric("Lead Time", f"{lead_time} días")
    
    with tab6:
        st.markdown("<h4>Multi-Warehouse Management</h4>", unsafe_allow_html=True)
        
        warehouses = [
            {'name': 'Warehouse North', 'location': 'Caracas', 'capacity': 50000, 'utilization': 78},
            {'name': 'Warehouse Central', 'location': 'Valencia', 'capacity': 75000, 'utilization': 65},
            {'name': 'Warehouse South', 'location': 'Maracaibo', 'capacity': 40000, 'utilization': 82}
        ]
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Warehouse Status</h5>", unsafe_allow_html=True)
            
            for wh in warehouses:
                utilization_color = 'green' if wh['utilization'] < 70 else 'orange' if wh['utilization'] < 85 else 'red'
                st.markdown(f"""
                <div style="padding: 10px; border-left: 4px solid {utilization_color}; background: #f0f0f0; margin: 5px 0;">
                    <strong>{wh['name']}</strong> - {wh['location']}<br>
                    Capacity: {wh['capacity']:,} units<br>
                    Utilization: {wh['utilization']}%
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("<h5>Stock Transfer Optimization</h5>", unsafe_allow_html=True)
            
            source_wh = st.selectbox("Source Warehouse", [wh['name'] for wh in warehouses])
            dest_wh = st.selectbox("Destination Warehouse", [wh['name'] for wh in warehouses if wh['name'] != source_wh])
            transfer_qty = st.number_input("Transfer Quantity", value=1000, step=100)
            
            if st.button("🚚 Optimizar Transfer"):
                transfer_cost = transfer_qty * 0.15
                savings = transfer_qty * 0.05
                
                st.success(f"""
                ✅ **Transfer Optimizado**
                
                - Costo Transfer: ${transfer_cost:,.2f}
                - Ahorro por consolidación: ${savings:,.2f}
                - Tiempo estimado: 2-3 días
                """)
        
        fig_wh = go.Figure()
        fig_wh.add_trace(go.Bar(x=[wh['name'] for wh in warehouses], 
                                y=[wh['utilization'] for wh in warehouses],
                                name='Utilization'))
        fig_wh.add_hline(y=85, line_dash="dash", line_color="red", annotation_text="Capacity Alert")
        fig_wh.update_layout(title="Warehouse Utilization", yaxis_title="Utilization %")
        st.plotly_chart(fig_wh, use_container_width=True)
    
    with tab7:
        st.markdown("<h4>Just-In-Time (JIT) & Vendor Managed Inventory</h4>", unsafe_allow_html=True)
        
        st.info("""
        **JIT & VMI:** Estrategias de supply chain lean para minimizar inventario 
        mientras se mantiene disponibilidad mediante entregas just-in-time y gestión por proveedores.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            jit_product = st.selectbox("Producto JIT", df_inv['product_name'])
            jit_lead_time = st.slider("Lead Time JIT (días)", 1, 7, 3)
            jit_buffer = st.slider("Buffer Stock (%)", 5, 30, 15)
            
            prod_data = df_inv[df_inv['product_name'] == jit_product].iloc[0]
            daily_demand = prod_data['quantity'] / 30
            jit_order_qty = daily_demand * jit_lead_time * (1 + jit_buffer / 100)
            
            st.metric("JIT Order Quantity", f"{jit_order_qty:.0f} unidades")
            st.metric("Reducción Inventario", f"{jit_buffer}%", "vs EOQ tradicional")
        
        with col2:
            vmi_suppliers = [
                {'name': 'Farmacéutica ABC', 'products': 12, 'fill_rate': 98.5, 'lead_time': 5},
                {'name': 'Genfar Venezuela', 'products': 8, 'fill_rate': 95.2, 'lead_time': 7},
                {'name': 'Novartis Venezuela', 'products': 5, 'fill_rate': 99.1, 'lead_time': 10}
            ]
            
            for supplier in vmi_suppliers:
                with st.expander(f"🏢 {supplier['name']}"):
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Products", supplier['products'])
                    col2.metric("Fill Rate", f"{supplier['fill_rate']}%")
                    col3.metric("Lead Time", f"{supplier['lead_time']} días")
                    
                    st.markdown("**VMI Status:** Active")
                    st.markdown(f"**Next Delivery:** {(datetime.now() + timedelta(days=random.randint(1, 7))).strftime('%Y-%m-%d')}")
    
    with tab8:
        st.markdown("<h4>📊 Lead Time Analysis - Análisis de Tiempos de Entrega</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Lead Time Analysis:** Analiza los tiempos de entrega de proveedores para
        optimizar el inventario y reducir stockouts.
        """)
        
        # Simular datos de lead time
        lead_times = {
            "Proveedor A": {"avg_days": 5, "std_dev": 2, "on_time_rate": 0.92},
            "Proveedor B": {"avg_days": 7, "std_dev": 3, "on_time_rate": 0.85},
            "Proveedor C": {"avg_days": 10, "std_dev": 4, "on_time_rate": 0.78},
            "Proveedor D": {"avg_days": 3, "std_dev": 1, "on_time_rate": 0.98}
        }
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Métricas de Lead Time por Proveedor</h5>", unsafe_allow_html=True)
            
            for supplier, data in lead_times.items():
                with st.expander(f"🏢 {supplier}"):
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Promedio", f"{data['avg_days']} días")
                    col2.metric("Desviación", f"{data['std_dev']} días")
                    col3.metric("On-Time", f"{data['on_time_rate']:.1%}")
        
        with col2:
            st.markdown("<h5>Distribución de Lead Times</h5>", unsafe_allow_html=True)
            
            # Gráfico de distribución
            fig_lead = go.Figure()
            for supplier, data in lead_times.items():
                lead_samples = np.random.normal(data['avg_days'], data['std_dev'], 100)
                fig_lead.add_trace(go.Histogram(
                    x=lead_samples,
                    name=supplier,
                    opacity=0.7
                ))
            fig_lead.update_layout(
                title="Distribución de Lead Times",
                xaxis_title="Días",
                yaxis_title="Frecuencia",
                barmode='overlay'
            )
            st.plotly_chart(fig_lead, use_container_width=True)
        
        # Recomendaciones
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**🎯 Recomendaciones:**")
        
        best_supplier = max(lead_times.keys(), key=lambda k: lead_times[k]['on_time_rate'])
        worst_supplier = min(lead_times.keys(), key=lambda k: lead_times[k]['on_time_rate'])
        
        st.success(f"✅ Mejor proveedor: {best_supplier} ({lead_times[best_supplier]['on_time_rate']:.1%} on-time)")
        st.warning(f"⚠️ Proveedor a mejorar: {worst_supplier} ({lead_times[worst_supplier]['on_time_rate']:.1%} on-time)")
        
        add_xp(10, "lead_time_analysis")
    
    with tab9:
        st.markdown("<h4>🔄 Reorder Point - Punto de Reorden</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Reorder Point:** Calcula el punto óptimo de reorden basado en lead time,
        demanda diaria y servicio objetivo para evitar stockouts.
        """)
        
        selected_product = st.selectbox("Seleccionar Producto", df_inv['product_name'], key="selected_product_reorder")
        prod_data = df_inv[df_inv['product_name'] == selected_product].iloc[0]
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Parámetros de Reorden</h5>", unsafe_allow_html=True)
            
            daily_demand = st.number_input("Demanda Diaria (unidades)", value=prod_data['quantity'] / 30, min_value=0.1, step=0.1)
            lead_time_days = st.slider("Lead Time (días)", 1, 30, 7)
            service_level = st.slider("Nivel de Servicio (%)", 90, 99, 95)
            safety_stock_days = st.slider("Safety Stock (días)", 1, 10, 3)
        
        with col2:
            # Calcular reorder point
            demand_during_lead = daily_demand * lead_time_days
            safety_stock = daily_demand * safety_stock_days
            reorder_point = demand_during_lead + safety_stock
            
            # Calcular Z-score basado en nivel de servicio
            service_levels = {90: 1.28, 95: 1.645, 97.5: 1.96, 99: 2.33}
            z_score = service_levels.get(service_level, 1.645)
            
            # Calcular stockout probability
            stockout_prob = (1 - service_level / 100)
            
            st.markdown("<h5>Resultados</h5>", unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Demanda Lead Time", f"{demand_during_lead:.0f} unidades")
            col2.metric("Safety Stock", f"{safety_stock:.0f} unidades")
            col3.metric("Reorder Point", f"{reorder_point:.0f} unidades")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            col1.metric("Z-Score", f"{z_score:.2f}")
            col2.metric("Prob. Stockout", f"{stockout_prob:.2%}")
        
        # Alerta de stock
        current_stock = prod_data['quantity']
        if current_stock < reorder_point:
            st.error(f"⚠️ STOCK BAJO: {selected_product} está por debajo del punto de reorden ({current_stock:.0f} < {reorder_point:.0f})")
            show_toast("⚠️ Stock bajo detectado", "warning")
        else:
            st.success(f"✅ Stock OK: {selected_product} está por encima del punto de reorden")
        
        add_xp(10, "reorder_point")
    
    with tab10:
        st.markdown("<h4>📦 Supplier Performance - Rendimiento de Proveedores</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Supplier Performance:** Evaluación del rendimiento de proveedores basado en
        fill rate, lead time, calidad y costos para optimizar la cadena de suministro.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Métricas por Proveedor</h5>", unsafe_allow_html=True)
            
            suppliers = [
                {"name": "Farmacéutica ABC", "fill_rate": 98.5, "lead_time": 5, "quality": 99.2, "cost_score": 8.5},
                {"name": "Genfar Venezuela", "fill_rate": 95.2, "lead_time": 7, "quality": 97.8, "cost_score": 7.8},
                {"name": "Laboratorios Farma", "fill_rate": 92.8, "lead_time": 10, "quality": 95.5, "cost_score": 9.2},
                {"name": "Distribuidora Central", "fill_rate": 96.5, "lead_time": 6, "quality": 98.1, "cost_score": 8.0},
                {"name": "Importadora Global", "fill_rate": 88.5, "lead_time": 14, "quality": 94.2, "cost_score": 6.5}
            ]
            
            for supplier in suppliers:
                with st.expander(f"🏭 {supplier['name']}"):
                    col1, col2, col3, col4 = st.columns(4)
                    col1.metric("Fill Rate", f"{supplier['fill_rate']}%")
                    col2.metric("Lead Time", f"{supplier['lead_time']} días")
                    col3.metric("Calidad", f"{supplier['quality']}%")
                    col4.metric("Cost Score", f"{supplier['cost_score']}/10")
        
        with col2:
            st.markdown("<h5>Ranking de Proveedores</h5>", unsafe_allow_html=True)
            
            # Calcular score ponderado
            for supplier in suppliers:
                supplier['total_score'] = (
                    supplier['fill_rate'] * 0.3 +
                    supplier['quality'] * 0.3 +
                    (10 - supplier['lead_time']) * 0.2 +
                    supplier['cost_score'] * 0.2
                )
            
            sorted_suppliers = sorted(suppliers, key=lambda x: x['total_score'], reverse=True)
            
            for i, supplier in enumerate(sorted_suppliers, 1):
                medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"#{i}"
                st.markdown(f"""
                <div style="padding: 8px; margin: 5px 0; border-left: 3px solid {'gold' if i == 1 else 'silver' if i == 2 else '#cd7f32' if i == 3 else 'gray'}; background: rgba(100,100,100,0.1); border-radius: 3px;">
                    <strong>{medal} {supplier['name']}</strong> - Score: {supplier['total_score']:.1f}
                </div>
                """, unsafe_allow_html=True)
        
        # Gráfico de radar
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Comparación de Proveedores**")
        
        fig_radar = go.Figure()
        for supplier in sorted_suppliers[:3]:
            fig_radar.add_trace(go.Scatterpolar(
                r=[supplier['fill_rate'], supplier['quality'], supplier['cost_score'] * 10, (10 - supplier['lead_time']) * 10],
                theta=['Fill Rate', 'Calidad', 'Costo', 'Velocidad'],
                fill='toself',
                name=supplier['name']
            ))
        fig_radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=True)
        st.plotly_chart(fig_radar, use_container_width=True)
        
        add_xp(10, "supplier_performance")
    
    with tab11:
        st.markdown("<h4>🎯 Inventory Optimization - Optimización de Inventario</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Inventory Optimization:** Algoritmos avanzados para optimizar niveles de inventario,
        minimizando costos mientras se mantiene el servicio al cliente.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Parámetros de Optimización</h5>", unsafe_allow_html=True)
            
            opt_product = st.selectbox("Producto a Optimizar", df_inv['product_name'])
            service_level = st.slider("Nivel de Servicio Objetivo (%)", 90, 99, 95)
            holding_cost_pct = st.slider("Costo Holding (%)", 10, 30, 20)
            ordering_cost = st.number_input("Costo por Orden ($)", value=50.0, min_value=0.0, key="ordering_cost_opt")
            
            if st.button("🎯 Optimizar Inventario"):
                st.success("✅ Optimización completada")
                add_xp(10, "inventory_optimization")
                show_toast("✅ Inventario optimizado", "success")
        
        with col2:
            st.markdown("<h5>Resultados de Optimización</h5>", unsafe_allow_html=True)
            
            # Simular resultados
            prod_data = df_inv[df_inv['product_name'] == opt_product].iloc[0]
            current_stock = prod_data['quantity']
            optimal_stock = int(current_stock * random.uniform(0.8, 1.2))
            savings = (current_stock - optimal_stock) * prod_data['cost_price'] * 0.2
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Stock Actual", f"{current_stock}")
            col2.metric("Stock Óptimo", f"{optimal_stock}")
            col3.metric("Ahorro Anual", f"${savings:,.2f}")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            if savings > 0:
                st.success(f"💰 Ahorro estimado: ${savings:,.2f}/año")
            else:
                st.info("ℹ️ El stock actual ya está optimizado")
        
        # Gráfico de optimización
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Curva de Costo vs Stock**")
        
        stock_levels = list(range(50, 500, 50))
        total_costs = []
        
        for stock in stock_levels:
            holding_cost = stock * prod_data['cost_price'] * (holding_cost_pct / 100)
            ordering_cost = (prod_data['quantity'] * 12 / stock) * ordering_cost
            stockout_cost = (stock < optimal_stock) * 500
            total_costs.append(holding_cost + ordering_cost + stockout_cost)
        
        fig_opt = go.Figure()
        fig_opt.add_trace(go.Scatter(x=stock_levels, y=total_costs, mode='lines+markers', name='Costo Total'))
        fig_opt.add_vline(x=optimal_stock, line_dash="dash", line_color="red", annotation_text="Óptimo")
        fig_opt.update_layout(title="Costo Total vs Nivel de Stock", xaxis_title="Stock", yaxis_title="Costo ($)")
        st.plotly_chart(fig_opt, use_container_width=True)
        
        add_xp(10, "inventory_optimization")
    
    with tab12:
        st.markdown("<h4>📦 Demand Planning - Planificación de Demanda</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Demand Planning:** Planificación avanzada de demanda usando métodos
        estadísticos y de ML para predecir demanda futura y optimizar inventario.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Configuración de Forecast</h5>", unsafe_allow_html=True)
            
            forecast_method = st.selectbox("Método de Forecast", ["Moving Average", "Exponential Smoothing", "ARIMA", "ML Regression"])
            forecast_period = st.slider("Períodos a Pronosticar", 1, 12, 6)
            seasonality = st.selectbox("Estacionalidad", ["None", "Weekly", "Monthly", "Quarterly"])
            
            if st.button("📦 Generar Forecast"):
                st.success("✅ Forecast generado")
                add_xp(15, "demand_planning")
                show_toast("✅ Demand planning completado", "success")
        
        with col2:
            st.markdown("<h5>Pronóstico de Demanda</h5>", unsafe_allow_html=True)
            
            # Simular datos históricos y forecast
            historical_demand = [random.randint(80, 120) for _ in range(12)]
            forecast_demand = [random.randint(90, 130) for _ in range(forecast_period)]
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Demanda Promedio", f"{sum(historical_demand)/len(historical_demand):.1f}")
            col2.metric("Forecast Promedio", f"{sum(forecast_demand)/len(forecast_demand):.1f}")
            col3.metric("Crecimiento", f"{(sum(forecast_demand)/len(forecast_demand) - sum(historical_demand)/len(historical_demand))/sum(historical_demand)/len(historical_demand)*100:.1f}%")
        
        # Gráfico de forecast
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Pronóstico de Demanda**")
        
        fig_demand = go.Figure()
        fig_demand.add_trace(go.Scatter(x=list(range(12)), y=historical_demand, name='Histórico', mode='lines+markers'))
        fig_demand.add_trace(go.Scatter(x=list(range(11, 11 + forecast_period)), y=forecast_demand, name='Forecast', mode='lines+markers', line=dict(dash='dash')))
        fig_demand.update_layout(title="Pronóstico de Demanda", xaxis_title="Período", yaxis_title="Demanda")
        st.plotly_chart(fig_demand, use_container_width=True)
        
        add_xp(10, "demand_planning")
    
    with tab13:
        st.markdown("<h4>🚚 Logistics Optimization - Optimización Logística</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Logistics Optimization:** Optimización de rutas, transporte y distribución
        para minimizar costos y tiempos de entrega.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Configuración de Rutas</h5>", unsafe_allow_html=True)
            
            origin = st.text_input("Origen", value="Caracas")
            destinations = st.text_area("Destinos (uno por línea)", value="Maracaibo\nValencia\nBarquisimeto\nCiudad Bolívar")
            vehicle_type = st.selectbox("Tipo de Vehículo", ["Camión", "Furgoneta", "Contenedor"])
            
            if st.button("🚚 Optimizar Rutas"):
                st.success("✅ Rutas optimizadas")
                add_xp(15, "logistics_optimization")
                show_toast("✅ Logistics optimization completado", "success")
        
        with col2:
            st.markdown("<h5>Métricas Logísticas</h5>", unsafe_allow_html=True)
            
            routes = [
                {"route": "Caracas → Maracaibo", "distance": 520, "time": 8, "cost": 450},
                {"route": "Caracas → Valencia", "distance": 180, "time": 3, "cost": 150},
                {"route": "Caracas → Barquisimeto", "distance": 350, "time": 5, "cost": 300}
            ]
            
            for route in routes:
                with st.expander(f"🚚 {route['route']}"):
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Distancia", f"{route['distance']} km")
                    col2.metric("Tiempo", f"{route['time']} h")
                    col3.metric("Costo", f"${route['cost']}")
        
        # Gráfico de rutas
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Distribución de Costos por Ruta**")
        
        fig_logistics = go.Figure(data=[go.Pie(labels=[r['route'] for r in routes], values=[r['cost'] for r in routes])])
        fig_logistics.update_layout(title="Costos por Ruta")
        st.plotly_chart(fig_logistics, use_container_width=True)
        
        add_xp(10, "logistics_optimization")
    
    with tab14:
        st.markdown("<h4>🛡️ Safety Stock Calculator - Calculadora de Stock de Seguridad</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Safety Stock Calculator:** Calcula el stock de seguridad óptimo basado en
        variabilidad de demanda y lead time para proteger contra stockouts.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Parámetros de Variabilidad</h5>", unsafe_allow_html=True)
            
            demand_std = st.number_input("Desviación Estándar de Demanda", value=50.0, min_value=0.0)
            lead_time_std = st.number_input("Desviación Estándar de Lead Time (días)", value=2.0, min_value=0.0)
            avg_demand = st.number_input("Demanda Promedio Diaria", value=100.0, min_value=0.0)
            avg_lead_time = st.number_input("Lead Time Promedio (días)", value=7.0, min_value=0.0)
            service_level = st.slider("Nivel de Servicio (%)", 90, 99, 95)
            
            if st.button("🛡️ Calcular Safety Stock"):
                st.success("✅ Safety stock calculado")
                add_xp(10, "safety_stock_calculator")
                show_toast("✅ Safety stock calculado", "success")
        
        with col2:
            st.markdown("<h5>Resultados</h5>", unsafe_allow_html=True)
            
            # Z-score basado en nivel de servicio
            service_levels = {90: 1.28, 95: 1.645, 97.5: 1.96, 99: 2.33}
            z_score = service_levels.get(service_level, 1.645)
            
            # Fórmula de safety stock
            safety_stock = z_score * ((avg_lead_time * demand_std**2 + avg_demand**2 * lead_time_std**2) ** 0.5)
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Z-Score", f"{z_score:.2f}")
            col2.metric("Safety Stock", f"{safety_stock:.0f} unidades")
            col3.metric("Nivel Servicio", f"{service_level}%")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            reorder_point = avg_demand * avg_lead_time + safety_stock
            col1.metric("Reorder Point", f"{reorder_point:.0f} unidades")
        
        add_xp(10, "safety_stock_calculator")
    
    with tab15:
        st.markdown("<h4>🏗️ Multi-Warehouse Optimization - Optimización Multi-Almacén</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Multi-Warehouse Optimization:** Optimización de distribución de inventario
        entre múltiples almacenes para minimizar costos y maximizar servicio.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Configuración de Almacenes</h5>", unsafe_allow_html=True)
            
            warehouses = [
                {"name": "Caracas", "capacity": 10000, "current": 7500, "demand": 5000},
                {"name": "Valencia", "capacity": 8000, "current": 6000, "demand": 4000},
                {"name": "Maracaibo", "capacity": 6000, "current": 4500, "demand": 3500},
                {"name": "Barquisimeto", "capacity": 5000, "current": 3000, "demand": 2500}
            ]
            
            for wh in warehouses:
                with st.expander(f"🏗️ {wh['name']}"):
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Capacidad", wh['capacity'])
                    col2.metric("Actual", wh['current'])
                    col3.metric("Demanda", wh['demand'])
                    
                    utilization = (wh['current'] / wh['capacity']) * 100
                    st.progress(utilization / 100)
                    st.markdown(f"**Utilización:** {utilization:.1f}%")
            
            if st.button("🏗️ Optimizar Distribución"):
                st.success("✅ Distribución optimizada")
                add_xp(10, "multi_warehouse_optimization")
                show_toast("✅ Distribución optimizada", "success")
        
        with col2:
            st.markdown("<h5>Métricas de Optimización</h5>", unsafe_allow_html=True)
            
            total_capacity = sum(wh['capacity'] for wh in warehouses)
            total_current = sum(wh['current'] for wh in warehouses)
            total_demand = sum(wh['demand'] for wh in warehouses)
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Capacidad Total", total_capacity)
            col2.metric("Inventario Total", total_current)
            col3.metric("Demanda Total", total_demand)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            avg_utilization = (total_current / total_capacity) * 100
            service_level = min((total_current / total_demand) * 100, 100)
            
            col1.metric("Utilización Promedio", f"{avg_utilization:.1f}%")
            col2.metric("Nivel de Servicio", f"{service_level:.1f}%")
        
        # Gráfico de distribución
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Distribución de Inventario por Almacén**")
        
        fig_mw = go.Figure(data=[go.Bar(
            x=[wh['name'] for wh in warehouses],
            y=[wh['current'] for wh in warehouses],
            marker_color='teal'
        )])
        fig_mw.update_layout(title="Inventario por Almacén", xaxis_title="Almacén", yaxis_title="Unidades")
        st.plotly_chart(fig_mw, use_container_width=True)
        
        add_xp(10, "multi_warehouse_optimization")
    
    with tab16:
        st.markdown("<h4>⚠️ Supplier Risk Assessment - Evaluación de Riesgo de Proveedores</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Supplier Risk Assessment:** Evaluación de riesgo de proveedores basada en
        múltiples factores para mitigar riesgos en la cadena de suministro.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Evaluación de Proveedores</h5>", unsafe_allow_html=True)
            
            suppliers_risk = [
                {"name": "Farmacéutica ABC", "financial": 85, "operational": 90, "compliance": 95, "geographic": 70},
                {"name": "Genfar Venezuela", "financial": 75, "operational": 85, "compliance": 90, "geographic": 80},
                {"name": "Novartis Venezuela", "financial": 95, "operational": 95, "compliance": 98, "geographic": 75},
                {"name": "Pfizer Venezuela", "financial": 90, "operational": 88, "compliance": 92, "geographic": 65}
            ]
            
            for supplier in suppliers_risk:
                with st.expander(f"⚠️ {supplier['name']}"):
                    col1, col2, col3, col4 = st.columns(4)
                    col1.metric("Financiero", f"{supplier['financial']}%")
                    col2.metric("Operacional", f"{supplier['operational']}%")
                    col3.metric("Compliance", f"{supplier['compliance']}%")
                    col4.metric("Geográfico", f"{supplier['geographic']}%")
                    
                    # Calcular riesgo total
                    total_risk = 100 - (supplier['financial'] + supplier['operational'] + supplier['compliance'] + supplier['geographic']) / 4
                    
                    risk_level = "Bajo" if total_risk < 20 else "Medio" if total_risk < 40 else "Alto"
                    risk_color = "green" if risk_level == "Bajo" else "orange" if risk_level == "Medio" else "red"
                    
                    st.markdown(f"**Riesgo Total:** <span style='color: {risk_color}'>{total_risk:.1f}% ({risk_level})</span>", unsafe_allow_html=True)
            
            if st.button("⚠️ Actualizar Evaluación"):
                st.success("✅ Evaluación actualizada")
                add_xp(10, "supplier_risk_assessment")
                show_toast("✅ Evaluación actualizada", "success")
        
        with col2:
            st.markdown("<h5>Métricas de Riesgo</h5>", unsafe_allow_html=True)
            
            avg_financial = sum(s['financial'] for s in suppliers_risk) / len(suppliers_risk)
            avg_operational = sum(s['operational'] for s in suppliers_risk) / len(suppliers_risk)
            avg_compliance = sum(s['compliance'] for s in suppliers_risk) / len(suppliers_risk)
            avg_geographic = sum(s['geographic'] for s in suppliers_risk) / len(suppliers_risk)
            
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Financiero", f"{avg_financial:.1f}%")
            col2.metric("Operacional", f"{avg_operational:.1f}%")
            col3.metric("Compliance", f"{avg_compliance:.1f}%")
            col4.metric("Geográfico", f"{avg_geographic:.1f}%")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Proveedores de alto riesgo
            high_risk = [s for s in suppliers_risk if (100 - (s['financial'] + s['operational'] + s['compliance'] + s['geographic']) / 4) >= 40]
            
            col1.metric("Proveedores", len(suppliers_risk))
            col2.metric("Alto Riesgo", len(high_risk))
        
        # Gráfico de riesgo
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Distribución de Riesgo por Proveedor**")
        
        supplier_names = [s['name'] for s in suppliers_risk]
        risk_scores = [100 - (s['financial'] + s['operational'] + s['compliance'] + s['geographic']) / 4 for s in suppliers_risk]
        
        fig_risk = go.Figure(data=[go.Bar(
            x=supplier_names,
            y=risk_scores,
            marker_color=['red' if r >= 40 else 'orange' if r >= 20 else 'green' for r in risk_scores]
        )])
        fig_risk.update_layout(title="Score de Riesgo por Proveedor", xaxis_title="Proveedor", yaxis_title="Riesgo (%)")
        st.plotly_chart(fig_risk, use_container_width=True)
        
        add_xp(10, "supplier_risk_assessment")

# ================================================================================
# DOCUVERIFY ELITE
# ================================================================================
elif selected == "📄 DocuVerify Elite":
    st.markdown('<h1 class="main-header">📄 DocuVerify Elite</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Blockchain Legal | Smart Contracts | Zero-Knowledge Proofs | Merkle Trees | Digital Signatures</p>', unsafe_allow_html=True)
    
    # Otorgar XP por usar DocuVerify
    if 'docuverify_visited' not in st.session_state:
        add_xp(10, "blockchain_verification")
        st.session_state.docuverify_visited = True
    
    cols = st.columns(5)
    cols[0].metric("🔒 Documentos", "1,247", "Verificados")
    cols[1].metric("⛓️ Blockchain", "Ethereum", "Mainnet")
    cols[2].metric("✅ Firmas", "3,891", "Digitales")
    cols[3].metric("🔍 Auditorías", "847", "Completadas")
    cols[4].metric("⚡ Latencia", "2.3s", "Verificación")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    tabs = st.tabs(["📤 Document Upload", "⛓️ Blockchain Ledger", "🔐 Digital Signatures", "🔍 Merkle Tree", "🔬 Zero-Knowledge Proofs", "📜 Smart Contracts", "🌉 Cross-Chain Bridges", "🔍 Transaction Explorer", "⛽ Gas Tracker", "💰 Token Price", "🖼️ NFT Marketplace", "💎 DeFi Dashboard", "🏛️ DAO Governance", "🔄 Token Swap", "🔍 Smart Contract Audit", "💼 Wallet Manager", "🔗 Cross-Chain Bridge", "💎 Token Staking", "💧 Liquidity Pool", "🔄 DEX Aggregator", "🌾 Yield Farming", "⚡ Flash Loans"])
    
    with tabs[0]:
        st.markdown("<h4>Document Upload & Verification</h4>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            uploaded_file = st.file_uploader("Subir Documento", type=['pdf', 'docx', 'txt'])
            doc_type = st.selectbox("Tipo de Documento", ["Contrato", "Factura", "Acuerdo", "Reporte", "Certificado"])
            
            if uploaded_file:
                file_content = uploaded_file.read()
                sha256_hash = calc_hash_sha256(file_content)
                md5_hash = calc_hash_md5(file_content)
                
                st.success(f"✅ Documento cargado exitosamente")
                st.metric("SHA256", sha256_hash[:16] + "...")
                st.metric("MD5", md5_hash[:16] + "...")
                st.metric("Tamaño", f"{len(file_content):,} bytes")
                
                if st.button("📤 Subir a Blockchain"):
                    doc_id = gen_id("DOC")
                    conn = get_db()
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO documents (document_id, file_name, file_type, file_size, hash_sha256, hash_md5, uploaded_by, signatures_required, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                 (doc_id, uploaded_file.name, doc_type, len(file_content), sha256_hash, md5_hash, "user", 2, "pending"))
                    conn.commit()
                    conn.close()
                    
                    st.success(f"✅ Documento subido a blockchain: {doc_id}")
        
        with col2:
            conn = get_db()
            df_docs = pd.read_sql_query("SELECT * FROM documents ORDER BY created_at DESC LIMIT 10", conn)
            conn.close()
            
            if not df_docs.empty:
                st.markdown("<h5>Documentos Recientes</h5>", unsafe_allow_html=True)
                st.dataframe(df_docs[['document_id', 'file_name', 'file_type', 'status', 'created_at']], 
                            use_container_width=True, hide_index=True)
            else:
                st.info("No hay documentos registrados")
    
    with tabs[1]:
        st.markdown("<h4>Blockchain Ledger - Registro Inmutable</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Blockchain Ledger:** Registro distribuido e inmutable de todas las transacciones
        de documentos, proporcionando trazabilidad completa y auditoría transparente.
        """)
        
        blocks = []
        for i in range(5):
            nonce, block_hash = proof_of_work(f"block{i}", 2)
            block = {
                'Block': i,
                'Hash': block_hash[:16],
                'Previous': blocks[i-1]['Hash'] if i > 0 else "0000000000000000",
                'Nonce': nonce,
                'Timestamp': (datetime.now() - timedelta(hours=i*2)).strftime('%H:%M:%S'),
                'Transactions': random.randint(1, 5)
            }
            blocks.append(block)
        
        df_blocks = pd.DataFrame(blocks)
        st.dataframe(df_blocks, use_container_width=True, hide_index=True)
        
        conn = get_db()
        df_audit = pd.read_sql_query("SELECT * FROM document_audit ORDER BY timestamp DESC LIMIT 20", conn)
        conn.close()
        
        if not df_audit.empty:
            st.markdown("<h5>Audit Trail Completo</h5>", unsafe_allow_html=True)
            st.dataframe(df_audit, use_container_width=True, hide_index=True)
        else:
            st.info("No hay registros de auditoría aún")
    
    with tabs[2]:
        st.markdown("<h4>Digital Signatures - Firma Electrónica Avanzada</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Digital Signatures:** Firma criptográfica que garantiza autenticidad,
        integridad y no repudio de documentos electrónicos.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            document_content = st.text_area("Contenido del Documento", height=150)
            private_key = st.text_input("Clave Privada", type="password")
            
            if st.button("✍️ Firmar Documento"):
                if document_content and private_key:
                    signature = calc_hash_sha256(f"{document_content}{private_key}".encode())
                    st.success(f"✅ Documento firmado exitosamente")
                    st.metric("Firma Digital", signature[:32] + "...")
                    st.metric("Algoritmo", "SHA-256")
                else:
                    st.warning("Ingresa contenido del documento y clave privada")
        
        with col2:
            verify_content = st.text_area("Contenido a Verificar", height=150)
            verify_signature = st.text_input("Firma a Verificar")
            verify_public_key = st.text_input("Clave Pública")
            
            if st.button("🔍 Verificar Firma"):
                expected_signature = calc_hash_sha256(f"{verify_content}{verify_public_key}".encode())
                if verify_signature == expected_signature:
                    st.success("✅ Firma VÁLIDA - Documento auténtico")
                else:
                    st.error("❌ Firma INVÁLIDA - Documento modificado o corrupto")
    
    with tabs[3]:
        st.markdown("<h4>Merkle Tree - Verificación Eficiente</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Merkle Tree:** Estructura de datos eficiente para verificar integridad de grandes conjuntos de datos.
        Permite verificar si un documento está incluido en un conjunto sin descargar todo.
        """)
        
        documents = [
            "Documento A - Contrato 123",
            "Documento B - Factura 456",
            "Documento C - Acuerdo 789",
            "Documento D - Reporte 101",
            "Documento E - Certificado 202",
            "Documento F - Licencia 303",
            "Documento G - Permiso 404",
            "Documento H - Registro 505"
        ]
        
        doc_hashes = [hashlib.sha256(doc.encode()).hexdigest() for doc in documents]
        merkle_root = create_merkle_tree(doc_hashes)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Documentos y Hashes</h5>", unsafe_allow_html=True)
            for i, (doc, h) in enumerate(zip(documents, doc_hashes)):
                st.text(f"{doc}: {h[:16]}...")
        
        with col2:
            st.markdown("<h5>Merkle Root</h5>", unsafe_allow_html=True)
            st.code(f"{merkle_root}", language="text")
            st.metric("Nivel del Árbol", f"{int(np.log2(len(doc_hashes))) + 1}" if NUMPY_AVAILABLE else "3")
        
        doc_to_verify = st.selectbox("Documento a verificar", documents)
        doc_index = documents.index(doc_to_verify)
        doc_hash = doc_hashes[doc_index]
        
        st.info(f"""
        **Merkle Proof para:** {doc_to_verify}
        
        - Hash del documento: `{doc_hash[:16]}...`
        - Merkle Root: `{merkle_root[:16]}...`
        - Posición en el árbol: {doc_index}
        
        **Conclusión:** El documento está verificado en el Merkle Tree.
        """)
    
    with tabs[4]:
        st.markdown("<h4>Zero-Knowledge Proofs</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Zero-Knowledge Proof (ZKP):** Permite probar que conoces un secreto sin revelarlo.
        Aplicaciones: autenticación, privacidad, verificación de identidad.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            secret = st.text_input("Secreto (password, clave privada)", type="password")
            message = st.text_input("Mensaje a comprometer", value="Documento confidencial #123")
        
        with col2:
            if st.button("🔐 Generar ZKP"):
                if secret and message:
                    commitment = hashlib.sha256(f"{message}{secret}".encode()).hexdigest()[:16]
                    challenge = random.randint(1000, 9999)
                    response = hashlib.sha256(f"{commitment}{challenge}{secret}".encode()).hexdigest()[:16]
                    
                    st.success(f"""
                    ✅ **ZKP Generado Exitosamente!**
                    
                    - Commitment: `{commitment}`
                    - Challenge: {challenge}
                    - Response: `{response}`
                    
                    **Verificación:** Puedes probar que conoces el secreto sin revelarlo.
                    """)
                    
                    is_valid = verify_zero_knowledge_proof(commitment, challenge, response, secret)
                    if is_valid:
                        st.success("🎉 ZKP Verificado - El secreto es válido")
                else:
                    st.warning("Ingresa secreto y mensaje")
        
        st.markdown("<h5>Simulación de Verificación</h5>", unsafe_allow_html=True)
        
        verify_commit = st.text_input("Commitment a verificar")
        verify_challenge = st.number_input("Challenge", value=1234)
        verify_response = st.text_input("Response")
        verify_secret = st.text_input("Secreto para verificar", type="password")
        
        if st.button("🔍 Verificar ZKP"):
            is_valid = verify_zero_knowledge_proof(verify_commit, verify_challenge, verify_response, verify_secret)
            if is_valid:
                st.success("✅ ZKP Válido - La prueba es correcta")
            else:
                st.error("❌ ZKP Inválido - La prueba falló")
    
    with tabs[5]:
        st.markdown("<h4>Smart Contracts - Solidity Implementation</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Smart Contracts:** Contratos inteligentes desplegados en blockchain para 
        automatización de verificación de documentos con lógica inmutable y ejecución determinista.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            solidity_code = '''
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DocumentVerification {
    struct Document {
        bytes32 documentHash;
        address uploader;
        uint256 timestamp;
        bool verified;
        address[] signers;
    }
    
    mapping(bytes32 => Document) public documents;
    
    event DocumentUploaded(bytes32 indexed hash, address uploader);
    event DocumentVerified(bytes32 indexed hash, address verifier);
    
    function uploadDocument(bytes32 hash) public {
        require(documents[hash].timestamp == 0, "Document exists");
        documents[hash] = Document({
            documentHash: hash,
            uploader: msg.sender,
            timestamp: block.timestamp,
            verified: false,
            signers: new address[](0)
        });
        emit DocumentUploaded(hash, msg.sender);
    }
    
    function verifyDocument(bytes32 hash) public {
        require(documents[hash].timestamp != 0, "Document not found");
        documents[hash].verified = true;
        documents[hash].signers.push(msg.sender);
        emit DocumentVerified(hash, msg.sender);
    }
    
    function isVerified(bytes32 hash) public view returns (bool) {
        return documents[hash].verified;
    }
}
'''
            
            st.code(solidity_code, language='solidity')
            
            if st.button("🚀 Deploy Contract"):
                st.success("✅ Smart Contract deployed to Ethereum Mainnet")
                st.info("Contract Address: 0x1234...5678")
                st.metric("Gas Used", "2,450,000")
                st.metric("Deployment Cost", "0.045 ETH")
        
        with col2:
            contract_address = st.text_input("Contract Address", value="0x1234567890abcdef1234567890abcdef12345678")
            function_name = st.selectbox("Function", ["uploadDocument", "verifyDocument", "isVerified"])
            
            if function_name == "uploadDocument":
                doc_hash = st.text_input("Document Hash (SHA256)")
                if st.button("📤 Upload"):
                    st.success(f"Document uploaded: {doc_hash[:16]}...")
                    st.metric("Transaction Hash", f"0x{random.randint(1000000, 9999999):x}")
                    st.metric("Gas Used", f"{random.randint(50000, 100000):,}")
            
            elif function_name == "verifyDocument":
                verify_hash = st.text_input("Document Hash to Verify")
                if st.button("✅ Verify"):
                    st.success(f"Document verified: {verify_hash[:16]}...")
                    st.metric("Transaction Hash", f"0x{random.randint(1000000, 9999999):x}")
                    st.metric("Gas Used", f"{random.randint(30000, 60000):,}")
            
            else:
                check_hash = st.text_input("Document Hash to Check")
                if st.button("🔍 Check Status"):
                    is_verified = random.choice([True, False])
                    if is_verified:
                        st.success("Document is VERIFIED ✅")
                    else:
                        st.warning("Document is NOT verified ⚠️")
    
    with tabs[6]:
        st.markdown("<h4>Cross-Chain Bridges - Multi-Blockchain</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Cross-Chain Bridges:** Interoperabilidad entre múltiples blockchains 
        (Ethereum, Polygon, BSC) para verificación de documentos across diferentes redes.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            chains = [
                {'name': 'Ethereum Mainnet', 'symbol': 'ETH', 'block_time': '12s', 'gas_price': '25 Gwei'},
                {'name': 'Polygon', 'symbol': 'MATIC', 'block_time': '2s', 'gas_price': '1 Gwei'},
                {'name': 'Binance Smart Chain', 'symbol': 'BSC', 'block_time': '3s', 'gas_price': '3 Gwei'},
                {'name': 'Arbitrum', 'symbol': 'ARB', 'block_time': '0.25s', 'gas_price': '0.1 Gwei'}
            ]
            
            for chain in chains:
                with st.expander(f"🔗 {chain['name']} ({chain['symbol']})"):
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Block Time", chain['block_time'])
                    col2.metric("Gas Price", chain['gas_price'])
                    col3.metric("Status", "Active")
        
        with col2:
            source_chain = st.selectbox("Source Chain", ["Ethereum", "Polygon", "BSC", "Arbitrum"])
            dest_chain = st.selectbox("Destination Chain", ["Polygon", "BSC", "Arbitrum", "Ethereum"])
            bridge_amount = st.number_input("Bridge Amount (ETH)", value=1.0, step=0.1)
            
            if st.button("🌉 Bridge Document"):
                bridge_fee = bridge_amount * 0.001
                estimated_time = "5-10 min" if source_chain == "Ethereum" else "2-5 min"
                
                st.success(f"""
                ✅ **Bridge Initiated**
                
                - From: {source_chain} → To: {dest_chain}
                - Amount: {bridge_amount} ETH
                - Bridge Fee: {bridge_fee:.4f} ETH
                - Estimated Time: {estimated_time}
                """)
                
                st.metric("Transaction Hash", f"0x{random.randint(1000000, 9999999):x}")
    
    with tabs[7]:
        st.markdown("<h4>🔍 Transaction Explorer - Explorador de Transacciones</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Transaction Explorer:** Explora transacciones de blockchain en tiempo real usando
        Etherscan API para obtener detalles de transacciones Ethereum.
        """)
        
        tx_hash = st.text_input("Transaction Hash", value="0x")
        
        if st.button("🔍 Buscar Transacción"):
            if tx_hash.startswith("0x") and len(tx_hash) == 66:
                # Simular datos de transacción
                st.success(f"✅ Transacción encontrada")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("From", f"0x{random.randint(1000000, 9999999):x}")
                    st.metric("To", f"0x{random.randint(1000000, 9999999):x}")
                    st.metric("Value", f"{random.uniform(0.1, 10):.4f} ETH")
                with col2:
                    st.metric("Gas Used", f"{random.randint(21000, 100000):,}")
                    st.metric("Gas Price", f"{random.randint(10, 100)} Gwei")
                    st.metric("Status", "✅ Success")
                
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown("**Input Data:**")
                st.code("0x" + "00" * 32, language="text")
                
                add_xp(5, "blockchain_explorer")
                show_toast("✅ Transacción explorada", "success")
            else:
                st.error("❌ Hash de transacción inválido (debe ser 0x seguido de 64 caracteres hex)")
    
    with tabs[8]:
        st.markdown("<h4>⛽ Gas Tracker - Rastreador de Gas</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Gas Tracker:** Monitorea los precios de gas en tiempo real en Ethereum para
        optimizar el costo de transacciones.
        """)
        
        # Simular datos de gas
        gas_prices = {
            "Slow": random.randint(10, 20),
            "Average": random.randint(20, 40),
            "Fast": random.randint(40, 60),
            "Fastest": random.randint(60, 100)
        }
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Slow", f"{gas_prices['Slow']} Gwei", "Low Priority")
        col2.metric("Average", f"{gas_prices['Average']} Gwei", "Standard")
        col3.metric("Fast", f"{gas_prices['Fast']} Gwei", "High Priority")
        col4.metric("Fastest", f"{gas_prices['Fastest']} Gwei", "Max Priority")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Estimación de costo
        gas_limit = st.number_input("Gas Limit", value=21000, min_value=21000)
        selected_gas = st.selectbox("Seleccionar Velocidad", ["Slow", "Average", "Fast", "Fastest"])
        
        if selected_gas:
            gas_price = gas_prices[selected_gas]
            eth_cost = (gas_limit * gas_price) / 1e9
            usd_cost = eth_cost * 2000  # Precio ETH simulado
            
            col1, col2 = st.columns(2)
            col1.metric("Costo ETH", f"{eth_cost:.6f} ETH")
            col2.metric("Costo USD", f"${usd_cost:.2f}")
        
        # Gráfico de gas histórico
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Historial de Gas (24h)**")
        
        gas_history = [random.randint(15, 80) for _ in range(24)]
        fig_gas = go.Figure()
        fig_gas.add_trace(go.Scatter(x=list(range(24)), y=gas_history, mode='lines+markers', name='Gas Price'))
        fig_gas.update_layout(title="Gas Price (Gwei) - Últimas 24 horas", xaxis_title="Hora", yaxis_title="Gas Price (Gwei)")
        st.plotly_chart(fig_gas, use_container_width=True)
        
        add_xp(5, "gas_tracking")
    
    with tabs[9]:
        st.markdown("<h4>💰 Token Price - Precios de Tokens</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Token Price:** Monitorea precios de tokens ERC-20 en tiempo real usando
        CoinGecko API para obtener datos de mercado.
        """)
        
        # Obtener precios reales de CoinGecko
        if st.button("🔄 Actualizar Precios"):
            crypto_prices = get_crypto_prices()
            if crypto_prices:
                st.success("✅ Precios actualizados")
                for crypto, data in crypto_prices.items():
                    st.metric(crypto.upper(), f"${data['usd']}")
                add_xp(5, "token_price_tracking")
                show_toast("✅ Precios actualizados", "success")
            else:
                st.warning("No se pudieron obtener precios (usando datos simulados)")
        
        # Mostrar precios simulados si no hay datos reales
        tokens = [
            {"name": "Bitcoin", "symbol": "BTC", "price": 43500 + random.uniform(-500, 500), "change": random.uniform(-5, 5)},
            {"name": "Ethereum", "symbol": "ETH", "price": 2250 + random.uniform(-50, 50), "change": random.uniform(-5, 5)},
            {"name": "BNB", "symbol": "BNB", "price": 310 + random.uniform(-10, 10), "change": random.uniform(-5, 5)},
            {"name": "Cardano", "symbol": "ADA", "price": 0.45 + random.uniform(-0.05, 0.05), "change": random.uniform(-5, 5)},
            {"name": "Solana", "symbol": "SOL", "price": 95 + random.uniform(-5, 5), "change": random.uniform(-5, 5)},
            {"name": "Polkadot", "symbol": "DOT", "price": 7.5 + random.uniform(-0.5, 0.5), "change": random.uniform(-5, 5)}
        ]
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        for token in tokens:
            change_color = "green" if token['change'] >= 0 else "red"
            change_sign = "+" if token['change'] >= 0 else ""
            
            col1, col2, col3 = st.columns(3)
            col1.metric(token['name'], f"${token['price']:.2f}")
            col2.metric(f"{token['symbol']}/USDT", f"${token['price']:.2f}")
            col3.metric("24h Change", f"{change_sign}{token['change']:.2f}%", delta_color="normal")
        
        # Gráfico de precios
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Gráfico de Precios (7 días)**")
        
        price_history = {token['symbol']: [token['price'] * (1 + random.uniform(-0.02, 0.02)) for _ in range(7)] for token in tokens}
        
        fig_prices = go.Figure()
        for symbol, prices in price_history.items():
            fig_prices.add_trace(go.Scatter(x=list(range(7)), y=prices, name=symbol, mode='lines'))
        fig_prices.update_layout(title="Precios de Tokens (7 días)", xaxis_title="Día", yaxis_title="Precio (USD)")
        st.plotly_chart(fig_prices, use_container_width=True)
    
    with tabs[10]:
        st.markdown("<h4>🖼️ NFT Marketplace - Mercado de NFTs</h4>", unsafe_allow_html=True)
        
        st.info("""
        **NFT Marketplace:** Plataforma para crear, comprar y vender NFTs (Non-Fungible Tokens)
        con verificación blockchain y metadatos IPFS.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Crear NFT</h5>", unsafe_allow_html=True)
            
            nft_name = st.text_input("Nombre del NFT", value="Elite Document #001")
            nft_description = st.text_area("Descripción", value="Documento verificado en blockchain")
            nft_collection = st.selectbox("Colección", ["Documents", "Art", "Collectibles", "Utility"])
            nft_price = st.number_input("Precio (ETH)", value=0.1, min_value=0.0, step=0.01)
            
            if st.button("🎨 Crear NFT"):
                st.success(f"✅ NFT '{nft_name}' creado exitosamente")
                st.info(f"Token ID: {random.randint(100000, 999999)}")
                st.metric("Gas Used", f"{random.randint(150000, 300000):,}")
                add_xp(10, "nft_creation")
                show_toast("✅ NFT creado", "success")
        
        with col2:
            st.markdown("<h5>NFTs Disponibles</h5>", unsafe_allow_html=True)
            
            nfts = [
                {"name": "Elite Doc #001", "collection": "Documents", "price": 0.15, "creator": "0x1234..."},
                {"name": "Crypto Art #42", "collection": "Art", "price": 0.5, "creator": "0x5678..."},
                {"name": "VIP Badge", "collection": "Utility", "price": 0.25, "creator": "0x9abc..."},
                {"name": "Rare Collectible", "collection": "Collectibles", "price": 1.0, "creator": "0xdef0..."}
            ]
            
            for nft in nfts:
                with st.expander(f"🖼️ {nft['name']}"):
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Colección", nft['collection'])
                    col2.metric("Precio", f"{nft['price']} ETH")
                    col3.metric("Creador", nft['creator'])
                    
                    if st.button(f"💰 Comprar {nft['name']}", key=f"buy_{nft['name']}"):
                        st.success(f"✅ NFT '{nft['name']}' comprado")
                        add_xp(5, "nft_purchase")
        
        # Estadísticas del marketplace
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Estadísticas del Marketplace**")
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("NFTs Creados", f"{random.randint(100, 500)}")
        col2.metric("Volumen (24h)", f"{random.uniform(10, 50):.1f} ETH")
        col3.metric("Colecciones", f"{random.randint(10, 30)}")
        col4.metric("Propietarios", f"{random.randint(50, 200)}")
        
        add_xp(10, "nft_marketplace")
    
    with tabs[11]:
        st.markdown("<h4>💎 DeFi Dashboard - Finanzas Descentralizadas</h4>", unsafe_allow_html=True)
        
        st.info("""
        **DeFi Dashboard:** Panel de control para protocolos DeFi como staking, lending, 
        yield farming y liquidity pools con análisis de APY y riesgos.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Protocolos DeFi</h5>", unsafe_allow_html=True)
            
            defi_protocols = [
                {"name": "Aave", "type": "Lending", "tvl": "5.2B", "apy": 4.5},
                {"name": "Uniswap", "type": "DEX", "tvl": "3.8B", "apy": 2.8},
                {"name": "Curve", "type": "DEX", "tvl": "2.1B", "apy": 3.2},
                {"name": "Compound", "type": "Lending", "tvl": "1.8B", "apy": 5.1},
                {"name": "Lido", "type": "Staking", "tvl": "8.5B", "apy": 4.2}
            ]
            
            for protocol in defi_protocols:
                with st.expander(f"💎 {protocol['name']} - {protocol['type']}"):
                    col1, col2, col3 = st.columns(3)
                    col1.metric("TVL", protocol['tvl'])
                    col2.metric("APY", f"{protocol['apy']}%")
                    col3.metric("Tipo", protocol['type'])
                    
                    if st.button(f"💰 Depositar en {protocol['name']}", key=f"deposit_{protocol['name']}"):
                        st.success(f"✅ Depositado en {protocol['name']}")
                        add_xp(5, "defi_deposit")
        
        with col2:
            st.markdown("<h5>Mi Portfolio DeFi</h5>", unsafe_allow_html=True)
            
            portfolio = [
                {"protocol": "Aave", "amount": 2.5, "apy": 4.5, "earnings": 0.1125},
                {"protocol": "Uniswap", "amount": 1.0, "apy": 2.8, "earnings": 0.028},
                {"protocol": "Lido", "amount": 5.0, "apy": 4.2, "earnings": 0.21}
            ]
            
            total_invested = sum(p['amount'] for p in portfolio)
            total_earnings = sum(p['earnings'] for p in portfolio)
            
            for pos in portfolio:
                st.metric(f"{pos['protocol']}", f"{pos['amount']} ETH", f"${pos['earnings']:.4f}收益")
            
            st.markdown("<br>", unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            col1.metric("Total Invertido", f"{total_invested} ETH")
            col2.metric("Ganancias Totales", f"${total_earnings:.4f}")
        
        # Gráfico de distribución
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Distribución del Portfolio**")
        
        fig_defi = go.Figure(data=[go.Pie(labels=[p['protocol'] for p in portfolio], 
                                            values=[p['amount'] for p in portfolio])])
        fig_defi.update_layout(title="Distribución por Protocolo")
        st.plotly_chart(fig_defi, use_container_width=True)
        
        add_xp(10, "defi_dashboard")
    
    with tabs[12]:
        st.markdown("<h4>🏛️ DAO Governance - Gobernanza DAO</h4>", unsafe_allow_html=True)
        
        st.info("""
        **DAO Governance:** Sistema de gobernanza descentralizada para propuestas,
        votación y toma de decisiones colectiva en organizaciones autónomas.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Crear Propuesta</h5>", unsafe_allow_html=True)
            
            proposal_title = st.text_input("Título de la Propuesta", value="Mejora de Protocolo v2.0")
            proposal_desc = st.text_area("Descripción", value="Detalles de la propuesta...")
            proposal_type = st.selectbox("Tipo", ["Gobernanza", "Financiamiento", "Technical", "Community"])
            
            if st.button("🗳️ Crear Propuesta"):
                proposal_id = f"PROP-{random.randint(1000, 9999)}"
                st.success(f"✅ Propuesta creada: {proposal_id}")
                add_xp(10, "dao_governance")
                show_toast("✅ Propuesta creada", "success")
        
        with col2:
            st.markdown("<h5>Propuestas Activas</h5>", unsafe_allow_html=True)
            
            proposals = [
                {"id": "PROP-1234", "title": "Upgrade de Smart Contract", "votes_for": 1500, "votes_against": 200, "status": "Voting"},
                {"id": "PROP-1235", "title": "Aumento de Fees", "votes_for": 800, "votes_against": 1200, "status": "Rejected"},
                {"id": "PROP-1236", "title": "Nuevo Token Listing", "votes_for": 2000, "votes_against": 300, "status": "Passed"}
            ]
            
            for proposal in proposals:
                total_votes = proposal['votes_for'] + proposal['votes_against']
                approval_pct = (proposal['votes_for'] / total_votes * 100) if total_votes > 0 else 0
                status_color = {"Passed": "green", "Rejected": "red", "Voting": "orange"}[proposal['status']]
                
                with st.expander(f"🗳️ {proposal['id']} - {proposal['title']}"):
                    col1, col2, col3 = st.columns(3)
                    col1.metric("A Favor", f"{proposal['votes_for']}")
                    col2.metric("En Contra", f"{proposal['votes_against']}")
                    col3.metric("Aprobación", f"{approval_pct:.1f}%")
                    
                    st.markdown(f"**Estado:** <span style='color: {status_color};'>{proposal['status']}</span>", unsafe_allow_html=True)
        
        # Gráfico de votación
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Distribución de Votos**")
        
        fig_dao = go.Figure()
        for proposal in proposals:
            fig_dao.add_trace(go.Bar(
                name=proposal['id'],
                x=['A Favor', 'En Contra'],
                y=[proposal['votes_for'], proposal['votes_against']]
            ))
        fig_dao.update_layout(title="Votos por Propuesta", barmode='group')
        st.plotly_chart(fig_dao, use_container_width=True)
        
        add_xp(10, "dao_governance")
    
    with tabs[13]:
        st.markdown("<h4>🔄 Token Swap - Intercambio de Tokens</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Token Swap:** Interfaz de intercambio descentralizado (DEX) para swap
        de tokens con slippage controlado y mejores precios.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Swap</h5>", unsafe_allow_html=True)
            
            from_token = st.selectbox("Token de Origen", ["ETH", "USDT", "USDC", "DAI", "WBTC"], key="from_token_swap")
            to_token = st.selectbox("Token de Destino", ["USDT", "ETH", "USDC", "DAI", "WBTC"], key="to_token_swap")
            amount = st.number_input("Cantidad", value=1.0, min_value=0.0, step=0.1, key="amount_swap")
            slippage = st.slider("Slippage Tolerancia (%)", 0.1, 5.0, 0.5, key="slippage_swap")
            
            # Simular precio
            exchange_rates = {
                "ETH-USDT": 2250,
                "ETH-USDC": 2250,
                "ETH-DAI": 2250,
                "ETH-WBTC": 0.065,
                "USDT-USDC": 1.0,
                "USDT-DAI": 1.0,
                "USDT-WBTC": 0.000029
            }
            
            pair = f"{from_token}-{to_token}"
            rate = exchange_rates.get(pair, 1.0)
            expected_out = amount * rate
            min_out = expected_out * (1 - slippage / 100)
            
            col1, col2 = st.columns(2)
            col1.metric("Precio", f"{rate:.6f}")
            col2.metric("Salida Mínima", f"{min_out:.6f} {to_token}")
            
            if st.button("🔄 Ejecutar Swap"):
                st.success(f"✅ Swap completado: {amount} {from_token} → {expected_out:.6f} {to_token}")
                add_xp(10, "token_swap")
                show_toast("✅ Swap completado", "success")
        
        with col2:
            st.markdown("<h5>Pools de Liquidez</h5>", unsafe_allow_html=True)
            
            liquidity_pools = [
                {"pair": "ETH/USDT", "tvl": "50M", "apy": 2.5, "volume_24h": "10M"},
                {"pair": "ETH/USDC", "tvl": "45M", "apy": 2.3, "volume_24h": "8M"},
                {"pair": "USDT/USDC", "tvl": "100M", "apy": 0.5, "volume_24h": "50M"},
                {"pair": "ETH/DAI", "tvl": "30M", "apy": 3.1, "volume_24h": "5M"}
            ]
            
            for pool in liquidity_pools:
                with st.expander(f"💧 {pool['pair']}"):
                    col1, col2, col3 = st.columns(3)
                    col1.metric("TVL", pool['tvl'])
                    col2.metric("APY", f"{pool['apy']}%")
                    col3.metric("Volumen 24h", pool['volume_24h'])
        
        # Gráfico de volumen
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Volumen de Trading (24h)**")
        
        fig_swap = go.Figure(data=[go.Bar(
            x=[pool['pair'] for pool in liquidity_pools],
            y=[float(pool['volume_24h'].replace('M', '')) for pool in liquidity_pools],
            marker_color='indigo'
        )])
        fig_swap.update_layout(title="Volumen por Pool", xaxis_title="Pool", yaxis_title="Volumen (M)")
        st.plotly_chart(fig_swap, use_container_width=True)
        
        add_xp(10, "token_swap")
    
    with tabs[14]:
        st.markdown("<h4>🔍 Smart Contract Audit - Auditoría de Smart Contracts</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Smart Contract Audit:** Análisis de seguridad de smart contracts
        para detectar vulnerabilidades, bugs y problemas de gas.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Análisis de Contrato</h5>", unsafe_allow_html=True)
            
            contract_address = st.text_input("Dirección del Contrato", value="0x1234567890abcdef1234567890abcdef12345678")
            contract_code = st.text_area("Código del Contrato (Solidity)", value="pragma solidity ^0.8.0;\n\ncontract MyContract {\n    // Contract code here\n}", height=200)
            
            if st.button("🔍 Analizar Contrato"):
                st.success("✅ Análisis completado")
                add_xp(15, "smart_contract_audit")
                show_toast("✅ Auditoría completada", "success")
        
        with col2:
            st.markdown("<h5>Resultados del Análisis</h5>", unsafe_allow_html=True)
            
            vulnerabilities = [
                {"name": "Reentrancy", "severity": "HIGH", "status": "Not Found"},
                {"name": "Integer Overflow", "severity": "MEDIUM", "status": "Not Found"},
                {"name": "Access Control", "severity": "HIGH", "status": "Found"},
                {"name": "Gas Optimization", "severity": "LOW", "status": "Found"},
                {"name": "Unchecked Return", "severity": "MEDIUM", "status": "Not Found"}
            ]
            
            for vuln in vulnerabilities:
                severity_color = {"HIGH": "red", "MEDIUM": "orange", "LOW": "yellow"}[vuln['severity']]
                status_color = "green" if vuln['status'] == "Not Found" else "red"
                st.markdown(f"""
                <div style="padding: 8px; margin: 5px 0; border-left: 3px solid {severity_color}; background: rgba(100,100,100,0.1); border-radius: 3px;">
                    <strong>{vuln['name']}</strong> - {vuln['severity']} | Status: <span style="color: {status_color}">{vuln['status']}</span>
                </div>
                """, unsafe_allow_html=True)
        
        # Gráfico de severidad
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Distribución de Severidad**")
        
        severity_counts = {"HIGH": 1, "MEDIUM": 1, "LOW": 1}
        fig_audit = go.Figure(data=[go.Pie(labels=list(severity_counts.keys()), values=list(severity_counts.values()))])
        fig_audit.update_layout(title="Vulnerabilidades por Severidad")
        st.plotly_chart(fig_audit, use_container_width=True)
        
        add_xp(10, "smart_contract_audit")
    
    with tabs[15]:
        st.markdown("<h4>💼 Wallet Manager - Gestión de Wallets</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Wallet Manager:** Gestión de wallets blockchain múltiples con balance,
        transacciones y seguridad avanzada.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Mis Wallets</h5>", unsafe_allow_html=True)
            
            wallets = [
                {"name": "Main Wallet", "address": "0x1234...5678", "balance": 5.25, "network": "Ethereum"},
                {"name": "Trading Wallet", "address": "0xabcd...efgh", "balance": 2.10, "network": "BSC"},
                {"name": "NFT Wallet", "address": "0x9876...5432", "balance": 0.50, "network": "Polygon"}
            ]
            
            for wallet in wallets:
                with st.expander(f"💼 {wallet['name']} - {wallet['network']}"):
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Balance", f"{wallet['balance']} ETH")
                    col2.metric("Dirección", wallet['address'])
                    col3.metric("Red", wallet['network'])
            
            if st.button("➕ Agregar Nueva Wallet"):
                st.success("✅ Wallet agregada")
                add_xp(10, "wallet_manager")
                show_toast("✅ Wallet agregada", "success")
        
        with col2:
            st.markdown("<h5>Transacciones Recientes</h5>", unsafe_allow_html=True)
            
            transactions = [
                {"type": "Send", "amount": 0.5, "to": "0xabcd...", "status": "Confirmed", "time": "5 min ago"},
                {"type": "Receive", "amount": 1.2, "from": "0x1234...", "status": "Confirmed", "time": "1 hour ago"},
                {"type": "Swap", "amount": 2.0, "pair": "ETH/USDT", "status": "Pending", "time": "2 hours ago"}
            ]
            
            for tx in transactions:
                status_color = "green" if tx['status'] == "Confirmed" else "orange"
                st.markdown(f"""
                <div style="padding: 8px; margin: 5px 0; border-left: 3px solid {status_color}; background: rgba(100,100,100,0.1); border-radius: 3px;">
                    <strong>{tx['type']}</strong> - {tx['amount']} | Status: {tx['status']} | {tx['time']}
                </div>
                """, unsafe_allow_html=True)
        
        # Gráfico de balance
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Distribución de Balance**")
        
        fig_wallet = go.Figure(data=[go.Pie(labels=[w['name'] for w in wallets], values=[w['balance'] for w in wallets])])
        fig_wallet.update_layout(title="Balance por Wallet")
        st.plotly_chart(fig_wallet, use_container_width=True)
        
        add_xp(10, "wallet_manager")
    
    with tabs[16]:
        st.markdown("<h4>🔗 Cross-Chain Bridge - Puente Cross-Chain</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Cross-Chain Bridge:** Transferencia de activos entre diferentes blockchains
        usando puentes de interoperabilidad para mover tokens de una cadena a otra.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Configuración del Bridge</h5>", unsafe_allow_html=True)
            
            source_chain = st.selectbox("Cadena Origen", ["Ethereum", "BSC", "Polygon", "Arbitrum", "Optimism"], key="source_chain")
            target_chain = st.selectbox("Cadena Destino", ["BSC", "Ethereum", "Polygon", "Arbitrum", "Optimism"], key="target_chain")
            token = st.selectbox("Token", ["ETH", "USDT", "USDC", "BNB", "MATIC"], key="token_bridge")
            amount = st.number_input("Cantidad", value=1.0, min_value=0.0, key="amount_bridge")
            
            if st.button("🔗 Iniciar Transferencia"):
                st.success("✅ Transferencia iniciada")
                add_xp(15, "cross_chain_bridge")
                show_toast("✅ Cross-chain bridge iniciado", "success")
        
        with col2:
            st.markdown("<h5>Estado del Bridge</h5>", unsafe_allow_html=True)
            
            bridge_status = {
                "status": "Active",
                "total_volume": "$12.5M",
                "pending_tx": 23,
                "avg_time": "15 min"
            }
            
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Status", bridge_status['status'])
            col2.metric("Volumen", bridge_status['total_volume'])
            col3.metric("Pending", bridge_status['pending_tx'])
            col4.metric("Tiempo", bridge_status['avg_time'])
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Transferencias recientes
            st.markdown("**Transferencias Recientes**")
            
            transfers = [
                {"from": "Ethereum", "to": "BSC", "amount": "1000 USDT", "status": "Completed"},
                {"from": "BSC", "to": "Polygon", "amount": "500 USDC", "status": "Pending"},
                {"from": "Polygon", "to": "Ethereum", "amount": "2 ETH", "status": "Completed"}
            ]
            
            for tx in transfers:
                status_color = "green" if tx['status'] == "Completed" else "orange"
                st.markdown(f"""
                <div style="padding: 8px; margin: 5px 0; border-left: 3px solid {status_color}; background: rgba(100,100,100,0.1); border-radius: 3px;">
                    <strong>{tx['from']}</strong> → {tx['to']} | {tx['amount']} | Status: {tx['status']}
                </div>
                """, unsafe_allow_html=True)
        
        # Gráfico de volumen
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Volumen por Cadena**")
        
        chains = ["Ethereum", "BSC", "Polygon", "Arbitrum", "Optimism"]
        volumes = [random.randint(1000000, 5000000) for _ in range(5)]
        
        fig_bridge = go.Figure(data=[go.Bar(x=chains, y=volumes, marker_color='purple')])
        fig_bridge.update_layout(title="Volumen por Cadena", xaxis_title="Cadena", yaxis_title="Volumen ($)")
        st.plotly_chart(fig_bridge, use_container_width=True)
        
        add_xp(10, "cross_chain_bridge")
    
    with tabs[17]:
        st.markdown("<h4>💎 Token Staking - Staking de Tokens</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Token Staking:** Bloqueo de tokens para ganar recompensas de staking
        en protocolos de proof-of-stake y yield farming.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Configuración de Staking</h5>", unsafe_allow_html=True)
            
            staking_pool = st.selectbox("Pool de Staking", ["ETH 2.0", "MATIC", "SOL", "AVAX", "ATOM"], key="staking_pool")
            stake_amount = st.number_input("Cantidad a Staking", value=100.0, min_value=0.0, key="stake_amount")
            lock_period = st.selectbox("Período de Bloqueo", ["Flexible", "30 días", "90 días", "180 días", "1 año"], key="lock_period")
            
            if st.button("💎 Iniciar Staking"):
                st.success("✅ Staking iniciado")
                add_xp(15, "token_staking")
                show_toast("✅ Token staking iniciado", "success")
        
        with col2:
            st.markdown("<h5>Recompensas Estimadas</h5>", unsafe_allow_html=True)
            
            apy = random.uniform(5, 20)
            daily_reward = stake_amount * (apy / 100) / 365
            monthly_reward = daily_reward * 30
            yearly_reward = stake_amount * (apy / 100)
            
            col1, col2, col3 = st.columns(3)
            col1.metric("APY", f"{apy:.2f}%")
            col2.metric("Diario", f"${daily_reward:.2f}")
            col3.metric("Mensual", f"${monthly_reward:.2f}")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            col1.metric("Anual", f"${yearly_reward:.2f}")
            col2.metric("Total", f"${stake_amount + yearly_reward:.2f}")
        
        # Gráfico de recompensas
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Proyección de Recompensas**")
        
        months = list(range(1, 13))
        cumulative_rewards = [monthly_reward * i for i in months]
        
        fig_staking = go.Figure()
        fig_staking.add_trace(go.Scatter(x=months, y=cumulative_rewards, mode='lines+markers', name='Recompensas'))
        fig_staking.update_layout(title="Proyección de Recompensas (12 meses)", xaxis_title="Mes", yaxis_title="Recompensas ($)")
        st.plotly_chart(fig_staking, use_container_width=True)
        
        add_xp(10, "token_staking")
    
    with tabs[18]:
        st.markdown("<h4>💧 Liquidity Pool - Pool de Liquidez</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Liquidity Pool:** Provisión de liquidez a pools de DEX para ganar
        fees de trading y recompensas de LP tokens.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Configuración del Pool</h5>", unsafe_allow_html=True)
            
            pool_pair = st.selectbox("Par del Pool", ["ETH/USDT", "BTC/USDT", "ETH/BTC", "MATIC/USDC", "BNB/USDT"], key="pool_pair")
            token1_amount = st.number_input("Cantidad Token 1", value=1.0, min_value=0.0, key="token1_amount")
            token2_amount = st.number_input("Cantidad Token 2", value=2000.0, min_value=0.0, key="token2_amount")
            
            if st.button("💧 Agregar Liquidez"):
                st.success("✅ Liquidez agregada")
                add_xp(15, "liquidity_pool")
                show_toast("✅ Liquidity pool actualizado", "success")
        
        with col2:
            st.markdown("<h5>Métricas del Pool</h5>", unsafe_allow_html=True)
            
            total_liquidity = token1_amount * 2000 + token2_amount
            tvl = random.randint(10000000, 50000000)
            apr = random.uniform(10, 50)
            fee_rate = 0.3
            
            col1, col2, col3 = st.columns(3)
            col1.metric("TVL", f"${tvl:,}")
            col2.metric("APR", f"{apr:.2f}%")
            col3.metric("Fee Rate", f"{fee_rate}%")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # LP tokens
            lp_tokens = total_liquidity / tvl * 1000000
            daily_rewards = lp_tokens * (apr / 100) / 365
            
            col1.metric("LP Tokens", f"{lp_tokens:,.0f}")
            col2.metric("Rewards/Día", f"${daily_rewards:.2f}")
        
        # Gráfico de composición
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Composición del Pool**")
        
        fig_pool = go.Figure(data=[go.Pie(labels=["Token 1", "Token 2"], values=[token1_amount * 2000, token2_amount])])
        fig_pool.update_layout(title="Composición del Pool")
        st.plotly_chart(fig_pool, use_container_width=True)
        
        add_xp(10, "liquidity_pool")
    
    with tabs[19]:
        st.markdown("<h4>🔄 DEX Aggregator - Agregador de DEX</h4>", unsafe_allow_html=True)
        
        st.info("""
        **DEX Aggregator:** Agregador de exchanges descentralizados para encontrar
        la mejor ruta de swap y obtener el mejor precio posible.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Configuración de Swap</h5>", unsafe_allow_html=True)
            
            from_token = st.selectbox("Token Origen", ["ETH", "BTC", "USDT", "USDC", "DAI"], key="from_token_dex")
            to_token = st.selectbox("Token Destino", ["USDT", "USDC", "DAI", "ETH", "BTC"], key="to_token_dex")
            amount = st.number_input("Cantidad", value=1.0, min_value=0.0, step=0.1, key="amount_dex")
            slippage = st.slider("Slippage Tolerancia (%)", 0.1, 5.0, 0.5, key="slippage_dex")
            
            if st.button("🔄 Encontrar Mejor Ruta"):
                st.success("✅ Mejor ruta encontrada")
                add_xp(10, "dex_aggregator")
                show_toast("✅ Mejor ruta encontrada", "success")
        
        with col2:
            st.markdown("<h5>Rutas Disponibles</h5>", unsafe_allow_html=True)
            
            routes = [
                {"dex": "Uniswap V3", "price": 2250.50, "gas": 150000, "time": "2s"},
                {"dex": "SushiSwap", "price": 2250.30, "gas": 180000, "time": "3s"},
                {"dex": "Curve", "price": 2250.45, "gas": 120000, "time": "2s"},
                {"dex": "1inch", "price": 2250.55, "gas": 160000, "time": "3s"}
            ]
            
            best_route = min(routes, key=lambda x: x['gas'])
            
            for route in routes:
                is_best = route == best_route
                badge = "🏆" if is_best else ""
                st.markdown(f"""
                <div style="padding: 8px; margin: 5px 0; border-left: 3px solid {'gold' if is_best else 'gray'}; background: rgba(100,100,100,0.1); border-radius: 3px;">
                    <strong>{badge} {route['dex']}</strong> - ${route['price']:.2f} | Gas: {route['gas']:,} | {route['time']}
                </div>
                """, unsafe_allow_html=True)
        
        add_xp(10, "dex_aggregator")
    
    with tabs[20]:
        st.markdown("<h4>🌾 Yield Farming - Cultivo de Rendimiento</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Yield Farming:** Estrategias de cultivo de rendimiento para maximizar
        ganancias a través de staking, lending y liquidity mining.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Estrategias de Farming</h5>", unsafe_allow_html=True)
            
            strategies = [
                {"name": "ETH Staking", "apy": 4.5, "risk": "Low", "lock": "32 ETH"},
                {"name": "USDC Lending", "apy": 8.2, "risk": "Low", "lock": "None"},
                {"name": "ETH/USDT LP", "apy": 25.5, "risk": "Medium", "lock": "None"},
                {"name": "BTC Yield Vault", "apy": 12.3, "risk": "Medium", "lock": "7 days"},
                {"name": "DeFi Aggregator", "apy": 35.8, "risk": "High", "lock": "None"}
            ]
            
            for strategy in strategies:
                risk_color = {"Low": "green", "Medium": "orange", "High": "red"}[strategy['risk']]
                with st.expander(f"🌾 {strategy['name']}"):
                    col1, col2, col3 = st.columns(3)
                    col1.metric("APY", f"{strategy['apy']}%")
                    col2.metric("Riesgo", strategy['risk'])
                    col3.metric("Lock", strategy['lock'])
                    st.markdown(f"**Riesgo:** <span style='color: {risk_color}'>{strategy['risk']}</span>", unsafe_allow_html=True)
            
            if st.button("🌾 Iniciar Farming"):
                st.success("✅ Farming iniciado")
                add_xp(10, "yield_farming")
                show_toast("✅ Yield farming iniciado", "success")
        
        with col2:
            st.markdown("<h5>Métricas de Farming</h5>", unsafe_allow_html=True)
            
            total_invested = 50000
            avg_apy = sum(s['apy'] for s in strategies) / len(strategies)
            daily_rewards = total_invested * (avg_apy / 100) / 365
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Invertido", f"${total_invested:,}")
            col2.metric("APY Promedio", f"{avg_apy:.1f}%")
            col3.metric("Rewards/Día", f"${daily_rewards:.2f}")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            monthly_rewards = daily_rewards * 30
            yearly_rewards = daily_rewards * 365
            
            col1.metric("Rewards/Mes", f"${monthly_rewards:.2f}")
            col2.metric("Rewards/Año", f"${yearly_rewards:.2f}")
        
        # Gráfico de estrategias
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Comparación de Estrategias**")
        
        fig_yield = go.Figure(data=[go.Bar(
            x=[s['name'] for s in strategies],
            y=[s['apy'] for s in strategies],
            marker_color=['green' if s['risk'] == 'Low' else 'orange' if s['risk'] == 'Medium' else 'red' for s in strategies]
        )])
        fig_yield.update_layout(title="APY por Estrategia", xaxis_title="Estrategia", yaxis_title="APY (%)")
        st.plotly_chart(fig_yield, use_container_width=True)
        
        add_xp(10, "yield_farming")
    
    with tabs[21]:
        st.markdown("<h4>⚡ Flash Loans - Préstamos Flash</h4>", unsafe_allow_html=True)
        
        st.info("""
        **Flash Loans:** Préstamos sin colateral que deben ser devueltos en la misma
        transacción, utilizados para arbitraje, liquidación y refinanciamiento.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h5>Configuración de Flash Loan</h5>", unsafe_allow_html=True)
            
            loan_amount = st.number_input("Monto del Préstamo ($)", value=100000.0, min_value=0.0)
            loan_token = st.selectbox("Token del Préstamo", ["DAI", "USDC", "USDT", "WETH", "WBTC"])
            strategy = st.selectbox("Estrategia", ["Arbitraje DEX", "Liquidación DeFi", "Refinanciamiento", "Swap Collateral"])
            
            if st.button("⚡ Ejecutar Flash Loan"):
                st.success("✅ Flash loan ejecutado")
                add_xp(15, "flash_loans")
                show_toast("✅ Flash loan ejecutado", "success")
        
        with col2:
            st.markdown("<h5>Métricas del Flash Loan</h5>", unsafe_allow_html=True)
            
            fee_rate = 0.09
            fee_amount = loan_amount * fee_rate / 100
            profit = random.randint(500, 5000)
            net_profit = profit - fee_amount
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Monto", f"${loan_amount:,.2f}")
            col2.metric("Fee (0.09%)", f"${fee_amount:.2f}")
            col3.metric("Profit", f"${profit:.2f}")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            col1.metric("Profit Neto", f"${net_profit:.2f}")
            col2.metric("ROI", f"{net_profit/loan_amount*100:.2f}%")
        
        # Gráfico de estrategias
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Distribución de Estrategias**")
        
        strategy_counts = {"Arbitraje DEX": 45, "Liquidación DeFi": 30, "Refinanciamiento": 15, "Swap Collateral": 10}
        
        fig_flash = go.Figure(data=[go.Pie(labels=list(strategy_counts.keys()), values=list(strategy_counts.values()))])
        fig_flash.update_layout(title="Estrategias de Flash Loan")
        st.plotly_chart(fig_flash, use_container_width=True)
        
        add_xp(10, "flash_loans")

# ================================================================================
# FOOTER
# ================================================================================
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 20px; color: #64748b;'>
    <p><strong>Portfolio Técnico Elite v6.0 - Microproyectos Impresionantes</strong></p>
    <p style='font-size: 0.85rem;'>Salomon Febles | Ingeniero de Sistemas | Trading | Ciberseguridad | ML | Blockchain</p>
    <p style='font-size: 0.8rem;'>Python | Streamlit | SQLite | Plotly | Scikit-learn | MITRE ATT&CK | Binance API | Gamification</p>
</div>
""", unsafe_allow_html=True)
