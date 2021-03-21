import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, num=30)
a = np.array([1,3,3,2,1])
b = np.array([1,1,2,2,1])

plt.plot(a, b, linewidth=1)


plt.xlabel('x')
plt.ylabel('y')
plt.show()

