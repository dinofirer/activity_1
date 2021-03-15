import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,10,0.1)
sin_x = np.sin(x)

#plot the sine wave:
plt.plot(x, sin_x)
plt.title('Sine wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.show()
