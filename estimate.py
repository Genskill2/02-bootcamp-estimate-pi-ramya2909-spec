import math
import numpy as np
import random
import unittest

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
def w_n(n):
    pi_value = 1    
    for i in range(1,n):
        pi_value *= ((4*pow(i, 2))/((4*pow(i, 2))-1))
    return(value*2)

def monte_carlo(N):
    n=0
    xpoints=np.random.random(N)
    ypoints=np.random.random(N)
    for i in range(N):
        if(xpoints[i]**2+ypoints[i]**2)<=1:
            n=n+1
    pi=4.0*(n/N)
    return(pi)
        
    
if _name_ == "_main_":
    unittest.main()
