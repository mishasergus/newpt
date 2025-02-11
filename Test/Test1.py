from abc import  abstractmethod
import time
import os
from operator import index

#
# class Student:
#     def __init__(self, name, surename, marks):
#         self.name = name
#         self.surename = surename
#         self.marks = marks
#         self.midle_mark = 0
#
#     def add_mark(self):
#         while True:
#             zminna = int(input("Enter mark(0 to close): "))
#             if zminna == 0:
#                 break
#             self.marks.append(zminna)
#     def mid_mark(self):
#         sum = 0
#         n_of_marks = 0
#         for i in self.marks:
#             sum += i
#             n_of_marks += 1
#         self.midle_mark = sum/n_of_marks
#     def show(self):
#         print(f"name {self.name}, surename {self.surename}, marks {self.marks}")
#
#
#
# obg1 = Student("def", "def", [])
# obg2 = Student("def", "def", [])
# obg1.add_mark()
# obg1.mid_mark()
# print(obg1.midle_mark)
# obg2.add_mark()
# obg2.mid_mark()
# print(obg2.midle_mark)
#
# students = [obg1, obg2]
#
# for i in students:
#     if i.midle_mark > 4:
#         i.show()
# //////////////////////////////////////////////////////////////////////////////////
# class Store:
#     def __init__(self, name, location):
#         self.name = name
#         self.location = location
# class Buther_s(Store):
#     def __init__(self, name, location, list_of_products):
#         super().__init__(name, location)
#         self.list_of_products = list_of_products
# class Market(Store):
#     def __init__(self, name, location,list_of_E_products):
#         super().__init__(name, location)
#         self.list_of_E_products = list_of_E_products

# //////////////////////////////////////////////////////////////////////////////////
# file_r = "File.txt"
# file_w = "File_w.txt"
# num_of_lines = 0
# num_of_words = 0
# line = ''
# with open(file_r,"r") as myFile:
#     line = myFile.readlines()
#     print(line)
#     num_of_lines = line.__len__()
#     for i in line:
#         num_of_words += i.count(" ") + 1
# print(f"{num_of_words} words")
# print(f"{num_of_lines} lines")
#
# with open("File_w.txt","w") as IFile:
#     IFile.write(f"words: {num_of_words}  ")
#     IFile.write(f"lines: {num_of_lines}  ")
# //////////////////////////////////////////////////////////////////////////////////
# lis_of_marks = []
# best = 0
# while True:
#             zminna = int(input("Enter mark(0 to close): "))
#             if zminna == 0:
#                 break
#             lis_of_marks.append(zminna)
# for i in lis_of_marks:
#     if i > best:
#         best = i
# if best >= 4:
#     print("ZDAV (Pass)")
# else:
#     print("F-")

# //////////////////////////////////////////////////////////////////////////////////
# lis_of_comp_inv = ["Privat-50.", "Privat-20.", "Mono-20."]
# lis_of_comp = []
# lis_of_inv = []
# n_of_inv = 0
# for i in lis_of_comp_inv:
#     lis_of_comp.append(i[0:i.index('-')])
# print(lis_of_comp)
# for i in lis_of_comp_inv:
#     lis_of_inv.append(int(i[i.index('-')+1:i.index('.')]))
# print(lis_of_inv)
# company = input("Enter company: ")
# for i in lis_of_comp_inv:
#     if company in i:
#         print(i)
# index_partime = 0
# for i in lis_of_comp:
#     if company == i:
#         n_of_inv += lis_of_inv[index_partime]
#     index_partime += 1
# print(n_of_inv)
# //////////////////////////////////////////////////////////////////////////////////
# file = "Log.txt"
# with open("Log.txt", "w") as IFile:
#     while True:
#         massage = input(": ")
#         IFile.write(f"{massage},\n")
#         IFile.write(f"{time.localtime()},\n")