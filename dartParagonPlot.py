import matplotlib.pyplot as plt
import json

paragonLvlsJson = open('dartParagonLvls.json', 'r')
paragonLvls = json.load(paragonLvlsJson)
pierce = paragonLvls['pierce']
damage = paragonLvls['damage']
ceramicDamage = paragonLvls['ceramicDamage']
bossDamage = paragonLvls['bossDamage']
eliteDamage = paragonLvls['eliteDamage']
rate = paragonLvls['rate']
paragonLvlsJson.close()

paragonDegreeJson = open('paragonLevelingData.json', 'r')
paragonDegree = json.load(paragonDegreeJson)
power = paragonDegree['powerDegreeRequirements']
paragonDegreeJson.close()

plt.scatter(range(0, 101), [power[0]] + power)
plt.xticks(range(0, 101, 5))
plt.xlim(left=1)
plt.grid()
plt.xlabel('degree')
plt.ylabel('power')
plt.title('power vs degree')
plt.show()

plt.scatter(range(0, 101), [pierce[0]] + pierce)
plt.xticks(range(0, 101, 5))
plt.xlim(left=1)
plt.grid()
plt.xlabel('degree')
plt.ylabel('pierce')
plt.title('pierce vs degree')
plt.show()

plt.scatter(range(0, 101), [damage[0]] + damage)
plt.xticks(range(0, 101, 5))
plt.xlim(left=1)
plt.grid()
plt.xlabel('degree')
plt.ylabel('damage')
plt.title('damage vs degree')
plt.show()

plt.scatter(range(0, 101), [ceramicDamage[0]] + ceramicDamage)
plt.xticks(range(0, 101, 5))
plt.xlim(left=1)
plt.grid()
plt.xlabel('degree')
plt.ylabel('additional ceramic damage')
plt.title('additional ceramic damage vs degree')
plt.show()

plt.scatter(range(0, 101), [bossDamage[0]] + bossDamage)
plt.xticks(range(0, 101, 5))
plt.xlim(left=1)
plt.grid()
plt.xlabel('degree')
plt.ylabel('additional normal boss damage')
plt.title('additional normal boss damage vs degree')
plt.show()

plt.scatter(range(0, 101), [eliteDamage[0]] + eliteDamage)
plt.xticks(range(0, 101, 5))
plt.xlim(left=1)
plt.grid()
plt.xlabel('degree')
plt.ylabel('additional elite boss damage')
plt.title('additional elite boss damage vs degree')
plt.show()

plt.scatter(range(0, 101), [rate[0]] + rate)
plt.xticks(range(0, 101, 5))
plt.xlim(left=1)
plt.grid()
plt.xlabel('degree')
plt.ylabel('rate')
plt.title('rate vs degree')
plt.show()
