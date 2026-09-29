import matplotlib.pyplot as plt
import math
import numpy as np

# Rounding for distance variation 
def round1(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

# Planets and gravity
planetsG = {
    "Earth": 9.8,
    "Jupiter": 24.79,
    "Mars": 3.73,
    "Saturn": 10.44,
    "Venus": 8.87,
    "Neptune": 11.15,
    "Mercury": 3.7,
    "Uranus": 8.69
}

# Static values
Height = 1.7
Vavg = 3.25

angles = list(range(-45, 46, 10))


fig, axes = plt.subplots(2, 5, figsize=(18, 8))
axes = axes.flatten()  

for i, angle in enumerate(angles):
    ax = axes[i]
    theta = np.radians(angle)

    for key, value in planetsG.items():
        Time = round1(math.sqrt(3.4 / value), 2)

        vx = Vavg * np.cos(theta)
        vy = Vavg * np.sin(theta)

        T = np.linspace(0, Time, 100)
        x = vx * T
        y = Height + (vy * T) - (0.5 * value * T**2)
        if key == "Uranus":
            ax.plot(x,y, lw =2.5, color = "yellow", label =f"{key} (g={value})")
        elif key == "Venus":
            ax.plot(x,y, lw =2.5, color = "#FF007F", label =f"{key} (g={value})")
        else:
            ax.plot(x, y,lw =2.5, label=f"{key} (g={value})")
    

    ax.set_title(f"{angle}°")
    ax.set_xlim(0, 3)
    ax.set_ylim(0, Height + 0.5)
    ax.grid(True)

# Shared labels
fig.suptitle("Particle Trajectiries from Sneezing at Varying Angles while talking or sneezing", fontsize=16)
fig.text(0.5, 0.04, "Distance (m)", ha='center')
fig.text(0.04, 0.5, "Height (m)", va='center', rotation='vertical')

# Single legend for entire figure
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, title ="Gravity in m/s^2", loc='upper right')

plt.tight_layout(rect=[0.05, 0.05, 0.95, 0.92]) # type: ignore
plt.show()