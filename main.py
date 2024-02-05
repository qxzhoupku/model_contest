import xarray as xr
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


os.chdir(os.path.dirname(__file__))

# 读取GMT v3兼容的NetCDF文件
file_path = "../GMRTv4_2_20240205topo.grd"  # 替换为你的NetCDF文件路径
dataset = xr.open_dataset(file_path, engine='scipy')

# 打印数据集的信息
print(dataset)

# 打印各个变量的值
print("x_range:", dataset['x_range'].values)
print("y_range:", dataset['y_range'].values)
print("dimension:", dataset['dimension'].values)
print("dimension product:", np.prod(dataset['dimension'].values))
print("spacing:", dataset['spacing'].values)
print("z.shape:", dataset['z'].shape)
print("z:", dataset['z'].values)
print(dataset['z'].shape)  # 打印数据数组的形状


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
surf = ax.plot_surface(x_grid, y_grid, z_grid, cmap='viridis')

# 翻转 y 轴方向
# plt.gca().invert_xaxis()

# 添加标签和标题
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_title('3D Surface Plot')

# 显示图形
plt.show()
