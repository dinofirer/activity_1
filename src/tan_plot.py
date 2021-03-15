import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,10,0.1)
cos_x = np.cos(x)

plt.plot(x, cos_x)
plt.title('Cos')
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.show()
