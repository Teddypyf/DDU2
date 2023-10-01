import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 5, 0.1)

y = np.array(x * x * x)
plt.plot(
    x,
    y,
)
plt.show()
