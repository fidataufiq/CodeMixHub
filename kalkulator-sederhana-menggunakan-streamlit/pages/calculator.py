import streamlit as st

def main():
    st.title("Kalkulator Sederhana")
    
    # Input untuk angka
    num1 = st.number_input("Masukkan angka pertama:", format="%.2f")
    num2 = st.number_input("Masukkan angka kedua:", format="%.2f")
    
    # Pilih operasi
    operation = st.selectbox("Pilih operasi:", ["Tambah", "Kurang", "Kali", "Bagi"])
    
    # Hasil
    if st.button("Hitung"):
        if operation == "Tambah":
            result = num1 + num2
        elif operation == "Kurang":
            result = num1 - num2
        elif operation == "Kali":
            result = num1 * num2
        elif operation == "Bagi":
            result = num1 / num2 if num2 != 0 else "Tidak dapat membagi dengan nol"
        
        st.success(f"Hasil: {result}")

if __name__ == "__main__":
    main()
