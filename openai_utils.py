# openai_utils.py

import streamlit as st
import openai

def setup_openai_api():
    """
    Load your OpenAI API key from st.secrets or an environment variable.
    Adjust as needed if you store your key differently.
    """
    # If you store your key in the Streamlit secrets manager:
    openai.api_key = st.secrets.get("OPENAI_API_KEY", "")

    # Alternatively, if you store your key in an environment variable:
    # import os
    # openai.api_key = os.environ.get("OPENAI_API_KEY", "")
    #
    # You can remove or comment out whichever approach you don't need.


def generate_ai_summary(file, folder, project):
    """
    Generates custom AI summaries based on the file name and project.
    Each project has specialized summaries for common document types.
    """
    file_lower = file.lower()
    
    # Determine file type
    if "term sheet" in file_lower or "termsheet" in file_lower:
        return generate_term_sheet_summary(project)
    elif "credit approval" in file_lower or "credit assessment" in file_lower:
        return generate_credit_approval_summary(project)
    elif "facility agreement" in file_lower or "loan agreement" in file_lower:
        return generate_facility_agreement_summary(project)
    elif "financial model" in file_lower or "model.xlsx" in file_lower:
        return generate_financial_model_summary(project)
    elif "security" in file_lower or "collateral" in file_lower:
        return generate_security_package_summary(project)
    elif "due diligence" in file_lower or "duediligence" in file_lower:
        return generate_due_diligence_summary(project)
    elif "covenant" in file_lower or "compliance" in file_lower:
        return generate_covenant_summary(project)
    elif "presentation" in file_lower or ".ppt" in file_lower:
        return generate_presentation_summary(project)
    else:
        # Generic summary for unrecognized file types
        return f"""### AI Summary of {file}

This document from the {folder} folder in the {project} project appears to be a {file.split('.')[-1].upper()} file.

The document contains important information related to the {project} transaction. It should be reviewed in detail by the team.

Key elements likely include financial terms, legal provisions, or analytical data relevant to the {project} project.
"""


