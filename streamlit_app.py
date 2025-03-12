# main.py
import streamlit as st
from streamlit_option_menu import option_menu

# Import your separate modules
import style
import introduction
import assistant
import vault
import workflows
from workflows.workflows_main import display_workflows
import data_utils
import openai_utils
import utils

def main():
    # Basic Streamlit config
    st.set_page_config(
        page_title="Donna",
        page_icon="🔎",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Inject your custom CSS
    style.inject_css()

    # Initialize session state variables
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "projects" not in st.session_state:
        st.session_state.projects = {}
    if "current_project" not in st.session_state:
        st.session_state.current_project = None
    if "selected_category" not in st.session_state:
        st.session_state.selected_category = "All"
    if "current_workflow" not in st.session_state:
        st.session_state.current_workflow = None
    if "current_vault_project" not in st.session_state:
        st.session_state.current_vault_project = None

    # If using OpenAI:
    openai_utils.setup_openai_api()  # loads st.secrets, etc.

    # Sidebar
    with st.sidebar:
        st.markdown('<div class="logo-text">Donna</div>', unsafe_allow_html=True)
        selected = option_menu(
            menu_title=None,
            options=["Introduction", "Assistant", "Vault", "Workflows"],
            icons=["house", "chat", "folder", "grid"],
            menu_icon=None,
            default_index=0,
            styles={
                "container": {"padding": "0", "background-color": "transparent"},
                "icon": {"color": "rgba(255, 255, 255, 0.7)", "font-size": "16px"},
                "nav-link": {
                    "font-size": "14px",
                    "text-align": "left",
                    "padding": "0.75rem 1.5rem",
                    "color": "rgba(255, 255, 255, 0.8)"
                },
                "nav-link-selected": {"background-color": "#2a2c32", "color": "white"},
            }
        )

    # Routing to each "page"
    if selected == "Introduction":
        introduction.display_introduction()
    elif selected == "Assistant":
        assistant.display_assistant()
    elif selected == "Vault":
        vault.display_vault()
    elif selected == "Workflows":
        workflows.workflows_main.display_workflows()

if __name__ == "__main__":
    main()
