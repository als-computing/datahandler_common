import pytest 
from .. import common_handler
import numpy as np

class Image:
    def __init__(self, imageArr):
        self.data = imageArr

image =  np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

def test_handler():
    np.save('./data.npy',image) 

    testFits = common_handler.NPYHandler('./data.npy')
    array = testFits()

    assert np.array_equal(image, array)
