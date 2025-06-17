def fact(num):
    fNum = 1
    for i in range(1,num+1):
        fNum *= i
    return  fNum
    # if num == 0:
    #     return 1 #ЦЕ Я ШУКАВ ЯК ЩЕ МОЖНА ОПТИМЦЗУВАТИ
    # else:
    #     return num * fact(num - 1)

lis = [fact(i) for i in range(0,7)]
print(lis)
print([lis[i] for i in range(2,7,2)])