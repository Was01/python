import numpy as np

## Indexação e cortes (slices) de arrays

a=np.arange(10,21)
print(a)

b=np.random.randint(1,5,size=(5,5))
print(b)


## slices
print(b[3:5,0:2])


from skimage import io
import matplotlib.pyplot as plt

img=io.imread('imagem.jpg') ##Carregamento da imagem
plt.imshow(img) ##Exibição da imagem

print(img)

print(img.shape)

nova_img=img[200:1100,250:1600]
plt.imshow(nova_img)