import matplotlib.pyplot as plt
import math
import numpy as np

#Rounding for distance variation 
def round1(n, decimals=0):
        multiplier = 10 ** decimals
        return math.ceil(n * multiplier) / multiplier

#Planets and gravity
planetsG ={
    "Earth": 9.8,
    "Jupiter": 24.79,
    "Mars": 3.73,
    "Saturn": 10.44,
    "Venus": 8.87,
    "Neptune": 11.15,
    "Mercury": 3.7,
    "Uranus" :8.69
}
#Static values
Height = 1.7
angle = 0


#Plotting

 
plt.figure(figsize=(10, 5))
theta = np.radians(angle)

for key, value in planetsG.items():   
        #Logic for graphing and velocity
        Vtalk = round1(1.5 * math.sqrt(value / 9.8), 2)
        Vsneeze = 5 * round1(math.sqrt(value / 9.8), 2)
        
        Vavg = 3.25
       
        Time = round1(math.sqrt(3.4/value), 2)
        vx = Vavg * np.cos(theta)
        vy = Vavg * np.sin(theta)

        time_of_flight = math.sqrt((2 * Height) / value )
        T = np.linspace(0, Time, 100)
        x = vx * T
        y = Height + (vy * T) - (0.5 * value * T**2)
        if key == "Uranus":
            plt.plot(x,y, lw =2.5, color = "yellow", label =f"{key} (g={value})")
        elif key == "Venus":
            plt.plot(x,y, lw =2.5, color = "#FF007F", label =f"{key} (g={value})")
        elif key == "Mercury":
            plt.plot(x,y, lw =2.5, color = "#8AD5EE", label =f"{key} (g={value})")
        elif key =="Mars":
            plt.plot(x,y, lw =2.5, color = "#125619", label =f"{key} (g={value})")
        else:
            plt.plot(x,y,lw = 2.5, label=f"{key} (g={value})")    

        

#Graph customization
plt.title(f"Particle trajectories at a constant initial velocity")
plt.xlabel("Distance(m)")
plt.ylabel("Height(m)")
plt.legend(title ="Gravity in m/s^2", loc='upper right')
plt.grid(True)
plt.xlim(0,3)
plt.ylim(0, Height + 0.5)
plt.show()