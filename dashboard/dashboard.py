import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load data
all_df = pd.read_csv('dashboard/main_data.csv')

# Create Streamlit app
st.title('Bike Sharing Dataset Dashboard')

with st.sidebar:
    st.image("https://ouch-cdn2.icons8.com/5ojUcTG0qFIin-W97Glji…Tk1/NWYtNGQwZS05YjZh/LTU3NjBjMzA5ZDA5/MC5zdmc.png")
    st.header('Bike Sharing Dataset Dashboard')


# Sidebar menu
menu_selection = st.sidebar.selectbox('Select an Option', ('Data Overview', 'Perbandingan Jumlah Penyewa Sepeda Setiap Tahun Berdasarkan Musim', 'Pengaruh Musim Terhadap Jumlah Penyewa Sepeda', 'Perbandingan Jumlah Penyewa Sepeda Casual dan Registered di Setiap Tahun' ))

# Data overview section
if menu_selection == 'Data Overview':
    st.header('Data Overview')
    st.write('Main data:')
    st.write(all_df.head(20))

# EDA Visualization section
elif menu_selection == 'Perbandingan Jumlah Penyewa Sepeda Setiap Tahun Berdasarkan Musim':
    st.subheader('Perbandingan Jumlah Penyewa Sepeda Setiap Tahun Berdasarkan Musim')
    # Visualization code for Question 1
    by_season_year_df = all_df.groupby(["season_day", "year_day"])["cnt_day"].sum().reset_index()
    fig1, ax1 = plt.subplots()
    sns.barplot(
        x="season_day",
        y="cnt_day",
        hue="year_day",
        data=by_season_year_df,
        palette="Set2",
        ax=ax1
    )
    ax1.set_title('Perbandingan Jumlah Penyewa Sepeda Setiap Tahun Berdasarkan Musim')
    ax1.set_xlabel('Musim')
    ax1.legend(title='Tahun')
    ax1.set_ylabel('Jumlah Penyewa Sepeda')
    st.pyplot(fig1)

elif menu_selection == 'Pengaruh Musim Terhadap Jumlah Penyewa Sepeda':
    st.subheader('Pengaruh Musim Terhadap Jumlah Penyewa Sepeda')
    # Visualization code for Question 2
    by_season_mean = all_df.groupby(["season_day"])["cnt_day"].mean().reset_index()
    fig2, ax2 = plt.subplots()
    sns.lineplot(data=by_season_mean, x='season_day', y='cnt_day', marker='o', linewidth=2, color="#72BCD4", label='Mean', ax=ax2)
    ax2.set_title('Pengaruh Musim Terhadap Jumlah Penyewa Sepeda')
    ax2.set_xlabel('Kondisi Cuaca')
    ax2.set_ylabel('Rata-rata Jumlah Penyewa Sepeda')
    ax2.tick_params(axis='x', labelrotation=45)
    st.pyplot(fig2)

elif menu_selection == 'Perbandingan Jumlah Penyewa Sepeda Casual dan Registered di Setiap Tahun':
    st.subheader('Perbandingan Jumlah Penyewa Sepeda Casual dan Registered di Setiap Tahun')
    # Visualization code for Question 3
    perbandingan_df = all_df.groupby("year_day").agg({
        "casual_day": "sum",
        "registered_day": "sum"
    }).reset_index()

    fig3, ax3 = plt.subplots()
    ax3.bar(perbandingan_df["year_day"], perbandingan_df["casual_day"], label="Casual")
    ax3.bar(perbandingan_df["year_day"], perbandingan_df["registered_day"], bottom=perbandingan_df["casual_day"], label="Registered")
    ax3.set_xlabel("Tahun")
    ax3.set_ylabel("Total Penyewa Sepeda")
    ax3.set_title("Perbandingan Jumlah Penyewa Terdaftar dan Tidak Terdaftar Setiap Tahun")
    ax3.legend()
    ax3.set_xticks(perbandingan_df["year_day"])
    ax3.ticklabel_format(style='plain', axis='y')
    st.pyplot(fig3)

# Conclusion section
elif menu_selection == 'Conclusion':
    st.header('Conclusion')
    st.write('Your conclusion here...')
