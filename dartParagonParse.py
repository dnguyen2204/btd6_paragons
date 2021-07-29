import json

paragonLvls = {
    'pierce': [200],
    'damage': [20],
    'ceramicDamage': [30],
    'bossDamage': [80],
    'eliteDamage': [20],
    'rate': [0.3]
}

for i in range(1, 100):
    file = open('dartParagon/DartParagon' + str(i + 1) + '.json', 'r')
    data = json.load(file)

    weapon = None
    for behavior in data['behaviors']:
        if behavior['$type'] == 'Assets.Scripts.Models.Towers.Behaviors.Attack.AttackModel, Assembly-CSharp':
            weapon = behavior['weapons'][0]

    projectile = weapon['projectile']

    paragonLvls['rate'].append(weapon['Rate'])
    paragonLvls['pierce'].append(projectile['pierce'])

    for behavior in projectile['behaviors']:
        if behavior['$type'] == 'Assets.Scripts.Models.Towers.Projectiles.Behaviors.DamageModel, Assembly-CSharp':
            paragonLvls['damage'].append(behavior['damage'])
        elif behavior['$type'] == 'Assets.Scripts.Models.Towers.Projectiles.Behaviors.DamageModifierForTagModel, Assembly-CSharp':
            if behavior['tag'] == 'Ceramic':
                paragonLvls['ceramicDamage'].append(behavior['damageAddative'])
            elif behavior['tag'] == 'Boss':
                paragonLvls['bossDamage'].append(behavior['damageAddative'])
            elif behavior['tag'] == 'Elite':
                paragonLvls['eliteDamage'].append(behavior['damageAddative'])

    file.close()

paragonLvlsJson = open('dartParagonLvls.json', 'w')
json.dump(paragonLvls, paragonLvlsJson, indent=4)
paragonLvlsJson.close()
