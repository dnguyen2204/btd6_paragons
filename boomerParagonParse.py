import json

paragonLvls = {
    'main': {
        'pierce': [100.0],
        'damage': [20.0],
        'bossDamage': [60.0],
        'eliteDamage': [20.0],
        'rate': [0.04]
    },
    'orbit': {
        'pierce': [1000.0],
        'damage': [20.0],
        'ceramicDamage': [20.0],
        'moabDamage': [20.0],
        'fortifiedDamage': [2.0],
        'bossDamage': [160.0],
        'eliteDamage': [40.0],
        'rate': [0.1]
    },
    'press': {
        'pierce': [300.0],
        'damage': [1.0],
        'moabDamage': [19.0],
        'bossDamage': [0],
        'eliteDamage': [20.0],        
        'rate': [2.5]
    },
    'pressExplosion': {
        'pierce': [20.0],
        'damage': [100.0],
        'bossDamage': [0],
        'eliteDamage': [100]
    }
}

for i in range(1, 100):
    file = open('boomerParagon/BoomerParagon' + str(i + 1) + '.json', 'r')
    data = json.load(file)

    weapons = []
    for behavior in data['behaviors']:
        if behavior['$type'] == 'Assets.Scripts.Models.Towers.Behaviors.Attack.AttackModel, Assembly-CSharp':
            weapons.append(behavior['weapons'][0])

    projectiles = []
    for weapon in weapons:
        projectiles.append(weapon['projectile'])

    paragonLvls['main']['rate'].append(weapons[0]['Rate'])
    paragonLvls['orbit']['rate'].append(weapons[1]['Rate'])
    paragonLvls['press']['rate'].append(weapons[2]['Rate'])

    paragonLvls['main']['pierce'].append(projectiles[0]['pierce'])
    paragonLvls['orbit']['pierce'].append(projectiles[1]['pierce'])
    paragonLvls['press']['pierce'].append(projectiles[2]['pierce'])
    
    for behavior in projectiles[0]['behaviors']:
        if behavior['$type'] == 'Assets.Scripts.Models.Towers.Projectiles.Behaviors.DamageModel, Assembly-CSharp':
            paragonLvls['main']['damage'].append(behavior['damage'])
        elif behavior['$type'] == 'Assets.Scripts.Models.Towers.Projectiles.Behaviors.DamageModifierForTagModel, Assembly-CSharp':
            if behavior['tag'] == 'Boss':
                paragonLvls['main']['bossDamage'].append(behavior['damageAddative'])
            elif behavior['tag'] == 'Elite':
                 paragonLvls['main']['eliteDamage'].append(behavior['damageAddative'])

    for behavior in projectiles[1]['behaviors']:
        if behavior['$type'] == 'Assets.Scripts.Models.Towers.Projectiles.Behaviors.DamageModel, Assembly-CSharp':
            paragonLvls['orbit']['damage'].append(behavior['damage'])
        elif behavior['$type'] == 'Assets.Scripts.Models.Towers.Projectiles.Behaviors.DamageModifierForTagModel, Assembly-CSharp':
            if behavior['tag'] == 'Ceramic':
                paragonLvls['orbit']['ceramicDamage'].append(behavior['damageAddative'])
            elif behavior['tag'] == 'Moabs':
                 paragonLvls['orbit']['moabDamage'].append(behavior['damageAddative'])
            elif behavior['tag'] == 'Fortified':
                paragonLvls['orbit']['fortifiedDamage'].append(behavior['damageAddative'])
            elif behavior['tag'] == 'Boss':
                paragonLvls['orbit']['bossDamage'].append(behavior['damageAddative'])
            elif behavior['tag'] == 'Elite':
                 paragonLvls['orbit']['eliteDamage'].append(behavior['damageAddative'])

    pressBoss = False
    pressExplosionBoss = False

    for behavior in projectiles[2]['behaviors']:
        if behavior['$type'] == 'Assets.Scripts.Models.Towers.Projectiles.Behaviors.DamageModel, Assembly-CSharp':
            paragonLvls['press']['damage'].append(behavior['damage'])
        elif behavior['$type'] == 'Assets.Scripts.Models.Towers.Projectiles.Behaviors.DamageModifierForTagModel, Assembly-CSharp':
            if behavior['tag'] == 'Moabs':
                 paragonLvls['press']['moabDamage'].append(behavior['damageAddative'])
            elif behavior['tag'] == 'Boss':
                paragonLvls['press']['bossDamage'].append(behavior['damageAddative'])
                pressBoss = True
            elif behavior['tag'] == 'Elite':
                 paragonLvls['press']['eliteDamage'].append(behavior['damageAddative'])
        elif behavior['$type'] == 'Assets.Scripts.Models.Towers.Projectiles.Behaviors.CreateProjectileOnExhaustFractionModel, Assembly-CSharp':
            paragonLvls['pressExplosion']['pierce'].append(behavior['projectile']['pierce'])
            for behavior2 in behavior['projectile']['behaviors']:
                if behavior2['$type'] == 'Assets.Scripts.Models.Towers.Projectiles.Behaviors.DamageModel, Assembly-CSharp':
                    paragonLvls['pressExplosion']['damage'].append(behavior2['damage'])
                elif behavior2['$type'] == 'Assets.Scripts.Models.Towers.Projectiles.Behaviors.DamageModifierForTagModel, Assembly-CSharp':
                    if behavior2['tag'] == 'Boss':
                        paragonLvls['pressExplosion']['bossDamage'].append(behavior2['damageAddative'])
                        pressExplosionBoss = True
                    elif behavior2['tag'] == 'Elite':
                        paragonLvls['pressExplosion']['eliteDamage'].append(behavior2['damageAddative'])

    if not pressBoss:
        paragonLvls['pressExplosion']['bossDamage'].append(0)

    if not pressExplosionBoss:
        paragonLvls['press']['bossDamage'].append(0)

    file.close()

paragonLvlsJson = open('boomerParagonLvls.json', 'w')
json.dump(paragonLvls, paragonLvlsJson, indent=4)
paragonLvlsJson.close()
