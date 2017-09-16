from tkinter import *

from PIL import Image, ImageTk

import reader

from Digit import Digit

from Network import Network

import Serializer


class DigitClassifier:

    def __init__(self):
        self.c = 0

        self.train_images = None

        self.test_images = None

        self.network = None

        self.root = None

        self.img_label = None
        self.cor_label = None
        self.ans_label = None

        self.img = None

    @staticmethod
    def study(_network: Network, _train_images, n):

        for i in range(n):
            _network.study(_train_images[i].matrix, _train_images[i].digit)

            if i % 100 == 0:
                print('{0:.1f}%'.format(i / (n / 100)))

    def show(self):

        self.img = ImageTk.PhotoImage(self.test_images[self.c].image.resize((112, 112)))

        self.img_label['image'] = self.img

        self.cor_label['text'] = str(self.test_images[self.c].digit)

        self.ans_label['text'] = str(self.network.get_answer(self.test_images[self.c].matrix))

    @staticmethod
    def check(_network: Network, _train_images, n):
        y = 0
        for i in range(n):
            if _network.get_answer(_train_images[i].matrix) == _train_images[i].digit:
                y += 1

            if i % 100 == 0:
                print('{0:.1f}%'.format(i / (n / 100)))

        return y / n

    def main(self):
        test = True

        root = Tk()

        self.train_images = reader.read('Files/train-images.idx3-ubyte', 'Files/train-labels.idx1-ubyte', 60000)

        self.test_images = reader.read('Files/t10k-images.idx3-ubyte', 'Files/t10k-labels.idx1-ubyte', 10000)

        self.img = ImageTk.PhotoImage(self.test_images[self.c].image.resize((112, 112)))

        self.img_label = Label(root, image=self.img)

        self.cor_label = Label(root, text=str(self.test_images[self.c].digit), font=("Courier", 72))

        self.network = Network(28)

        # study(network, train_images, 60000)

        Serializer.deserialize(self.network)

        if test:
            print('Checking...')

            result = DigitClassifier.check(self.network, self.test_images, 10000)

            print('Checking done, result is {0:.2f}%'.format(result * 100))

        self.ans_label = Label(root, text=str(
            self.network.get_answer(self.test_images[self.c].matrix)
            ), font=("Courier", 72))

        def left(event=None):
            if self.c > 0:
                self.c -= 1
                self.show()

        def right(event=None):
            if self.c < 9999:
                self.c += 1
                self.show()

        button_left = Button(root, command=left, text='<', font=("Courier", 72))
        button_right = Button(root, command=right, text='>', font=("Courier", 72))

        self.img_label.grid(row=0, column=2)
        self.cor_label.grid(row=0, column=1)
        self.ans_label.grid(row=0, column=3)
        button_left.grid(row=0, column=0)
        button_right.grid(row=0, column=4)

        root.mainloop()

if __name__ == '__main__':
    d = DigitClassifier()
    d.main()
