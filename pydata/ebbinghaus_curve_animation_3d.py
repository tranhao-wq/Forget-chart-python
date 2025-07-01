import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.cm as cm

# Dữ liệu Ebbinghaus Forgetting Curve
labels = [
    "0 phút", "20 phút", "1 giờ", "9 giờ", "1 ngày", "2 ngày", "6 ngày", "31 ngày"
]
time_hours = [0, 1/3, 1, 9, 24, 48, 144, 744]
memory_percent = [100, 58, 44, 36, 34, 27, 25, 21]
z = np.zeros_like(time_hours)

colors = cm.viridis(np.linspace(0, 1, len(time_hours)))

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-10, 760)
ax.set_ylim(15, 105)
ax.set_zlim(-1, 1)
ax.set_xticks(time_hours)
ax.set_xticklabels(labels, rotation=30, ha='right', fontsize=10)
ax.set_xlabel('Thời gian sau khi học (từ 0 phút đến 31 ngày)', labelpad=15)
ax.set_ylabel('Tỷ lệ nhớ thông tin (%)')
ax.set_zlabel('Trục phụ (z)')
ax.set_title('Đường cong quên lãng 3D: Con người quên dần kiến thức theo thời gian nếu không ôn lại', fontsize=13)

# Giải thích ý nghĩa dưới biểu đồ
fig.subplots_adjust(bottom=0.18)
fig.text(0.5, 0.04,
    "Biểu đồ cho thấy: Ngay sau khi học, ta nhớ 100%. Sau 1 ngày chỉ còn nhớ ~34%. "
    "Nếu không ôn lại, kiến thức sẽ tiếp tục giảm dần.",
    wrap=True, horizontalalignment='center', fontsize=11)

line, = ax.plot([], [], [], color='royalblue', marker='o', label='Tỷ lệ nhớ', linewidth=2)
scatter = None
point_annot = None

# Animation function
def animate(i):
    global scatter, point_annot
    x = time_hours[:i+1]
    y = memory_percent[:i+1]
    z_vals = np.zeros_like(x)
    line.set_data(x, y)
    line.set_3d_properties(z_vals)
    # Remove previous scatter and annotation
    if scatter is not None:
        scatter.remove()
    if point_annot is not None:
        point_annot.remove()
    # Hiệu ứng: điểm chuyển màu, điểm mới nhất lớn hơn
    sizes = [60]*(i) + [120]  # điểm mới nhất lớn hơn
    scatter = ax.scatter(x, y, z_vals, color=colors[:i+1], s=sizes, zorder=5)
    # Chú thích động cho các mốc đặc biệt
    if labels[i] in ["0 phút", "1 ngày", "31 ngày"]:
        point_annot = ax.text(x[-1], y[-1], 0.2, f"{labels[i]}: {y[-1]}% nhớ", color='red', fontsize=10, bbox=dict(boxstyle='round,pad=0.3', fc='yellow', alpha=0.7))
    else:
        point_annot = None
    return line,

ani = animation.FuncAnimation(fig, animate, frames=len(time_hours), interval=1200, blit=False, repeat=False)

ax.legend()
ani.save('ebbinghaus_curve_3d.gif', writer='pillow', fps=1)
plt.show() 