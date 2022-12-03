"""
EJEMPLO
Gráfica de barras agrupadas con desviación estándar muestral
"""

import matplotlib.pyplot as plt
import numpy as np

#Definir grupos
x = np.arange(2)

#valores de los promedios EN ORDEN [A, B]
p1_p = [32.03333333, 42.96666667]
p2_p = [40.4333333, 65.16666667]
p3_p = [21.9, 35.33333333]


#desviaciones estándar EN ORDEN [A,B]
p1_ds =[0.2081666, 0.2081666]
p2_ds = [0.115470054, 0.152752523]
p3_ds = [10, 0.057735027]

width = 0.15

#CONSTRUCCION de gráfica
plt.bar(x-0.2, p1_p, width, color = '#E0E0E0', edgecolor = 'black', yerr = p1_ds, capsize = 5)
plt.bar(x, p2_p, width, color = '#616161', edgecolor = 'black', yerr = p2_ds, capsize = 5)
plt.bar(x+0.2, p3_p, width, color = '#9E9E9E', edgecolor = 'black', yerr = p3_ds, capsize = 5)

plt.show()
#plt.savefig('plantas_ejemplo', dpi = 1800)

