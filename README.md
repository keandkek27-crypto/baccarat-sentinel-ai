# 🃏 Baccarat Sentinel AI (Real-time Analytics)

ระบบวิเคราะห์ความน่าจะเป็นและตรวจจับเค้าไพ่บาคาร่าแบบ Real-time โดยใช้ Python Engine ในการคำนวณสถิติสะสม

## 🌟 Features
* **Real-time Input:** รองรับการบันทึกผล Player, Banker และ Tie
* **Pattern Recognition:** ตรวจจับเค้าไพ่มังกร, ปิงปอง และลูกคู่โดยอัตโนมัติ
* **Probability Engine:** คำนวณ % การออกผลตามหลักสถิติย้อนหลัง
* **Dual UI:** เลือกใช้งานได้ทั้งแบบ Web Dashboard (Streamlit) และ Terminal (CLI)

## 🛠️ Architecture
โปรเจกต์นี้ถูกแบ่งออกเป็น 2 ส่วนหลัก:
1. **Core Engine (`engine_core.py`):** หัวใจหลักที่ใช้คำนวณ Algorithm และวิเคราะห์ Pattern
2. **Interface Layers:**
   * `app.py`: หน้าจอเว็บสำหรับใช้งานผ่าน Browser/Mobile
   * `terminal_app.py`: หน้าจอดำสำหรับสาย Light-weight รันผ่าน Command Line

## 🚀 Quick Start

### 1. Installation
ติดตั้ง Library ที่จำเป็น:
```powershell```

```bash
pip install streamlit
```
### 2. Running the Web UI
เปิดใช้งานหน้า Dashboard:
`PowerShell`
```bash
`python -m streamlit run app.py`
```

### 3. Running the Terminal UI
เปิดใช้งานผ่านหน้า ui:

`PowerShell`
```bash
`python terminal_app.py`
```

### 📊 Logic & Analytics
ระบบใช้ฟังก์ชัน `calculate_probability()` เพื่อประมวลผลความถี่ของสถิติ และ `analyze_pattern()` เพื่อแจ้งเตือนจุดเปลี่ยนของไพ่:
ฝั่ง,สัญลักษณ์,สีที่แสดงใน UI
| ฝั่ง  | สัญลักษณ์  | สี  |
| :--- | :---: | ---: |
| **Player** | `P` | 🔵 Blue |
| **Banker** | `B` | 🔴 Red |
| **Tie** | `T` | 🟢 Green |


## 📂 Project Structure

```text
.
├── .github/workflows/   # CI/CD Automation
├── engine_core.py       # การประมวลผลหลัก (Algorithm)
├── app.py               # Streamlit Web Application
├── terminal_app.py      # CLI Terminal Application
└── README.md            # คู่มือการใช้งาน
```
### 📥 Latest Release
v2.1.0-Stable

* เพิ่มการรองรับผล Tie (เสมอ)

* ปรับปรุง UI ให้รองรับการกดผ่าน Mobile Browser

* เพิ่มระบบแจ้งเตือนเค้าไพ่มังกร

###  🤝 Contributing
โปรเจกต์นี้สร้างขึ้นเพื่อการศึกษาด้านสถิติและความน่าจะเป็น หากต้องการพัฒนาต่อ สามารถ Fork และส่ง Pull Request มาได้เลย!
