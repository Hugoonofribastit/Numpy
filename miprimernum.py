import numpy as np
import matplotlib.pyplot as plt


# Vectores

v1 = np.array([0,1,2,3,4,5,6,7,8,9], dtype="float")

print("v1 =", v1)
# Tipo de dato
print("data type: ", v1.dtype)


#Matrices

m1 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print("M1 =", m1)

#Shape
m1.shape


#Tensores
t1 = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])
print("T1 = ",t1)
print("shape : ", t1.shape)

#Nbytes

print("V1 NBYTES", v1.nbytes)
print("M1 NBYTES", m1.nbytes)
print("T1 NBYTES", t1.nbytes)


#INICIALIZACIÓN DE OBJETOS ()

v3 = np.zeros(6, dtype="int64")
m3 = np.zeros((3,3))
t3 = np.zeros((3,4,6))

# np.ones()

v4 = np.ones(9, dtype="int64")
m4 = np.ones((2,3))

print("v4 =", v4)
print("m4 =", m4)
                             
                        
# Full.

v5 = np.full((4),8)
m5 = np.full((3,2),4)

print("v5 =", v5)
print("m5 =", m5)


# Operaciones
data = np.array([1,2,3])
data[1]
data[0:2]
data[1:]
print(data[data >= 1])
print(data[data % 3 == 0])


np.linspace(0,10, num=20)

a = np.array([1,2,3])
b = a.copy()
b[0] = 30
a

# matriz random de 4 x 2 con valores que van del 0 al 1
x3 = np.random.rand(4,2)
x3

# matriz random de 2 x 2  con el maximo valor seteado en 10
x4 = np.random.randint(10,size=(2,2))
x4
#matriz random de enteros que va del -100 al 200 que tiene 4 filas y 3 columnas
x5 = np.random.randint(-100,200,size=(4,3))

### Operaciones matematicas

a = np.array([1,2,3])
#a + 2
#a * 2
#a ** 3
#a/ 2
#np.cos(a)
#np.sin(a)


### Vectores
#segemento orientado de recta (plano / espacio  array o lista para el informatico)

plt.quiver(0,0,2,2,color="red",angles="xy",scale=1)
plt.ylim(0,10)
plt.xlim(0,10)
plt.show()
 