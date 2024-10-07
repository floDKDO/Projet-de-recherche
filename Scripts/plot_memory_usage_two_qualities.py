import matplotlib.pyplot as plt

#le fichier 'memory_RSS_f1_*.txt' contient les valeurs mesurées
with open('memory_RSS_f1_1080p.txt', 'r') as file:
    memory_usage1 = [int(line.strip()) for line in file] #enlever les whitespaces, convertir en int
    
with open('memory_RSS_f1_360p.txt', 'r') as file:
    memory_usage2 = [int(line.strip()) for line in file] #enlever les whitespaces, convertir en int

time_seconds1 = list(range(len(memory_usage1))) #0->len-1, converti en liste pour plt.plot
time_seconds2 = list(range(len(memory_usage2))) #0->len-1, converti en liste pour plt.plot

mean_memory1 = sum(memory_usage1) / len(memory_usage1)
mean_memory2 = sum(memory_usage2) / len(memory_usage2)

plt.plot(time_seconds1, memory_usage1, linestyle='-', label='1080p F1 race')
plt.plot(time_seconds2, memory_usage2, linestyle='-', label='360p F1 race')

plt.xlabel('Time (seconds)')
plt.ylabel('Memory Usage (kB)')
plt.title('Memory Usage Over Time')

plt.grid(True)
plt.legend()

plt.show()



