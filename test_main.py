from unittest import TestCase
from main import Solver


class TestTest(TestCase):

    def test_negative_discr(self):
        s = Solver()

        self.assertRaises(Exception, s.demo, 2, 1, 2)


    def test_demo(self):
        self.fail()
