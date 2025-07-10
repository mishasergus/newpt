import numpy as np
import tkinter as tk
import random
import math

from matplotlib.pyplot import figure


class Figure: #Створюю матер клас фігури
    list_of_x_coords = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']#Масив з клітинками створений саме в класі а не
    #в об'єкті
    def __init__(self, canvas, game_ref, color, y_cord, x_letter, is_alive = True):#що незрозумілого це
        # конструктор іди гортай
        self.canvas = canvas#канвас це типу вікно
        self.game = game_ref#це буде клас гри
        self.color = color
        self.is_alive = is_alive

        self.y_cord = y_cord
        self.x_cord = Figure.list_of_x_coords.index(x_letter)#тут я беру букву та конвертую в індекс

        cell_width = int(self.canvas['width']) / 8#розраховую ширину клітинки
        cell_height = int(self.canvas['height']) / 8

        center_x = self.x_cord * cell_width + cell_width / 2
        # Координати канваса починаються з лівого верхнього кута
        # ми спочатку розраховуємо довж 1 кліт потім множимо на інд кліт а потім від шир канв відн
        # значення та ще половину кліт щоб текст був посередині
        center_y = (int(self.canvas['height']) - cell_height * self.y_cord) - (cell_height / 2)

        self.figure_id = self.canvas.create_text(#ця шняга малює на канвасі текст покищо тексту нема бо це конст
            center_x,
            center_y,
            text="",
            fill=self.color,
            font=("Arial Black", 35)
        )

class Pawn(Figure):
    def __init__(self, canvas, game_ref, color, y_cord, x_letter, is_alive = True):
        super().__init__(canvas, game_ref, color, y_cord, x_letter, is_alive)#конструктор успадкування
        self.canvas.itemconfig(self.figure_id, text="♙")# тут ми візуалізуємо ппішака типу в нього тепер є текст

class Chess:#клас гри
    def __init__(self,root):
        self.root = root#сам ткшний рут
        self.root.title("Chess")#заголовок

        self.board = [[None for _ in range(8)] for _ in range(8)]

        self.canvas = tk.Canvas(root, width=600, height=600, bg="#F5DEB3", highlightthickness=3,
                                highlightbackground="#F5DEB3")#Той самий легендарний канвас(леонардо малював монолізу тут)
        self.canvas.pack()#Розпаковую його в рут

        self.draw_board()#малюю чорні клітинки
        self.draw_figures()#фігури

    def draw_board(self):
        cell_size_x = int(self.canvas['width']) / 8#розраховую розмір клітинки
        cell_size_y = int(self.canvas['height']) / 8


        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 1:#перевіряю чи клітинка повинна бути чорною
                    x1 = j * cell_size_x#далі треба буде мати лівий верхній та правий нижній коорд клітинки(коорд поч з лівої
                    # верхньої частини жошки)
                    y1 = int(self.canvas['height']) - (i * cell_size_y) - cell_size_y
                    x2 = x1 + cell_size_x
                    y2 = y1 + cell_size_y
                    self.canvas.create_rectangle(#створюю клітинку
                        x1,
                        y1,
                        x2,
                        y2,
                        fill = '#8B4513'
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
            self.board[1][i] = Pawn(self.canvas, self, 'black',6,Figure.list_of_x_coords[i])
            self.board[7][i] = Pawn(self.canvas, self, 'white', 1, Figure.list_of_x_coords[i])
        # white Bishop
        # white Knight
        # white Queen
        # white King
        # white Knight
        # white Bishop
        # white Rook

if __name__ == "__main__":#якщо цей проект буде бібліотекою то все що нище не запуститься
    root = tk.Tk()#створюю вікно в тк
    app = Chess(root)#створюю об'єкт класу
    root.mainloop()# якщо не помиляюся ця штука закриває вікно без ерорів








