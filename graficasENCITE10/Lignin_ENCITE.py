# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 21:39:47 2022
Perfil lignoceluloso para ENCITE
@author: Paulina
"""

import matplotlib.pyplot as plt
import numpy as np

#Número de grupos
x = np.arange(3)

#valores prom en orden: Lig, Hem, Cel

ps_p = [22.66, 9.65, 27.20]
pc_p = [26.13, 11.59, 34.19]
si_p = [43.49, 9.15, 32.37]
ref_p = [41, 12, 11]

#valores sd en orden:Lig, Hem, Cel
ps_sd = [2.16, 0.87, 0.77]
pc_sd = [0.72, 1.22, 5.79]
si_sd = [0.24, 2.04, 2.43]

width = 0.15

#barras
plt.bar(x-0.2, ps_p, width, color='#E0E0E0', edgecolor = 'black', yerr = ps_sd, capsize = 5)
plt.bar(x, pc_p, width, color='#616161', edgecolor = 'black', yerr = pc_sd, capsize = 5)
plt.bar(x+0.20, si_p, width, color='#9E9E9E',edgecolor = 'black', yerr = si_sd, capsize = 5)
plt.bar(x+0.4, ref_p, width, color = "black", edgecolor ="black")

#plt.show()
plt.savefig('Lignin2_ENCITE.png', dpi=1800)