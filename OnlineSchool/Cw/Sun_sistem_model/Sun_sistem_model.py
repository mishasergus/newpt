import numpy as np
import matplotlib.pyplot as plt
from PIL.ImageOps import expand
from matplotlib.animation import FuncAnimation
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

class Planet:
    def __init__(self, radius, name, a_orbit,b_orbit,angle_velocity,mass,color):
        self.radius = radius
        self.name = name
        self.a_orbit = a_orbit
        self.b_orbit = b_orbit
        self.angle_velocity = angle_velocity
        self.mass = mass
        self.color = color

        self.angle = 0
        self.x = 0
        self.y = 0



    def movement(self):
        self.angle += self.angle_velocity * 0.002
        self.x = self.a_orbit * np.cos(self.angle)
        self.y = self.b_orbit * np.sin(self.angle)

    def drowPlanet(self,ax):
        return ax.plot([self.x], [self.y],'o', color = self.color, markersize = self.radius)[0]

    def drowNames(self,ax):
        return ax.text(self.x, self.y, self.name, color='white',ha='center',fontsize = 7)


    def drowOrbit(self,ax):
        alpha = np.linspace(0, 2 * np.pi, 50)
        x_orbit = self.a_orbit * np.cos(alpha)
        y_orbit = self.b_orbit * np.sin(alpha)
        ax.plot(x_orbit, y_orbit, linestyle = "--", color = 'white', linewidth = 0.1)

root = tk.Tk()
root.title("Sun sistem")

main_frame = tk.Frame(root)
main_frame.pack(side = tk.LEFT, fill = tk.BOTH,expand = True)
#             сторона | фрейм розтягується і в гор і в верт  | фрейм займає все вікно

left_frame = tk.Frame(main_frame, background = "black")
left_frame.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)


right_frame = tk.Frame(main_frame, background = "black")
right_frame.pack(side = tk.RIGHT, fill = tk.BOTH, expand = True)


# Вікно для побудови
fig1, ax1 = plt.subplots(figsize =(5,5))
ax1.set_aspect('equal')
ax1.set_facecolor('black')
ax1.set_xlim(-2.5,2.5)
ax1.set_ylim(-2.5,2.5)
ax1.set_title("Inside planets", color = "white")
fig1.patch.set_facecolor('black')
ax1.tick_params(colors = "white")
ax1.plot(0, 0, 'o',color = "yellow", markersize = 15)

asteroids = [Planet(name = "", radius = random.uniform(0.5,1), a_orbit = random.uniform(1.9,2.1),b_orbit = random.uniform(1.5,1.7), angle_velocity = 2*np.pi / (1716.675 / 365.25),
           mass = 1, color = "gray") for i in range(100)]
for asteroid in asteroids:
    asteroid.x = random.uniform(-asteroid.a_orbit, asteroid.a_orbit)
    znak = [1,-1]
    prom = random.randint(0,1)
    asteroid.y = znak[prom]*(asteroid.b_orbit/asteroid.a_orbit)*np.sqrt((asteroid.a_orbit**2)-(asteroid.x**2)) + random.uniform(-0.1,0.1)
    asteroid.angle = random.uniform(0, 2 * np.pi)
asterOrbit = Planet(name = "Great asteroid belt", radius = 0, a_orbit = 2,b_orbit = 1.6, angle_velocity = 2*np.pi / (1716.675 / 365.25),
           mass = 1, color = "black")
print(asteroids[0].x)
print(asteroids[0].y)
near_planets = [
    Planet(name = "Mercury", radius = 1, a_orbit = 0.3871,b_orbit = 0.3795, angle_velocity = 2*np.pi / (87.97 / 365.25),
           mass = 1, color = "brown"),
    Planet(name = "Venus", radius = 1, a_orbit = 0.7233,b_orbit = 0.7233, angle_velocity = 2 * np.pi / (224.7 / 365.25),
           mass = 1, color="orange"),
    Planet(name = "Earth", radius = 2, a_orbit = 1,b_orbit = 0.99, angle_velocity = 2 * np.pi / (365.25 / 365.25),
           mass = 1, color="green"),
    Planet(name = "Mars", radius = 2, a_orbit = 1.5237,b_orbit = 1.513, angle_velocity = 2 * np.pi / (686.98 / 365.25),
           mass = 1, color="red")
]

# Побудова орбіти

for planet in near_planets:
    planet.drowOrbit(ax1)
