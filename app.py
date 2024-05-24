"""
    A particle's position is given by the function x(t) = -t^3 + 3t, where t is time in seconds and x is position in meters.
    a) What are the particle's position and velocity at t = 0, t = 1s, and t = 2s?
    b) Plot the position and velocity functions over the time interval -3s <= t <= 3s
"""

import numpy as np
import matplotlib.pyplot as plt

# Define the time range
t = np.linspace(-3, 3, 100)

# Define the position function x(t) and velocity function v(t)
x_t = -t**3 + 3*t
v_t = -3*t**2 + 3 # Derivate of x(t), used to find the velocity

# Create the figure and axis
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

# Plot the position function
ax1.plot(t, x_t, label='x(t) = -t^3 + 3t')
ax1.axhline(0, color='black', linewidth=0.5)
ax1.axvline(0, color='black', linewidth=0.5)
ax1.grid(color='gray', linestyle='--', linewidth=0.5)
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Position (m)')
ax1.set_title('Position vs. Time')
ax1.legend()

# Plot the velocity function
ax2.plot(t, v_t, label='v(t) = -3t^2 + 3', color='orange')
ax2.axhline(0, color='black', linewidth=0.5)
ax2.axvline(0, color='black', linewidth=0.5)
ax2.grid(color='gray', linestyle='--', linewidth=0.5)
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Velocity (m/s)')
ax2.set_title('Velocity vs. Time')
ax2.legend()

# Display the plots
plt.tight_layout()
plt.show()