def generate_term_sheet_summary(project):
    """Generate a project-specific term sheet summary"""
    
    if project == "Athens":
        return """### Athens - Term Sheet Summary

This Term Sheet outlines preliminary terms for a €175M project financing facility for the Athens Urban Renewal mixed-use real estate development.

**Transaction Parties:**
- **Borrower:** Attica Development Consortium
- **Sponsors:** Athens Urban Ventures (60%), Municipal Development Fund (40%)
- **Arrangers:** Piraeus Bank, Alpha Bank, BNP Paribas
- **Facility Agent:** Piraeus Bank

**Key Financial Terms:**
- **Facility Amount:** €175,000,000
- **Tenor:** 12 years
- **Margin:** EURIBOR + 235bps, with step-down to 215bps after completion
- **Upfront Fee:** 125bps
- **Commitment Fee:** 30% of margin on undrawn amounts
- **Financial Covenants:** LTV ≤70%, DSCR ≥1.25x, LLCR ≥1.30x

**Project Specifics:**
- 320 residential units with 30% affordable housing component
- 15,000 sqm of commercial space with LEED certification target
- Phased development with completion milestones linked to drawdowns
"""
        
    elif project == "Sparta":
        return """### Sparta - Term Sheet Summary

This Term Sheet outlines terms for an €85M term loan to finance manufacturing expansion and acquisition of competitor brands for Laconia Fitness Group.

**Transaction Parties:**
- **Borrower:** Laconia Fitness Group
- **Guarantors:** All operating subsidiaries
- **Arrangers:** Deutsche Bank, Commerzbank
- **Facility Agent:** Deutsche Bank

**Key Financial Terms:**
- **Facility Amount:** €85,000,000
- **Tenor:** 7 years
- **Repayment:** 20% amortization during term, 80% bullet
- **Margin:** EURIBOR + 285bps, with leverage-based ratchet
- **Upfront Fee:** 150bps
- **Commitment Fee:** 40% of margin
- **Financial Covenants:** Leverage ≤3.5x, DSCR ≥1.25x

**Use of Proceeds:**
- €55M for production capacity expansion in Southern Europe
- €30M for acquisition of complementary product lines and IP
"""
        
    elif project == "Hades":
        return """### Hades - Term Sheet Summary

This Term Sheet outlines terms for a £220M project finance facility for the development of a rare earth minerals extraction and processing facility.

**Transaction Parties:**
- **Borrower:** Underworld Mining Ltd.
- **Sponsors:** Global Minerals Group (70%), Tech Metals Ventures (30%)
- **Arrangers:** Barclays, Standard Chartered, RBS
- **Facility Agent:** Barclays

**Key Financial Terms:**
- **Facility Amount:** £220,000,000
- **Tenor:** 15 years
- **Margin:** SONIA + 315bps, with completion step-down of 25bps
- **Upfront Fee:** 200bps
- **Commitment Fee:** 45% of margin
- **Financial Covenants:** DSCR ≥1.35x, LLCR ≥1.40x, Reserve tail ratio ≥25%

**Environmental Provisions:**
- Mandatory compliance with IFC Performance Standards
- Environmental bond of £50M during operational phase
- Quarterly reporting on water treatment system performance
"""
        
    elif project == "Olympus":
        return """### Olympus - Term Sheet Summary

This Term Sheet outlines preliminary terms and conditions for a €235M senior secured term loan facility for renewable energy portfolio expansion across Europe.

**Transaction Parties:**
- **Borrower:** Olympus Renewables S.A.
- **Guarantors:** All material subsidiaries (representing at least 85% of group EBITDA)
- **Arrangers:** BNP Paribas, Société Générale, Santander
- **Facility Agent:** BNP Paribas

**Key Financial Terms:**
- **Facility Amount:** €235,000,000
- **Tenor:** 15 years with sculpted repayment profile
- **Margin:** EURIBOR + 225bps, with 25bps step-down upon achieving COD
- **Upfront Fee:** 150bps
- **Commitment Fee:** 35% of margin on undrawn amounts
- **Financial Covenants:** DSCR ≥1.20x, LLCR ≥1.25x

**Portfolio Details:**
- 120MW combined capacity across solar (70MW) and wind (50MW) assets
- Sites in Spain (50%), Italy (30%), and Portugal (20%)
- Accordion feature allowing additional €100M for future acquisitions
"""
        
    elif project == "Troy":
        return """### Troy - Term Sheet Summary

This Term Sheet outlines terms for a US$125M acquisition financing package to support Trojan Shield's strategic expansion in cybersecurity services.

**Transaction Parties:**
- **Borrower:** Trojan Shield Technologies
- **Guarantors:** All acquired entities and material subsidiaries
- **Arrangers:** JP Morgan, Goldman Sachs, Morgan Stanley
- **Facility Agent:** JP Morgan

**Key Financial Terms:**
- **Facility Amount:** US$125,000,000
- **Tenor:** 6 years
- **Structure:** US$100M Term Loan, US$25M Revolving Credit Facility
- **Margin:** SOFR + 350bps, with leverage-based step-downs
- **Upfront Fee:** 200bps
- **Commitment Fee:** 40% of margin
- **Financial Covenants:** Leverage ≤4.5x with step-down to 3.5x, Interest cover ≥2.5x

**Acquisition Details:**
- Three target companies with specialized capabilities in defense, critical infrastructure, and financial services security
- Combined EBITDA multiple of 7.8x (6.2x with anticipated synergies)
- Equity contribution of 40% from sponsor
"""
        
    elif project == "Apollo":
        return """### Apollo - Term Sheet Summary

This Term Sheet outlines terms for a €200M ESG-linked revolving credit facility for Apollo Healthcare Sciences.

**Transaction Parties:**
- **Borrower:** Apollo Healthcare Sciences
- **Guarantors:** Parent company and material operating subsidiaries
- **Arrangers:** Credit Suisse, UBS, Deutsche Bank
- **Facility Agent:** Credit Suisse

**Key Financial Terms:**
- **Facility Amount:** €200,000,000
- **Tenor:** 5 years (4+1)
- **Margin:** EURIBOR + 185bps, with ±15bps ESG adjustment
- **Upfront Fee:** 100bps
- **Commitment Fee:** 35% of margin
- **Financial Covenants:** Net Debt/EBITDA ≤3.0x, EBITDA/Interest ≥4.0x

**ESG Framework:**
- Carbon reduction targets: 5% YoY reduction in Scope 1 & 2 emissions
- R&D investment: Minimum 15% of revenue in rare disease treatments
- Sustainability reporting: Quarterly KPI tracking and annual verification
- Margin benefit: -15bps for achieving all targets, +15bps for missing all targets
"""
    else:
        # Generic term sheet summary
        return f"""### {project} - Term Sheet Summary

This Term Sheet outlines preliminary terms and conditions for proposed financing related to the {project} project.

The document contains confidential information about facility amount, tenor, pricing, and key covenants. It is subject to final credit approval and documentation.

Review the full document for complete details about security package, conditions precedent, and other key provisions relevant to the transaction.
"""


