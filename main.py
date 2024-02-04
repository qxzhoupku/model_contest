import numpy as np
import matplotlib.pyplot as plt
import os
from osgeo import gdal
from osgeo import osr
from osgeo import ogr
from osgeo import gdal_array
from osgeo import gdalconst

# 切换到当前目录
os.chdir(os.path.dirname(__file__))
print(os.getcwd())

# 打开.grd文件
dataset = gdal.Open('GMRTv4_2_20240202topo.tif')

# 读取数据
band = dataset.GetRasterBand(1)
data = band.ReadAsArray()

# 获取地理坐标信息
geotransform = dataset.GetGeoTransform()
x_origin = geotransform[0]
y_origin = geotransform[3]
pixel_width = geotransform[1]
pixel_height = geotransform[5]

# 打印数据信息
print('数据大小:', data.shape)
print('地理坐标原点:', x_origin, y_origin)
print('像素宽度:', pixel_width)
print('像素高度:', pixel_height)

# 创建地理坐标网格
x_size = dataset.RasterXSize
y_size = dataset.RasterYSize
x_end = x_origin + x_size * pixel_width
y_end = y_origin + y_size * pixel_height
x = np.linspace(x_origin, x_end, x_size)
y = np.linspace(y_origin, y_end, y_size)

# 绘制图像
plt.imshow(data, extent=[x_origin, x_end, y_origin, y_end], cmap='terrain')
plt.colorbar(label='Depth (meters)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Depth Map')
plt.show()

# 关闭数据集
dataset = None
