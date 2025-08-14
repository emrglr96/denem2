from openai import OpenAI
import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()


# Güvenlik için API anahtarı koddan kaldırıldı. Ortam değişkeninden alınabilir.
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("❌ API anahtarı bulunamadı! Lütfen .env dosyasına OPENAI_API_KEY ekleyin.")
    exit(1)

try:
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Merhaba"}],
        max_tokens=10
    )
    print("✅ API anahtarı çalışıyor!")
    print(f"Yanıt: {response.choices[0].message.content}")
except Exception as e:
    print(f"❌ Hata: {e}")