asterOrbit.drowOrbit(ax1)

# Поч положення планет

# Анімація
astName = asterOrbit.drowNames(ax1)

asteroidPosition = [asteroid.drowPlanet(ax1) for asteroid in asteroids]

near_planetPoints = [planet.drowPlanet(ax1) for planet in near_planets]
near_planetNames = [planet.drowNames(ax1) for planet in near_planets]
# print(type(near_planetPoints[0]))
# print(type(near_planetNames[0]))
def near_planet_animation(frame):
    for i, planet in enumerate(near_planets):
        planet.movement()
        near_planetPoints[i].set_data([planet.x],[planet.y])
        near_planetNames[i].set_position((planet.x,planet.y+0.1))
    for i, asteroid in enumerate(asteroids):
        asteroid.movement()
        asteroidPosition[i].set_data([asteroid.x],[asteroid.y])
    astName.set_position((asteroids[0].x, asteroids[0].y + 0.15))
    return near_planetPoints+near_planetNames+asteroidPosition+[astName]

canvas1 = FigureCanvasTkAgg(fig1,master=left_frame)
#                               місце знаходження
canvas1.get_tk_widget().pack(fill = tk.BOTH,expand = True)

ani1 = FuncAnimation(fig1, near_planet_animation, frames = 480, interval = 3)
"""                                                                        , blit = True"""


###########################################

fig2, ax2 = plt.subplots(figsize =(5,5))
ax2.set_aspect('equal')
ax2.set_facecolor('black')
ax2.set_xlim(-45,45)
ax2.set_ylim(-45,45)
ax2.set_title("Far planets", color = "white")
fig2.patch.set_facecolor('black')
ax2.tick_params(colors = "white")
ax2.plot(0, 0, 'o',color = "yellow", markersize = 15)

far_planets = [
    Planet(name = "Jupiter", radius = 1, a_orbit = 5.2026,b_orbit = 5.1898, angle_velocity = 2 * np.pi / (4331.865 / 4331.865),
            mass = 1, color="white"),
    Planet(name = "Saturn", radius = 5/6.5, a_orbit = 9.5371,b_orbit = 9.5212, angle_velocity = 2 * np.pi / (10759 / 4331.865),
            mass = 1, color="orange"),
    Planet(name = "Uranus", radius = 5/13.5, a_orbit = 19.1913,b_orbit = 19.1487, angle_velocity = 2 * np.pi / (30687 / 4331.865),
            mass = 1, color="cyan"),
    Planet(name = "Neptun", radius = 5/14, a_orbit = 30.069,b_orbit = 30.0661, angle_velocity = 2 * np.pi / (60190 / 4331.865),
            mass = 1, color="blue"),
    Planet(name = "Pluto", radius = 5/20, a_orbit = 39.4820,b_orbit = 38.4290, angle_velocity = 2 * np.pi / (90560 / 4331.865),
            mass = 1, color="grey")
]

# Побудова орбіти

for planet in far_planets:
    planet.drowOrbit(ax2)

# Поч положення планет

# Анімація

far_planetPoints = [planet.drowPlanet(ax2) for planet in far_planets]
far_planetNames = [planet.drowNames(ax2) for planet in far_planets]

def far_planet_animation(frame):
    for i, planet in enumerate(far_planets):
        planet.movement()
        far_planetPoints[i].set_data([planet.x],[planet.y])
        far_planetNames[i].set_position((planet.x, planet.y+1.5))
    return far_planetPoints+far_planetNames

canvas2 = FigureCanvasTkAgg(fig2,master=right_frame)
#                               місце знаходження
canvas2.get_tk_widget().pack(fill = tk.BOTH,expand = True)

ani2 = FuncAnimation(fig2, far_planet_animation, frames = 480, interval = 3)
"""                                                                        , blit = True"""
def on_closing():
    if 'ani1' in globals() and ani1 is not None:
        ani1.event_source.stop()
    if 'ani2' in globals() and ani2 is not None:
        ani2.event_source.stop()

    # Спробуйте явно знищити полотна перед root.destroy()
    if 'canvas1' in globals() and canvas1 is not None:
        canvas1.get_tk_widget().destroy()
    if 'canvas2' in globals() and canvas2 is not None:
        canvas2.get_tk_widget().destroy()

    # Закрити фігури Matplotlib, щоб звільнити ресурси
    plt.close(fig1)
    plt.close(fig2)

    root.destroy()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
