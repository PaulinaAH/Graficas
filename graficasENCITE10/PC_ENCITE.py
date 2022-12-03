"""
Created on Mon Nov  7 23:19:48 2022
Poder calorífico ENCITE
@author: Paulina
"""

import matplotlib.pyplot as plt
import numpy as np

#Número de grupos
x = np.arange(2)

#valores prom en orden: [teórico, real]

ps_p = [19.19, 20.84]
pc_p = [21.83, 21.24]
si_p = [20.23, 23.18]

#valores sd en orden: [teórico, real]

ps_sd = [1.13, 0.20]
pc_sd = [0.40, 0.04]
si_sd = [0.85, 0.20]

width = 0.15

#barras
plt.bar(x-0.2, ps_p, width, color='#E0E0E0', edgecolor = 'black', yerr = ps_sd, capsize = 5)
plt.bar(x, pc_p, width, color='#616161', edgecolor = 'black', yerr = pc_sd, capsize = 5)
plt.bar(x+0.20, si_p, width, color='#9E9E9E',edgecolor = 'black', yerr = si_sd, capsize = 5)
plt.axhline(y=20.7, color = "black", linestyle ="--")

#plt.show()
plt.savefig('PCStVsReal_CIOP2.png', dpi=1800)
