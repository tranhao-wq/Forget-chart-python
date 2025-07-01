import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Dữ liệu Ebbinghaus Forgetting Curve
labels = [
    "0 phút", "20 phút", "1 giờ", "9 giờ", "1 ngày", "2 ngày", "6 ngày", "31 ngày"
]
time_hours = [0, 1/3, 1, 9, 24, 48, 144, 744]
memory_percent = [100, 58, 44, 36, 34, 27, 25, 21]

fig, ax = plt.subplots(figsize=(10,5))
ax.set_xlim(-10, 760)
ax.set_ylim(15, 105)
ax.set_xticks(time_hours)
ax.set_xticklabels(labels, rotation=30, ha='right', fontsize=10)
ax.set_xlabel('Thời gian sau khi học (từ 0 phút đến 31 ngày)', labelpad=15)
ax.set_ylabel('Tỷ lệ nhớ thông tin (%)')
ax.set_title('Đường cong quên lãng: Con người quên dần kiến thức theo thời gian nếu không ôn lại', fontsize=13)
ax.grid(True, linestyle='--', alpha=0.6)

# Giải thích ý nghĩa dưới biểu đồ
fig.subplots_adjust(bottom=0.22)
fig.text(0.5, 0.02,
    "Biểu đồ cho thấy: Ngay sau khi học, ta nhớ 100%. Sau 1 ngày chỉ còn nhớ ~34%. "
    "Nếu không ôn lại, kiến thức sẽ tiếp tục giảm dần.",
    wrap=True, horizontalalignment='center', fontsize=11)

line, = ax.plot([], [], color='royalblue', marker='o', label='Tỷ lệ nhớ', linewidth=2)
point_annot = ax.annotate('', xy=(0,0), xytext=(15,15), textcoords='offset points',
                         bbox=dict(boxstyle='round,pad=0.3', fc='yellow', alpha=0.7),
                         arrowprops=dict(arrowstyle='->', color='gray'), fontsize=10)
point_annot.set_visible(False)

# Animation function
def animate(i):
    x = time_hours[:i+1]
    y = memory_percent[:i+1]
    line.set_data(x, y)
    if i >= 0:
        ax.collections.clear()  # clear scatter
        ax.scatter(x, y, color='crimson', s=60, zorder=5)
        # Chú thích động cho các mốc đặc biệt
        if labels[i] in ["0 phút", "1 ngày", "31 ngày"]:
            point_annot.xy = (x[-1], y[-1])
            point_annot.set_text(f"{labels[i]}: {y[-1]}% nhớ")
            point_annot.set_visible(True)
        else:
            point_annot.set_visible(False)
    return line, point_annot

ani = animation.FuncAnimation(fig, animate, frames=len(time_hours), interval=1200, blit=False, repeat=False)

ax.legend()
plt.show() 