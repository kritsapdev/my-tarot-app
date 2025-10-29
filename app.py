import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# --- การตั้งค่าพื้นฐาน ---
load_dotenv()
# ดึง API Key: ตรวจสอบจาก Streamlit Secrets ก่อน, ถ้าไม่มีให้ดึงจาก .env (สำหรับ Local)
try:
    # สำหรับ Streamlit Cloud
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
except KeyError:
    # สำหรับ Local Environment
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)


# --- ส่วนของการโหลดโมเดล (ใช้ Cache เพื่อความเร็ว) ---
@st.cache_resource
def load_model():
    return genai.GenerativeModel('gemini-2.5-flash')

model = load_model()

# --- ส่วนของหน้าเว็บ ---
st.set_page_config(page_title="เว็บแอปหมอดูไพ่ยิปซี", page_icon="🔮")
st.title("🔮 เว็บแอปหมอดูไพ่ยิปซี")
st.write("ลองทดสอบคุยกับ AI หมอดูของเรา")

user_question = st.text_input("ถามคำถามสิ:")

if st.button("ส่งคำถาม"):
    if user_question:
        st.info(f"คำถามของคุณคือ: {user_question}")
        
        # --- ใช้ Spinner เพื่อแสดงสถานะกำลังโหลด ---
        with st.spinner("กำลังทำนาย... กรุณารอสักครู่ ⏳"):
            # ส่งคำถามไปให้ AI
            response = model.generate_content(user_question)
            
            # แสดงคำตอบจาก AI
            st.markdown(response.text)
    else:
        st.warning("กรุณาพิมพ์คำถามก่อนกดส่ง")