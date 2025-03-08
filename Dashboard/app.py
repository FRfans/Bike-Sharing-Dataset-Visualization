
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from scipy.stats import pearsonr
from datetime import datetime

# Load dataset
df_day = pd.read_csv("all_data.csv")

df_day["dateday"] = pd.to_datetime(df_day["dateday"])

def format_currency(value):
    return f"AUD{value:,.2f}".replace(",", ".")

# Streamlit Sidebar
st.sidebar.subheader("Rentang Waktu")
start_date, end_date = st.sidebar.date_input("Pilih rentang waktu:", [df_day["dateday"].min(), df_day["dateday"].max()])

# Filter berdasarkan rentang waktu
df_filtered = df_day[(df_day["dateday"] >= pd.to_datetime(start_date)) & (df_day["dateday"] <= pd.to_datetime(end_date))]

# Dashboard Header
st.title("Bike Sharing Dashboard 🚴")

# KPI Metrics
col1, col2 = st.columns(2)
col1.metric("Total Orders", len(df_filtered))
col2.metric("Total Revenue", format_currency(df_filtered["total_rentals"].sum()))

# Daily Orders Trend
st.subheader("Daily Orders Trend")
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(df_filtered["dateday"], df_filtered["total_rentals"], marker='o', linestyle='-', color='skyblue', alpha=0.7)
ax.set_xlabel("Date")
ax.set_ylabel("Total Rentals")
st.pyplot(fig)

# Best & Worst Performing Season for Casual Users
st.subheader("Best & Worst Performing Season for Casual Users")

avg_casual_per_season = df_day.groupby("season")["casual_users"].mean().sort_values()

plt.figure(figsize=(12, 6))
sns.barplot(x=avg_casual_per_season.index, y=avg_casual_per_season.values, palette="Blues")
plt.title("Rata-rata Pengguna Kasual Berdasarkan Musim")
plt.xlabel("Musim")
plt.ylabel("Rata-rata Pengguna Kasual")
st.pyplot(plt)

# Best & Worst Performing Season for Registered Users
st.subheader("Best & Worst Performing Season for Registered Users")

avg_registered_per_season = df_day.groupby("season")["registered_users"].mean().sort_values()

plt.figure(figsize=(12, 6))
sns.barplot(x=avg_registered_per_season.index, y=avg_registered_per_season.values, palette="Reds")
plt.title("Rata-rata Pengguna Terdaftar Berdasarkan Musim")
plt.xlabel("Musim")
plt.ylabel("Rata-rata Pengguna Terdaftar")
st.pyplot(plt)


st.caption("Copyright © 2025 Bike Sharing Dashboard")
