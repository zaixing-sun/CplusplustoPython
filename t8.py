import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

FONTSIZE = 10
ALPHA = 0.75
# 设置全局字体和刻度
plt.rc('font', family='Times New Roman', size=FONTSIZE)
plt.rc('xtick', labelsize=FONTSIZE)
plt.rc('ytick', labelsize=FONTSIZE)

# 创建图形对象
fig = plt.figure(figsize=(14, 8))

# 添加3D子图用于绘制长方体动画
ax1 = fig.add_subplot(121, projection='3d')

# 添加2D子图用于绘制y方向总和随时间变化的曲线
ax2 = fig.add_axes([0.6, 0.55, 0.2, 0.2])
ax2.set_xlabel('Time')
ax2.set_ylabel('Memory Usage (%)')
ax2.set_ylim([0, 105])
ax2.set_xlim([0, 14])

# 指定 x 轴刻度显示的数字
ax2.set_xticks([0, 2, 4, 6, 8, 10, 12, 14])
ax2.set_xticklabels(['0', '2', '4', '6', '8', '10', '12', '14'])

# 指定 y 轴刻度显示的数字
ax2.set_yticks([0, 20, 40, 60, 80, 100])
ax2.set_yticklabels(['0', '20', '40', '60', '80', '100'])

# 添加2D子图用于绘制z方向总和随时间变化的曲线
ax3 = fig.add_axes([0.6, 0.2, 0.2, 0.2])
ax3.set_xlabel('Time')
ax3.set_ylabel('CPU Usage (%)')
ax3.set_ylim([0, 105])
ax3.set_xlim([0, 14])

# 指定 x 轴刻度显示的数字
ax3.set_xticks([0, 2, 4, 6, 8, 10, 12, 14])
ax3.set_xticklabels(['0', '2', '4', '6', '8', '10', '12', '14'])

# 指定 y 轴刻度显示的数字
ax3.set_yticks([0, 20, 40, 60, 80, 100])
ax3.set_yticklabels(['0', '20', '40', '60', '80', '100'])


# 初始化存储随时间变化的总和
time_data = np.linspace(0, 14, 140)
memory_usage = np.zeros_like(time_data)
cpu_usage = np.zeros_like(time_data)

def draw_cube(ax, origin, x_len, y_len, z_len, face_color, edge_color='dimgray', alpha=ALPHA):
    x, y, z = origin
    vertices = np.array([[x, y, z],
                         [x + x_len, y, z],
                         [x + x_len, y + y_len, z],
                         [x, y + y_len, z],
                         [x, y, z + z_len],
                         [x + x_len, y, z + z_len],
                         [x + x_len, y + y_len, z + z_len],
                         [x, y + y_len, z + z_len]])

    edges = [[vertices[j] for j in [0, 1, 2, 3]],
             [vertices[j] for j in [4, 5, 6, 7]],
             [vertices[j] for j in [0, 1, 5, 4]],
             [vertices[j] for j in [2, 3, 7, 6]],
             [vertices[j] for j in [1, 2, 6, 5]],
             [vertices[j] for j in [4, 7, 3, 0]]]

    faces = Poly3DCollection(edges, linewidths=1, edgecolors=edge_color, alpha=alpha, facecolors=face_color)
    ax.add_collection3d(faces)

    return (x + x_len / 2, y + y_len / 5 , z + z_len ) #  + 0.5

def check_limits(y_start, y_len, z_start, z_len):
    if y_start + y_len > 8 or z_start + z_len > 10:
        raise ValueError("Memory or CPU limit exceeded!")

