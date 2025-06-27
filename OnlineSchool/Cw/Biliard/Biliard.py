import numpy as np
import matplotlib.pyplot as plt
from PIL.ImageOps import expand
from matplotlib.animation import FuncAnimation
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import math

class Ball:
    current_id = 0

    def __init__(self,canvas, x, y, v_x, v_y,radius = 20, colour = 'red'):
        self.canvas = canvas
        self.radius = radius
        self.colour = 'red'
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.active = True

        self.id = Ball.current_id
        Ball.current_id += 1

        self.inf = [0,1]

        self.ball_id = self.canvas.create_oval(
            x - radius, y - radius,
            x + radius, y + radius,
            fill = colour,outline = 'black'
        )

        self.text_id = self.canvas.create_text(
            x, y,
            text = str(self.id),
            fill='white',
            font=("Arial Black", 12)
        )

    def move(self):
        if not self.active:
            return
        self.x += self.v_x * 1
        self.y += self.v_y * 1

        self.v_x -= self.v_x * 0.02
        self.v_y -= self.v_y * 0.02

        self.wall_collision_check()
        self.canvas.coords(self.ball_id,
                           self.x - self.radius, self.y - self.radius,
                           self.x + self.radius, self.y + self.radius)
        self.canvas.coords(self.text_id,
                           self.x, self.y)

    def wall_collision_check(self):
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        if self.x - self.radius <= 0 or self.x + self.radius >= width:
            self.v_x = -self.v_x
            self.inf[0] += 1
        if self.y - self.radius <= 0 or self.y + self.radius >= height:
            self.v_y = -self.v_y
            self.inf[0] += 1

    def collision_check(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        dist = np.sqrt(dx ** 2 + dy ** 2)
        if dist == 0:
            dist = 0.05
        if dist < other.radius + self.radius:
            nx = dx / dist
            ny = dy / dist
            p1 = self.v_x * nx + self.v_y * ny
            p2 = other.v_x * nx + other.v_y * ny
            self.v_x += (p2-p1) * nx
            self.v_y += (p2 - p1) * ny
            other.v_x += (p1 - p2) * nx
            other.v_y += (p1 - p2) * ny
            overlap = other.radius + self.radius - dist
            self.x -= nx * overlap / 2
            self.y -= ny * overlap / 2
            other.x += nx * overlap / 2
            other.y += ny * overlap / 2
            self.inf[0] += 1
            other.inf[0] += 1


class TableApp:
    def __init__(self,root):
        self.root = root
        self.root.title("BILIARD")
        self.scoreN = 0

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(side = tk.LEFT)

        self.canvas = tk.Canvas(self.main_frame, width = 800, height = 400, bg = "green",highlightthickness=3,highlightbackground="black")
        self.canvas.pack()

        self.inf_frame = tk.Frame(root)
        self.inf_frame.pack(side = tk.RIGHT, fill = tk.Y)

        self.score = tk.Label(self.inf_frame, text=f"Score: {self.scoreN}", font=("Arial Black", 20))
        self.score.pack(pady=5)

        self.getter = tk.Entry(self.inf_frame, width=50)
        self.getter.pack(pady=5)

        self.text_is_exist = tk.Label(self.inf_frame, text=f"Is exist: ", font=("Arial Black", 10))
        self.text_is_exist.pack(pady=5)

        self.text_num_of_collisions = tk.Label(self.inf_frame, text=f"Collisions: ", font=("Arial Black", 10))
        self.text_num_of_collisions.pack(pady=5)

        self.scrollbar = tk.Scrollbar(self.inf_frame)
        self.scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

        self.inf_text = tk.Text(self.inf_frame,width=15,yscrollcommand=self.scrollbar.set)
        self.inf_text.pack(side=tk.LEFT, fill=tk.BOTH,expand = True)
        self.scrollbar.config(command=self.inf_text.yview)

        self.clear_button = tk.Button(self.inf_frame,text = "Clear", command=self.clear_info)
        self.clear_button.pack(pady = 10)

        self.pockets = []
        self.balls = []




        self.first_click = None
        self.click_indicator = None

        self.canvas.bind("<Button-1>", self.click)
        self.drow_pockets()
        self.ball_move()

    def drow_pockets(self):
        width = int(self.canvas['width'])
        height = int(self.canvas['height'])

        par = [
            (0,0,30),
            (width // 2, -10, 30),
            (width, 0, 30),
            (0, height, 30),
            (width // 2, height+10, 30),
            (width, height, 30)
        ]
        for x,y,r in par:
            poc = self.canvas.create_oval(
            x - r, y - r,
            x + r, y + r,
            fill='black'
            )
            self.pockets.append([x,y,r])


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

            ball = Ball(self.canvas, x1, y1, v_x, v_y)
            self.balls.append(ball)
            self.first_click = None
            self.canvas.delete(self.click_indicator)

    def check_pockets(self, ball):
        for x, y, r in self.pockets:
            if (((ball.x - x) ** 2) + ((ball.y - y) ** 2) <= r**2):
                self.scoreN += 1
                self.score.config(text=str(f"Score: {self.scoreN}"))
                return True
        return False

    def inf_update(self):
        yview = self.inf_text.yview()

        self.inf_text.delete(1.0, tk.END)

        for ball in self.balls:
            inf = f"Id: {ball.id}:\n"
            inf += f"Collisions: {ball.inf[0]}:\n"
            inf += f"Is alive: {ball.inf[1]}:\n"

            self.inf_text.insert(tk.END,inf)

        self.inf_text.yview_moveto(yview[0])

    def clear_info(self):
        for ball in self.balls:
            ball.inf[0] = 0
        self.inf_update()
    def ball_move(self):
        index = 0
        try:
            if int(self.getter.get()) >= 0 and int(self.getter.get()) < len(self.balls):
                index = int(self.getter.get())
        except:
            index = 0
        try:
            self.text_num_of_collisions.config(text=str(f"Collisions: {self.balls[index].inf[0]}"))
            self.text_is_exist.config(text=str(f"Is exist: {bool(self.balls[index].inf[1])}"))
        except:
            self.text_num_of_collisions.config(text=str(f"Collisions: 0"))
            self.text_is_exist.config(text=str(f"Is exist: False"))
        for ball in self.balls:
            ball.move()
        for i in range(len(self.balls)):
            for j in range(i + 1, len(self.balls)):
                if self.balls[i].active and self.balls[j].active:
                    self.balls[i].collision_check(self.balls[j])

        for ball in self.balls:
            if ball.active and self.check_pockets(ball):
                self.canvas.delete(ball.ball_id)
                self.canvas.delete(ball.text_id)
                ball.active = False
                ball.inf[1] = 0
        self.inf_update()
        self.root.after(30, self.ball_move)




if __name__ == "__main__":
    root = tk.Tk()
    app = TableApp(root)
    root.mainloop()