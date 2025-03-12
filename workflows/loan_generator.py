import streamlit as st
import random
from datetime import datetime

def display_loan_agreement_generator():
    """
    The Loan Agreement / Transaction Capture Form workflow.
    """
    st.subheader("Loan Agreement / Transaction Capture Form")

    # Example project names (could come from st.session_state.projects)
    project_names = ["None / No Project", "Athens", "Sparta", "Hades", "Olympus", "Troy", "Apollo"]
    selected_project = st.selectbox("Select a Project", project_names, index=0)

    if selected_project != "None / No Project":
        st.info(f"Using project: {selected_project}")
        auto_populate = st.checkbox("Auto-populate form based on project data", value=True)
    else:
        auto_populate = False

    # Example data for pre-populating form fields
    project_data = {
        "Athens": {
            "transaction_name": "Athens Renewable Energy Financing",
            "borrower": "Athens Green Power Ltd.",
            "borrower_type": "Corporate",
            "transaction_type": "Term Loan",
            "currency": "EUR",
            "amount": "350,000,000",
            "term": "7 years",
            "purpose": "Financing construction of solar power facilities in southern Greece",
            "facility_agent": "RMB Bank",
            "security_package": "First ranking security over project assets and shares",
            "guarantors": "Athens Holdings and all material subsidiaries",
            "governing_law": "English Law",
            "interest_rate": "EURIBOR + 2.75%",
            "interest_period": "3 months",
            "upfront_fee": "1.25%",
            "commitment_fee": "35% of applicable margin",
            "financial_covenants": "Leverage ratio ≤4.0x, Interest cover ≥3.0x",
        },
        "Sparta": {
            "transaction_name": "Sparta Manufacturing Expansion",
            "borrower": "Laconia Fitness Group",
            "borrower_type": "Corporate",
            "transaction_type": "Term Loan",
            "currency": "EUR",
            "amount": "85,000,000",
            "term": "7 years",
            "purpose": "Manufacturing capacity expansion and acquisition of complementary product lines",
            "facility_agent": "Deutsche Bank",
            "security_package": "First ranking security over manufacturing assets, IP rights, and share pledge",
            "guarantors": "Laconia Holdings and operating subsidiaries",
            "governing_law": "German Law",
            "interest_rate": "EURIBOR + 2.85%",
            "interest_period": "3 months",
            "upfront_fee": "1.50%",
            "commitment_fee": "40% of applicable margin",
            "financial_covenants": "Leverage ratio ≤3.5x, DSCR ≥1.25x",
        },
        "Hades": {
            "transaction_name": "Hades Mineral Extraction Project",
            "borrower": "Underworld Mining Ltd.",
            "borrower_type": "Corporate",
            "transaction_type": "Project Finance",
            "currency": "GBP",
            "amount": "220,000,000",
            "term": "15 years",
            "purpose": "Development of rare earth minerals extraction facility with advanced environmental safeguards",
            "facility_agent": "Barclays",
            "security_package": "Comprehensive security over mining rights, processing facilities, and offtake contracts",
            "guarantors": "Parent company completion guarantee during construction phase",
            "governing_law": "English Law",
            "interest_rate": "SONIA + 3.15%",
            "interest_period": "6 months",
            "upfront_fee": "2.00%",
            "commitment_fee": "45% of applicable margin",
            "financial_covenants": "DSCR ≥1.35x, LLCR ≥1.40x, Reserve tail ratio ≥25%",
        },
        "Olympus": {
            "transaction_name": "Olympus Renewable Energy Portfolio",
            "borrower": "Olympus Renewables S.A.",
            "borrower_type": "Corporate",
            "transaction_type": "Project Finance",
            "currency": "EUR",
            "amount": "235,000,000",
            "term": "15 years",
            "purpose": "Construction and operation of a 120MW renewable energy portfolio across multiple European markets",
            "facility_agent": "BNP Paribas",
            "security_package": "First ranking security over all project assets, shares, and contracts",
            "guarantors": "Parent company support until COD, then project assets only",
            "governing_law": "French Law",
            "interest_rate": "EURIBOR + 2.25% with 25bps step-down upon achieving COD",
            "interest_period": "6 months",
            "upfront_fee": "1.50%",
            "commitment_fee": "35% of applicable margin",
            "financial_covenants": "DSCR ≥1.20x, LLCR ≥1.25x, maximum leverage ratio of 75% during construction",
        },
        "Troy": {
            "transaction_name": "Troy Cybersecurity Acquisition",
            "borrower": "Trojan Shield Technologies",
            "borrower_type": "Corporate",
            "transaction_type": "Acquisition Financing",
            "currency": "USD",
            "amount": "125,000,000",
            "term": "6 years",
            "purpose": "Strategic acquisition of complementary cybersecurity service providers to expand service offerings",
            "facility_agent": "JP Morgan",
            "security_package": "Share pledge over acquired entities, floating charge over all assets",
            "guarantors": "All material group companies post-acquisition",
            "governing_law": "New York Law",
            "interest_rate": "SOFR + 3.50%",
            "interest_period": "3 months",
            "upfront_fee": "2.00%",
            "commitment_fee": "40% of applicable margin",
            "financial_covenants": "Leverage ratio ≤4.5x with step-down to 3.5x, Interest cover ≥2.5x",
        },
        "Apollo": {
            "transaction_name": "Apollo ESG-Linked RCF",
            "borrower": "Apollo Healthcare Sciences",
            "borrower_type": "Corporate",
            "transaction_type": "Revolving Credit Facility",
            "currency": "EUR",
            "amount": "200,000,000",
            "term": "5 years",
            "purpose": "R&D expansion and implementation of sustainable manufacturing practices with ESG performance incentives",
            "facility_agent": "Credit Suisse",
            "security_package": "Unsecured, negative pledge package",
            "guarantors": "Parent company and material operating subsidiaries",
            "governing_law": "Swiss Law",
            "interest_rate": "EURIBOR + 1.85% with 15bps ESG adjustment",
            "interest_period": "1, 3 or 6 months",
            "upfront_fee": "1.00%",
            "commitment_fee": "35% of applicable margin",
            "financial_covenants": "Net Debt/EBITDA ≤3.0x, EBITDA/Interest ≥4.0x, ESG targets to be reported quarterly",
        },
        # Add more if you like...
    }

    project_values = project_data.get(selected_project, {}) if auto_populate else {}

    with st.form("loan_form", clear_on_submit=False):
        st.subheader("1. Basic Transaction Information")
        cols = st.columns(2)
        with cols[0]:
            tx_id = st.text_input("Transaction ID", value="TX-" + datetime.now().strftime("%y%m%d-") + str(random.randint(1000, 9999)))
            tx_name = st.text_input("Transaction Name", value=project_values.get("transaction_name", ""))
            borrower = st.text_input("Borrower", value=project_values.get("borrower", ""))
            borrower_type = st.selectbox("Borrower Type",
                ["Corporate", "SPV", "Public Entity", "Public-Private Partnership", "Individual", "Other"],
                index=0
            )
        with cols[1]:
            tx_type = st.selectbox("Transaction Type",
                ["Term Loan", "Revolving Credit Facility", "Syndicated Loan", "Project Finance", "Acquisition Financing", "Bridge Loan", "Other"],
                index=0
            )
            currency = st.selectbox("Currency", ["USD", "EUR", "GBP", "JPY", "CHF", "ZAR", "Other"], index=1)
            amount = st.text_input("Amount", value=project_values.get("amount", ""))
            term = st.text_input("Term", value=project_values.get("term", ""))

        purpose = st.text_area("Purpose", value=project_values.get("purpose", ""), height=100)

        st.subheader("2. Key Parties")
        cols = st.columns(2)
        with cols[0]:
            facility_agent = st.text_input("Facility Agent", value=project_values.get("facility_agent", ""))
        with cols[1]:
            security_package = st.text_area("Security Package", value=project_values.get("security_package", ""), height=100)

        guarantors = st.text_area("Guarantors", value=project_values.get("guarantors", ""), height=100)
        governing_law = st.text_input("Governing Law", value=project_values.get("governing_law", ""))

        st.subheader("3. Financial Terms")
        cols = st.columns(2)
        with cols[0]:
            interest_rate = st.text_input("Interest Rate", value=project_values.get("interest_rate", ""))
            interest_period = st.text_input("Interest Period", value=project_values.get("interest_period", ""))
        with cols[1]:
            upfront_fee = st.text_input("Upfront Fee", value=project_values.get("upfront_fee", ""))
            commitment_fee = st.text_input("Commitment Fee", value=project_values.get("commitment_fee", ""))

        financial_covenants = st.text_area("Financial Covenants", value=project_values.get("financial_covenants", ""), height=100)

        st.subheader("4. Status and Classification")
        cols = st.columns(2)
        with cols[0]:
            form_capturer = st.text_input("Who captured the form?", "")
            rating_lgd = st.text_input("Rating and LGD", "")
            dealmakers = st.text_input("Name of Dealmakers responsible", "")
        with cols[1]:
            is_distressed = st.selectbox("Is the loan currently in distress?", ["No", "Yes", "Watch List"], index=0)
            in_apm_portfolio = st.selectbox("Is the loan in the APM portfolio?", ["Yes", "No"], index=0)
            selldown_reasons = st.text_input("Reasons for distribution/sell-down", "")
            business_unit = st.selectbox("Which Business Unit originated the loan?",
                ["DFS", "REIB", "Infrastructure", "Resources", "LevFin", "FOGS", "Principal Investments"],
                index=2
            )
            tx_mgmt_team = st.text_input("Which Transaction Management Team?", "")
            initial_lender = st.text_input("Name of Initial Lender", "")

        form_submitted = st.form_submit_button("Generate Agreement Summary")

    if form_submitted:
        summary = f"""# LOAN AGREEMENT SUMMARY

## TRANSACTION DETAILS
* **Transaction ID:** {tx_id}
* **Transaction Name:** {tx_name}
* **Borrower:** {borrower}
* **Borrower Type:** {borrower_type}
* **Transaction Type:** {tx_type}
* **Currency:** {currency}
* **Amount:** {amount}
* **Term:** {term}
* **Purpose:** {purpose}

## PARTIES & LEGAL
* **Facility Agent:** {facility_agent}
* **Guarantors:** {guarantors}
* **Security Package:** {security_package}
* **Governing Law:** {governing_law}

## FINANCIAL TERMS
* **Interest Rate:** {interest_rate}
* **Interest Period:** {interest_period}
* **Upfront Fee:** {upfront_fee}
* **Commitment Fee:** {commitment_fee}
* **Financial Covenants:** {financial_covenants}

## PROJECT REFERENCE
Project: {selected_project if selected_project != "None / No Project" else "No project assigned"}
Document generated: {datetime.now().strftime('%d %B %Y, %H:%M')}
Status: {is_distressed}
APM Portfolio: {in_apm_portfolio}
Selldown Reasons: {selldown_reasons}
"""

        st.success("Agreement summary generated successfully!")
        st.markdown(summary)
        st.download_button(
            "Download Summary",
            data=summary,
            file_name=f"Loan_Agreement_Summary_{tx_name.replace(' ', '_') if tx_name else 'Unnamed'}.md",
            mime="text/markdown"
        )

        # If you want to store it in st.session_state for later usage, do so here
        # if selected_project != "None / No Project":
        #     # st.session_state.projects[selected_project]["loan_summaries"] = ...
        #     pass
