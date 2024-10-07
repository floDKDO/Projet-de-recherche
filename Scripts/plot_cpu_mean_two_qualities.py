import matplotlib.pyplot as plt
import numpy as np

# Valeurs obtenues avec les mesures
applications = ['1080p F1 race', '360p F1 race']
cpu = [4.90625, 5.0325]

num_apps = len(applications)
bar_width = 0.5

# retourne un tableau de la forme [0, 1, 2, 3], un indice par application
index = np.arange(num_apps)

plt.grid(zorder=0)
plt.bar(index[0], cpu[0], bar_width, zorder = 3)
plt.bar(index[1], cpu[1], bar_width, zorder = 3)

plt.xlabel('Videos')
plt.ylabel('CPU Usage (%)')
plt.title('Average CPU usage for two video qualities')
plt.xticks(index, applications)  # mettre les noms des applications au centre des deux barres
#plt.legend()



plt.show()