from PIL import Image
from Digit import Digit
import numpy

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def read(imagefile, labelfile, n):
    i = open(imagefile, 'rb')
    l = open(labelfile, 'rb')
    i.read(4)  # magic 1
    i.read(4)  # numImages
    i.read(4)  # numRows
    i.read(4)  # numCols

    l.read(4)  # magic 2
    l.read(4)  # numImages

    images = []

    for k in range(0, n):
        image = Image.new('L', (28, 28))
        image.putdata(i.read(784))

        m = numpy.matrix(list(chunks(list(image.getdata()), 28)))

        d = Digit(image, m, int.from_bytes(l.read(1), byteorder='big'))

        images.append(d)

    return images