def update(frame):
    ax1.cla()
    ax1.set_xlim([0, 14])
    ax1.set_ylim([0, 8])
    ax1.set_zlim([0, 10])
    ax1.set_xlabel('Time', fontdict={'family': 'Times New Roman', 'size': FONTSIZE})
    ax1.set_ylabel('Memory', fontdict={'family': 'Times New Roman', 'size': FONTSIZE})
    ax1.set_zlabel('CPU', fontdict={'family': 'Times New Roman', 'size': FONTSIZE})

    total_memory = 0
    total_cpu = 0
    labels = []

    if frame <= 20:
        t = frame / 10
        check_limits(0, 1, 0, 10)
        labels.append((*draw_cube(ax1, (0, 0, 0), t, 1, 10, 'plum', edge_color='darkgrey', alpha=ALPHA), 'Task A: 10'))
        total_memory = 1
        total_cpu = 10
    elif frame <= 80:
        t = (frame - 20) / 10
        labels.append((*draw_cube(ax1, (0, 0, 0), 2, 1, 10, 'plum', edge_color='darkgrey', alpha=ALPHA), 'Task A: 10'))
        check_limits(0, 4, 0, 4)
        labels.append((*draw_cube(ax1, (2, 0, 0), t, 4, 4, 'skyblue', edge_color='darkgrey', alpha=ALPHA), 'Task B: 01'))
        check_limits(4, 1, 4, 6)
        labels.append((*draw_cube(ax1, (2, 4, 4), t, 1, 6, 'plum', edge_color='darkgrey', alpha=ALPHA), 'Task A: 10'))
        total_memory = 5
        total_cpu = 10
    elif frame <= 120:
        t = (frame - 80) / 10
        labels.append((*draw_cube(ax1, (0, 0, 0), 2, 1, 10, 'plum', edge_color='darkgrey', alpha=ALPHA), 'Task A: 10'))
        labels.append((*draw_cube(ax1, (2, 0, 0), 6, 4, 4, 'skyblue', edge_color='darkgrey', alpha=ALPHA), 'Task B: 01'))   
        labels.append((*draw_cube(ax1, (2, 4, 4), 6, 1, 6, 'plum', edge_color='darkgrey', alpha=ALPHA), 'Task A: 10'))
        check_limits(0, 4, 0, 4)
        labels.append((*draw_cube(ax1, (8, 0, 0), t, 4, 4, 'skyblue', edge_color='darkgrey', alpha=ALPHA), 'Task B: 01'))   
        check_limits(4, 4, 4, 6)
        labels.append((*draw_cube(ax1, (8, 4, 4), t, 4, 6, 'lightgreen', edge_color='darkgrey', alpha=ALPHA), 'Task C: 11'))
        total_memory = 8
        total_cpu = 10
    elif frame <= 140:
        t = (frame - 120) / 10
        labels.append((*draw_cube(ax1, (0, 0, 0), 2, 1, 10, 'plum', edge_color='darkgrey', alpha=ALPHA), 'Task A: 10'))
        labels.append((*draw_cube(ax1, (2, 0, 0), 6, 4, 4, 'skyblue', edge_color='darkgrey', alpha=ALPHA), 'Task B: 01'))   
        labels.append((*draw_cube(ax1, (2, 4, 4), 6, 1, 6, 'plum', edge_color='darkgrey', alpha=ALPHA), 'Task A: 10'))        
        labels.append((*draw_cube(ax1, (8, 0, 0), 4, 4, 4, 'skyblue', edge_color='darkgrey', alpha=ALPHA), 'Task B: 01'))   
        labels.append((*draw_cube(ax1, (8, 4, 4), 4, 4, 6, 'lightgreen', edge_color='darkgrey', alpha=ALPHA), 'Task C: 11'))
        check_limits(0, 2, 0, 4)
        labels.append((*draw_cube(ax1, (12, 0, 0), t, 2, 4, 'skyblue', edge_color='darkgrey', alpha=ALPHA), 'Task B: 01')) 
        check_limits(2, 2, 4, 4)
        labels.append((*draw_cube(ax1, (12, 2, 4), t, 2, 4, 'lightgreen', edge_color='darkgrey', alpha=ALPHA), 'Task C: 11'))  
        check_limits(4, 4, 8, 2)
        labels.append((*draw_cube(ax1, (12, 4, 8), t, 4, 2, 'lightcoral', edge_color='darkgrey', alpha=ALPHA), 'Task D: 00'))
        total_memory = 8
        total_cpu = 10

    for label in labels:
        ax1.text(label[0], label[1], label[2], label[3], color='black', ha='center', va='bottom', zorder=10, fontdict={'family': 'Times New Roman', 'size': FONTSIZE})

    memory_usage[frame] = (total_memory / 8) * 100
    cpu_usage[frame] = (total_cpu / 10) * 100

    # 清除并更新内存使用曲线
    ax2.cla()
    ax2.set_xlabel('Time', fontdict={'family': 'Times New Roman', 'size': FONTSIZE})
    ax2.set_ylabel('Total Memory Usage (%)', fontdict={'family': 'Times New Roman', 'size': FONTSIZE})
    ax2.set_ylim([0, 105])
    ax2.set_xlim([0, 14])
    ax2.plot(time_data[:frame+1], memory_usage[:frame+1], color='blue')
    ax2.set_title('Total Memory Usage (%)', fontdict={'family': 'Times New Roman', 'size': FONTSIZE})

    # 清除并更新CPU使用曲线
    ax3.cla()
    ax3.set_xlabel('Time', fontdict={'family': 'Times New Roman', 'size': FONTSIZE})
    ax3.set_ylabel('Total CPU Usage (%)', fontdict={'family': 'Times New Roman', 'size': FONTSIZE})
    ax3.set_ylim([0, 105])
    ax3.set_xlim([0, 14])
    ax3.plot(time_data[:frame+1], cpu_usage[:frame+1], color='red')
    ax3.set_title('Total CPU Usage (%)', fontdict={'family': 'Times New Roman', 'size': FONTSIZE})

    ax1.tick_params(axis='both', which='major', labelsize=FONTSIZE)
    ax2.tick_params(axis='both', which='major', labelsize=FONTSIZE)
    ax3.tick_params(axis='both', which='major', labelsize=FONTSIZE)

# 创建动画
ani = FuncAnimation(fig, update, frames=len(time_data), interval=100)

plt.tight_layout()
plt.show()

