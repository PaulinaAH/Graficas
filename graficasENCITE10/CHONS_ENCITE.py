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
ps_p = [47.28, 5.47, 36.72, 1.89, 0.12]
pc_p = [47.37, 5.57, 40.03, 1.73, 0.06]
si_p = [49.82, 5.80, 38.10, 1.27, 0.04]
ref_p = [43.40, 6.10,44.20, 0.00, 0.50]

#valores sd en orden: C H O N S
ps_sd = [1.69, 0.22, 1.85, 0.27, 0.02]
pc_sd = [0.77, 0.05, 0.55, 0.04, 0.05]
si_sd = [1.34, 0.17, 1.41, 0.03, 0.03]

width = 0.15


#barras
plt.bar(x-0.2, ps_p, width, color='#E0E0E0', edgecolor = 'black', yerr = ps_sd, capsize = 3)
plt.bar(x, pc_p, width, color='#616161', edgecolor = 'black', yerr = pc_sd, capsize = 3)
plt.bar(x+0.2, si_p, width, color='#9E9E9E',edgecolor = 'black', yerr = si_sd, capsize = 3)
plt.bar(x+0.4, ref_p, width, color = "black", edgecolor ="black")

plt.show()
#plt.savefig('chons_ENCITE.png', dpi=1800)

