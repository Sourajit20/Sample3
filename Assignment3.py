import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import csv

def generate_normal_distribution(mean, standard_deviation, number_of_samples):
  """Generates a normal distribution with the specified mean, standard deviation, and number of samples."""
  samples = np.random.normal(mean, standard_deviation, number_of_samples)
  return samples

def plot_histogram(samples):
  """Plots the histogram of the specified samples."""
  plt.hist(samples)
  plt.xlabel("Value")
  plt.ylabel("Number of samples")
  plt.title("Histogram of normal distribution")
  # This line has been modified to import plotly.express instead of plotly.tools
  st.plotly_chart(plt.gcf())

def download_data(samples):
  """Downloads the specified samples into a .csv file."""
  with open("data.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Value"])
    for sample in samples:
      writer.writerow([sample])

st.title("Normal distribution generator")

mean = st.slider("Mean", 0, 10, 5)
standard_deviation = st.slider("Standard deviation", 0, 5, 1)
number_of_samples = st.slider("Number of samples", 10, 1000, 100)

samples = generate_normal_distribution(mean, standard_deviation, number_of_samples)

# This line has been modified to use plotly.express instead of plotly.tools
st.plotly_chart(plot_histogram(samples))

download_button = st.button("Download data")

if download_button:
  download_data(samples)
