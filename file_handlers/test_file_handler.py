import pytest 
from .common_handler import NPYHandler
import numpy as np

class Image:
    def __init__(self, imageArr):
        self.data = imageArr

image =  np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

def test_handler():
    np.save('./test.npy',image) 

    testFits = NPYHandler('./test.npy')
    array = testFits()

    assert np.array_equal(image, array)
