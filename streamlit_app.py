import streamlit as st
import os

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

# Ana bölüm
st.header("Belge İşleme Uygulaması")
st.write("Bu uygulamayı kullanarak belgeleri analiz edebilirsiniz.")

# Dosya yükleme bölümü
uploaded_file = st.file_uploader("Bir belge yükleyin", type=["pdf", "docx", "txt"])
if uploaded_file is not None:
    st.success("Dosya başarıyla yüklendi!")
    # Dosya işleme kodları buraya eklenecek
    st.write(f"Dosya adı: {uploaded_file.name}")
    st.write(f"Dosya boyutu: {uploaded_file.size} bytes")

# Demo bilgisi
st.subheader("Demo İşlevsellik")
if st.button("Demo Başlat"):
    with st.spinner("İşlem gerçekleştiriliyor..."):
        # Burada örnek bir işlem yapabilirsiniz
        import time
        time.sleep(2)
    st.balloons()
    st.success("İşlem tamamlandı!")

# Footer
st.markdown("---")
st.caption("© 2025 Arabica Projesi")
