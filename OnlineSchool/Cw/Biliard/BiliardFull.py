import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import random
import math

class Ball:

    def __init__(self,canvas, game_ref,x, y, v_x = 0, v_y = 0,radius = 15, colour = 'red',number = 0):
        self.canvas = canvas
        self.game = game_ref
        self.colour = 'red'
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.radius = radius
        self.active = True
        self.number = number

        self.ball_id = self.canvas.create_oval(
            x - radius, y - radius,
            x + radius, y + radius,
            fill = colour,outline = 'black'
        )

        self.text_id = self.canvas.create_text(
            x, y,
            text = str(self.number) if self.number != 0 else " ",
            fill='white',
            font=("Arial Black", 10)
        )

    def move(self):
        if not self.active:
            return
        self.x += self.v_x * 1
        self.y += self.v_y * 1

        self.v_x *= 0.98
        self.v_y *= 0.98

        if abs(self.v_x) < 0.2: self.v_x = 0
        if abs(self.v_y) < 0.2: self.v_y = 0

        self.wall_collision_check()

        self.canvas.coords(self.ball_id,
                           self.x - self.radius, self.y - self.radius,
                           self.x + self.radius, self.y + self.radius)
        self.canvas.coords(self.text_id,
                           self.x, self.y)

        for x, y, r in self.game.pockets:
            if (((self.x - x) ** 2) + ((self.y - y) ** 2) <= r**2):
                self.active = False
                self.canvas.delete(self.ball_id)
                self.canvas.delete(self.text_id)
                self.game.ball_potted(self)
                break

    def wall_collision_check(self):
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        if self.x - self.radius < 1:
            self.v_x = -self.v_x
            self.x = self.radius + 1
        if self.x + self.radius > width - 1:
            self.v_x = -self.v_x
            self.x = width - self.radius - 1
        if self.y - self.radius < 1:
            self.v_y = -self.v_y
            self.y = self.radius + 1
        if self.y + self.radius > height - 1:
            self.v_y = -self.v_y
            self.y = height -  self.radius - 1

    def is_moving(self):
        return abs(self.v_x) > 0 or abs(self.v_y) > 0

