import unittest

from mihto import Mihto


class TestParser(unittest.TestCase):

    def setUp(self):
        self.env = {'a': 0, 'b': 1.23}
        self.mihto = Mihto(self.env)
        self.evaluate = lambda expression: self.mihto.evaluate(expression)

    def test_lt_eq_true(self):
        expression = "1 <= 1"
        self.assertTrue(self.evaluate(expression))

    def test_lt_eq_false(self):
        expression = "1 <= 0"
        self.assertFalse(self.evaluate(expression))

    def test_gt_eq_true(self):
        expression = "1 >= 1"
        self.assertTrue(self.evaluate(expression))

    def test_gt_eq_false(self):
        expression = "0 >= 1"
        self.assertFalse(self.evaluate(expression))

    def test_equals_true(self):
        expression = "1 = 1"
        self.assertTrue(self.evaluate(expression))

    def test_equals_false(self):
        expression = "1 = 0"
        self.assertFalse(self.evaluate(expression))

    def test_not_equals_true(self):
        expression = "1 != 0"
        self.assertTrue(self.evaluate(expression))

    def test_not_equals_false(self):
        expression = "1 != 1"
        self.assertFalse(self.evaluate(expression))

    def test_and_true(self):
        expression = "1 = 1 y 1 = 1"
        self.assertTrue(self.evaluate(expression))

    def test_and_false_all_false(self):
        expression = "1 = 0 y 1 = 0"
        self.assertFalse(self.evaluate(expression))

    def test_and_false_first_false(self):
        expression = "1 = 0 y 1 = 1"
        self.assertFalse(self.evaluate(expression))

    def test_and_false_second_false(self):
        expression = "1 = 1 y 1 = 0"
        self.assertFalse(self.evaluate(expression))

    def test_or_false(self):
        expression = "1 = 0 o 1 = 0"
        self.assertFalse(self.evaluate(expression))

    def test_or_true_all_true(self):
        expression = "1 = 1 o 1 = 1"
        self.assertTrue(self.evaluate(expression))

    def test_or_true_first_true(self):
        expression = "1 = 1 o 1 = 0"
        self.assertTrue(self.evaluate(expression))

    def test_or_true_second_true(self):
        expression = "1 = 0 o 1 = 1"
        self.assertTrue(self.evaluate(expression))

    def test_var_ref_integer(self):
        expression = "a = 0"
        self.assertTrue(self.evaluate(expression))

    def test_var_ref_float(self):
        expression = "b > 1"
        self.assertTrue(self.evaluate(expression))
