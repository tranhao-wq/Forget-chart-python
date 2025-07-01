import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Dữ liệu Ebbinghaus Forgetting Curve
labels = [
    "0 phút", "20 phút", "1 giờ", "9 giờ", "1 ngày", "2 ngày", "6 ngày", "31 ngày"
]
# Đổi thời gian về đơn vị giờ để dễ vẽ
time_hours = [0, 1/3, 1, 9, 24, 48, 144, 744]
memory_percent = [100, 58, 44, 36, 34, 27, 25, 21]

# --- Biểu đồ 2D ---
plt.figure(figsize=(10,5))
plt.plot(time_hours, memory_percent, marker='o', color='blue', label='Tỷ lệ nhớ')
plt.xticks(time_hours, labels, rotation=30, ha='right', fontsize=10)
plt.xlabel('Thời gian sau khi học (từ 0 phút đến 31 ngày)', labelpad=15)
plt.ylabel('Tỷ lệ nhớ thông tin (%)')
plt.title('Đường cong quên lãng: Con người quên dần kiến thức theo thời gian nếu không ôn lại', fontsize=13)
plt.grid(True)
plt.tight_layout(rect=[0, 0.10, 1, 1])

# Thêm chú thích giải thích ý nghĩa
plt.figtext(0.5, -0.08,
    "Biểu đồ cho thấy: Ngay sau khi học, ta nhớ 100%. Sau 1 ngày chỉ còn nhớ ~34%. "
    "Nếu không ôn lại, kiến thức sẽ tiếp tục giảm dần.",
    wrap=True, horizontalalignment='center', fontsize=11)

# Đánh dấu một số mốc quan trọng
for x, y, label in zip(time_hours, memory_percent, labels):
    if label in ["0 phút", "1 ngày", "31 ngày"]:
        plt.annotate(f"{y}%", (x, y), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10, color='red')

plt.legend()
plt.show()

# --- Biểu đồ 3D ---
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
z = np.zeros_like(time_hours)
ax.plot(time_hours, memory_percent, z, marker='o', label='Tỷ lệ nhớ')
ax.set_xlabel('Thời gian (giờ)')
ax.set_ylabel('Tỷ lệ nhớ (%)')
ax.set_zlabel('Trục phụ (z)')
ax.set_title('Đường cong quên lãng (3D)')
plt.show() 