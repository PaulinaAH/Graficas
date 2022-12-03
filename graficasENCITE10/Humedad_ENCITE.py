# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 22:57:41 2022
Humedades para ENCITE 10
@author: Paulina
"""

import matplotlib.pyplot as plt 
import numpy as np

#Número de grupos
x = np.arange(2)


#valores prom en orden: C H O N S
ps_p = [8.95, 9.57]
pc_p = [17.21, 10.94]
si_p = [12.75, 9.05]
ref_p = [11, 13]

#valores sd en orden: C H O N S
ps_sd = [0.82, 0.06]
pc_sd = [0.51, 0.05]
si_sd = [0.79, 0.06]

width = 0.15

#barras

plt.bar(x-0.2, ps_p, width, color='#E0E0E0', edgecolor = 'black', yerr = ps_sd, capsize = 5)
plt.bar(x, pc_p, width, color='#616161', edgecolor = 'black', yerr = pc_sd, capsize = 5)
plt.bar(x+0.20, si_p, width, color='#9E9E9E',edgecolor = 'black', yerr = si_sd, capsize = 5)
plt.bar(x+0.40, ref_p, width, color='black',edgecolor = 'black', capsize = 5)

#plt.show()
plt.savefig('Humedad_ENCITE.png', dpi=1800)
