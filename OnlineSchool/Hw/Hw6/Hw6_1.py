import numpy as np
import pandas as pd

u_i_vs_r = pd.read_csv("8-u_i_vs_r_segmented.csv")
lisOfDir = []
r = 0
uv = 0
ia = 0
for i in range(len(u_i_vs_r['U_V'])):
    if u_i_vs_r['U_V'].iloc[i][0] == 'r':
        r = float(u_i_vs_r['U_V'].iloc[i][4:])
        continue
    uv = float(u_i_vs_r['U_V'].iloc[i])
    ia = float(u_i_vs_r['I_A'].iloc[i])
    lisOfDir.append({'R_CM':r,
                     'U_V':uv,
                     'I_A':ia
                     })
lisOfDir = pd.DataFrame(lisOfDir)
lisOfDir = lisOfDir.pivot_table(
    index='R_CM',  # Назва стовпця з df_long_format для індексу
    columns='U_V',  # Назва стовпця з df_long_format для колонок
    values='I_A',  # Назва стовпця з df_long_format для значень у клітинках
    aggfunc='first'  # Використовуємо 'first', оскільки для кожної комбінації має бути лише одне значення
)
lisOfDir = lisOfDir.fillna('-')
print(lisOfDir)
