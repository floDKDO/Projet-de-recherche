import matplotlib.pyplot as plt

#le fichier 'cpu_percent_one_ps_f1_*.txt' contient les valeurs mesurées
with open('cpu_percent_one_ps_f1_1080p.txt', 'r') as file:
    cpu_usage1 = [float(line.strip().replace(',', '.')) for line in file] #enlever les whitespaces, convertir en int
    
with open('cpu_percent_one_ps_f1_360p.txt', 'r') as file:
    cpu_usage2 = [float(line.strip().replace(',', '.')) for line in file] #enlever les whitespaces, convertir en int

time_seconds1 = list(range(len(cpu_usage1))) #0->len-1, converti en liste pour plt.plot
time_seconds2 = list(range(len(cpu_usage2))) #0->len-1, converti en liste pour plt.plot

plt.plot(time_seconds1, cpu_usage1, linestyle='-', label='1080p F1 race')
plt.plot(time_seconds2, cpu_usage2, linestyle='-', label='360p F1 race')

plt.xlabel('Time (seconds)')
plt.ylabel('CPU Usage (%)')
plt.title('CPU Usage Over Time')

plt.ylim(0, 25)
plt.grid(True)
plt.legend()

plt.show()