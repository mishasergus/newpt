import numpy as np
import tkinter as tk
import random
import math

from matplotlib.pyplot import figure


class Figure: #Створюю матер клас фігури
    list_of_x_coords = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']#Масив з клітинками створений саме в класі а не
    #в об'єкті
    def __init__(self, canvas, game_ref, color, y_cord, x_letter, is_alive = True, is_active = False):#що незрозумілого це
        # конструктор іди гортай
        self.canvas = canvas#канвас це типу вікно
        self.game = game_ref#це буде клас гри
        self.color = color
        self.is_alive = is_alive
        self.is_active = is_active

        self.y_cord = y_cord
        self.x_cord = Figure.list_of_x_coords.index(x_letter)#тут я беру букву та конвертую в індекс

        self.center_x = self.x_cord * self.game.cell_width + self.game.cell_width / 2
        # Координати канваса починаються з лівого верхнього кута
        # ми спочатку розраховуємо довж 1 кліт потім множимо на інд кліт а потім від шир канв відн
        # значення та ще половину кліт щоб текст був посередині
        self.center_y = (float(self.canvas['height']) - self.game.cell_height * self.y_cord) - (self.game.cell_height / 2)

        self.figure_id = self.canvas.create_text(#ця шняга малює на канвасі текст покищо тексту нема бо це конст
            self.center_x,
            self.center_y,
            text="",
            fill=self.color,
            font=("Arial Black", 35)
        )

    def show_variants(self):
        pass

    def delete_variants(self):
        pass
    #self.canvas.delete(self.points[0])

class Pawn(Figure):
    def __init__(self, canvas, game_ref, color, y_cord, x_letter, is_alive = True, is_active = False, have_ever_moved = False):
        super().__init__(canvas, game_ref, color, y_cord, x_letter, is_alive, is_active)#конструктор успадкування
        self.canvas.itemconfig(self.figure_id, text="♙")# тут ми візуалізуємо ппішака типу в нього тепер є текст
        self.have_ever_moved = have_ever_moved#Типу це спец штука для пішака бо пішак спочатку може ходити на 2 вперед замість 1
        self.variants = []
        self.points = []

    def show_variants(self):
        self.points = []
        for i in range(1,3):
            if self.y_cord < 7 and self.game.board[self.y_cord + i][self.x_cord] is None and i == 1:
                self.points.append(self.canvas.create_oval(
                    self.center_x - 5, self.center_y - 5 - self.game.cell_height * i,
                    self.center_x + 5, self.center_y + 5 - self.game.cell_height * i,
                    fill="gray",
                    outline=""  # прибираю чорну обводку
                ))
            elif not self.have_ever_moved and self.game.board[self.y_cord + i][self.x_cord] is None:
                self.points.append(self.canvas.create_oval(
                    self.center_x - 5, self.center_y - 5 - self.game.cell_height * 2,
                    self.center_x + 5, self.center_y + 5 - self.game.cell_height * 2,
                    fill="gray",
                    outline=""  # прибираю чорну обводку
                ))
            else:
                break
            self.variants.append([self.y_cord + i, self.x_cord])
        if (self.y_cord < 7 and self.x_cord != 0):
            obj = self.game.board[self.y_cord + 1][self.x_cord - 1]
            if (obj is not None and
                    ((obj.color == 'black' and self.game.white_moving) or
                    (obj.color == 'white' and not self.game.white_moving))):
                self.points.append(self.canvas.create_oval(
                    self.center_x - 5 - self.game.cell_width, self.center_y - 5 - self.game.cell_height,
                    self.center_x + 5 - self.game.cell_width, self.center_y + 5 - self.game.cell_height,
                    fill="gray",
                    outline=""  # прибираю чорну обводку
                ))
                self.variants.append([self.y_cord + 1, self.x_cord - 1])
        if (self.y_cord < 7 and self.x_cord != 7):
            obj = self.game.board[self.y_cord + 1][self.x_cord + 1]
            if (obj is not None and
                ((obj.color == 'black' and self.game.white_moving) or
                (obj.color == 'white' and not self.game.white_moving))):
                self.points.append(self.canvas.create_oval(
                    self.center_x - 5 + self.game.cell_width, self.center_y - 5 - self.game.cell_height,
                    self.center_x + 5 + self.game.cell_width, self.center_y + 5 - self.game.cell_height,
                    fill="gray",
                    outline=""  # прибираю чорну обводку
                ))
                self.variants.append([self.y_cord + 1, self.x_cord + 1])
        print(self.variants)

