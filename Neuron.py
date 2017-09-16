import numpy


class Neuron:
    def __init__(self, n):
        self.n = n
        self.weights = numpy.random.random_integers(0, 10, (n, n))
        self.minimum = 50

    def transfer_hard(self, _input: numpy.matrix):
        power = 0
        for i in range(self.n):
            for j in range(self.n):
                power += self.weights[i, j] * _input[i, j]

        return 1 if power >= self.minimum else 0

    def transfer(self, _input: numpy.matrix):
        power = 0
        for i in range(self.n):
            for j in range(self.n):
                power += self.weights[i, j] * _input[i, j]

        return power

    def change_weights(self, _input: numpy.matrix, d):
        for i in range(self.n):
            for j in range(self.n):
                self.weights[i, j] += d * _input[i, j]
