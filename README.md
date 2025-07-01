# 🧠 Ebbinghaus Forgetting Curve Visualization
## Pics
![image](https://github.com/user-attachments/assets/579cea9e-13f6-4f86-b2ec-691b57ec8e63)
![image](https://github.com/user-attachments/assets/d262d056-e6fa-413e-b5fa-526c3dcf69f0)
![image](https://github.com/user-attachments/assets/e12d71db-c03d-41c2-b6c8-88ab814f908b)
![image](https://github.com/user-attachments/assets/5c7a8fb0-9595-4001-9f14-24f640f72541)
![image](https://github.com/user-attachments/assets/2962cb1e-4e29-4b53-a2be-ee25735e1e70)
![image](https://github.com/user-attachments/assets/bf55fb9b-e4d1-41d4-8b2b-892d65a704bc)
![image](https://github.com/user-attachments/assets/b673f09c-0cf0-44ae-aa03-5ffac46485dc)
![image](https://github.com/user-attachments/assets/f99e7cd4-5f9c-438e-a0ad-81e2ca64e179)

## 📖 Introduction
This Python project visualizes the **Ebbinghaus Forgetting Curve**, showing how humans forget information over time without review. It includes:
- 📊 2D & 3D static charts
- 🎞️ Animated 2D & 3D charts (with GIF export)
- 🧑‍💻 Friendly for non-coders

## ❓ What is the Forgetting Curve?
- The **forgetting curve** shows: Right after learning, you remember 100%. After 1 day, only ~34% remains. Without review, knowledge keeps fading.
- The chart helps you realize the importance of reviewing.

## 🚀 Usage

### 1. Install dependencies
```bash
pip install matplotlib numpy pillow
```

### 2. Run the scripts
- **2D & 3D static:**
  - `pydata/ebbinghaus_curve.py`
- **2D animation:**
  - `pydata/ebbinghaus_curve_animation.py`
- **3D animation (auto-export GIF):**
  - `pydata/ebbinghaus_curve_animation_3d.py`

```bash
python pydata/ebbinghaus_curve.py
python pydata/ebbinghaus_curve_animation.py
python pydata/ebbinghaus_curve_animation_3d.py
```

### 3. 🎬 GIF Export
- When running `ebbinghaus_curve_animation_3d.py`, a GIF file is created: `ebbinghaus_curve_3d.gif`
- Open this file to view the animation without running Python again.

## 📝 Data Explanation
- **labels:** Time after learning (0 min, 20 min, 1 hour, ...)
- **memory_percent:** Remaining memory (%)
- **Animation:** Dynamic effect helps visualize the forgetting process.

---

## 👤 Author
[tranhao-wq](https://github.com/tranhao-wq) 
