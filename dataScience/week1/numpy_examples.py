import numpy as np

aList = [1,2,3]
npArray = np.array(aList)

a2dList = [[1,2], [3,4], [5,6]]
np2dArray = np.array(a2dList)
print(np2dArray.shape)

a = np.arange(0, 30, 2)
print(a)
b = a.reshape(5,3)
print(a)
print(b)
a.resize(3,5)
print(a)


quiz1 = np.arange(36).reshape(6,6)
print(quiz1)
print(quiz1[::7])
print(quiz1[::2])
print(quiz1[1::2])
print(quiz1[:, ::2])
print(quiz1[0:6,::-7])
print(quiz1[0:6,::-2])
print(quiz1[:,::7])
print(quiz1[:,::2])
print(quiz1.reshape(36)[::7])
