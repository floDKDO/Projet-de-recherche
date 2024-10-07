import matplotlib.pyplot as plt
import numpy as np

# Valeurs obtenues avec les mesures
applications = ['1080p F1 race', '360p F1 race']
memory = [672275.64, 574019.28]

# Valeurs des intervalles de confiances à 95%
memory_ci_95_min = [670447.625, 569382.508]
memory_ci_95_max = [674103.655, 578656.052]

memory_half_widths = [(ci_max - ci_min) / 2 for ci_min, ci_max in zip(memory_ci_95_min, memory_ci_95_max)]

num_apps = len(applications)
bar_width = 0.5

# retourne un tableau de la forme [0, 1, 2, 3], un indice par application
index = np.arange(num_apps)

plt.grid(zorder=0)
plt.bar(index[0], memory[0], bar_width, zorder = 3)
plt.bar(index[1], memory[1], bar_width, zorder = 3)

# Afficher la barre d'erreur
plt.errorbar(index, memory, yerr=np.transpose(memory_half_widths), fmt='none', capsize=5, color='black', zorder = 4)

plt.xlabel('Videos')
plt.ylabel('Memory Usage (kB)')
plt.title('Average memory usage for two video qualities with a 95% confidence interval')
plt.xticks(index, applications)  # mettre les noms des applications au centre des deux barres
#plt.legend()

plt.ylim(550000, 700000)

plt.show()
