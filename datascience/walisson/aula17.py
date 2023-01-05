import numpy as np
import matplotlib.pyplot as plt

##Plots

x=np.arange(0,10,0.01)
y1=np.sin(x) ## primeira curva
y2=np.cos(x) ## segunda curva
y3=np.sin(x)*2
y4=np.sin(2*x)


##Subplots
plt.figure(figsize=(12,6))

plt.subplot(2,2,1)
plt.plot(x,y1,label='sin(x)')
plt.subplot(2,2,2)
plt.plot(x,y2,label='cos(x)')
plt.subplot(2,2,3)
plt.plot(x,y3,label='2*sin(x)')
plt.subplot(2,2,4)
plt.plot(x,y4,label='sin(2*x)')
plt.tight_layout()
