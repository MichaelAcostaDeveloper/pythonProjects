import matplotlib.pyplot as plt

import numpy as np


def lineal(m,b,x):
    return m*x+b

print(lineal(8,5,6))
x=np.linspace(-2,10,num=100)
plt.plot(x,lineal(2,6,x))

