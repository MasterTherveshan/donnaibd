# workflows/bond_analysis.py

import os
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl

from utils.helpers import load_data

def show_bond_analysis_workflow():
    """
    Bond Analysis focusing on any Issuer Name containing 'inguza' (case-insensitive).
    Three 'pop' visuals:
      1) Maturity Year vs. Nominal (Beeswarm)
      2) Issue Date vs. Nominal (Scatter)
      3) Instrument Status vs. Nominal (Violin+Swarm)

    Minimal aggregator logic, 'Economist-style' aesthetic, no scientific notation,
    and each axis calls ticklabel_format to avoid KeyError with rcParams.
    """

    st.title("Inguza Bond Analysis Dashboard")

    # 1) Load Data
    default_file_path = os.path.join("data", "data.xlsx")
    st.write("**Upload a bond dataset** (XLSX or CSV) or let the app use `data/data.xlsx` by default.")
    user_file = st.file_uploader("Upload your bond data", type=["xlsx", "csv"])

    if user_file:
        df = load_data(user_file)
        if df is not None:
            st.success(f"Using uploaded file: {user_file.name}")
        else:
            st.error("Could not load the uploaded file. Please try again.")
            return
    else:
        if os.path.exists(default_file_path):
            df = load_data(default_file_path)
            st.warning("No file uploaded; using default `data/data.xlsx`.")
        else:
            st.error("No file uploaded, and `data/data.xlsx` not found.")
            return

    if df is None or df.empty:
        st.error("No valid bond data loaded.")
        return

    # 2) Filter for 'inguza' in Issuer Name (case-insensitive)
    if "Issuer Name" not in df.columns:
        st.error("Missing 'Issuer Name' column. Cannot filter for 'inguza'.")
        return

    mask_inguza = df["Issuer Name"].str.contains("inguza", case=False, na=False)
    df_inguza = df[mask_inguza].copy()

    if df_inguza.empty:
        st.warning("No data found where Issuer Name contains 'inguza'. Check your dataset.")
        return

    st.markdown(f"**Data for Inguza** – Rows: {len(df_inguza):,}")
    st.dataframe(df_inguza.head(5), use_container_width=True)

    # 3) Minimal cleaning: convert columns if they exist
    if "Issue Date" in df_inguza.columns:
        df_inguza["Issue Date"] = pd.to_datetime(df_inguza["Issue Date"], errors="coerce")

    if "Maturity Date Year" in df_inguza.columns:
        df_inguza["Maturity Date Year"] = pd.to_numeric(df_inguza["Maturity Date Year"], errors="coerce")

    if "Nominal Amount" in df_inguza.columns:
        df_inguza["Nominal Amount"] = pd.to_numeric(df_inguza["Nominal Amount"], errors="coerce")

    # 4) Seaborn "Economist Style" Setup
    sns.set_theme(style="whitegrid", context="talk")
    # Turn off offset for axis
    mpl.rcParams["axes.formatter.useoffset"] = False
    mpl.rcParams["font.size"] = 12
    mpl.rcParams["axes.titlesize"] = 14
    mpl.rcParams["axes.labelsize"] = 12

    # 5) Create 3 Tabs
    tab1, tab2, tab3 = st.tabs([
        "Maturity vs. Nominal",
        "Issue Date vs. Nominal",
        "Status vs. Nominal"
    ])

    # -------------------------------------------------------------------------
    # TAB 1: Maturity Year vs. Nominal (Beeswarm)
    # -------------------------------------------------------------------------
    with tab1:
        st.subheader("1) Maturity Year vs. Nominal Amount (Beeswarm)")
        needed_cols = {"Maturity Date Year", "Nominal Amount"}
        if not needed_cols.issubset(df_inguza.columns):
            st.warning(f"Missing columns for this plot: {needed_cols}.")
        else:
            subset = df_inguza.dropna(subset=needed_cols)
            if subset.empty:
                st.info("No valid rows after dropping missing Maturity/ Nominal data.")
            else:
                # Convert Maturity Date Year to string/categorical for beeswarm
                subset["Maturity Date Year"] = subset["Maturity Date Year"].astype(int).astype(str)

                fig, ax = plt.subplots(figsize=(8, 5))
                sns.swarmplot(
                    x="Maturity Date Year",
                    y="Nominal Amount",
                    data=subset,
                    color="dodgerblue",
                    size=5,
                    ax=ax
                )
                ax.set_title("Inguza – Maturity Year vs. Nominal Amount")
                ax.set_xlabel("Maturity Year")
                ax.set_ylabel("Nominal Amount (ZAR)")
                plt.xticks(rotation=45)

                # Force plain style numeric formatting on Y-axis
                ax.ticklabel_format(style="plain", axis="y", useOffset=False)

                st.pyplot(fig)

    # -------------------------------------------------------------------------
    # TAB 2: Issue Date vs. Nominal (Scatter)
    # -------------------------------------------------------------------------
    with tab2:
        st.subheader("2) Issue Date vs. Nominal Amount (Scatter)")
        needed_cols = {"Issue Date", "Nominal Amount"}
        if not needed_cols.issubset(df_inguza.columns):
            st.warning(f"Missing columns for this plot: {needed_cols}.")
        else:
            subset = df_inguza.dropna(subset=needed_cols)
            if subset.empty:
                st.info("No valid rows after dropping missing Issue Date/ Nominal data.")
            else:
                fig, ax = plt.subplots(figsize=(8, 5))
                ax.scatter(
                    subset["Issue Date"],
                    subset["Nominal Amount"],
                    color="darkred",
                    alpha=0.6,
                    s=40
                )
                ax.set_title("Inguza – Issue Date vs. Nominal Amount")
                ax.set_xlabel("Issue Date")
                ax.set_ylabel("Nominal Amount (ZAR)")
                plt.xticks(rotation=30)

                # Force plain style numeric formatting on Y-axis
                ax.ticklabel_format(style="plain", axis="y", useOffset=False)

                st.pyplot(fig)

    # -------------------------------------------------------------------------
    # TAB 3: Instrument Status vs. Nominal (Violin+Swarm)
    # -------------------------------------------------------------------------
    with tab3:
        st.subheader("3) Instrument Status vs. Nominal Amount (Violin + Swarm)")
        needed_cols = {"Instrument Status", "Nominal Amount"}
        if not needed_cols.issubset(df_inguza.columns):
            st.warning(f"Missing columns for this plot: {needed_cols}.")
        else:
            subset = df_inguza.dropna(subset=needed_cols)
            if subset.empty:
                st.info("No valid rows after dropping missing Instrument Status/ Nominal data.")
            else:
                fig, ax = plt.subplots(figsize=(8, 5))
                # Violin plot
                sns.violinplot(
                    x="Instrument Status",
                    y="Nominal Amount",
                    data=subset,
                    inner=None,
                    color="lightgray",
                    cut=0,
                    ax=ax
                )
                # Swarm on top
                sns.swarmplot(
                    x="Instrument Status",
                    y="Nominal Amount",
                    data=subset,
                    size=4,
                    edgecolor="gray",
                    linewidth=0.5,
                    ax=ax
                )
                ax.set_title("Inguza – Instrument Status vs. Nominal Amount")
                ax.set_xlabel("Instrument Status")
                ax.set_ylabel("Nominal Amount (ZAR)")
                plt.xticks(rotation=30)

                # Force plain style numeric formatting on Y-axis
                ax.ticklabel_format(style="plain", axis="y", useOffset=False)

                st.pyplot(fig)

    st.success("Inguza Bond Analysis complete!")
