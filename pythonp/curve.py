import matplotlib.pyplot as plt
import numpy as np

 
x=range(0,100)
y1 = x*2


plt.plot(x, y1, 'b--', label='Diagonal Line')  

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Half Parabolic Curve')

plt.legend()
plt.show()