def generate_credit_approval_summary(project):
    """Generate a project-specific credit approval summary"""
    
    if project == "Athens":
        return """### Athens - Credit Approval Summary

**Credit Committee Decision:** Approved with conditions  
**Risk Rating:** BB / Acceptable (3.5)  
**LGD:** 35%  
**Committee Date:** March 27, 2024

**Transaction Overview:**  
€175M project financing for mixed-use urban development with 320 residential units and commercial space in central Athens. Project includes sustainability features and affordable housing component.

**Key Risk Factors:**
- Construction completion risk for phased development
- Real estate market conditions in Athens CBD
- Regulatory changes affecting zoning or affordable housing requirements

**Mitigants:**
- Strong pre-sales (45% of residential units)
- Experienced developer with 5 successful similar projects
- Phased drawdown tied to completion milestones
- Independent technical advisor oversight

**Conditions for Approval:**
- Minimum pre-sales of 60% before second phase funding
- Cost overrun facility of €20M to be provided by sponsors
- Satisfactory environmental due diligence
"""
        
    elif project == "Sparta":
        # Add more project-specific credit approval summaries
        return """### Sparta - Credit Approval Summary

**Credit Committee Decision:** Approved  
**Risk Rating:** BB+ / Acceptable (3.0)  
**LGD:** 30%  
**Committee Date:** November 18, 2023

**Transaction Overview:**  
€85M term loan for manufacturing capacity expansion and acquisition of competitor brands for Laconia Fitness Group, a leading fitness equipment manufacturer in Southern Europe.

**Key Risk Factors:**
- Integration risk for acquired product lines
- Post-Covid fitness industry volatility
- Supply chain constraints for raw materials

**Mitigants:**
- Strong market position (25% market share in target countries)
- Demonstrated cash flow with 5-year CAGR of 18%
- Product diversification strategy reduces single product risk
- Secured offtake agreements with major gym chains

**Conditions for Approval:**
- Maximum leverage of 3.5x at closing
- Minimum liquidity reserve of €10M
- Completion of anti-trust clearance
"""
    
    # Add more project-specific summaries here...
    
    elif project == "Olympus":
        return """### Olympus - Credit Approval Summary

**Credit Committee Decision:** Approved with conditions  
**Risk Rating:** BB+ / Acceptable (3.0)  
**LGD:** 30%  
**Committee Date:** October 5, 2023

**Transaction Overview:**  
€235M senior debt for the construction and operation of a 120MW portfolio of solar and wind assets across Spain, Italy, and Portugal, with accordion feature for future acquisitions.

**Key Risk Factors:**
- Construction and completion risk across multiple sites
- Weather-related production variability
- Regulatory changes in renewable energy subsidies
- Interconnection delays

**Mitigants:**
- Geographical diversification across three countries
- 70% of expected production covered by long-term PPAs
- Experienced EPC contractors with strong track records
- Conservative P90 production assumptions for financial model
- Debt sizing based on 1.35x minimum DSCR

**Conditions for Approval:**
- Independent Engineer confirmation of technical assumptions
- Financial close for all sites within 9 months
- Minimum 25% equity contribution
- Full contingency funding in place
"""
    
    # Generic credit approval summary as fallback
    else:
        return f"""### {project} - Credit Approval Summary

**Credit Committee Decision:** [Decision]  
**Risk Rating:** [Rating]  
**LGD:** [Percentage]  
**Committee Date:** [Date]

**Transaction Overview:**  
This document summarizes the credit committee's assessment and decision regarding the {project} transaction.

The document contains a detailed analysis of the credit risks, financial projections, and key mitigating factors considered in the approval process.

Specific conditions attached to the approval are outlined along with required monitoring parameters for the duration of the facility.
"""


