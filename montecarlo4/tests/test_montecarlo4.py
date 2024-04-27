"""
Unit and regression test for the montecarlo4 package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import montecarlo4


def test_montecarlo4_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "montecarlo4" in sys.modules
