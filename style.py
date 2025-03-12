# style.py
import streamlit as st

def inject_css():
    all_css = """
    <style>
    /* --- Base Resets & Shared Elements --- */
    .stApp {
        background-color: white;
    }
    [data-testid="stSidebar"] {
        background-color: #17191e;
    }
    h1, h2, h3, h4, h5, h6, p, span, label, div, .stMarkdown {
        color: black !important;
    }
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] div, [data-testid="stSidebar"] a,
    [data-testid="stSidebar"] label {
        color: white !important;
    }
    .logo-text {
        color: white !important;
        font-size: 24px !important;
        font-weight: 400 !important;
        padding: 25px 20px !important;
        font-family: serif !important;
        border-bottom: 1px solid rgba(255,255,255,0.1) !important;
        margin-bottom: 10px !important;
    }

    /* --- Buttons: now gray, pill-shaped style --- */
    .stButton > button,
    button[kind="primary"],
    button[data-testid="stFormSubmitButton"] {
        background: linear-gradient(180deg, #e2e2e2, #c8c8c8) !important; /* Gray gradient */
        color: #333 !important;               /* Dark text */
        border: 1px solid #aaa !important;    /* Subtle border */
        border-radius: 15px !important;       /* Pill shape */
        font-size: 14px !important;
        font-weight: 600 !important;
        box-shadow: none !important;
        padding: 0.6rem 1rem !important;
        transition: background 0.2s ease !important;
        cursor: pointer;
    }
    .stButton > button:hover {
        background: linear-gradient(180deg, #d1d1d1, #b4b4b4) !important; /* Darker gray hover */
        color: #333 !important;
    }

    /* --- Assistant tab chat input --- */
    div[data-testid="stChatInputContainer"] textarea {
        background-color: #f8f8f8 !important;
        color: #333 !important;
        border: 1px solid #ccc !important;
    }
    div[data-testid="stButton"] > button {
        margin-top: 8px !important;
        margin-bottom: 0 !important;
    }

    /* --- Knowledge Base & Projects Filters in the Assistant Tab --- */
    .selection-card {
        background-color: white;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .kb-section, .projects-section {
        padding-left: 12px !important;
        border-left: 3px solid #3f8cff !important; /* Subtle accent bar */
        margin-bottom: 24px !important;
    }
    .section-header {
        font-size: 16px !important;
        font-weight: 600 !important;
        color: #333 !important;
        margin-bottom: 12px !important;
    }

    /* --- Multiselect boxes & tags --- */
    div[data-testid="stMultiSelect"] div,
    div[data-baseweb="select"] {
        background-color: #ffffff !important;
        color: #333 !important;
    }
    div[data-baseweb="tag"] {
        background-color: #f0f0f0 !important;
        color: #333 !important;
        border: 1px solid #3f8cff !important;
        border-radius: 12px !important;
        margin: 2px 5px 2px 0 !important;
        padding: 2px 8px !important;
        font-size: 13px !important;
    }
    div[data-baseweb="tag"] svg {
        color: #333 !important;
    }
    div[data-baseweb="menu"] {
        background-color: #fff !important;
        border: 1px solid #ccc !important;
    }
    div[data-baseweb="menu"] div[role="option"] {
        background-color: #fff !important;
        color: #333 !important;
    }
    div[data-baseweb="menu"] div[role="option"]:hover {
        background-color: #f0f6ff !important;
    }
    div[data-baseweb="menu"] div[aria-selected="true"] {
        background-color: #e0ecff !important;
    }

    /* --- Original Chat Bubbles (kept for reference; overridden below) --- */
    .user-bubble {
        display: flex;
        justify-content: flex-end;
        margin-bottom: 10px;
    }
    .user-bubble > div {
        background-color: #e6f7ff;
        padding: 10px 15px;
        border-radius: 15px 15px 0 15px;
        max-width: 80%;
        color: black;
    }
    .assistant-bubble {
        display: flex;
        margin-bottom: 10px;
    }
    .assistant-bubble > div {
        background-color: #f0f0f0;
        padding: 10px 15px;
        border-radius: 15px 15px 15px 0;
        max-width: 80%;
        color: black;
    }

    /* --- Enhanced Chat Container & Bubbles --- */
    .chat-container {
        background: linear-gradient(135deg, #ffffff, #f9f9f9);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        max-height: 60vh;
        overflow-y: auto;
        margin-bottom: 20px;
    }
    .user-bubble {
        display: flex;
        justify-content: flex-end;
        margin-bottom: 10px;
    }
    .user-bubble > div {
        background-color: #d0eaff;
        padding: 10px 15px;
        border-radius: 15px 15px 0 15px;
        max-width: 80%;
        color: black;
        margin: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .assistant-bubble {
        display: flex;
        margin-bottom: 10px;
    }
    .assistant-bubble > div {
        background-color: #f0f0f0;
        padding: 10px 15px;
        border-radius: 15px 15px 15px 0;
        max-width: 80%;
        color: black;
        margin: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .avatar {
        font-size: 24px;
        margin-right: 10px;
    }
    .user-avatar {
        order: 1;
    }
    .assistant-avatar {
        order: -1;
    }

    /* --- Workflow Card Styling --- */
    .workflow-card {
        background-color: #f7f7f7;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .workflow-card h3 {
        margin-top: 0;
        font-size: 18px;
        font-weight: 500;
        color: #333;
    }
    .workflow-card p {
        font-size: 14px;
        color: #666;
        margin-bottom: 10px;
    }
    .workflow-meta {
        font-size: 12px;
        color: #666;
        margin-top: 10px;
    }

    /* --- Project Card (Vault) --- */
    .project-card {
        background-color: #1e2025;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 15px;
        border: 1px solid #292d33;
        transition: all 0.2s ease;
        cursor: pointer;
    }
    .project-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        border-color: #3f8cff;
    }
    .project-card h3 {
        margin-top: 0;
        color: white !important;
        font-size: 18px;
        font-weight: 500;
    }
    .project-card p {
        color: #a0a0a0 !important;
        font-size: 14px;
        margin-bottom: 10px;
    }
    .project-date {
        color: #777 !important;
        font-size: 12px;
    }
    .project-stats {
        display: flex;
        justify-content: space-between;
        margin-top: 15px;
        border-top: 1px solid #333;
        padding-top: 10px;
    }
    .project-stat {
        color: #999 !important;
        font-size: 13px;
    }

    /* --- File Explorer / Vault Layout --- */
    .file-explorer {
        background-color: #1e2025;
        border-radius: 8px;
        padding: 5px;
        border: 1px solid #292d33;
        margin-top: 20px;
    }
    .breadcrumb {
        display: flex;
        align-items: center;
        padding: 5px 15px;
        background-color: #252830;
        border-radius: 4px;
        margin-bottom: 15px;
    }
    .breadcrumb-item {
        color: #999 !important;
        font-size: 14px;
    }
    .breadcrumb-separator {
        margin: 0 8px;
        color: #666 !important;
    }
    .action-bar {
        display: flex;
        gap: 10px;
        margin-bottom: 15px;
    }
    .search-box {
        flex-grow: 1;
        background-color: #252830;
        border: 1px solid #333;
        border-radius: 4px;
        padding: 6px 12px;
        color: white !important;
    }
    .folder {
        padding: 10px 15px;
        margin: 5px 0;
        border-radius: 4px;
        cursor: pointer;
        display: flex;
        align-items: center;
    }
    .folder:hover {
        background-color: #292d33;
    }
    .file {
        padding: 8px 15px 8px 35px;
        margin: 2px 0;
        border-radius: 4px;
        cursor: pointer;
        display: flex;
        align-items: center;
    }
    .file:hover {
        background-color: #292d33;
    }
    .file-icon {
        margin-right: 10px;
    }

    /* --- Summaries / AI output boxes --- */
    .summary-marker {
        display: none;
    }

    /* Vault area fix: ensure white text on dark background */
    .file-explorer,
    .file-explorer * {
        color: #fff !important;
    }
    
    /* Fix dark buttons with dark text - ensure white text on dark backgrounds */
    .stButton > button:contains("AI Summary"),
    button[kind="primary"][data-testid="baseButton-primary"] {
        color: #fff !important;
    }
    
    /* Style for dark background buttons */
    button[style*="background-color: rgb(30, 32, 37)"],
    button[style*="background-color: #1e2025"],
    .stButton > button[style*="background: rgb(30, 32, 37)"],
    .stButton > button[style*="background: #1e2025"] {
        color: #fff !important;
    }
    
    /* Make loan generator buttons and dark-themed elements readable */
    .loan-generator button,
    .loan-generator .stButton > button,
    [data-testid="stAppViewBlockContainer"] button[style*="background-color: #252830"] {
        color: #fff !important; 
    }
    
    /* Make form fields and selectboxes in Loan Generator visible */
    div[data-testid="stTextInput"] input,
    div[data-testid="stTextArea"] textarea,
    div[data-testid="stNumberInput"] input,
    div[data-testid="stSelectbox"] .css-1c2x0ld,
    div[data-testid="stSelectbox"] .css-1d391kg,
    div[data-testid="stSelectbox"] .css-1vbd788,
    div[data-testid="stSelectbox"] .css-1f6xf2k,
    div[data-testid="stSelectbox"] .css-14x0xsk {
        background-color: #fff !important;
        color: #000 !important;
    }

    /* Fix AI Summary buttons - specifically target the dark buttons shown in the vault */
    .stButton > button[data-testid="baseButton-secondary"] {
        color: white !important;
    }
    
    /* Fix for AI Summary buttons in file explorer */
    button:contains("AI Summary"),
    .file-explorer .stButton > button,
    .file-explorer [data-testid="baseButton-secondary"],
    [data-testid="stAppViewBlockContainer"] .stButton > button[style*="background-color: rgb(30, 32, 37)"],
    [data-testid="stAppViewBlockContainer"] .stButton > button[style*="background-color: #1e2025"] {
        color: white !important;
    }
    
    /* Target loan generator dark buttons specifically */
    .stButton > button[data-testid="baseButton-primary"],
    .stButton > button[style*="background-color: #252830"] {
        color: white !important;
    }

    /* Complete rewrite for AI Summary buttons */
    button,
    .stButton button {
        background-color: #e2e2e2 !important;
        color: #333333 !important;
        border: 1px solid #aaaaaa !important;
        border-radius: 15px !important;
    }
    
    /* Override specifically for dark-themed buttons */
    button[style*="background-color: rgb(19, 23, 32)"],
    button[style*="background-color: #131720"],
    button[style*="background-color: rgb(30, 32, 37)"],
    button[style*="background-color: #1e2025"] {
        background-color: #e2e2e2 !important;
        color: #333333 !important;
        border: 1px solid #aaaaaa !important;
        border-radius: 15px !important;
    }

    /* Fix Loan Generator dropdown menus - black on black issue */
    div[data-baseweb="select"] ul,
    div[data-baseweb="select"] ul li,
    div[data-baseweb="popover"] ul,
    div[data-baseweb="popover"] ul li,
    div[data-baseweb="menu"] ul,
    div[data-baseweb="menu"] ul li {
        background-color: white !important;
        color: #333 !important;
    }
    
    /* Style for dropdown options */
    div[role="listbox"] div[role="option"] {
        background-color: white !important;
        color: #333 !important;
    }
    
    /* Selected option in dropdown */
    div[role="listbox"] div[aria-selected="true"] {
        background-color: #e0ecff !important;
        color: #333 !important;
    }
    
    /* Hover state for options */
    div[role="listbox"] div[role="option"]:hover {
        background-color: #f0f6ff !important;
        color: #333 !important;
    }

    /* Fix for dropdown selectors themselves - the trigger elements */
    div[data-testid="stSelectbox"] > div[data-baseweb="select"] > div,
    [data-testid="stSelectbox"] [role="combobox"],
    select + div[data-baseweb="select"] div[aria-selected] {
        background-color: white !important;
        color: #333 !important;
        border: 1px solid #ccc !important;
    }
    
    /* Fix for the selected values that show in the dropdown trigger */
    [data-testid="stSelectbox"] [role="combobox"] span,
    [data-testid="stSelectbox"] div[data-baseweb="select"] div span,
    [data-testid="stSelectbox"] div[class*="valueContainer"] div {
        color: #333 !important;
    }
    
    /* Make all SVG icons in dropdowns visible */
    [data-testid="stSelectbox"] svg,
    div[data-baseweb="select"] svg {
        fill: #333 !important;
    }
    
    /* Fix for specific dark select boxes in the loan form */
    .element-container div[data-baseweb="select"] div {
        background-color: white !important;
        color: #333 !important;
    }

    /* Fix dark sidebar panel text in RCF Calculator */
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] h4,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] div.stTitle,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] .main-header,
    [data-testid="stSidebar"] .sidebar-content div,
    [data-testid="stSidebar"] .element-container {
        color: white !important;
    }
    
    /* Specifically target the RCF-CLN Inputs title and other similar headings */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div > div:first-child {
        color: white !important;
        font-weight: bold !important;
    }
    </style>
    """
    st.markdown(all_css, unsafe_allow_html=True)
