import unittest
import math
from io import StringIO
import sys
import random
import numpy as np


# Unit testing 
class TestSaturn(unittest.TestCase):
    
    def setUp(self): # the values and function used
        self.r = 58232*pow(10, 3)
        self.M = 5.683*pow(10, 26)
        self.g_s = 10.44
        self.G = 6.674*pow(10, -11)
        self.rho = 1000
        self.r_d = 500 * pow(10, -9)
        self.V = 4/3 * math.pi * pow(self.r_d, 3)
        self.m_p = 513
        self.x = [random.uniform(-100, 100) for n in range(50)]
        self.y = [random.uniform(-100, 100) for n in range(50)]
        self.T = math.sqrt(4 * pow(math.pi, 2) / (self.G * self.M) * pow(self.r, 3))
        self.Omega = 2 * math.pi / self.T
        self.v_x = -2 / 3 * self.Omega * np.array(self.y)
        self.F_g = self.G * self.M * self.m_p / pow(self.r, 2)
        self.g_g = self.F_g / self.m_p
        self.KE = 0.5 * self.m_p * np.power(self.v_x, 2)
    
    def test_F_g_positive(self): # testing if F_g is positive
        result = self.F_g
        self.assertGreater(result, 0)
        
    def test_g_g_positive(self): # testing if g_g is positive
        result = self.g_g
        self.assertGreater(result, 0)
    
    def test_V_positive(self): # testing if V is positive
        result = self.V
        self.assertGreater(result, 0)

    def test_v_x_positive(self): # testing if all values for v_x are positive
        for x in self.v_x:
            self.assertGreaterEqual(x, 0)


if __name__ == '__main__':
    unittest.main()
