# workflows/workflows_main.py

import streamlit as st
import utils.helpers

# Import each workflow's display function
from workflows.bond_analysis import show_bond_analysis_workflow
from workflows.loan_generator import display_loan_agreement_generator
from workflows.rcf_calculator import display_rcf_calculator

def display_workflows():
    """
    This is the main entry point for the "Workflows" page/tab.
    It shows the 3 workflow cards. Once the user picks one,
    we show the corresponding logic below.
    """
    st.title("Workflows")
    st.header("Recommended for You")

    col1, col2 = st.columns(2)

    with col1:
        # Loan Agreement Card
        st.markdown("""
        <div class="workflow-card">
            <h3>Loan Agreement Generator</h3>
            <p>Generate a customized loan agreement based on your inputs.</p>
            <div class="workflow-meta">Output • 2 steps</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("▶ Start Loan Generator", key="start_loan_gen"):
            st.session_state.current_workflow = "loan_generator"

        # Bond Analysis Card
        st.markdown("""
        <div class="workflow-card" style="margin-top: 2rem;">
            <h3>Bond Data Analysis</h3>
            <p>Upload & analyze bond data, focusing on interactive baseline plots.</p>
            <div class="workflow-meta">📊 Data & Charts • interactive steps</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("▶ Start Bond Analysis", key="start_bond_analysis"):
            st.session_state.current_workflow = "bond_analysis"

    with col2:
        # RCF Calculator Card
        st.markdown("""
        <div class="workflow-card">
            <h3>RCF-CLN Calculator</h3>
            <p>Calculate and analyze Revolving Credit Facility metrics.</p>
            <div class="workflow-meta">🔢 Calculation • 1 step</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("▶ Start RCF Calculator", key="start_rcf"):
            st.session_state.current_workflow = "rcf_calculator"

    # If the user selected a workflow, show it
    if st.session_state.get("current_workflow"):
        st.markdown("---")
        col_clear, _ = st.columns([1, 4])
        with col_clear:
            if st.button("← Back to Workflows", key="back_to_workflows"):
                st.session_state.current_workflow = None
                utils.helpers.safe_rerun()

        if st.session_state.current_workflow == "loan_generator":
            display_loan_agreement_generator()
        elif st.session_state.current_workflow == "bond_analysis":
            show_bond_analysis_workflow()
        elif st.session_state.current_workflow == "rcf_calculator":
            display_rcf_calculator()
