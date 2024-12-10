import streamlit as st
import pages.home as home
import pages.calculator as calculator
import pages.about as about

# Konfigurasi aplikasi
st.set_page_config(
    page_title="Kalkulator Sederhana",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Navigasi dengan sidebar
page = st.sidebar.selectbox(
    "Pilih Halaman",
    ["Halaman Utama", "Kalkulator", "Tentang"]
)

if page == "Halaman Utama":
    home.main()
elif page == "Kalkulator":
    calculator.main()
elif page == "Tentang":
    about.main()
