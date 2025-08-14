import pandas as pd
import streamlit as st

def load_data():
    """Demo veri yükleme fonksiyonu"""
    data = {
        'Tarih': ['2025-01-01', '2025-02-01', '2025-03-01', '2025-04-01', '2025-05-01'],
        'Değer': [100, 150, 130, 170, 190]
    }
    return pd.DataFrame(data)

def visualize_data(df):
    """Veri görselleştirme fonksiyonu"""
    st.line_chart(df.set_index('Tarih'))
    
    st.subheader("Veri Tablosu")
    st.dataframe(df)
