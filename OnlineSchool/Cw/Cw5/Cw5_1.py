import  matplotlib.pyplot as plt
import  numpy as np

data = np.loadtxt("furie-law.csv", delimiter = ',', skiprows = 1).T
print(data)
tau = data[0]
tCold = np.array(data[1])
tHot = np.array(data[2])
mCold = 1
mHot = 1
c = 4200

plt.plot(tau, tCold, color = "blue", marker='o')
plt.plot(tau, tHot, color = "red", marker='o')
plt.grid()
plt.xlabel("tau, c")
plt.ylabel("t, c")
plt.show()
###########HOT########
d_tau = np.array([tau[i]-tau[i-1] for i in range(1,len(tau))])
d_T_own = np.array([tHot[i-1]-tHot[i] for i in range(1,len(tHot))])
d_Q_tauHot = c*mHot*d_T_own/d_tau
dt = tHot - tCold
print(d_tau)
print(d_T_own)
print(d_Q_tauHot)
print(len(d_tau))
dt =dt[:-1]
plt.plot(dt, d_Q_tauHot, color = "black", marker='o')
plt.show()
