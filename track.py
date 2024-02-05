import xarray as xr
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


os.chdir(os.path.dirname(__file__))

# 读取GMT v3兼容的NetCDF文件
file_path = "../GMRTv4_2_20240205topo.grd"  # 替换为你的NetCDF文件路径
dataset = xr.open_dataset(file_path, engine='scipy')

# 获取 x 轴和 y 轴的范围和间距
x_start, x_end = dataset['x_range'][0], dataset['x_range'][1]
y_start, y_end = dataset['y_range'][0], dataset['y_range'][1]
x_spacing, y_spacing = dataset['spacing'][0], dataset['spacing'][1]

# 根据范围和间距创建 x 和 y 的格点
x = np.linspace(x_start, x_end, dataset['dimension'].values[0])
y = np.linspace(y_start, y_end, dataset['dimension'].values[1])
y = np.flipud(y)

# 将 x 和 y 轴的格点转换为二维数组
x_grid, y_grid = np.meshgrid(x, y)

# 获取 z 轴的数据
z_data = dataset['z'].values

# 将 z 轴的数据按照网格大小重新排列成二维数组
z_grid = z_data.reshape(len(y), len(x))

# 创建 3D 图形对象
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制 3D 表面图
surf = ax.plot_surface(x_grid, y_grid, z_grid, cmap='viridis', alpha = 0.5)

# 添加标签和标题
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_zlabel('Altitude/m')
ax.set_title('Ocean Current and submersible track')

# 指定要绘制洋流的位置，这里简单地使用网格点的四分之一位置
num_points = 20  # 指定要绘制的点数
x_indices = np.linspace(0, len(x) - 1, num_points, dtype=int)
y_indices = np.linspace(0, len(y) - 1, num_points, dtype=int)
selected_positions = [(x_idx, y_idx) for x_idx in x_indices for y_idx in y_indices]

# 洋流速度
u_velocity = np.ones(len(selected_positions)) * -0.05  # 沿 x 方向的洋流速度为0.05
v_velocity = np.ones(len(selected_positions)) * 0.05

# 在海平面上绘制洋流矢量箭头
for pos_index, (i, j) in enumerate(selected_positions):
    length_0 = np.sqrt(x_grid[i, j]**2 + y_grid[i, j]**2) / 100 * np.random.uniform(0.8, 1.2) / np.sqrt(30 + np.abs(z_grid[i, j]))
    if z_grid[i, j] >= 0:
        continue
    ax.quiver(x_grid[i, j], y_grid[i, j], 0, u_velocity[pos_index]* np.random.uniform(0.7, 1.3), v_velocity[pos_index]* np.random.uniform(0.7, 1.3), 0, length = length_0, normalize=True, color='deepskyblue', arrow_length_ratio=0.2)
        

# 显示图形
# plt.show()

pos = [20.4, 38.4, 0]
x_list = []
y_list = []
z_list = []
for i in range(450):
    pos[0] += -0.05 * np.random.uniform(-0.3, 1.2) / 100
    pos[1] += 0.05 * np.random.uniform(-0.3, 1.2) / 100
    pos[2] -= 500 * np.random.uniform(-0.3, 1.2) / 100 * 3
    x_list.append(pos[0])
    y_list.append(pos[1])
    z_list.append(pos[2])

ax.plot(x_list, y_list, z_list, color = "red")

plt.show()