class Billiard:
    def __init__(self,root):
        self.root = root
        self.root.title("BILLIARD")

        self.canvas = tk.Canvas(root, width=800, height=400, bg="green", highlightthickness=3,
                                highlightbackground="black")
        self.canvas.pack(side = tk.LEFT)

        self.control_frame = tk.Frame(root)
        self.control_frame.pack(side=tk.RIGHT, fill = tk.Y)

        self.name1_var = tk.StringVar(value = "Player 1")
        self.name2_var = tk.StringVar(value = "Player 2")

        self.first_player = 1

        tk.Label(self.control_frame,text = "Name of first player").pack()
        tk.Entry(self.control_frame, textvariable=self.name1_var).pack()

        tk.Label(self.control_frame, text="Name of second player").pack()
        tk.Entry(self.control_frame, textvariable=self.name2_var).pack()

        tk.Button(self.control_frame, text="First player starts", command=lambda : self.set_starting_player(1)).pack()
        tk.Button(self.control_frame, text="Second player starts", command=lambda: self.set_starting_player(2)).pack()

        self.info = tk.Text(self.control_frame,width=30)
        self.info.pack(fill = tk.BOTH, expand = True)

        self.restatart_button = tk.Button(self.control_frame, text="Restart game", command=self.restart_game)
        self.restatart_button.pack(pady = 15)

        self.canvas.bind("<Button-1>",self.start_shot)
        self.canvas.bind("<ButtonRelease-1>", self.shoot)

        self.restart_game()

        self.root.after(100, self.ball_move)

    def set_starting_player(self,player):
        self.first_player = player
        # new game
        self.restart_game()



    def init_game(self):
        self.canvas.delete("all")
        self.balls = []
        self.current_player = self.first_player
        self.potted = {1:0, 2:0}
        self.game_over = False
        self.place_cue_ball = False
        self.just_shot = False
        self.can_shoot = True
        self.scored_this_turn = False
        self.cue_line = None
        self.aim_line = None
        self.cue_start = None
        self.pockets = []
        self.drow_pockets()
        self.setup_balls()
        self.update_info()

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
            self.canvas.create_oval(
            x - r, y - r,
            x + r, y + r,
            fill='black'
            )
            self.pockets.append([x,y,r])

    def setup_balls(self):
        start_x = 600
        start_y = 200
        spacing = 2
        count = 1
        for row in range(5):
            for j in range(row+1):
                if count > 15:
                    return
                x = start_x + row * 2 * 15 * math.cos(math.radians(30))
                y = start_y + (j - row / 2) * (2 * 15 + spacing)
                self.balls.append(Ball(self.canvas,self,x,y,0,0,15,'red',count))
                count += 1

        self.cue_ball = Ball(self.canvas,self,150,200,0,0,15,'white',0)
        self.balls.append(self.cue_ball)

    def start_shot(self, event):
        if self.game_over:
            return
        if self.place_cue_ball:
            self.cue_ball = Ball(self.canvas,self, event.x, event.y,0,0,15,'white',0)
            self.balls.append(self.cue_ball)
            self.place_cue_ball = False
            self.can_shoot = True
            self.update_info()
            return
        if not self.can_shoot or self.cue_ball is None:
            return
        if any(ball.is_moving() for ball in self.balls):
            return
        self.cue_start = (event.x,event.y)
        self.aim_line = self.canvas.create_line(
            self.cue_ball.x, self.cue_ball.y,
            event.x, event.y, fill = "white",
            dash = (3,2)
        )
        self.canvas.bind("<Motion>", self.update_aim_line)
    def update_aim_line(self, event):
        if self.aim_line:
            self.canvas.coords(self.aim_line,self.cue_ball.x, self.cue_ball.y,event.x, event.y)

    def shoot(self, event):
        if not self.cue_start or self.game_over or self.place_cue_ball:
            return
        dx = self.cue_start[0] - event.x
        dy = self.cue_start[1] - event.y
        self.cue_ball.v_x = 0.2 * dx
        self.cue_ball.v_y = 0.2 * dy
        self.just_shot = True
        self.scored_this_turn = False
        self.can_shoot = False
        if self.aim_line:
            self.canvas.delete(self.aim_line)
        self.aim_line = None
        self.cue_start = None

    def ball_move(self):
        any_moving = False
        for ball in self.balls:
            if ball.active:
                ball.move()
                any_moving = any_moving or ball.is_moving()

        self.collision_check()
        if self.just_shot and not any_moving:
            self.resolve_turn()
            self.just_shot = False

        self.update_info()
        self.root.after(30, self.ball_move)

    def collision_check(self):
        for i in range(len(self.balls)):
            for j in range(i + 1, len(self.balls)):
                ball_1 = self.balls[i]
                ball_2 = self.balls[j]
                if not ball_1.active or not ball_2.active:
                    continue
                dx = ball_2.x - ball_1.x
                dy = ball_2.y - ball_1.y
                dist = math.sqrt(dx**2 + dy**2)
                if dist == 0:
                    dist = 0.05
                if dist < ball_2.radius + ball_1.radius:
                    nx = dx / dist
                    ny = dy / dist
                    p1 = ball_1.v_x * nx + ball_1.v_y * ny
                    p2 = ball_2.v_x * nx + ball_2.v_y * ny
                    ball_1.v_x += (p2 - p1) * nx
                    ball_1.v_y += (p2 - p1) * ny
                    ball_2.v_x += (p1 - p2) * nx
                    ball_2.v_y += (p1 - p2) * ny
                    overlap = ball_2.radius + ball_1.radius - dist + 0.1
                    ball_1.x -= nx * overlap / 2
                    ball_1.y -= ny * overlap / 2
                    ball_2.x += nx * overlap / 2
                    ball_2.y += ny * overlap / 2

    def ball_potted(self, ball):
        self.canvas.delete(ball.ball_id)
        self.canvas.delete(ball.text_id)
        self.balls.remove(ball)
        if ball.number == 0:
            self.place_cue_ball = True
            self.cue_ball = None
            self.scored_this_turn = False
            self.update_info()
        else:
            self.potted[self.current_player] += 1
            self.scored_this_turn = True

    def update_info(self):
        self.info.delete(1.0,tk.END)
        self.info.insert(tk.END, f"{self.get_player_name(self.current_player)}\n")
        self.info.insert(tk.END, f"Points: {self.potted[self.current_player]}\n")
        if self.game_over:
            self.info.insert(tk.END, f"Game over\n")
        if self.place_cue_ball:
            self.info.insert(tk.END, f"Place cue ball pls\n")


    def resolve_turn(self):
        if self.potted[self.current_player] >= 8:
            self.info.insert(tk.END, f"{self.get_player_name(self.current_player)} won.Game over")
            self.game_over = True
            self.can_shoot = False
        else:
            if not self.scored_this_turn:
                self.current_player = 3 - self.current_player
                self.update_info()
            if self.place_cue_ball:
                self.can_shoot = False
            else:
                self.can_shoot = True
        self.scored_this_turn = False

    def get_player_name(self, number):
        return self.name1_var.get() if number == 1 else self.name2_var.get()


    def restart_game(self):
        self.init_game()


if __name__ == "__main__":
    root = tk.Tk()
    app = Billiard(root)
    root.mainloop()