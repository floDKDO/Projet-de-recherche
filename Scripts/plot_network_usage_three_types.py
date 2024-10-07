import matplotlib.pyplot as plt

#le fichier 'network_bytes_received_*.txt' contient les valeurs mesurées
with open('network_bytes_received_f1_1080p.txt', 'r') as file:
    network_usage = [int(line.strip()) / 1000 for line in file] #enlever les whitespaces, convertir en int
    
with open('network_bytes_received_cartoon.txt', 'r') as file:
    network_usage2 = [int(line.strip()) / 1000 for line in file] #enlever les whitespaces, convertir en int
    
with open('network_bytes_received_black.txt', 'r') as file:
    network_usage3 = [int(line.strip()) / 1000 for line in file] #enlever les whitespaces, convertir en int

time_seconds = list(range(len(network_usage))) #0->len-1, converti en liste pour plt.plot
time_seconds2 = list(range(len(network_usage2))) #0->len-1, converti en liste pour plt.plot
time_seconds3 = list(range(len(network_usage3))) #0->len-1, converti en liste pour plt.plot

plt.plot(time_seconds, network_usage, linestyle='-', label='F1 race')
plt.plot(time_seconds2, network_usage2, linestyle='-', label='cartoon')
plt.plot(time_seconds3, network_usage3, linestyle='-', label='black video')

plt.xlabel('Time (seconds)')
plt.ylabel('Network Usage (kB)')
plt.title('Network Usage Over Time')

plt.grid(True)
plt.legend()

plt.show()
