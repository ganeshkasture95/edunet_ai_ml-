import numpy as np
from scipy import stats

# arr = np.array([1,2,3,4,5])
# print(arr)
# print(arr.shape)
# print(arr.ndim)
# print(arr.size)
# print(arr.dtype)
# print(arr.itemsize)



# string = input()


# stringrev = string[::-1]

# if string == stringrev:
#     print("The ztring is a palinfderome")


data = np.array([2,4,6,8,9,10,4,16])

meen = np.mean(data)
meedian = np.median(data)
std = np.std(data)
variance = np.var(data)

mode_value, mode_count = stats.mode(data)

print(f"Mode: {mode_value[0]}, Frequency: {mode_count[0]}")



print(meen,meedian,std,variance)
