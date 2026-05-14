import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------
# PAGE CONFIGURATION
# -----------------------------------
st.set_page_config(
    page_title="Graph Dashboard",
    layout="wide"
)

# -----------------------------------
# TITLE
# -----------------------------------
st.title("📊 Streamlit Graph Dashboard")

st.markdown("E:\streamlit_graph_dashboard\9. Sales-Data-Analysis.csv")

# -----------------------------------
# FILE UPLOADER
# -----------------------------------
uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

# -----------------------------------
# IF FILE UPLOADED
# -----------------------------------
if uploaded_file is not None:

    # Read Dataset
    df = pd.read_csv(uploaded_file)

    # -----------------------------------
    # SHOW DATASET
    # -----------------------------------
    st.subheader("📁 Dataset Preview")

    st.dataframe(df.head())

    # -----------------------------------
    # DATASET SHAPE
    # -----------------------------------
    st.subheader("📌 Dataset Shape")

    st.write(df.shape)

    # -----------------------------------
    # DATA TYPES
    # -----------------------------------
    st.subheader("📋 Data Types")

    st.write(df.dtypes)

    # -----------------------------------
    # MISSING VALUES
    # -----------------------------------
    st.subheader("❌ Missing Values")

    st.write(df.isnull().sum())

    # -----------------------------------
    # STATISTICAL SUMMARY
    # -----------------------------------
    st.subheader("📈 Statistical Summary")

    st.write(df.describe())

    # -----------------------------------
    # COLUMN SELECTION
    # -----------------------------------
    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns

    st.subheader("🎯 Select Columns for Graph")

    x_column = st.selectbox(
        "Select X-axis",
        df.columns
    )

    y_column = st.selectbox(
        "Select Y-axis",
        numeric_columns
    )

    # ==================================================
    # BAR CHART
    # ==================================================
    st.subheader("📊 Bar Chart")

    fig1, ax1 = plt.subplots(figsize=(8, 5))

    df.groupby(x_column)[y_column].sum().plot(
        kind='bar',
        ax=ax1
    )

    plt.xlabel(x_column)
    plt.ylabel(y_column)

    st.pyplot(fig1)

    # ==================================================
    # LINE CHART
    # ==================================================
    st.subheader("📈 Line Chart")

    fig2, ax2 = plt.subplots(figsize=(8, 5))

    df.groupby(x_column)[y_column].sum().plot(
        kind='line',
        ax=ax2
    )

    st.pyplot(fig2)

    # ==================================================
    # HISTOGRAM
    # ==================================================
    st.subheader("📉 Histogram")

    fig3, ax3 = plt.subplots(figsize=(8, 5))

    df[y_column].plot(
        kind='hist',
        bins=10,
        ax=ax3
    )

    st.pyplot(fig3)

    # ==================================================
    # SCATTER PLOT
    # ==================================================
    st.subheader("🔵 Scatter Plot")

    fig4, ax4 = plt.subplots(figsize=(8, 5))

    ax4.scatter(
        df[y_column],
        df[y_column]
    )

    ax4.set_xlabel(y_column)
    ax4.set_ylabel(y_column)

    st.pyplot(fig4)

    # ==================================================
    # PIE CHART
    # ==================================================
    st.subheader("🥧 Pie Chart")

    fig5, ax5 = plt.subplots(figsize=(7, 7))

    df[x_column].value_counts().head(5).plot(
        kind='pie',
        autopct='%1.1f%%',
        ax=ax5
    )

    plt.ylabel("")

    st.pyplot(fig5)

    # ==================================================
    # HEATMAP
    # ==================================================
    st.subheader("🔥 Correlation Heatmap")

    fig6, ax6 = plt.subplots(figsize=(8, 5))

    sns.heatmap(
        df.corr(numeric_only=True),
        annot=True,
        cmap='coolwarm',
        ax=ax6
    )

    st.pyplot(fig6)

    # -----------------------------------
    # SUCCESS MESSAGE
    # -----------------------------------
    st.success("✅ Graphs Generated Successfully")

# -----------------------------------
# IF NO FILE UPLOADED
# -----------------------------------
else:

    st.warning("E:\streamlit_graph_dashboard\9. Sales-Data-Analysis.csv")