from Neuron import Neuron
import numpy


class Network:
    def __init__(self, n):
        self.neurons = tuple([Neuron(n) for _ in range(10)])

    def __handle_hard(self, _input: numpy.matrix):
        output = [self.neurons[i].transfer_hard(_input) for i in range(10)]
        return output

    def __handle(self, _input: numpy.matrix):
        output = [self.neurons[i].transfer_hard(_input) for i in range(10)]
        return output

    def get_answer(self, _input: numpy.matrix):
        output = self.__handle(_input)

        _max = 0

        for i in range(1, 10):
            if output[i] > output[_max]:
                _max = i

        return _max

    def study(self, _input: numpy.matrix, correct):
        correct_output = [0] * 10
        correct_output[correct] = 1

        output = self.__handle_hard(_input)

        while not Network.__compare_arrays(correct_output, output):
            for i in range(10):
                dif = correct_output[i] - output[i]
                self.neurons[i].change_weights(_input, dif)
            output = self.__handle_hard(_input)

    @staticmethod
    def __compare_arrays(a, b):
        for i in range(10):
            if a[i] != b[i]:
                return False

        return True

