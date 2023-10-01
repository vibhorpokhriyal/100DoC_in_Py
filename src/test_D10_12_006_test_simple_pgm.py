import unittest
import D10_12_005_simple_pgm

class TestSimple(unittest.TestCase):
    def test_hello_name(self):
        input_data = "Vibhor"
        result = D10_12_005_simple_pgm.hello_name(input_data)
        self.assertEqual(result, "Hello Vibhor")


if __name__ == "__main__":
    unittest.main()
    