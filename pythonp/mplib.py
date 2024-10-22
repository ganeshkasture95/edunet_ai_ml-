import matplotlib.pyplot as plt

# X and Y data points for a diagonal line
x = [0, 100]
y = [0, 200]


plt.plot(x, y, 'b--', label='Diagonal Line')  # 'b--' for blue dotted line

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Diagonal Dotted Blue Line')

plt.legend()

plt.show()




