'''

Given an array containing both negative and positive integers. Find the contiguous sub-array with maximum sum.

'''

import numpy as np

def find_max_sum(array):
    max_so_far = 0
    max_ending_here = 0

    for a in array:
        max_ending_here = max_ending_here + a
        if max_ending_here < 0 : max_ending_here = 0
        if max_so_far < max_ending_here : max_so_far = max_ending_here

    return max_so_far

def test():
    a = np.array([2, 3, -6, 7, -2, -6, 3, -3, 9, 11])    # should return 20
    r = find_max_sum(a)
    assert r == 20

test()