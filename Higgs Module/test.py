import numpy as np
import pytest
from navigation import HyperdimensionalNavigator

def test_quaternion_trajectory():
    navigator = HyperdimensionalNavigator()
    coords = np.array([[0,0,0,0], [1,0,0,0], [1,1,0,0]])
    prob = navigator.quaternion_trajectory(coords)
    assert isinstance(prob, complex)
    assert abs(prob) > 0
