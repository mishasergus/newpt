import random
import  matplotlib.pyplot as plt
# dirF = {}
# nOf = 0
# lenth = 0
# F = 0
# for i in range(0,10):
#     F = random.randint(F+1,F+4)
#     lenth = random.randint(lenth + 20, lenth + 100)
#     dirF[F] = lenth
#     print(f"{nOf}  |  F: {F}H  |  l: {lenth}m")
#     nOf += 1
# startIndex = int(input("Start(index): "))
# endIndex = int(input("End(index): "))
# arrOfF = list(dirF.keys())
# if startIndex < endIndex:
#     l = dirF[arrOfF[endIndex]] - dirF[arrOfF[startIndex]]
#     print(f"l: {l}")
#     Fmid = 0
#     for i in range(startIndex, endIndex + 1):
#         Fmid += arrOfF[i]
#     Fmid /= endIndex - startIndex + 1
#     print(f"Fmidle: {Fmid}")
#     print(f"A: {Fmid * l}Dg")
########################PLT########################

# x = []
# y = []
# for i in range(10):
#     x.append(i)
#     y.append(i**2)

# plt.plot(x, y, color = "red", linestyle='--', marker='o')
# plt.title("Qadrat") #НАЗВА
# plt.xlabel("numbs") #НАЗВА ВІСІ X
# plt.ylabel("qadr of numbs") #НАЗВА ВІСІ Y
# plt.grid(True) #СІТКА
# plt.show() #Ну так
#
# x = [1,2,3,4,5,6,7,8,9,10]
#
# plt.plot(x,[x[i-1] ** 2 for i in x], label = "x^2", color = "red" , linestyle='--', marker='o')
# plt.plot(x,[x[i-1] ** 3 for i in x], label = "x^3",color = "blue" , linestyle='--', marker='o')
#
# plt.legend()
# plt.grid(True)
# plt.title("Func")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.show()


########################PROGA######################
# n = 10
# forces = []
# displacements = []
# x = 0
# error = False
#
# for i in range(n):
#     f = random.uniform(5, 100)
#     x += random.uniform(0.2, 3)
#     forces.append(f)
#     displacements.append(x)
#
# print(f"Index | Power(N) | Coord(m)")
#
# for i in range(n):
#     print(f"{i:>5} | {forces[i]:>8.2f} | {displacements[i]:>7.2f}")
# try:
#     startIndex = int(input("Start(index): "))
# except ValueError:
#     print("ERROR")
#     startIndex = -1
#     error = True
# if startIndex < 0 or startIndex >= n:
#     error = True
# while error:
#     try:
#         startIndex = int(input("Start(index): "))
#         if startIndex >= 0 and startIndex < n:
#             error = False
#     except ValueError:
#         print("ERROR")
#
# try:
#     endIndex = int(input("End(index): "))
# except ValueError:
#     print("ERROR")
#     endIndex = -1
#     error = True
# if endIndex < 0 or endIndex >= n:
#     error = True
# while error:
#     try:
#         endIndex = int(input("End(index): "))
#         if endIndex >= 0 and endIndex < n:
#             error = False
#     except ValueError:
#         print("ERROR")
# work = 0
# if endIndex < startIndex:
#     startIndex,endIndex = endIndex, startIndex
# for i in range(startIndex, endIndex):
#     f1 = forces[i]
#     f2 = forces[i + 1]
#     x1 = displacements[i]
#     x2 = displacements[i + 1]
#     delta_x = x2 - x1
#     avarage_force = (f1 + f2) / 2
#     work += avarage_force * delta_x
# print(f"Work: {work:.2f}Dg")
#
# plt.plot(displacements,forces, label = "A",color = "blue" , linestyle='--', marker='o')
#
# select_x = displacements[startIndex:endIndex + 1]
# select_y = forces[startIndex:endIndex + 1]
# plt.fill_between(select_x,select_y, label = f"WORK: {work:.2f} Dg",color = "red",alpha = 0.7)

# plt.legend()
# plt.grid(True)
# plt.title("A")
# plt.xlabel("L")
# plt.ylabel("F")
#
# plt.show()

# lis = [0] * 5
# print(lis)
#
# def fact(num):
#     fNum = 1
#     for i in range(1,num+1):
#         fNum *= i
#     return  fNum
#     # if num == 0:
#     #     return 1 #ЦЕ Я ШУКАВ ЯК ЩЕ МОЖНА ОПТИМЦЗУВАТИ
#     # else:
#     #     return num * fact(num - 1)
#
# lis = [fact(i) for i in range(0,7)]
# print(lis)
# print([lis[i] for i in range(2,7,2)])


# n = 1
# j = 2
# n, j = j, n
# print(n)
# print(j)






















