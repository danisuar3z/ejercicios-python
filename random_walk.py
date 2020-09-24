# -*- coding: utf-8 -*-

# random_walk.py
# Daniel T. Suarez - suarezdanieltomas@gmail.com
# Ejercicio 6.10: Caminatas al azar

import numpy as np
from matplotlib import pyplot as plt


def randomwalk(largo):
    pasos = np.random.randint(-1, 2, largo)
    return pasos.cumsum()


# Genero datos
N = 100000
caminatas = [randomwalk(N) for i in range(12)]

# Busco la que mas se aleja y la que menos
dist_final = [abs(caminata[-1]) for caminata in caminatas]
max_index = dist_final.index(max(dist_final))
min_index = dist_final.index(min(dist_final))

# %%

# Ploteo
# Titulo principal
plt.suptitle('   Random walks')
ax1 = plt.subplot(2, 1, 1)
ax1.spines['bottom'].set_position(('data', 0))
ax1.spines['top'].set_color('none')
for i, caminata in enumerate(caminatas):
    # Matcheo los colores de los casos especiales
    if i == min_index:
        ax1.plot(caminata, linewidth=0.3, color='black')
    elif i == max_index:
        ax1.plot(caminata, linewidth=0.3, color='purple')
    else:
        ax1.plot(caminata, linewidth=0.3)
    plt.ylim(-600, 700)
    plt.yticks([-500, 0, 500])
    plt.xticks([0, 50000, 100000])
    plt.ylabel('Distance')
    # Titulo graph superior
    plt.title('12 walks')

# Mas alejada
plt.subplot(2, 2, 3)
plt.plot(caminatas[max_index], color='purple')
plt.ylim(-600, 700)
plt.yticks([-500, 0, 500])
plt.xticks([0, 50000, 100000])
plt.xlabel('Time')
plt.title('The one that moves further away')

# Menos alejada
plt.subplot(2, 2, 4)
plt.plot(caminatas[min_index], color='black')
plt.ylim(-600, 700)
plt.yticks([-500, 0, 500])
plt.xticks([0, 50000, 100000])
plt.xlabel('Time')
plt.title('The one that moves the least away')
