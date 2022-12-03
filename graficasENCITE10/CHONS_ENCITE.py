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
ps_p = [49.28, 7.47, 38.72, 3.89, 1.12]
pc_p = [47.37, 8.57, 45.03, 4.73, 1.06]
si_p = [49.82, 7.80, 41.10, 3.27, 2.04]
ref_p = [47.40, 9.10,48.20, 2.00, 1.50]

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