# def plot_max_range(ax):
#     # 绘制 y 轴方向的最大范围矩形
#     y_max_rect = np.array([[0, 0, 0],
#                            [14, 0, 0],
#                            [14, 8, 0],
#                            [0, 8, 0],
#                            [0, 0, 0]])
#     ax.plot(y_max_rect[:,0], y_max_rect[:,1], y_max_rect[:,2], color='red', alpha=ALPHA)

#     # 绘制 z 轴方向的最大范围矩形
#     z_max_rect = np.array([[0, 0, 0],
#                            [14, 0, 0],
#                            [14, 0, 10],
#                            [0, 0, 10],
#                            [0, 0, 0]])
#     ax.plot(z_max_rect[:,0], z_max_rect[:,1], z_max_rect[:,2], color='red', alpha=ALPHA)

# 定义函数来绘制最终静态图像
def plot_final_frame():
    ax1.set_xlim([0, 14])
    ax1.set_ylim([0, 8])
    ax1.set_zlim([0, 10])
    ax1.set_xlabel('Time', fontname='Times New Roman')
    ax1.set_ylabel('Memory', fontname='Times New Roman')
    ax1.set_zlabel('CPU', fontname='Times New Roman')
    ax1.tick_params(axis='both', which='major', labelsize=FONTSIZE)

    # # 指定 x 轴刻度显示的数字
    # ax1.set_xticks([0, 1, 3, 5, 7, 9, 11, 13, 14])
    # ax1.set_xticklabels(['0', '1', '3', '5', '7', '9', '11', '13', '14'])

    # # 绘制最大范围矩形
    # plot_max_range(ax1)

    total_memory = 0
    total_cpu = 0
    labels = []

    # 时间间隔 [0, 3]
    t = 2
    labels.append((*draw_cube(ax1, (0, 0, 0), t, 1, 10, 'plum', edge_color='darkgrey', alpha=ALPHA), 'Task A: 10'))

    # 时间间隔 [3, 7]
    t = 6
    labels.append((*draw_cube(ax1, (2, 4, 4), t, 1, 6, 'plum', edge_color='darkgrey', alpha=ALPHA), 'Task A: 10'))
    labels.append((*draw_cube(ax1, (2, 0, 0), t, 4, 4, 'skyblue', edge_color='darkgrey', alpha=ALPHA), 'Task B: 01'))

    # 时间间隔 [7, 13]
    t = 4
    labels.append((*draw_cube(ax1, (8, 0, 0), t, 4, 4, 'skyblue', edge_color='darkgrey', alpha=ALPHA), 'Task B: 01'))   
    labels.append((*draw_cube(ax1, (8, 4, 4), t, 4, 6, 'lightgreen', edge_color='darkgrey', alpha=ALPHA), 'Task C: 11'))

    # 时间间隔 [13, 14]
    t = 2
    labels.append((*draw_cube(ax1, (12, 0, 0), t, 2, 4, 'skyblue', edge_color='darkgrey', alpha=ALPHA), 'Task B: 01')) 
    labels.append((*draw_cube(ax1, (12, 2, 4), t, 2, 4, 'lightgreen', edge_color='darkgrey', alpha=ALPHA), 'Task C: 11'))  
    labels.append((*draw_cube(ax1, (12, 4, 8), t, 4, 2, 'lightcoral', edge_color='darkgrey', alpha=ALPHA), 'Task D: 00'))

    for label in labels:
        ax1.text(label[0], label[1], label[2], label[3], color='black', ha='center', va='bottom', zorder=10, fontname='Times New Roman')

    # 设置纵向压缩比例
    ax1.get_proj = lambda: np.dot(Axes3D.get_proj(ax1), np.diag([1, 1, 0.75, 1]))

    # 更新 memory_usage 和 cpu_usage 数组
    for i, t in enumerate(time_data):
        if t <= 2:
            memory_usage[i] = (1 / 8) * 100
            cpu_usage[i] = (10 / 10) * 100
        elif t <= 8:
            memory_usage[i] = (5 / 8) * 100
            cpu_usage[i] = (10 / 10) * 100
        elif t <= 12:
            memory_usage[i] = (8 / 8) * 100
            cpu_usage[i] = (10 / 10) * 100
        else:
            memory_usage[i] = (8 / 8) * 100
            cpu_usage[i] = (10 / 10) * 100

    # 绘制内存使用曲线
    ax2.plot(time_data, memory_usage, color='blue')
    # ax2.set_title('Total Memory Usage (%)', fontname='Times New Roman')

    # 绘制CPU使用曲线
    ax3.plot(time_data, cpu_usage, color='red')
    # ax3.set_title('Total CPU Usage (%)', fontname='Times New Roman')

# 定义旋转函数
def rotate(angle):
    ax1.view_init(elev=30, azim=angle)

# # 开启交互模式
# plt.ion()


# 绘制最终静态图像
plot_final_frame()

# 创建旋转动画
# ani = FuncAnimation(fig, rotate, frames=np.arange(0, 360, 2), interval=100)

plt.tight_layout()

plt.show()
# # 关闭交互模式
# plt.ioff()