import numpy as np
import matplotlib.pyplot as plt
i=0

np.random.seed(56)
rNumbers = np.random.randint(6, size=100)+1

a=np.count_nonzero(rNumbers == 1)
b=np.count_nonzero(rNumbers == 2)
c=np.count_nonzero(rNumbers == 3)
d=np.count_nonzero(rNumbers == 4)
e=np.count_nonzero(rNumbers == 5)
f=np.count_nonzero(rNumbers == 6)
print(a,b,c,d,e,f)


labels, counts = np.unique(rNumbers, return_counts=True)
plt.bar(labels, counts, align='center')
plt.gca().set_xticks(labels)
plt.show()
