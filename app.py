import streamlit as st
import engine_core
import time

# ตั้งค่าหน้าเว็บให้ดูเป็นมืออาชีพ
st.set_page_config(page_title="Baccarat AI Sentinel", layout="wide")

st.title("🃏 Baccarat Intelligence Dashboard (Tie Edition)")

if 'history' not in st.session_state:
    st.session_state.history = []

# --- Sidebar: ส่วนควบคุม ---
with st.sidebar:
    st.header("🎮 บันทึกผลหน้างาน")
    st.write("กดปุ่มตามผลที่ออกจริง")
    
    # สร้าง 3 คอลัมน์สำหรับ P, B, T
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("🔵 P", use_container_width=True):
            st.session_state.history.append('P')
            st.rerun()
    with c2:
        if st.button("🔴 B", use_container_width=True):
            st.session_state.history.append('B')
            st.rerun()
    with c3:
        if st.button("🟢 T", use_container_width=True):
            st.session_state.history.append('T')
            st.rerun()
            
    st.divider()
    if st.button("🗑️ Reset Data", use_container_width=True):
        st.session_state.history = []
        st.rerun()

# --- Main Area: ส่วนวิเคราะห์ ---
if st.session_state.history:
    # 1. วิเคราะห์ Pattern และ Probability
    pattern = engine_core.analyze_pattern(st.session_state.history)
    probs = engine_core.calculate_probability(st.session_state.history)
    
    # แสดงค่าความน่าจะเป็นแบบแถบสี
    st.subheader("📊 วิเคราะห์ความน่าจะเป็นสะสม")
    col_p, col_b, col_t = st.columns(3)
    col_p.metric("Player", f"{probs['Player']}%")
    col_b.metric("Banker", f"{probs['Banker']}%")
    col_t.metric("Tie", f"{probs['Tie']}%")
    
    # 2. คำแนะนำจาก Secret Engine
    st.divider()
    # ใช้ความยาวประวัติเป็น Seed ส่งเข้า Engine
    score = engine_core.calculate_secret_score(len(st.session_state.history))
    
    st.subheader("🔮 คำแนะนำตาถัดไป")
    if score > 60:
        st.error(f"### แนะนำลงทุน: **BANKER (แดง)** 🔴 (ความมั่นใจ {score}%)")
    elif score < 40:
        st.info(f"### แนะนำลงทุน: **PLAYER (น้ำเงิน)** 🔵 (ความมั่นใจ {100-score}%)")
    else:
        st.warning(f"### สถานะ: **รอดูเชิง หรือ ลงเสมอ (TIE)** 🟢")

    # 3. แสดงเค้าไพ่ล่าสุด
    st.divider()
    st.write("🕒 **ประวัติ 15 ตาล่าสุด:**")
    # ตกแต่งตัวอักษรสีตามผล
    colored_history = []
    for x in st.session_state.history[-15:]:
        if x == 'P': colored_history.append(f":blue[{x}]")
        elif x == 'B': colored_history.append(f":red[{x}]")
        else: colored_history.append(f":green[{x}]")
    
    st.markdown(" ### " + "  ➡  ".join(colored_history))
    st.caption(f"Engine Alert: {pattern}")

else:
    st.info("💡 เริ่มต้นโดยการกดบันทึกผลทางด้านซ้ายมือ เพื่อให้ AI เริ่มประมวลผล")

st.caption(f"System Version: {engine_core.get_version()}")