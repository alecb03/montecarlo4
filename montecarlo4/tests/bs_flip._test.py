"""
Tests the flip_site bitstring method
"""

import montecarlo4
from montecarlo4 import BitString
import pytest

def test_bs_flip():
    """
    A function that tests if fliping bitstring is working correctly 
    """
    my_bs = BitString(8)
    my_bs.flip_site(2)
    my_bs.flip_site(2)

    my_bs.flip_site(2)
    my_bs.flip_site(7)
    my_bs.flip_site(0)

    assert(len(my_bs) == 8)