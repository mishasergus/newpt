import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Planet:
    def __init__(self, radius, name, radius_orbit,angle_velocity,mass,color):
        self.radius = radius
        self.name = name
        self.radius_orbit = radius_orbit
        self.angle_velocity = angle_velocity
        self.mass = mass
        self.color = color

        self.angle = 0
        self.x = 0
        self.y = 0

    def movement(self):
        self.angle += self.angle_velocity * 0.1
        self.x = self.radius_orbit * np.cos(self.angle)
        self.y = self.radius_orbit * np.sin(self.angle)

    def drowPlanet(self,ax):
        return ax.plot([self.x], [self.y], 'o',color = self.color, markersize = self.radius)[0]

    def drowOrbit(self,ax):
        alpha = np.linspace(0, 2 * np.pi, 50)
        x_orbit = self.radius_orbit * np.cos(alpha)
        y_orbit = self.radius_orbit * np.sin(alpha)
        ax.plot(x_orbit, y_orbit, linestyle = "--", color = 'white', linewidth = 0.1)



# Вікно для побудови
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_facecolor('black')
ax.set_xlim(-35,35)
ax.set_ylim(-35,35)

sun = ax.plot(0, 0, 'o',color = "yellow", markersize = 5)[0]

planets = [
    Planet(name = "Jupiter", radius = 0.5, radius_orbit = 5.2, angle_velocity = 2 * np.pi / (4331.865 / 365.25),
            mass = 1, color="white"),
    Planet(name = "Saturn", radius = 5/11, radius_orbit = 9.58, angle_velocity = 2 * np.pi / (10759 / 365.25),
            mass = 1, color="orange"),
    Planet(name = "Uran", radius = 5/27, radius_orbit = 19, angle_velocity = 2 * np.pi / (30687 / 365.25),
            mass = 1, color="cyan"),
    Planet(name = "Neptun", radius = 5/28, radius_orbit = 30.1, angle_velocity = 2 * np.pi / (60190 / 365.25),
            mass = 1, color="blue")
]

# Побудова орбіти

for planet in planets:
    planet.drowOrbit(ax)

# Поч положення планет

# Анімація

planetPoints = [planet.drowPlanet(ax) for planet in planets]

def planet_animation(frame):
    for i, planet in enumerate(planets):
        planet.movement()
        planetPoints[i].set_data([planet.x],[planet.y])
    return planetPoints


ani = FuncAnimation(fig, planet_animation, frames = 480, interval = 4, blit = True)

plt.title("Sun sistem")
plt.show()