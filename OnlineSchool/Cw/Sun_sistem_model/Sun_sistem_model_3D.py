import numpy as np
import matplotlib.pyplot as plt
from PIL.ImageOps import expand
from matplotlib.animation import FuncAnimation
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
from mpl_toolkits.mplot3d import Axes3D, proj3d

class Planet:
    def __init__(self, radius, name, a_orbit, b_orbit, angle_velocity, mass, color, tilt = 0):
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
        self.z = 0
        self.tilt = np.radians(tilt)



    def movement(self, time_scale = 0.004):
        self.angle += self.angle_velocity * time_scale
        self.x = self.a_orbit * np.cos(self.angle)
        self.y = self.b_orbit * np.sin(self.angle)
        self.z = self.y * np.tan(self.tilt)






    def drowPlanet(self,ax):
        return ax.plot([self.x], [self.y],[self.z],'o', color = self.color, markersize = self.radius)[0]

    def drowNames(self,ax):
        return ax.text2D(self.x, self.y, self.name, color='white',ha='center',fontsize = 7)


    def drowOrbit(self,ax):
        alpha = np.linspace(0, 2 * np.pi, 200)
        x_orbit = self.a_orbit * np.cos(alpha)
        y_orbit = self.b_orbit * np.sin(alpha)
        z_orbit = y_orbit * np.tan(self.tilt)
        ax.plot(x_orbit, y_orbit, z_orbit, linestyle = '--', color = 'white', linewidth = 0.3)



ax_limit = 50
zoom_scale = 1
sun_size = 15
initial_time_scale = 0.004

root = tk.Tk()
root.title("Sun sistem")
root.state("zoomed")

time_scale_var = tk.StringVar()
time_scale_var.set(f"Time parameters: {initial_time_scale:.3f}")


main_frame = tk.Frame(root)
main_frame.pack(fill = tk.BOTH,expand = True)
#             фрейм розтягується і в гор і в верт  | фрейм займає все вікно

left_frame = tk.Frame(main_frame, background = "black")
left_frame.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)


right_frame = tk.Frame(main_frame, background = "black", width = 150)
right_frame.pack(side = tk.RIGHT, fill = tk.BOTH, expand = True)


# Вікно для побудови
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection = "3d")
ax.set_facecolor('black')
fig.patch.set_facecolor('black')
ax.set_title("Sun sistem", color = "white")
ax.tick_params(colors = "white")
ax.view_init(elev = 25, azim = 45)
ax.set_xlim(-ax_limit, ax_limit)
ax.set_ylim(-ax_limit, ax_limit)
ax.set_zlim(-ax_limit, ax_limit)

ax.plot([0], [0], [0], 'o', color = "yellow", markersize = sun_size)


asteroids = [Planet(name = "", radius = random.uniform(0.5, 1), a_orbit = random.uniform(1.9,2.1),b_orbit = random.uniform(1.5,1.7), angle_velocity = 2*np.pi / (1716.675 / 365.25),
           mass = 1, color = "gray",tilt = random.randint(-10,10)) for i in range(150)]
for asteroid in asteroids:
    asteroid.angle = random.uniform(0, 2 * np.pi)
asterOrbit = Planet(name = "Great asteroid belt", radius = 0, a_orbit = 2,b_orbit = 1.6, angle_velocity = 2*np.pi / (1716.675 / 365.25),
           mass = 1, color = "black")
planets = [
    Planet(name = "Mercury", radius = 1, a_orbit = 0.3871,b_orbit = 0.3795, angle_velocity = 2*np.pi / (87.97 / 365.25),
           mass = 1, color = "brown"),
    Planet(name = "Venus", radius = 2, a_orbit = 0.7233,b_orbit = 0.7233, angle_velocity = 2 * np.pi / (224.7 / 365.25),
           mass = 1, color="orange"),
    Planet(name = "Earth", radius = 2, a_orbit = 1,b_orbit = 0.99, angle_velocity = 2 * np.pi / (365.25 / 365.25),
           mass = 1, color="green"),
    Planet(name = "Mars", radius = 2, a_orbit = 1.5237,b_orbit = 1.513, angle_velocity = 2 * np.pi / (686.98 / 365.25),
           mass = 1, color="red"),
    Planet(name = "Jupiter", radius = 6, a_orbit = 5.2026,b_orbit = 5.1898, angle_velocity = 2 * np.pi / (4331.865 / 365.25),
            mass = 1, color="white"),
    Planet(name = "Saturn", radius = 4, a_orbit = 9.5371,b_orbit = 9.5212, angle_velocity = 2 * np.pi / (10759 / 365.25),
            mass = 1, color="orange"),
    Planet(name = "Uranus", radius = 3, a_orbit = 19.1913,b_orbit = 19.1487, angle_velocity = 2 * np.pi / (30687 / 365.25),
            mass = 1, color="cyan"),
    Planet(name = "Neptun", radius = 3, a_orbit = 30.069,b_orbit = 30.0661, angle_velocity = 2 * np.pi / (60190 / 365.25),
            mass = 1, color="blue"),
    Planet(name = "Pluto", radius = 1, a_orbit = 39.4820,b_orbit = 38.4290, angle_velocity = 2 * np.pi / (90560 / 365.25),
            mass = 1, color="grey", tilt = 17)
]

