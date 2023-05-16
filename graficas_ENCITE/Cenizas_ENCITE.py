# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 23:08:20 2022
Cenizas para ENCITE 10
@author: Paulina
"""

import matplotlib.pyplot as plt
import numpy as np

#Número de grupos
x = np.arange(1)

#promedios
ps_p = 12
pc_p = 12
si_p = 11
ref_p = 11

#desviación
ps_sd = 0.3
pc_sd = 0.2
si_sd = 0.7

#gráfica
plt.bar(x-1, height=ps_p, color='#E0E0E0', edgecolor = 'black', yerr = ps_sd, capsize = 5)
plt.bar(x, height=pc_p, color='#616161', edgecolor = 'black', yerr = pc_sd, capsize = 5)
plt.bar(x+1,height=si_p, color='#9E9E9E',edgecolor = 'black', yerr = si_sd, capsize = 5)
plt.bar(x+2, height=ref_p, color="black", edgecolor = "black")

plt.show()
#plt.savefig('Cenizas_ENCITE.png', dpi=1800)
