import unittest
from unittest import TestCase
from envtools import *

import numpy as np


class Test(TestCase):
    def test_stat(self):
        # self.fail()
        pass

    def test_s(self):
        # TestCase1
        o = 1
        self.assertEqual(repr(S(o)), 'Type:<class \'int\'>')

        # TestCase2
        o = 'abc'
        self.assertEqual(repr(S(o)), 'Type:<class \'str\'>')

        # TestCase3
        o = np.array([(20,), ['abcd', (-1, False)]])
        self.assertEqual(repr(S(o)), 'Type:<class \'numpy.ndarray\'>')

    def test_tracer(self):
        # self.fail()
        pass

    def test_problem(self):
        # self.fail()
        pass

    def test_refactogenerator(self):
        # self.fail()
        pass

    def test_view(self):
        # self.fail()
        pass


if __name__ == '__main__':
    unittest.main()
