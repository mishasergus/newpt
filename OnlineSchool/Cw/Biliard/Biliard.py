import numpy as np
import matplotlib.pyplot as plt
from PIL.ImageOps import expand
from matplotlib.animation import FuncAnimation
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import math

class Ball:
    def __init__(self,canvas, x, y, v_x, v_y,radius = 20,colour = 'red'):
        self.canvas = canvas
        self.radius = 20
        self.colour = 'red'
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y

        self.ball_id = self.canvas.create_oval(
            x - radius, y - radius,
            x + radius, y + radius,
            fill = colour,outline = 'black'
        )

    def move(self):
        self.x += self.v_x * 1
        self.y += self.v_y * 1
        self.v_x -= self.v_x*0.02
        self.v_y -= self.v_y * 0.02
        self.wall_collision_check()
        self.canvas.coords(self.ball_id,
                           self.x - self.radius, self.y - self.radius,
                           self.x + self.radius, self.y + self.radius)

    def wall_collision_check(self):
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        if self.x - self.radius <= 0 or self.x + self.radius >= width:
            self.v_x = -self.v_x
        if self.y - self.radius <= 0 or self.y + self.radius >= height:
            self.v_y = -self.v_y


class TableApp:
    def __init__(self,root):
        self.root = root
        self.root.title("BILIARD")
        self.scoreN = 0

        self.score = tk.Label(root, text = "0", font=("Arial Black", 20))
        self.score.pack()

        self.canvas = tk.Canvas(root, width = 800, height = 400, bg = "green",highlightthickness=3,highlightbackground="black")
        self.canvas.pack()
        self.louses_arr = [self.canvas.create_oval(
            0 - 30, 0 - 30,
            0 + 30, 0 + 30,
            fill='black'
        ),
        self.canvas.create_oval(
            0 - 30, 400 - 30,
            0 + 30, 400 + 30,
            fill='black'
        ),
        self.canvas.create_oval(
            800 - 30, 0 - 30,
            800 + 30, 0 + 30,
            fill='black'
        ),
        self.canvas.create_oval(
            800 - 30, 400 - 30,
            800 + 30, 400 + 30,
            fill='black'
        ),
        self.canvas.create_oval(
            400 - 30, -10 - 30,
            400 + 30, -10 + 30,
            fill='black'
        ),
        self.canvas.create_oval(
            400 - 30, 410 - 30,
            400 + 30, 410 + 30,
            fill='black'
        )
        ]

        self.louses_coord_arr = [[0, 0],
                                  [0, 400],
                                  [800, 0],
                                  [800, 400],
                                  [400, -10],
                                  [400, 410]
                                 ]

        self.first_click = None
        self.click_indicator = None
        self.ball = None

        self.canvas.bind("<Button-1>", self.click)
        self.ball_move()

    def click(self, event):
        if self.first_click is None:
            self.first_click = (event.x, event.y)
            r = 3

            self.click_indicator = self.canvas.create_oval(
                event.x - r, event.y - r,
                event.x + r, event.y + r,
                fill = "white"
            )
        else:
            x1, y1 = self.first_click
            x2, y2 = event.x, event.y

            dx = x2 - x1
            dy = y2 - y1

            speed_scale = 0.1

            v_x = dx * speed_scale
            v_y = dy * speed_scale

            if self.ball:
                self.canvas.delete(self.ball.ball_id)

            self.ball = Ball(self.canvas, x1, y1, v_x, v_y)

            self.first_click = None
            self.canvas.delete(self.click_indicator)
    def ball_move(self):
        if self.ball:
            self.ball.move()
            for x, y in self.louses_coord_arr:
                if(((self.ball.x - x)**2)+((self.ball.y - y)**2) <= 900):
                    self.canvas.delete(self.ball.ball_id)
                    self.ball = None
                    self.scoreN += 1
                    self.score.config(text=str(self.scoreN))
                    break
        self.root.after(30, self.ball_move)




if __name__ == "__main__":
    root = tk.Tk()
    app = TableApp(root)
    root.mainloop()