import matplotlib.pyplot as plt
import numpy as np

# Valeurs obtenues avec les mesures
applications = ['Angry Birds 2', 'Tetris' , 'Facebook', 'Gmail', 'Camera', 'Ebay']
cold_startup_times = [813, 424, 1053, 805, 555, 554]  # temps en ms
hot_startup_times = [183, 114, 106, 103, 147, 134]    # temps en ms

# Valeurs des intervalles de confiances à 95%
cold_ci_95_min = [782.898, 420.936, 1045.946, 770.768, 547.887, 551.722]
cold_ci_95_max = [843.102, 427.064, 1060.054, 839.232, 562.113, 556.278] 
hot_ci_95_min = [161.134, 107.188, 99.314, 90.866, 140.475, 124.742] 
hot_ci_95_max = [204.866, 120.212, 112.686, 115.134, 153.525, 143.258] 

cold_half_widths = [(ci_max - ci_min) / 2 for ci_min, ci_max in zip(cold_ci_95_min, cold_ci_95_max)]
hot_half_widths = [(ci_max - ci_min) / 2 for ci_min, ci_max in zip(hot_ci_95_min, hot_ci_95_max)]

num_apps = len(applications)
bar_width = 0.35

# retourne un tableau de la forme [0, 1, 2, 3], un indice par application
index = np.arange(num_apps)

fig, ax1 = plt.subplots()

plt.grid(zorder=0)
bars1 = ax1.bar(index, cold_startup_times, bar_width, label='Cold Startup', zorder = 3)
bars2 = ax1.bar(index + bar_width, hot_startup_times, bar_width, label='Hot Startup', zorder = 3)

# Afficher les barres d'erreurs
plt.errorbar(index, cold_startup_times, yerr=np.transpose(cold_half_widths), fmt='none', capsize=5, color='black', zorder = 4)
plt.errorbar(index + bar_width, hot_startup_times, yerr=np.transpose(hot_half_widths), fmt='none', capsize=5, color='black', zorder = 4)

ax1.set_xlabel('Applications')
ax1.set_ylabel('Startup Time (ms)')
ax1.set_title('Cold vs Hot Startup Time for Different Applications with 95% Confidence Interval')
ax1.set_xticks(index + bar_width / 2)
ax1.set_xticklabels(applications)
plt.xticks(rotation=45, ha='right')
ax1.legend(loc='upper left')
plt.yticks(np.arange(0, 1100, 100)) 


percentage_diff = [(hot - cold) / cold * 100 for hot, cold in zip(hot_startup_times, cold_startup_times)]

# Deuxième axe y
ax2 = ax1.twinx()
ax2.set_ylabel('Difference between hot and cold start (%)')
ax2.plot(index + bar_width / 2, percentage_diff, marker='D', color='black', label='Percentage difference', linestyle='None', ms=8)
ax2.tick_params(axis='y')
ax2.legend(markerfirst=False, loc='upper right')

# Axe y dans l'ordre croissant
ax2.set_ylim(ax2.get_ylim()[::-1])

plt.show()
