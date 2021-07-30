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

def plot(name, data):
    plt.scatter(range(0, 101), [data[0]] + data)
    plt.xticks(range(0, 101, 5))
    plt.xlim(left=1)
    plt.grid()
    plt.xlabel('degree')
    plt.ylabel(name)
    plt.title(name + ' vs degree')
    plt.get_current_fig_manager().window.state('zoomed')
    plt.show()

plot('pierce', pierce)
plot('damage', damage)
plot('additional ceramic damage', ceramicDamage)
plot('additional boss damage', bossDamage)
plot('additional elite damage', eliteDamage)
plot('rate', rate)
