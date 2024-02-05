import numpy as np
import matplotlib.pyplot as plt

# 定义 sech 函数
def sech(x):
    return 2 / (np.exp(x) + np.exp(-x))

def tanh(x):
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

def ddxsech(x):
    return -sech(x) * tanh(x)

# 生成 x 范围
x = np.linspace(-5, 5, 100)

# 计算 sech 函数的值
y = sech(x)

# 绘制 sech 函数的图形
plt.plot(x, y, label='sech(x)', color = 'black')

# 绘制直线 y = 3
plt.plot(x, np.full_like(x, 3), linestyle='--', label='y = 3')


xs = np.linspace(-5, 5, 10)
ys = np.linspace(0, 3, 11)
for x in xs:
    for y in ys:
        if y <= sech(x) or y >= 3:
            continue
        length_x = 0.2 / (1 + np.exp(-y + sech(x)))
        length_y = length_x * ddxsech(x) / (1 + 10 * np.exp(-y + sech(x)))
        plt.quiver(x, y, length_x, length_y, angles='xy', scale_units='xy', scale=0.5, width=0.002, color = "deepskyblue")


# 添加图例
# plt.legend()

# 添加标题和坐标轴标签
plt.title('Current Example')
plt.xlabel('x')
plt.ylabel('Function value')

# 显示网格
plt.grid(True)

# 显示图形
plt.show()
