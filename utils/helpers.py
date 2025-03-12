# utils/helpers.py

import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

def format_negatives(val):
    """Return '(x.xx)' for negative floats, or 'x.xx' if positive."""
    if isinstance(val, (int, float)):
        return f"({abs(val):,.2f})" if val < 0 else f"{val:,.2f}"
    return val

def display_table(df):
    """
    Formats and displays a DataFrame as an HTML table with styling
    (using html2canvas for screenshot).
    """
    # Convert numeric columns using format_negatives
    for col in df.columns:
        if col not in ["Item"]:  # e.g., skip a string column
            df[col] = df[col].apply(format_negatives)

    # Convert to HTML
    html_table = df.to_html(index=False, border=0, escape=False)

    # Add custom table class
    html_table = html_table.replace('class="dataframe"', 'class="rcf-table"')
    html_table = html_table.replace('<tr>', '<tr class="data-row">')
    html_table = html_table.replace('<tr class="data-row"><td><b>', '<tr class="section-header"><td><b>')

    # Minimal custom CSS for the table
    custom_css = """
    <style>
    .rcf-table {
        width: 100%;
        border-collapse: collapse;
        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", Roboto;
    }
    .rcf-table thead th {
        background-color: #4A5568;
        color: white;
        padding: 12px 16px;
        text-align: left;
        font-weight: 500;
        border: 1px solid #2D3748;
    }
    .rcf-table td {
        padding: 8px 16px;
        border: 1px solid #E2E8F0;
    }
    .rcf-table tr.section-header {
        background-color: #EBF8FF;
    }
    .rcf-table tr.section-header td {
        color: #2C5282;
        font-weight: 600;
    }
    .rcf-table tr:not(.section-header) {
        background-color: white;
    }
    /* Align numeric columns right */
    .rcf-table td:nth-child(2), .rcf-table td:nth-child(3), .rcf-table td:nth-child(4), .rcf-table td:nth-child(5), .rcf-table td:nth-child(6) {
        text-align: right;
        font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
        color: #2D3748;
    }
    .rcf-table tr:has(td:empty) {
        height: 8px;
        background-color: white;
    }
    </style>
    """

    # JavaScript for screenshot
    html2canvas_js = """
    <script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script>
    <script>
    function downloadTableImage() {
        const table = document.querySelector('.rcf-table');
        const options = {
            scale: 2,
            useCORS: true,
            backgroundColor: '#ffffff'
        };
        html2canvas(table, options).then(canvas => {
            const image = canvas.toDataURL('image/png', 1.0);
            const link = document.createElement('a');
            link.href = image;
            link.download = 'rcf_table.png';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        });
    }
    </script>
    <div style='width: 100%; padding: 10px 0;'>
        <button onclick="downloadTableImage()" 
                style="width: 100%;
                       background-color: rgb(43, 108, 176);
                       color: white;
                       padding: 0.6rem 0.6rem;
                       border: none;
                       border-radius: 0.25rem;
                       cursor: pointer;
                       font-weight: 500;
                       font-size: 1rem;
                       line-height: 1.4;
                       transition: background-color 0.2s;">
            📷 Download Image
        </button>
    </div>
    """

    final_html = custom_css + html_table + html2canvas_js
    components.html(final_html, height=800, scrolling=True)

def load_data(file):
    """
    Attempts to read an Excel or CSV file and return a DataFrame.
    """
    try:
        if isinstance(file, str):
            # local path
            if file.endswith(".xlsx"):
                return pd.read_excel(file)
            elif file.endswith(".csv"):
                return pd.read_csv(file)
            else:
                return None
        else:
            # user-uploaded file
            if file.name.endswith(".xlsx"):
                return pd.read_excel(file)
            elif file.name.endswith(".csv"):
                return pd.read_csv(file)
            else:
                return None
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# In utils/helpers.py (anywhere below your other helper functions):

def safe_rerun():
    """
    Calls st.experimental_rerun() if it exists; otherwise does nothing.
    Useful when you want to force a Streamlit rerun in older or
    restricted environments.
    """
    try:
        import streamlit as st
        st.experimental_rerun()
    except AttributeError:
        pass
