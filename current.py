import numpy as np
import matplotlib.pyplot as plt
import os
import gsw

os.chdir(os.path.dirname(__file__))

N_X = 100
N_Y = 100
N_Z = 10

def get_index(x, y, z):
    return x * N_Y * N_Z + y * N_Z + z

class Site(object):
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z
        self.__vx = 0
        self.__vy = 0
        self.__vz = 0
        self.__salinity = 0
        self.__temperature = 0
    
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def get_z(self):
        return self.__z

    def set_vx(self, vx):
        self.__vx = vx
    
    def set_vy(self, vy):
        self.__vy = vy
    
    def set_vz(self, vz):
        self.__vz = vz
    
    def get_vx(self):
        return self.__vx
    
    def get_vy(self):
        return self.__vy
    
    def get_vz(self):
        return self.__vz
    
    def set_salinity(self, salinity):
        self.__salinity = salinity
    
    def get_salinity(self):
        return self.__salinity
    
    def set_temperature(self, temperature):
        self.__temperature = temperature

    def get_temperature(self):
        return self.__temperature

# 生成网格lattice
x = np.linspace(0, 100, N_X + 1)
y = np.linspace(0, 100, N_Y + 1)
z = np.linspace(0, 10, N_Z + 1)
X, Y, Z = np.meshgrid(x, y, z)

# 在每个格点上生成站点
lattice = []
for i in range(N_X):
    for j in range(N_Y):
        for k in range(N_Z):
            lattice.append(Site(X[i, j, k], Y[i, j, k], Z[i, j, k]))

            