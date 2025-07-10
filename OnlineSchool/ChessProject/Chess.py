import numpy as np
import tkinter as tk
import random
import math

from matplotlib.pyplot import figure


class Figure: #Створюю матер клас фігури
    list_of_x_coords = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']#Масив з клітинками створений саме в класі а не
    #в об'єкті
    def __init__(self, canvas, game_ref, color, is_alive, y_cord, x_letter):#що незрозумілого це
        # конструктор іди гортай
        self.canvas = canvas#канвас це типу вікно
        self.game = game_ref#це буде клас гри
        self.color = color
        self.is_alive = is_alive

        self.y_cord = y_cord
        self.x_cord = Figure.list_of_x_coords.index(x_letter)#тут я беру букву та конвертую в індекс

        self.figure_id = self.canvas.create_text(#ця шняга малює на канвасі текст покищо тексту нема бо це конст
            (self.canvas['width'] - self.canvas['width'] / 8 * self.x_cord) - (self.canvas['width'] / 8 / 2),
            #Координати канваса починаються з лівого верхнього кута
            #ми спочатку розраховуємо довж 1 кліт потім множимо на інд кліт а потім від шир канв відн
            # значення та ще половину кліт щоб текст був посередині
            (self.canvas['height'] - self.canvas['height'] / 8 * self.y_cord) - (self.canvas['height'] / 8 / 2),
            text="",
            fill='black',
            font=("Arial Black", 12)
        )

class Pawn(Figure):
    def __init__(self, canvas, game_ref, color, is_alive, x_cord, y_letter):
        super().__init__(canvas, game_ref, color, is_alive, x_cord, y_letter)#конструктор успадкування
        self.canvas.itemconfig(self.figure_id, text="P")# тут ми візуалізуємо ппішака типу в нього тепер є текст









