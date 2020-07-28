import numpy as np

class NPYHandler():

    def __init__(self, path):
        self.__file_name = path
    
    def __call__(self):
        arr = np.load(self.__file_name)
        return arr
