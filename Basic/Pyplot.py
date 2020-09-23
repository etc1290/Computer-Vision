# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:14:55 2020

@author: ST16
"""

import matplotlib.pyplot as plt
import numpy as np

normal_samples = np.random.normal(size = 100000) # 生成 100000 組標準常態分配（平均值為 0，標準差為 1 的常態分配）隨機變數
uniform_samples = np.random.uniform(size = 100000) # 生成 100000 組介於 0 與 1 之間均勻分配隨機變數

plt.hist(normal_samples)
plt.show()
plt.hist(uniform_samples)
plt.show()