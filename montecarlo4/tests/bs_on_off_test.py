"""Tests the on and off  as well as int methods for bitsting class"""
import montecarlo4
from montecarlo4 import BitString
import pytest

def bs_on_off_test():
    """
    A function to test on / off and int methods for bitstring class
    """

    my_bs = BitString(13)
    my_bs.set_config([0,1,1,0,0,1,0,0,1,0,1,0,0])
    assert(my_bs.on() == 5)
    assert(my_bs.off() == 8)
    assert(my_bs.int() == 3220)
    