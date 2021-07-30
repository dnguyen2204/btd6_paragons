import matplotlib.pyplot as plt
import json

paragonLvlsJson = open('boomerParagonLvls.json', 'r')
paragonLvls = json.load(paragonLvlsJson)

mainPierce =                paragonLvls['main']['pierce']
mainDamage =                paragonLvls['main']['damage']
mainBossDamage =            paragonLvls['main']['bossDamage']
mainEliteDamage =           paragonLvls['main']['eliteDamage']
mainRate =                  paragonLvls['main']['rate']
orbitPierce =               paragonLvls['orbit']['pierce']
orbitDamage =               paragonLvls['orbit']['damage']
orbitCeramicDamage =        paragonLvls['orbit']['ceramicDamage']
orbitMoabDamage =           paragonLvls['orbit']['moabDamage']
orbitFortifiedDamage =      paragonLvls['orbit']['fortifiedDamage']
orbitBossDamage =           paragonLvls['orbit']['bossDamage']
orbitEliteDamage =          paragonLvls['orbit']['eliteDamage']
orbitRate =                 paragonLvls['orbit']['rate']
pressPierce =               paragonLvls['press']['pierce']
pressDamage =               paragonLvls['press']['damage']
pressMoabDamage =           paragonLvls['press']['moabDamage']
pressBossDamage =           paragonLvls['press']['bossDamage']
pressEliteDamage =          paragonLvls['press']['eliteDamage']
pressRate =                 paragonLvls['press']['rate']
pressExplosionPierce =      paragonLvls['main']['pierce']
pressExplosionDamage =      paragonLvls['main']['damage']
pressExplosionBossDamage =  paragonLvls['main']['bossDamage']
pressExplosionEliteDamage = paragonLvls['main']['eliteDamage']

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

plot('main pierce', mainPierce)
plot('main damage', mainDamage)
plot('main additional normal boss damage', mainBossDamage)
plot('main additional elite boss damage', mainEliteDamage)
plot('main rate', mainRate)
plot('orbitals pierce', orbitPierce)
plot('orbitals damage', orbitDamage)
plot('orbitals additional ceramic damage', orbitCeramicDamage)
plot('orbitals additional moab damage', orbitMoabDamage)
plot('orbitals additional fortified damage', orbitFortifiedDamage)
plot('orbitals additional normal boss damage', orbitBossDamage)
plot('orbitals additional elite boss damage', orbitEliteDamage)
plot('orbitals rate', orbitRate)
plot('press pierce', pressPierce)
plot('press damage', pressDamage)
plot('press additional moab damage', pressMoabDamage)
plot('press additional normal boss damage', pressBossDamage)
plot('press additional elite boss damage', pressEliteDamage)
plot('press rate', pressRate)
plot('press explosion pierce', pressExplosionPierce)
plot('press explosion damage', pressExplosionDamage)
plot('press explosion additionalnormal boss damage', pressExplosionBossDamage)
plot('press explosion additional elite boss damage', pressExplosionEliteDamage)
