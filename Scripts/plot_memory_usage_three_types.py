import matplotlib.pyplot as plt

#le fichier 'memory_RSS_*.txt' contient les valeurs mesurées
with open('memory_RSS_f1_1080p.txt', 'r') as file:
    memory_usage1 = [int(line.strip()) for line in file] #enlever les whitespaces, convertir en int
    
with open('memory_RSS_cartoon_1080p.txt', 'r') as file:
    memory_usage2 = [int(line.strip()) for line in file] #enlever les whitespaces, convertir en int
    
with open('memory_RSS_black_1080p.txt', 'r') as file:
    memory_usage3 = [int(line.strip()) for line in file] #enlever les whitespaces, convertir en int

time_seconds1 = list(range(len(memory_usage1))) #0->len-1, converti en liste pour plt.plot
time_seconds2 = list(range(len(memory_usage2))) #0->len-1, converti en liste pour plt.plot
time_seconds3 = list(range(len(memory_usage3))) #0->len-1, converti en liste pour plt.plot

mean_memory1 = sum(memory_usage1) / len(memory_usage1)
mean_memory2 = sum(memory_usage2) / len(memory_usage2)
mean_memory3 = sum(memory_usage3) / len(memory_usage3)

plt.plot(time_seconds1, memory_usage1, linestyle='-', label='F1 race')
plt.axhline(y=mean_memory1, color='darkblue', linestyle='--', label='F1 race average')
plt.plot(time_seconds2, memory_usage2, linestyle='-', label='cartoon')
plt.axhline(y=mean_memory2, color='peru', linestyle='--', label='cartoon average')
plt.plot(time_seconds3, memory_usage3, linestyle='-', label='black video')
plt.axhline(y=mean_memory3, color='darkgreen', linestyle='--', label='black video average')


plt.xlabel('Time (seconds)')
plt.ylabel('Memory Usage (kB)')
plt.title('Memory Usage Over Time')

plt.grid(True)
plt.legend(loc='center right', bbox_to_anchor=(1, 0.57), prop={'size': 9})

plt.show()