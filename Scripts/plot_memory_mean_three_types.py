import matplotlib.pyplot as plt
import numpy as np

# Valeurs obtenues avec les mesures
applications = ['F1 race', 'Cartoon', 'Black video']
memory = [672275.64, 585742.32, 548634.8]

# Valeurs des intervalles de confiances à 95%
memory_ci_95_min = [670447.625, 584609.188, 543552.684]
memory_ci_95_max = [674103.655, 586875.452, 553716.916]

memory_half_widths = [(ci_max - ci_min) / 2 for ci_min, ci_max in zip(memory_ci_95_min, memory_ci_95_max)]

num_apps = len(applications)
bar_width = 0.5

# retourne un tableau de la forme [0, 1, 2, 3], un indice par application
index = np.arange(num_apps)

plt.grid(zorder=0)
plt.bar(index[0], memory[0], bar_width, zorder = 3)
plt.bar(index[1], memory[1], bar_width, zorder = 3)
plt.bar(index[2], memory[2], bar_width, zorder = 3)

# Afficher la barre d'erreur
plt.errorbar(index, memory, yerr=np.transpose(memory_half_widths), fmt='none', capsize=5, color='black', zorder = 4)

plt.xlabel('Videos')
plt.ylabel('Memory Usage (kB)')
plt.title('Average memory usage for three types of videos with a 95% confidence interval')
plt.xticks(index, applications)  # mettre les noms des applications au centre des deux barres
#plt.legend()

plt.ylim(500000, 700000)

plt.show()