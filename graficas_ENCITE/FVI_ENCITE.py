# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 22:37:44 2022
FVI para ENCITE
@author: Paulina
"""

import matplotlib.pyplot as plt
import numpy as np

#Número de grupos
x = np.arange(1)

#promedios
ps_p = 237.02
pc_p = 215.69
si_p = 319.10
ref_p = 309

#desviación
ps_sd = 8.00
pc_sd = 12.12
si_sd = 5.17

#gráfica
plt.bar(x-1, height=ps_p, color='#E0E0E0', edgecolor = 'black', yerr = ps_sd, capsize = 5)
plt.bar(x, height=pc_p, color='#616161', edgecolor = 'black', yerr = pc_sd, capsize = 5)
plt.bar(x+1,height=si_p, color='#9E9E9E',edgecolor = 'black', yerr = si_sd, capsize = 5)
plt.bar(x+2, height=ref_p, color="black", edgecolor = "black")

#plt.show()
plt.savefig('FVI_ENCITE.png', dpi=1800)


