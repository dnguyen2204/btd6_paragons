import matplotlib.pyplot as plt
import json

file = open('paragonLvls.json', 'r')
data = json.load(file)

pierce = data['pierce']
damage = data['damage']
ceramicDamage = data['ceramicDamage']
bossDamage = data['bossDamage']
eliteDamage = data['eliteDamage']
rate = data['rate']

file.close()

plt.plot(rate, color='magenta', marker='o', mfc='pink')
plt.xticks(range(0, 101, 10))
plt.ylabel('rate')
plt.xlabel('degree')
plt.title("rate vs degree")
plt.show()
