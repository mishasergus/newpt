import pandas as pd

T_L = pd.read_csv("T(L).csv")
print(T_L)
# print(T_L['L_cm'])
# print("GGGGGGGGGGGGGGGGGGGGGG")
# print(T_L.head(2))
# print("GGGGGGGGGGGGGGGGGGGGGG")
# print(T_L.tail(2))
# print("GGGGGGGGGGGGGGGGGGGGGG")
# print(T_L.shape)
# print("GGGGGGGGGGGGGGGGGGGGGG")
# print(T_L.info())
# print("GGGGGGGGGGGGGGGGGGGGGG")
print(T_L.iloc[2])
print("GGGGGGGGGGGGGGGGGGGGGG")
print(T_L['L_cm'].iloc[2])
print("GGGGGGGGGGGGGGGGGGGGGG")
print(T_L.iloc[2:7])
print("GGGGGGGGGGGGGGGGGGGGGG")
print(T_L[T_L['L_cm']>40])