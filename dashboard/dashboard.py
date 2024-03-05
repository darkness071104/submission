import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load data
day_df = pd.read_csv("https://raw.githubusercontent.com/darkness071104/submission/main/data/day.csv")
hour_df = pd.read_csv("https://raw.githubusercontent.com/darkness071104/submission/main/data/hour.csv")
all_df = 

# Data cleaning and preprocessing (you may copy relevant code blocks from the provided code)

# Create Streamlit app
st.title('Bike Sharing Dataset Dashboard')
st.sidebar.title('Menu')

# Sidebar menu
menu_selection = st.sidebar.radio('Select an Option', ('Data Overview', 'EDA Visualization', 'Conclusion'))

# Data overview section
if menu_selection == 'Data Overview':
    st.header('Data Overview')
    st.write('Day DataFrame:')
    st.write(day_df.head())
    st.write('Hour DataFrame:')
    st.write(hour_df.head())

# EDA Visualization section
elif menu_selection == 'EDA Visualization':
    st.header('EDA Visualization')
    st.subheader('Perbandingan Jumlah Penyewa Sepeda Setiap Tahun Berdasarkan Musim')

    # Visualization code for Question 1
    by_season_year_df = day_df.groupby(["season", "year"])["cnt"].sum().reset_index()
    fig1, ax1 = plt.subplots()
    sns.barplot(
        x="season",
        y="cnt",
        hue="year",
        data=by_season_year_df,
        palette="Set2",
        ax=ax1
    )
    ax1.set_title('Perbandingan Jumlah Penyewa Sepeda Setiap Tahun Berdasarkan Musim')
    ax1.set_xlabel('Musim')
    ax1.set_ylabel('Jumlah Penyewa Sepeda')
    st.pyplot(fig1)

    st.subheader('Pengaruh Musim Terhadap Jumlah Penyewa Sepeda')

    # Visualization code for Question 2
    by_season_mean = day_df.groupby(["season"])["cnt"].mean().reset_index()
    fig2, ax2 = plt.subplots()
    sns.lineplot(data=by_season_mean, x='season', y='cnt', marker='o', linewidth=2, color="#72BCD4", label='Mean', ax=ax2)
    ax2.set_title('Pengaruh Musim Terhadap Jumlah Penyewa Sepeda')
    ax2.set_xlabel('Kondisi Cuaca')
    ax2.set_ylabel('Rata-rata Jumlah Penyewa Sepeda')
    ax2.tick_params(axis='x', labelrotation=45)
    st.pyplot(fig2)

    st.subheader('Perbandingan Jumlah Penyewa Sepeda Casual dan Registered di Setiap Tahun')

    # Visualization code for Question 3
    perbandingan_df = day_df.groupby(["year"]).agg({
        "casual": ["sum"],
        "registered": ["sum"]
    }).reset_index()

    fig3, ax3 = plt.subplots()
    ax3.bar(perbandingan_df["year"], perbandingan_df[("casual", "sum")], label="Casual")
    ax3.bar(perbandingan_df["year"], perbandingan_df[("registered", "sum")], bottom=perbandingan_df[("casual", "sum")], label="Registered")
    ax3.set_xlabel("Tahun")
    ax3.set_ylabel("Total Penyewa Sepeda")
    ax3.set_title("Perbandingan Jumlah Penyewa Sepeda Casual dan Registered di Setiap Tahun")
    ax3.legend()
    ax3.ticklabel_format(style='plain', axis='y')
    st.pyplot(fig3)

# Conclusion section
elif menu_selection == 'Conclusion':
    st.header('Conclusion')
    st.write('Your conclusion here...')
