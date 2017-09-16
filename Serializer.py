import yaml
from Network import Network
from Neuron import Neuron


def serialize(network: Network):
    save = []
    for i in network.neurons:
        save.append(i.weights)

    text = yaml.dump(save)

    f = open('network.yaml', 'w')

    f.write(text)

    f.close()


def deserialize(network: Network):
    f = open('network.yaml', 'r')

    text = f.read()

    f.close()

    save = yaml.load(text)

    for i in range(10):
        network.neurons[i].weights = save[i]
