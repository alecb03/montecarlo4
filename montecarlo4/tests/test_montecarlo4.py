"""
Unit and regression test for the montecarlo4 package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import montecarlo4
from montecarlo4 import *
import pytest
import networkx as nx


def test_montecarlo4_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "montecarlo4" in sys.modules



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



def test_bs_int_config():
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



def test_bs_on_off():
    """
    A function to test on / off and int methods for bitstring class
    """

    my_bs = BitString(13)
    my_bs.set_config([0,1,1,0,0,1,0,0,1,0,1,0,0])
    assert(my_bs.on() == 5)
    assert(my_bs.off() == 8)
    assert(my_bs.int() == 3220)



def test_final_bs():
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



def get_IsingHamiltonian(G, mus=None):
    if mus == None:
        mus = np.zeros(len(G.nodes()))

    if len(G.nodes()) != len(mus):
        error("DimensionMismatch")

    if len(G.nodes()) != len(mus):
        error(" Dimension Mismatch")
    J = [[] for i in G.nodes()]
    for e in G.edges:
        J[e[0]].append((e[1], G.edges[e]['weight']))
        J[e[1]].append((e[0], G.edges[e]['weight']))
    return montecarlo4.IsingHamiltonian(J,mus)

def test_ising():
    N = 6
    Jval = 2.0
    G = nx.Graph()
    G.add_nodes_from([i for i in range(N)])
    G.add_edges_from([(i,(i+1)% G.number_of_nodes() ) for i in range(N)])
    for e in G.edges:
        G.edges[e]['weight'] = Jval

    
    conf = montecarlo4.BitString(N)
    ham = get_IsingHamiltonian(G)

    # Compute the average values for Temperature = 1
    E, M, HC, MS = ham.compute_average_values(1)

    assert(np.isclose(E,  -11.95991923))
    assert(np.isclose(M,   -0.00000000))
    assert(np.isclose(HC,   0.31925472))
    assert(np.isclose(MS,   0.01202961))

            