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
        print("   🃏 BACCARAT SENTINEL (TIE EDITION) v2.1")
        print("="*60)
        
        # แสดงประวัติ
        history_str = " ".join(history[-15:]) if history else "ยังไม่มีข้อมูล"
        print(f"🕒 ประวัติล่าสุด: {history_str}")
        print("-" * 60)

        if history:
            # วิเคราะห์ Pattern
            pattern = engine_core.analyze_pattern(history)
            print(f"🔍 วิเคราะห์เค้าไพ่: {pattern}")

            # วิเคราะห์ความน่าจะเป็น
            probs = engine_core.calculate_probability(history)
            print(f"📊 โอกาสชนะ: [P: {probs['Player']}%] | [B: {probs['Banker']}%] | [T: {probs['Tie']}%]")

            # คำแนะนำ
            score = engine_core.calculate_secret_score(len(history))
            print("-" * 60)
            if score > 60:
                print(f"🚀 คำแนะนำ: >> [ BANKER 🔴 ] << (Confidence: {score}%)")
            elif score < 40:
                print(f"🚀 คำแนะนำ: >> [ PLAYER 🔵 ] << (Confidence: {100-score}%)")
            else:
                print(f"🚀 คำแนะนำ: >> [ ⚠️ เสมอ/รอจังหวะ 🟢 ] <<")
        
        print("-" * 60)
        print("กด [ p ]=PLAYER | [ b ]=BANKER | [ t ]=TIE | [ c ]=CLEAR | [ q ]=EXIT")
        choice = input("กรอกผลล่าสุด: ").lower()

        if choice == 'p':
            history.append('P')
        elif choice == 'b':
            history.append('B')
        elif choice == 't':
            history.append('T')
        elif choice == 'c':
            history = []
            print("ล้างข้อมูลแล้ว...")
            time.sleep(0.5)
        elif choice == 'q':
            break
        else:
            print("กรอกผิด!")
            time.sleep(0.5)

if __name__ == "__main__":
    main()