import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set custom page configuration
st.set_page_config(
    page_title="Normal Distribution App",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon=":chart_with_upwards_trend:",
)

# Sidebar styling
st.sidebar.header("Parameters")
st.sidebar.markdown(
    "<h2 style='text-align:center; color:#EEA637;'>Parameter Settings</h2>",
    unsafe_allow_html=True,
)

# Get user input
mean = st.sidebar.number_input("Mean", value=0.0)
std_dev = st.sidebar.number_input("Standard Deviation", value=1.0)
num_samples = st.sidebar.number_input("Number of Samples", value=1000)

# Generate random data
np.random.seed(0)  # For reproducibility
data = np.random.normal(mean, std_dev, num_samples)

# Plot styling
fig, ax = plt.subplots(figsize=(8, 6))
ax.hist(data, bins=30, edgecolor="k", color="#EEA637")
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Frequency", fontsize=14)
ax.set_title("Histogram of Generated Normal Distribution", fontsize=16)

# Display the plot using st.pyplot()
st.markdown(
    "<h1 style='text-align:center; color:#333;'>Histogram of Generated Normal Distribution</h1>",
    unsafe_allow_html=True,
)
st.pyplot(fig)

# Button styling
if st.button("Download Data as CSV", key="download_button"):
    df = pd.DataFrame(data, columns=["Value"])
    csv = df.to_csv(index=False)
    st.download_button(
        "<span style='color:#fff;'>Download CSV</span>",
        data=csv,
        file_name="generated_data.csv",
        unsafe_allow_html=True,
    )

# App footer
st.markdown("---")
st.markdown("Created by Sourajit")
