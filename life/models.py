#stores life models used in analysis
#each model describes properties of the Life object.

#local


#util
import numpy as np
import scipy as sp
from PIL import Image

class Life(object):
    #methods
    def __init__(self):
        self.array = np.zeros(0)

    def generate_random_array(self, shape, density):
        self.array = np.random.random(shape)
        N = self.array<density
        self.array = np.zeros(self.array.shape, int)
        self.array[N] = 1

    def read_image_to_binary(self, threshold, image_name):
        image = sp.misc.imread(image_name)
        self.array = image

    def update(self, number_of_steps):
        pass
