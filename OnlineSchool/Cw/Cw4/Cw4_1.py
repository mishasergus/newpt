import matplotlib.pyplot as plt

arr = [1,2]
print(sum(arr))

all_data = []
L = []
T = []

with open('T(L).csv', 'r') as my_file:
    print(my_file.readline())
    lst_line = my_file.readlines()
    for el in lst_line:
        el = [eval(a) for a in el.strip().split(',')]
        all_data.append(el)
        L.append(el[0])
        T.append(el[1])

print(all_data)
print(L)
print(T)

plt.grid()
plt.title('T(L)')
plt.plot([L[i] for i in range(len(L))],T,'r.')
plt.xlabel('L,cm')
plt.ylabel('T,c')
plt.plot()
plt.show()