def generate_facility_agreement_summary(project):
    """Generate a project-specific facility agreement summary"""
    # Implement similar project-specific logic as above
    return f"""### {project} - Facility Agreement Summary

This document constitutes the legally binding facility agreement for the {project} transaction.

It contains the detailed terms and conditions, representations and warranties, covenants, events of default, and other legal provisions governing the loan facility.

Key sections include the precise definitions of financial covenants, conditions precedent to drawdown, mandatory prepayment events, and the mechanics for interest calculation and payment.
"""


def generate_financial_model_summary(project):
    """Generate a project-specific financial model summary"""
    # Implement similar project-specific logic
    return f"""### {project} - Financial Model Summary

This financial model presents the detailed projections for the {project} transaction over the full loan term.

**Key Model Outputs:**
- Base Case DSCR: [Value]
- Project IRR: [Value]
- Equity IRR: [Value]
- Payback Period: [Value]

The model includes sensitivity analyses for key variables including [variables], and stress tests for downside scenarios.

All assumptions are documented in the Assumptions tab, with sources and rationale provided.
"""


def generate_security_package_summary(project):
    """Generate a project-specific security package summary"""
    # Implement similar project-specific logic
    return f"""### {project} - Security Package Summary

This document details the comprehensive security package supporting the {project} transaction.

The security structure includes [key security elements] designed to provide appropriate protection to lenders while allowing operational flexibility for the borrower.

Key intercreditor arrangements and priority of payments are clearly defined, along with enforcement mechanisms and step-in rights.
"""


def generate_due_diligence_summary(project):
    """Generate a project-specific due diligence summary"""
    # Implement similar project-specific logic
    return f"""### {project} - Due Diligence Summary

This report presents the findings from comprehensive due diligence conducted on the {project} transaction.

**Areas Covered:**
- Financial Due Diligence
- Legal Due Diligence
- Technical Due Diligence
- Environmental & Social Due Diligence
- Insurance Review
- [Other relevant areas]

Key findings and recommendations are summarized in the Executive Summary, with detailed analyses available in the respective appendices.
"""


def generate_covenant_summary(project):
    """Generate a project-specific covenant summary"""
    # Implement similar project-specific logic
    return f"""### {project} - Covenant Compliance Summary

This document summarizes the covenant compliance status for the {project} transaction.

**Current Compliance Status:**
- Financial Covenants: [Status]
- Information Covenants: [Status]
- General Undertakings: [Status]

Detailed calculations for financial covenants are provided, along with relevant supporting documentation and certifications from the borrower.
"""


def generate_presentation_summary(project):
    """Generate a project-specific presentation summary"""
    # Implement similar project-specific logic
    return f"""### {project} - Presentation Summary

This presentation provides an overview of the {project} transaction for [intended audience].

Key sections include:
- Transaction Overview
- Market Context
- Financial Structure
- Risk Analysis
- Implementation Timeline

The materials are designed to [purpose of presentation], with supporting data and visualizations to illustrate the key points.
"""


def call_openai_chat_completion(prompt):
    """
    Example helper if you want to call the OpenAI ChatCompletion API.
    You can adapt this as needed in your app code.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error calling OpenAI: {str(e)}"
