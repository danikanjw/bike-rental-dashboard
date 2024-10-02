import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Menyiapkan judul aplikasi
st.title('Bike Sharing Dashboard :bike:')

# Memuat dataset
day_df = pd.read_csv("dashboard/cleaned_day_data.csv")
hour_df = pd.read_csv("dashboard/cleaned_hour_data.csv")

# Hitung total penyewaan sepeda
total_rental = day_df['cnt'].sum()
st.write("Total Rentals: ", total_rental)

# Pertanyaan 1: Bagaimana kondisi cuaca memengaruhi jumlah penyewaan sepeda?
st.subheader('Impact of Weather on Rentals')

# Mengelompokkan penyewaan berdasarkan kondisi cuaca
weather_rentals = day_df.groupby('weathersit')['cnt'].sum().reset_index()

# Mapping deskripsi kondisi cuaca
weather_rentals['weathersit'] = weather_rentals['weathersit'].map({
    1: 'Clear, Few clouds, Partly cloudy',
    2: 'Mist + Cloudy, Mist + Broken clouds, Mist',
    3: 'Light Snow/Rain, Light Rain + Thunderstorm',
    4: 'Heavy Rain + Ice Pallets, Snow + Fog'
})

# Visualisasi
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=weather_rentals, y='weathersit', x='cnt', ax=ax, palette='coolwarm')
ax.set_title('Jumlah Penyewaan Sepeda Berdasarkan Kondisi Cuaca')
ax.set_xlabel('Jumlah Penyewaan Sepeda')
ax.set_ylabel('Kondisi Cuaca')
st.pyplot(fig)

# Pertanyaan 2: Pada pukul berapa jumlah penyewa mencapai puncaknya dan terendah?
st.subheader('Hourly Rental Trends')

# Mengelompokkan penyewaan sepeda berdasarkan jam
hourly_rentals = hour_df.groupby('hr')['cnt'].sum().reset_index()

# Visualisasi
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=hourly_rentals, x='hr', y='cnt', marker='o', ax=ax)
ax.set_title('Jumlah Penyewaan Sepeda Berdasarkan Jam')
ax.set_xlabel('Jam')
ax.set_ylabel('Jumlah Penyewaan Sepeda')
ax.grid(True)
st.pyplot(fig)

# Pertanyaan 3: Perbandingan penyewaan sepeda pada hari kerja vs hari libur
st.subheader('Comparison of Rentals on Workdays vs. Holidays')

# Menghitung total penyewaan untuk hari kerja dan hari libur
workday_rentals = day_df.groupby('workingday')['cnt'].sum().reset_index()

# Pie chart
labels = ['Hari Libur', 'Hari Kerja']
sizes = workday_rentals['cnt']

fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(sizes, labels=labels, autopct=lambda p: f'{int(p * sum(sizes) / 100)} ({p:.1f}%)', startangle=90, colors=['#ff9999', '#66b3ff'])
ax.set_title('Perbandingan Penyewaan Sepeda: Hari Kerja vs Hari Libur')
st.pyplot(fig)


