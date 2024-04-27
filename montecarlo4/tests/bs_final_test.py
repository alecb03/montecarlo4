"""
A test for set_config and set_int_config
"""

import montecarlo4
from montecarlo4 import BitString
import pytest

def final_bs_test():
    """
    a function that tests set_config and set_int_config to make sure they are equivalent
    """
    my_bs1 = BitString(13)
    my_bs1.set_config([0,1,1,0,0,1,0,1,1,0,1,0,0])

    my_bs2 = BitString(13)
    my_bs2.set_int_config(3252)


    assert(my_bs1 == my_bs2)

    my_bs2.flip_site(5)
    assert(my_bs1 != my_bs2)