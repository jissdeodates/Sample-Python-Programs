import matplotlib.pyplot as plt
import numpy as np

# Create sample data for plotting. Eg: sine wave
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

# Create figure and axes for plotting
fig, ax = plt.subplots()
ax.plot(t, s)

# Include axis info and title
ax.set(xlabel='time (s)', ylabel='Sine value', title='This is a sample sine wave plot')
ax.grid()

# Display the plot
plt.show()
