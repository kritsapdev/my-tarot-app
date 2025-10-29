import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# --- การตั้งค่าพื้นฐาน ---
# โหลด API Key จากไฟล์ .env
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# ตั้งค่า Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

# ตั้งค่าชื่อ Tab ของเว็บ
st.set_page_config(
    page_title="เว็บแอปหมอดูไพ่ยิปซี",
    page_icon="🔮"
)


# --- ส่วนของหน้าเว็บ ---
st.title("🔮 เว็บแอปหมอดูไพ่ยิปซี")
st.write("ลองทดสอบคุยกับ AI หมอดูของเรา")

# สร้างกล่องข้อความให้ผู้ใช้พิมพ์คำถาม
user_question = st.text_input("ถามคำถามสิ:")

# สร้างปุ่มสำหรับส่งคำถาม
if st.button("ส่งคำถาม"):
    if user_question:
        # ถ้ามีคำถามเข้ามา...
        st.info(f"คำถามของคุณคือ: {user_question}")
        
        # เริ่มเชื่อมต่อกับ Gemini Model
        model = genai.GenerativeModel('gemini-pro')
        
        # ส่งคำถามไปให้ AI
        response = model.generate_content(user_question)
        
        # แสดงคำตอบจาก AI
        st.markdown(response.text)
    else:
        # ถ้าไม่ได้พิมพ์คำถาม
        st.warning("กรุณาพิมพ์คำถามก่อนกดส่ง")