class Chess:#клас гри

    def __init__(self,root):
        self.root = root#сам ткшний рут
        self.root.title("Chess")#заголовок

        self.board = [[None for _ in range(8)] for _ in range(8)]#Створюємо дошку та зповнюємо нанами
        # !!!!ВАЖЛИВО!!!! ЯКЩО ВИВЕСТИ ДОШКУ ТО ВОНА БУДЕ ПЕРЕВЕРНУТА ТИПУ
        # W - white
        # B - black
        # W W W W W W W W
        # W W W W W W W W
        #
        #
        #
        #
        # B B B B B B B B
        # B B B B B B B B

        self.canvas = tk.Canvas(root, width=640, height=640, bg="#F5DEB3", highlightthickness=3,
                                highlightbackground="black")#Той самий легендарний канвас(леонардо малював монолізу тут)
        self.canvas.pack(side = tk.LEFT)#Розпаковую його в рут

        self.cell_width = float(self.canvas['width']) / 8  # розраховую ширину клітинки
        self.cell_height = float(self.canvas['height']) / 8

        self.draw_board()#малюю чорні клітинки
        self.draw_figures()#фігури

        self.white_moving = True # Змінна черги
        self.first_click = None #Перший клік який повинен вибрати фігуру

        self.canvas.bind("<Button-1>", self.click) # При натисканні лівої кнопки буде виклик self.click

    def draw_board(self):


        for i in range(8):
            for j in range(8):
                if (i + j) % 2 != 1:#перевіряю чи клітинка повинна бути чорною
                    x1 = j * self.cell_width#далі треба буде мати лівий верхній та правий нижній коорд клітинки(коорд поч з лівої
                    # верхньої частини жошки)
                    y1 = float(self.canvas['height']) - (i * self.cell_height) - self.cell_height
                    x2 = x1 + self.cell_width
                    y2 = y1 + self.cell_height
                    self.canvas.create_rectangle(#створюю клітинку
                        x1,
                        y1,
                        x2,
                        y2,
                        fill = '#8B4513',
                        outline=""# прибираю чорну обводку квадратів
                    )
    def draw_figures(self):
        # black Bishop
        # black Knight
        # black Queen
        # black King
        # black Knight
        # black Bishop
        # black Rook
        for i in range(8):#Pawns
            x = random.randint(2,5)
            self.board[x][i] = Pawn(self.canvas, self, 'black',x,Figure.list_of_x_coords[i])#створюю пішаків
            self.board[1][i] = Pawn(self.canvas, self, 'white', 1, Figure.list_of_x_coords[i])
        # white Bishop
        # white Knight
        # white Queen
        # white King
        # white Knight
        # white Bishop
        # white Rook

    def click(self,event):
        if self.first_click is None:# Перевірка чи є клік (першим) якщо не вибрана ніяка фігура
            row = 7 - int(event.y / self.cell_height)  # Рахую номен рядка
            col = int(event.x / self.cell_width)#Рахую номер колонки
            self.first_click = (row, col)# задаю у змінну коорд на дошці щоб потім ми знали з якою фігурою взаємодіємо
            if self.board[row][col] is not None:# перевіряю чи є на клітинці фігура
                on_cl = self.board[row][col]# щоб не звертатися до дошки роблю змінну
                if ((self.white_moving and on_cl.color == 'white') or
                    (not self.white_moving and on_cl.color == 'black')):#білі взаємодіють з білими а чорні з чорними
                    on_cl.is_active = True# роблю фігуру активною
                    on_cl.show_variants()
                else:
                    self.first_click = None#не вийде вибрати інший колір
            else:
                self.first_click = None#не вийде походити пустотою
        else:
            on_cl = self.board[self.first_click[0]][self.first_click[1]]
            self.first_click = None

if __name__ == "__main__":#якщо цей проект буде бібліотекою то все що нище не запуститься
    root = tk.Tk()#створюю вікно в тк
    app = Chess(root)#створюю об'єкт класу
    root.mainloop()# якщо не помиляюся ця штука закриває вікно без ерорів