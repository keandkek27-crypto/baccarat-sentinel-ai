import engine_core
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    history = []
    
    while True:
        clear_screen()
        print("="*60)
        print("   🃏 BACCARAT SENTINEL (MULTI-INPUT) v2.3")
        print("   [ P = Player | B = Banker | T = Tie ]") # เพิ่มคำอธิบายตรงนี้
        print("="*60)
        
        # แสดงประวัติ
        history_str = " ".join(history[-20:]) if history else "ยังไม่มีข้อมูล"
        print(f"🕒 ประวัติ ({len(history)} ตา): {history_str}")
        print("-" * 60)

        if history:
            # วิเคราะห์ Pattern และความน่าจะเป็น
            pattern = engine_core.analyze_pattern(history)
            print(f"🔍 วิเคราะห์เค้าไพ่: {pattern}")

            probs = engine_core.calculate_probability(history)
            print(f"📊 โอกาสชนะ: [P: {probs['Player']}%] | [B: {probs['Banker']}%] | [T: {probs['Tie']}%]")

            score = engine_core.calculate_secret_score(len(history))
            print("-" * 60)
            if score > 65:
                print(f"🚀 คำแนะนำ: >> [ BANKER 🔴 ] << (Confidence: {score}%)")
            elif score < 35:
                print(f"🚀 คำแนะนำ: >> [ PLAYER 🔵 ] << (Confidence: {100-score}%)")
            else:
                print(f"🚀 คำแนะนำ: >> [ ⚠️ รอจังหวะ 🟢 ] <<")
        
        print("-" * 60)
        print("💡 ใส่ผลลัพธ์: พิมพ์ติดกันได้เลย เช่น 'ppbpt'")
        print("กด [ u ]=ย้อนกลับ | [ c ]=ล้างทั้งหมด | [ q ]=ออก")
        raw_input = input("กรอกข้อมูล: ").lower().strip()

        if raw_input == 'q':
            break
        if raw_input == 'c':
            history = []
            continue
        if raw_input == 'u': # ระบบ Undo
            if history:
                history.pop()
            continue

        # จัดการกับ Input แบบชุด
        valid_chars = {'p', 'b', 't'}
        new_entries = []
        
        for char in raw_input:
            if char in valid_chars:
                new_entries.append(char.upper())
        
        if new_entries:
            history.extend(new_entries)
        else:
            if raw_input != 'u': # กันกรณีลบแล้วขึ้นเตือน
                print("⚠️ ข้อมูลไม่ถูกต้อง! กรุณาใช้ p, b หรือ t")
                time.sleep(0.8)

if __name__ == "__main__":
    main()