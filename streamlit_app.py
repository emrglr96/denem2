import streamlit as st
import os
from utils import load_data, visualize_data

st.set_page_config(
    page_title="Arabica App",
    page_icon="☕",
    layout="wide"
)

st.title("Arabica Uygulaması")
st.write("Bu uygulama, belgeleri işlemek için tasarlanmıştır.")

# Temel UI
st.sidebar.header("Kontrol Paneli")
st.sidebar.write("Bu sidebar'da kontrol seçenekleri yer alacak.")

# Sidebar seçenekleri
st.sidebar.subheader("Veri Görselleştirme")
show_data = st.sidebar.checkbox("Veri Grafiği Göster", value=True)

# Ana bölüm
st.header("Belge İşleme Uygulaması")
st.write("Bu uygulamayı kullanarak belgeleri analiz edebilirsiniz.")

tabs = st.tabs(["Belge Yükleme", "Veri Analizi", "Hakkında"])

with tabs[0]:
    # Dosya yükleme bölümü
    uploaded_file = st.file_uploader("Bir belge yükleyin", type=["pdf", "docx", "txt"])
    if uploaded_file is not None:
        st.success("Dosya başarıyla yüklendi!")
        # Dosya işleme kodları buraya eklenecek
        st.write(f"Dosya adı: {uploaded_file.name}")
        st.write(f"Dosya boyutu: {uploaded_file.size} bytes")

with tabs[1]:
    st.subheader("Veri Analizi")
    if show_data:
        df = load_data()
        visualize_data(df)
    else:
        st.info("Veri gösterimi kapalı. Görüntülemek için soldaki panelden seçeneği işaretleyin.")

with tabs[2]:
    st.subheader("Uygulama Hakkında")
    st.write("""
    Bu uygulama, Streamlit kullanılarak geliştirilmiştir.
    
    ### Özellikler:
    - Belge yükleme ve işleme
    - Veri analizi ve görselleştirme
    - Kullanıcı dostu arayüz
    
    Sorularınız için iletişime geçebilirsiniz.
    """)

# Demo bilgisi
st.subheader("Demo İşlevsellik")
col1, col2 = st.columns(2)
with col1:
    if st.button("Demo Başlat"):
        with st.spinner("İşlem gerçekleştiriliyor..."):
            # Burada örnek bir işlem yapabilirsiniz
            import time
            time.sleep(2)
        st.balloons()
        st.success("İşlem tamamlandı!")

with col2:
    st.metric(label="İşlem Süresi", value="2 sn", delta="-0.5 sn")

# Footer
st.markdown("---")
st.caption("© 2025 Arabica Projesi | Streamlit ile hazırlandı")
