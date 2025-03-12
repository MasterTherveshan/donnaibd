# vault.py
import streamlit as st
import time
import os
import utils.helpers
import openai_utils

def display_vault():
    """
    Displays the Document Vault page, including:
      - Project creation
      - Listing existing projects
      - Project detail view with file explorer
      - AI summary toggles
    """

    st.title("Document Vault")

    # Example project descriptions
    project_descriptions = {
        "Olympus": "Strategic financing for renewable energy portfolio expansion across Europe. Key focus on solar and wind assets.",
        "Hades": "Debt restructuring and refinancing for mining conglomerate facing liquidity challenges.",
        "Athens": "Project finance for infrastructure development including toll roads and municipal facilities.",
        "Sparta": "Leveraged buyout of defense technology firm with multiple tranches of debt.",
        "Troy": "Cross-border acquisition financing with complex FX considerations and regulatory approvals.",
        "Apollo": "Green bond issuance for sustainability-linked projects across multiple jurisdictions."
    }

    # Example creation dates
    project_dates = {
        "Olympus": "Created: 12 Mar 2023",
        "Hades": "Created: 05 Jun 2023",
        "Athens": "Created: 22 Jan 2023",
        "Sparta": "Created: 14 Apr 2023",
        "Troy": "Created: 30 Sep 2023",
        "Apollo": "Created: 08 Nov 2023"
    }

    # 1) Let user create a new project
    with st.expander("Create New Project"):
        col1, col2 = st.columns([3, 1])
        with col1:
            new_project = st.text_input("Project Name", key="new_project_input")
        with col2:
            if st.button("Create Project", use_container_width=True) and new_project:
                if new_project not in st.session_state.projects:
                    st.session_state.projects[new_project] = {
                        "files": [],
                        "created_at": time.strftime("%Y-%m-%d %H:%M"),
                        "description": "New project"
                    }
                    st.success(f"Created project: {new_project}")

    # 2) If user hasn't selected a project to view, show the "Recent Projects"
    if "current_vault_project" not in st.session_state:
        st.session_state.current_vault_project = None

    if not st.session_state.current_vault_project:
        st.subheader("Recent Projects")

        # Combine session-state projects with the example ones
        all_projects = list(project_descriptions.keys())
        for proj in st.session_state.projects:
            if proj not in all_projects:
                all_projects.append(proj)

        # Show them in a 2-col layout
        for i in range(0, len(all_projects), 2):
            cols = st.columns(2)
            for j in range(2):
                if i + j < len(all_projects):
                    proj = all_projects[i + j]
                    with cols[j]:
                        desc = project_descriptions.get(proj, "Project description not available")
                        date = project_dates.get(proj, "Created: Recently")
                        # Example file count
                        file_count = len(st.session_state.projects.get(proj, {}).get("files", [])) if proj in st.session_state.projects else 8
                        collab_count = 3 + (hash(proj) % 5)

                        # Create a clickable "card" using HTML
                        card_html = f"""
                        <div class="project-card" onclick="
                            var elements = window.parent.document.getElementsByTagName('button');
                            for (var i = 0; i < elements.length; i++) {{
                                if (elements[i].innerText.includes('View {proj}')) {{
                                    elements[i].click();
                                    break;
                                }}
                            }}">
                            <h3>{proj}</h3>
                            <p>{desc}</p>
                            <div class="project-date">{date}</div>
                            <div class="project-stats">
                                <div class="project-stat">📄 {file_count} files</div>
                                <div class="project-stat">👥 {collab_count} collaborators</div>
                            </div>
                        </div>
                        """
                        st.markdown(card_html, unsafe_allow_html=True)

                        # Hidden button that the JS snippet above can "click"
                        if st.button(f"View {proj}", key=f"view_{proj}"):
                            st.session_state.current_vault_project = proj
                            utils.helpers.safe_rerun()

    # 3) If user has selected a project, show the project detail view
    else:
        project = st.session_state.current_vault_project
        col1, col2 = st.columns([1, 6])
        with col1:
            if st.button("← Back to Projects"):
                st.session_state.current_vault_project = None
                utils.helpers.safe_rerun()

        with col2:
            st.subheader(project)

        # Show a short description
        desc = project_descriptions.get(project, "Project description not available")
        st.markdown(f"<p style='color:#a0a0a0;margin-bottom:20px;'>{desc}</p>", unsafe_allow_html=True)

        # Action bar
        col_a, col_b, col_c = st.columns([4, 1, 1])
        with col_a:
            st.markdown("<div class='search-box'>🔍 Search in this project...</div>", unsafe_allow_html=True)
        with col_b:
            st.button("New Folder", use_container_width=True)
        with col_c:
            upload_btn = st.button("Upload", use_container_width=True, type="primary")

        # Breadcrumb
        st.markdown(f"""
        <div class="breadcrumb">
            <span class="breadcrumb-item">Home</span>
            <span class="breadcrumb-separator">/</span>
            <span class="breadcrumb-item">Vault</span>
            <span class="breadcrumb-separator">/</span>
            <span class="breadcrumb-item" style="color:#3f8cff !important;">{project}</span>
        </div>
        """, unsafe_allow_html=True)

        # File explorer
        st.markdown("<div class='file-explorer'>", unsafe_allow_html=True)

        # Example folder/file structure
        # Adjust or load from session as needed
        folders = {
            "Documentation": ["Term Sheet.docx", "Credit Approval.pdf", "Board Presentation.pptx"],
            "Legal": ["Facility Agreement.pdf", "Security Documents.pdf", "Legal Opinion.docx"],
            "Models": ["Financial Model v1.xlsx", "Scenario Analysis.xlsx"],
            "Credit": ["Credit Memo.pdf", "Risk Assessment.docx"]
        }
        if project == "Olympus":
            folders["Renewable Assets"] = ["Wind Portfolio.xlsx", "Solar Valuation.pdf"]
        elif project == "Hades":
            folders["Restructuring"] = ["Debt Schedule.xlsx", "Creditor Presentation.pdf"]
        elif project == "Athens":
            folders["Infrastructure"] = ["Traffic Study.pdf", "Construction Timeline.xlsx"]
        elif project == "Sparta":
            folders["Due Diligence"] = ["Technical DD.pdf", "Commercial DD.pdf"]

        # Display each folder & 2 example files
        for folder, files in folders.items():
            st.markdown(f"""
            <div class="folder">
                <span class="folder-icon">📁</span> {folder}
            </div>
            """, unsafe_allow_html=True)

            for i, file in enumerate(files[:2]):
                date = f"{10 + i} {'Jan Feb Mar Apr May'.split()[i % 5]} 2023"
                file_icon = "📄"
                if file.endswith(".xlsx"):
                    file_icon = "📊"
                elif file.endswith(".pdf"):
                    file_icon = "📑"
                elif file.endswith(".pptx"):
                    file_icon = "📽️"

                file_key = f"{folder}_{file}".replace(" ", "_").replace(".", "_")
                cols = st.columns([12, 3, 5])
                with cols[0]:
                    st.markdown(f"""
                    <div style="display: flex; align-items: center;">
                        <span class="file-icon">{file_icon}</span> 
                        <span>{file}</span>
                    </div>
                    """, unsafe_allow_html=True)
                with cols[1]:
                    st.markdown(f"""
                    <div style="color: #777; font-size: 12px; text-align: right;">
                        {date}
                    </div>
                    """, unsafe_allow_html=True)
                with cols[2]:
                    ai_button = st.button("AI Summary", key=f"ai_{file_key}", help="Generate AI summary of this document")

                # State for toggling AI summary
                if f"show_{file_key}" not in st.session_state:
                    st.session_state[f"show_{file_key}"] = False

                if ai_button:
                    st.session_state[f"show_{file_key}"] = not st.session_state[f"show_{file_key}"]

                if st.session_state[f"show_{file_key}"]:
                    summary_content = openai_utils.generate_ai_summary(file, folder, project)
                    with st.container():
                        st.markdown(f'<div id="summary-{file_key}" class="summary-marker"></div>', unsafe_allow_html=True)
                        st.markdown(summary_content)

                    # CSS to style the summary container
                    st.markdown(f"""
                    <style>
                    .element-container:has(#summary-{file_key}) + .element-container {{
                        background-color: white;
                        border-left: 4px solid #3f8cff;
                        margin: 15px 0 25px 35px;
                        padding: 18px 20px;
                        border-radius: 6px;
                        box-shadow: 0 3px 10px rgba(0,0,0,0.08);
                    }}
                    .element-container:has(#summary-{file_key}) + .element-container div {{
                        background-color: transparent !important;
                        border: none !important;
                    }}
                    </style>
                    """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        # Upload new document
        if upload_btn:
            uploaded_files = st.file_uploader("Select files to upload", accept_multiple_files=True, key="vault_project_upload")
            if uploaded_files:
                for up_file in uploaded_files:
                    file_details = {
                        "name": up_file.name,
                        "type": up_file.type,
                        "size": up_file.size,
                        "uploaded_at": time.strftime("%Y-%m-%d %H:%M")
                    }
                    # Save to session
                    if project in st.session_state.projects:
                        st.session_state.projects[project]["files"].append(file_details)

                    st.success(f"Uploaded: {up_file.name}")
