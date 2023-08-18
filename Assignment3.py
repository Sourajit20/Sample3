import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Page layout
st.set_page_config(page_title="Normal Distribution App", layout="wide")

# Sidebar
st.sidebar.header("Parameters")
mean = st.sidebar.number_input("Mean", value=0.0)
std_dev = st.sidebar.number_input("Standard Deviation", value=1.0)
num_samples = st.sidebar.number_input("Number of Samples", value=1000)

# Generate random data
np.random.seed(0)  # For reproducibility
data = np.random.normal(mean, std_dev, num_samples)

# Histogram
st.header("Histogram of Generated Data")
plt.hist(data, bins=30, edgecolor="k")
plt.xlabel("Value")
plt.ylabel("Frequency")
st.pyplot()

# Download as CSV
if st.button("Download Data as CSV"):
    df = pd.DataFrame(data, columns=["Value"])
    csv = df.to_csv(index=False)
    st.download_button("Download CSV", data=csv, file_name="generated_data.csv")

# App footer
st.markdown("---")
st.markdown("Created by Your Name")
