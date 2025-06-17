import  matplotlib.pyplot as plt
import  numpy as np

data = np.loadtxt("T(S).csv", delimiter = ',', skiprows = 1).T
T_s, S_sm = data
T_s*=0.01
print(S_sm)
print(T_s)


# plt.plot(T_s, S_sm, color = "red", marker='o')
# plt.grid()
# plt.xlabel("T_s")
# plt.ylabel("S_sm")
# plt.show()

TMid = sum(T_s**2) / len(T_s)
SMid = sum(S_sm**2) / len(S_sm)
print(f"SMid:{SMid}")
print(f"TMid:{TMid}")
b = sum(np.array([(T_s[i]**2-TMid)*S_sm[i]**2 for i in range(len(S_sm))])) / sum(np.array([(T_s[i]**2-TMid)**2 for i in range(len(S_sm))]))
print(f"b:{b}")

a = SMid - b * TMid
print(f"a:{a}")

x_min = np.min(T_s)
x_max = np.max(T_s)
plt.plot(T_s**2, S_sm**2, color = "red", marker='o',linestyle=' ')
plt.plot(T_s**2, b*T_s**2+a, color = "green",linestyle='-')

# plt.plot([0,np.max(T_s)], [0+a,b*np.max(T_s)+a], color='blue', linestyle='-')

plt.grid()
plt.xlabel("T_s")
plt.ylabel("S_sm")
plt.show()