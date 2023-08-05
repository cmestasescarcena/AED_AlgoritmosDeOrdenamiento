import matplotlib.pyplot as plt
fig, ax = plt.subplots()
size         = ['100', '1000', '2000', '3000', '4000', '5000', '6000', '7000', '8000', '9000', '10000', '20000', '30000', '40000', '50000']
goTimes      = [0.00853, 0.83396, 3.51894, 8.48982, 16.24914, 25.70260, 29.76534, 47.91823, 74.56174, 86.11129, 139.94213, 595.70068, 1509.35840, 2965.99432, 4257.99858]
goTimes = list(map(lambda x: x / 1000, goTimes))
pythonTimes  = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
cppTimes     = [0.0001742667, 0.0091300000, 0.0353230667, 0.0840322667, 0.1446514000, 0.2287546667, 0.3355436000, 0.4525534000, 0.6416839333, 0.8691696667, 1.0102026000, 4.3920196000, 8.4991057333, 8.4991057333, 24.1031709333]
#cppTimes = list(map(lambda x: x * 1000, cppTimes))

allTimes     = {'Go':goTimes, 'Python': pythonTimes, 'C++': cppTimes}

ax.plot(size, allTimes['Go'], label = 'Go')
ax.plot(size, allTimes['Python'], label = 'Python')
ax.plot(size, allTimes['C++'], label = 'C++')
ax.legend(loc = 'upper left')
plt.xlabel('Cantidad de elementos')
plt.setp(ax.get_xticklabels(), rotation=30, ha='right')
plt.ylabel('Tiempo')
plt.title('Algoritmo de burbuja')

plt.show()