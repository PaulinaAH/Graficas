# -*- coding: utf-8 -*-
"""
Gráfica de barras para contenido elemental CHONS para ENCITE10
Autor: Paulina
"""

'''
Primero importaré las librerías que usaré para graficar
y agrupar mis barras
'''
import matplotlib.pyplot as plt 
import numpy as np

#Número de grupos
x = np.arange(5)

#valores promedio en orden: C H O N S
ps_p = [28, 47, 72, 38, 12]
pc_p = [47, 87, 43, 42, 16]
si_p = [49, 72, 50, 37, 24]
ref_p = [47, 91, 20, 20, 15]

#valores sd en orden: C H O N S
ps_sd = [1, 0.1, 1.5, 0.7, 0.2]
pc_sd = [0.2, 0.5, 0.5, 0.4, 0.5]
si_sd = [1.4, 0.7, 1.1, 0.3, 0.3]

width = 0.15


#barras
plt.bar(x-0.2, ps_p, width, color='#E0E0E0', edgecolor = 'black', yerr = ps_sd, capsize = 3)
plt.bar(x, pc_p, width, color='#616161', edgecolor = 'black', yerr = pc_sd, capsize = 3)
plt.bar(x+0.2, si_p, width, color='#9E9E9E',edgecolor = 'black', yerr = si_sd, capsize = 3)
plt.bar(x+0.4, ref_p, width, color = "black", edgecolor ="black")

plt.show()
#plt.savefig('chons_ENCITE.png', dpi=1800)

