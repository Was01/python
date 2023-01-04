import numpy as np

import matplotlib.pyplot as plt

array=np.arange(1,5)


plt.plot(array)

x=np.arange(0,10,0.2)
y=np.sin(x)

plt.plot(x,y)
plt.title('Seno')
plt.xlabel('x')
plt.ylabel('sen(x)')
plt.grid()