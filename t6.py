import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation

# 创建图形对象
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 定义长方体属性和绘制函数
cubes = []

def draw_cube(ax, origin, x_len, y_len, z_len, face_color, label, edge_color='dimgray', alpha=0.5):
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

    # 在长方体的中心位置添加文本标签
    ax.text(x + x_len / 2, y + y_len / 2, z + z_len / 2, label, color='black', ha='center', va='center')

def check_limits(y_start, y_len, z_start, z_len):
    if y_start + y_len > 8 or z_start + z_len > 10:
        raise ValueError("Memory or CPU limit exceeded!")

def update(frame):
    ax.cla()
    ax.set_xlim([0, 15])
    ax.set_ylim([0, 8])
    ax.set_zlim([0, 10])
    ax.set_xlabel('Time')
    ax.set_ylabel('Memory (scaled down by 10)')
    ax.set_zlabel('CPU (scaled down by 10)')

    if frame <= 3:
        check_limits(0, 2, 0, 4)
        draw_cube(ax, (0, 0, 0), frame, 2, 4, 'skyblue', 'Task A: 01', edge_color='darkgrey', alpha=0.5)  # 长方体A
        check_limits(2, 2, 4, 4)
        draw_cube(ax, (0, 2, 4), frame, 2, 4, 'lightgreen', 'Task B: 11', edge_color='darkgrey', alpha=0.5)  # 长方体B
        check_limits(4, 4, 8, 2)
        draw_cube(ax, (0, 4, 8), frame, 4, 2, 'lightcoral', 'Task C: 00', edge_color='darkgrey', alpha=0.5)  # 长方体C
    elif frame <= 7:
        # 时间间隔[0, 3]的长方体
        draw_cube(ax, (0, 0, 0), 3, 2, 4, 'skyblue', 'Task A: 01', edge_color='darkgrey', alpha=0.5)  # 长方体A
        draw_cube(ax, (0, 2, 4), 3, 2, 4, 'lightgreen', 'Task B: 11', edge_color='darkgrey', alpha=0.5)  # 长方体B
        draw_cube(ax, (0, 4, 8), 3, 4, 2, 'lightcoral', 'Task C: 00', edge_color='darkgrey', alpha=0.5)  # 长方体C

        # 时间间隔[3, 7]的长方体
        check_limits(0, 4, 0, 4)
        draw_cube(ax, (3, 0, 0), frame - 3, 4, 4, 'skyblue', 'Task A: 01', edge_color='darkgrey', alpha=0.5)  # 长方体A
        check_limits(4, 4, 4, 6)
        draw_cube(ax, (3, 4, 4), frame - 3, 4, 6, 'lightgreen', 'Task B: 11', edge_color='darkgrey', alpha=0.5)  # 长方体B
    elif frame <= 13:
        # 时间间隔[0, 3]的长方体
        draw_cube(ax, (0, 0, 0), 3, 2, 4, 'skyblue', 'Task A: 01', edge_color='darkgrey', alpha=0.5)  # 长方体A
        draw_cube(ax, (0, 2, 4), 3, 2, 4, 'lightgreen', 'Task B: 11', edge_color='darkgrey', alpha=0.5)  # 长方体B
        draw_cube(ax, (0, 4, 8), 3, 4, 2, 'lightcoral', 'Task C: 00', edge_color='darkgrey', alpha=0.5)  # 长方体C

        # 时间间隔[3, 7]的长方体
        draw_cube(ax, (3, 0, 0), 4, 4, 4, 'skyblue', 'Task A: 01', edge_color='darkgrey', alpha=0.5)  # 长方体A
        draw_cube(ax, (3, 4, 4), 4, 4, 6, 'lightgreen', 'Task B: 11', edge_color='darkgrey', alpha=0.5)  # 长方体B

        # 时间间隔[7, 13]的长方体
        check_limits(0, 4, 0, 4)
        draw_cube(ax, (7, 0, 0), frame - 7, 4, 4, 'skyblue', 'Task A: 01', edge_color='darkgrey', alpha=0.5)  # 长方体A
        check_limits(4, 1, 4, 6)
        draw_cube(ax, (7, 4, 4), frame - 7, 1, 6, 'plum', 'Task D: 10', edge_color='darkgrey', alpha=0.5)  # 长方体D
    elif frame <= 15:
        # 时间间隔[0, 3]的长方体
        draw_cube(ax, (0, 0, 0), 3, 2, 4, 'skyblue', 'Task A: 01', edge_color='darkgrey', alpha=0.5)  # 长方体A
        draw_cube(ax, (0, 2, 4), 3, 2, 4, 'lightgreen', 'Task B: 11', edge_color='darkgrey', alpha=0.5)  # 长方体B
        draw_cube(ax, (0, 4, 8), 3, 4, 2, 'lightcoral', 'Task C: 00', edge_color='darkgrey', alpha=0.5)  # 长方体C

        # 时间间隔[3, 7]的长方体
        draw_cube(ax, (3, 0, 0), 4, 4, 4, 'skyblue', 'Task A: 01', edge_color='darkgrey', alpha=0.5)  # 长方体A
        draw_cube(ax, (3, 4, 4), 4, 4, 6, 'lightgreen', 'Task B: 11', edge_color='darkgrey', alpha=0.5)  # 长方体B

        # 时间间隔[7, 13]的长方体
        draw_cube(ax, (7, 0, 0), 6, 4, 4, 'skyblue', 'Task A: 01', edge_color='darkgrey', alpha=0.5)  # 长方体A
        draw_cube(ax, (7, 4, 4), 6, 1, 6, 'plum', 'Task D: 10', edge_color='darkgrey', alpha=0.5)  # 长方体D

        # 时间间隔[13, 15]的长方体
        check_limits(0, 1, 0, 10)
        draw_cube(ax, (13, 0, 0), frame - 13, 1, 10, 'plum', 'Task D: 10', edge_color='darkgrey', alpha=0.5)  # 长方体D

# 创建动画
ani = FuncAnimation(fig, update, frames=np.linspace(0, 15, 150), interval=100)

plt.show()
