🃏 Baccarat Sentinel AI (Real-time Analytics)ระบบวิเคราะห์ความน่าจะเป็นและตรวจจับเค้าไพ่บาคาร่าแบบ Real-time โดยใช้ Python Engine ในการคำนวณสถิติสะสม🌟 FeaturesReal-time Input: รองรับการบันทึกผล Player, Banker และ TiePattern Recognition: ตรวจจับเค้าไพ่มังกร, ปิงปอง และลูกคู่โดยอัตโนมัติProbability Engine: คำนวณ % การออกผลตามหลักสถิติย้อนหลังDual UI: เลือกใช้งานได้ทั้งแบบ Web Dashboard (Streamlit) และ Terminal (CLI)🛠️ Architectureโปรเจกต์นี้ถูกแบ่งออกเป็น 2 ส่วนหลัก:Core Engine (engine_core.py): หัวใจหลักที่ใช้คำนวณ Algorithm และวิเคราะห์ PatternInterface Layers:app.py: หน้าจอเว็บสำหรับใช้งานผ่าน Browser/Mobileterminal_app.py: หน้าจอดำสำหรับสาย Light-weight รันผ่าน Command Line🚀 Quick Start1. Installationติดตั้ง Library ที่จำเป็น:PowerShellpip install streamlit
2. Running the Web UIเปิดใช้งานหน้า Dashboard:PowerShellpython -m streamlit run app.py
3. Running the Terminal UIเปิดใช้งานผ่านหน้าจอดำ:PowerShellpython terminal_app.py
📊 Logic & Analyticsระบบใช้ฟังก์ชัน calculate_probability() เพื่อประมวลผลความถี่ของสถิติ และ analyze_pattern() เพื่อแจ้งเตือนจุดเปลี่ยนของไพ่:ฝั่งสัญลักษณ์สีที่แสดงใน UIPlayerP🔵 BlueBankerB🔴 RedTieT🟢 Green📂 Project StructurePlaintext├── .github/workflows/    # CI/CD Automation
├── engine_core.py       # การประมวลผลหลัก (Algorithm)
├── app.py               # Streamlit Web Application
├── terminal_app.py      # CLI Terminal Application
└── README.md            # คู่มือการใช้งาน
🤝 Contributingโปรเจกต์นี้สร้างขึ้นเพื่อการศึกษาด้านสถิติและความน่าจะเป็น หากต้องการพัฒนาต่อ สามารถ Fork และส่ง Pull Request มาได้เลย!📥 Latest Releasev2.1.0-Stableเพิ่มการรองรับผล Tie (เสมอ)ปรับปรุง UI ให้รองรับการกดผ่าน Mobile Browserเพิ่มระบบแจ้งเตือนเค้าไพ่มังกร
