import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import random # <-- เพิ่ม library สำหรับการสุ่ม

# --- ข้อมูลสำรับไพ่ (Major Arcana 22 ใบ) ---
TAROT_CARDS = [
    "The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
    "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit",
    "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance",
    "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgement", "The World"
]

# --- การตั้งค่าพื้นฐาน ---
load_dotenv()
try:
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
except (KeyError, FileNotFoundError):
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

# --- ส่วนของการโหลดโมเดล (ใช้ Cache เพื่อความเร็ว) ---
@st.cache_resource
def load_model():
    return genai.GenerativeModel('gemini-pro')

model = load_model()

# --- ส่วนของหน้าเว็บ ---
st.set_page_config(page_title="เว็บแอปหมอดูไพ่ยิปซี", page_icon="🔮")
st.title("🔮 ไพ่ยิปซีทำนายดวงชะตา")
st.write("ตั้งจิตอธิษฐาน แล้วพิมพ์คำถามที่อยากรู้ จากนั้นกดเปิดไพ่")

# --- ส่วนของการรับคำถามและเปิดไพ่ ---
user_question = st.text_input("พิมพ์คำถามของคุณที่นี่:")

if st.button("เปิดไพ่ 3 ใบ"):
    if user_question:
        # สุ่มเลือกไพ่ที่ไม่ซ้ำกัน 3 ใบ
        drawn_cards = random.sample(TAROT_CARDS, 3)
        
        st.info(f"คำถามของคุณ: {user_question}")
        st.subheader("ไพ่ที่คุณเปิดได้คือ:")
        
        # แสดงไพ่ที่เปิดได้
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"**ใบที่ 1 (อดีต):**\n\n`{drawn_cards[0]}`")
        with col2:
            st.markdown(f"**ใบที่ 2 (ปัจจุบัน):**\n\n`{drawn_cards[1]}`")
        with col3:
            st.markdown(f"**ใบที่ 3 (อนาคต):**\n\n`{drawn_cards[2]}`")

        # (เราจะเพิ่มส่วนการทำนายด้วย AI ในขั้นตอนต่อไป)

    else:
        st.warning("กรุณาพิมพ์คำถามก่อนเปิดไพ่")