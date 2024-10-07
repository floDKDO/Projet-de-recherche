import matplotlib.pyplot as plt
import numpy as np

# Valeurs obtenues avec les mesures
applications = ['0', '2', '4', '6', '8']
cpu = [6.305, 25.9337, 28.8212, 32.3675, 36.9688]

# Valeurs des intervalles de confiances à 95%
cpu_ci_95_min = [5.116, 23.605, 26.553, 30.846, 35.803]
cpu_ci_95_max = [7.494, 28.262, 31.089, 33.889, 38.134]

cpu_half_widths = [(ci_max - ci_min) / 2 for ci_min, ci_max in zip(cpu_ci_95_min, cpu_ci_95_max)]

num_apps = len(applications)
bar_width = 0.5

# retourne un tableau de la forme [0, 1, 2, 3], un indice par application
index = np.arange(num_apps)

plt.grid(zorder=0)
plt.bar(index, cpu, bar_width, zorder = 3)

# Afficher la barre d'erreur
plt.errorbar(index, cpu, yerr=np.transpose(cpu_half_widths), fmt='none', capsize=5, color='black', zorder = 4)

plt.xlabel('Number of BG Apps')
plt.ylabel('CPU Usage (%)')
plt.title('Average CPU usage for all BG Apps number with a 95% confidence interval')
plt.xticks(index, applications)  # mettre les noms des applications au centre des deux barres
#plt.legend()



plt.show()