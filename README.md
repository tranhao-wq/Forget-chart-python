# 🧠 Ebbinghaus Forgetting Curve Visualization

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