import matplotlib.pyplot as plt
import json

paragonDegreeJson = open('paragonLevelingData.json', 'r')
paragonDegree = json.load(paragonDegreeJson)
power = paragonDegree['powerDegreeRequirements']
paragonDegreeJson.close()

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

plot('power', power)
