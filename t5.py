'''绘制3D动画，两个任务绘制成功'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation

# 创建图形对象
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def draw_cube(ax, origin, x_len, y_len, z_len, face_color, edge_color='dimgray', alpha=0.3):
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

def update(frame):
    ax.cla()
    ax.set_xlim([0, 20])
    ax.set_ylim([0, 80])
    ax.set_zlim([0, 100])
    ax.set_xlabel('Time')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    if frame <= 10:
        # 长方体A：y方向长度为30，z方向长度为50
        draw_cube(ax, (0, 0, 0), frame, 30, 50, 'skyblue', edge_color='darkgrey', alpha=0.5)
        # 长方体B：y方向长度为50，z方向长度为50
        draw_cube(ax, (0, 30, 50), frame, 50, 50, 'lightgreen', edge_color='darkgrey', alpha=0.5)
    elif frame > 10:
        # 在时间x=10时，长方体B从原来的尺寸变化为新的尺寸
        draw_cube(ax, (0, 0, 0), 10, 30, 50, 'skyblue', edge_color='darkgrey', alpha=0.5)  # 长方体A
        draw_cube(ax, (0, 30, 50), 10, 50, 50, 'lightgreen', edge_color='darkgrey', alpha=0.5)  # 长方体B原尺寸
        # 新尺寸长方体B，从x=10位置开始
        draw_cube(ax, (10, 0, 0), frame - 10, 80, 100, 'lightgreen', edge_color='darkgrey', alpha=0.5)

# 创建动画
ani = FuncAnimation(fig, update, frames=np.linspace(0, 20, 200), interval=100)

plt.show()
