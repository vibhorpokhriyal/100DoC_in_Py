import D10_12_my_sum

import unittest

from fractions import Fraction

class TestSum(unittest.TestCase):
    def test_sum_int(self):
        test_input_value = [1,2,3]
        result = D10_12_my_sum.sum(test_input_value)
        self.assertEqual(result, 6)

    def test_sum_fraction(self):
        test_input_value = [Fraction(1,4), Fraction(1,4), Fraction(2,5)]
        result = D10_12_my_sum.sum(test_input_value)
        self.assertEqual(result, 1)
    
    def test_bad_type(self):
        test_input_value = "banana"
        with self.assertRaises(TypeError):
            result = D10_12_my_sum.sum(test_input_value)


if __name__ == "__main__":
    unittest.main()