# Побудова орбіти

for planet in planets:
    planet.drowOrbit(ax)

asterOrbit.drowOrbit(ax)

# Поч положення планет

# Анімація
astName = asterOrbit.drowNames(ax)
asteroidPosition = [asteroid.drowPlanet(ax) for asteroid in asteroids]

planetPoints = [planet.drowPlanet(ax) for planet in planets]
planetNames = [planet.drowNames(ax) for planet in planets]
# print(type(near_planetPoints[0]))
# print(type(near_planetNames[0]))
def planet_animation(frame):
    for i, planet in enumerate(planets):
        planet.movement(initial_time_scale)
        planetPoints[i].set_data([planet.x],[planet.y])
        planetPoints[i].set_3d_properties([planet.z])
        x2d, y2d, _ = proj3d.proj_transform(planet.x, planet.y, planet.z, ax.get_proj())
        planetNames[i].set_position((x2d,y2d))
    for i, asteroid in enumerate(asteroids):
        asteroid.movement(initial_time_scale)
        asteroidPosition[i].set_data([asteroid.x],[asteroid.y])
        asteroidPosition[i].set_3d_properties([asteroid.z])
        x2d, y2d, _ = proj3d.proj_transform(asteroid.x, asteroid.y, asteroid.z, ax.get_proj())
    x2d, y2d, _ = proj3d.proj_transform(asteroids[0].x, asteroids[0].y, asteroids[0].z, ax.get_proj())
    astName.set_position((x2d, y2d))
    return planetPoints + planetNames + asteroidPosition + [astName]


ani = FuncAnimation(fig, planet_animation, frames = 1000, interval = 25, blit = False)
"""                                                                        , blit = True"""

def scroll(event):
    global zoom_scale
    if event.button == 'up':
        zoom_scale -= 0.01
    elif event.button == 'down':
        zoom_scale += 0.01

    scaled = ax_limit * zoom_scale
    ax.set_xlim(-scaled, scaled)
    ax.set_ylim(-scaled, scaled)
    ax.set_zlim(-scaled, scaled)
    fig.canvas.draw_idle()

def increase_time_speed():
    global initial_time_scale
    initial_time_scale *= 1.5
    time_scale_var.set(f"Time parameters: {initial_time_scale:.3f}")

def decrease_time_speed():
    global initial_time_scale
    initial_time_scale /= 1.5
    time_scale_var.set(f"Time parameters: {initial_time_scale:.3f}")

def reset_time_speed():
    global initial_time_scale
    initial_time_scale = 0.004
    time_scale_var.set(f"Time parameters: {initial_time_scale:.3f}")

canvas = FigureCanvasTkAgg(fig, master=left_frame)
canvas.get_tk_widget().pack(fill = tk.BOTH,expand = True)
canvas.draw()
canvas.mpl_connect('scroll_event', scroll)

tk.Label(right_frame, text = "Edit module", bg = 'black', fg = 'white', font = ("Arial Black", 14)).pack(pady = 10)
tk.Button(right_frame, text = "Speed_up", fg = 'white',command = increase_time_speed, bg = 'black', width = 15).pack(pady = 5)
tk.Button(right_frame, text = "Speed_down", fg = 'white',command = decrease_time_speed, bg = 'black', width = 15).pack(pady = 5)
tk.Button(right_frame, text = "Reset settings", fg = 'white',command = reset_time_speed, bg = 'black', width = 15).pack(pady = 5)
tk.Label(right_frame, textvariable = time_scale_var, bg = 'black',fg = 'white', font = ("Arial Black", 14)).pack(pady = 20)

ax.mouse_init()


def on_closing():
    if 'ani' in globals() and ani is not None:
        ani.event_source.stop()

    if 'canvas' in globals() and canvas is not None:
        canvas.get_tk_widget().destroy()

    plt.close(fig)

    root.destroy()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
