"""
Tests set_int_config method of bitstring class
"""

import montecarlo4
from montecarlo4 import BitString
import pytest
import numpy as np

def bs_int_config_test():
    """
    A fuction that tests set_int_config method of bitstring class
    """
    my_bs = BitString(20)
    my_bs.set_int_config(3221)
    # Let's make sure this worked:
    tmp = np.array([0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0,1,0,1])
    assert((my_bs.config == tmp).all())

    # We can provide an even stronger test here:
    for i in range(1000):
        my_bs.set_int_config(i) # Converts from integer to binary
        assert(my_bs.int() == i) # Converts back from binary to integer and tests