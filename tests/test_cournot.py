import numpy as np

def test_masking_logic():
    x = np.array([1,-2,4,0,-1])
    mask = x > 0
    assert (x * mask == np.array([1,0,4,0,0])).all()