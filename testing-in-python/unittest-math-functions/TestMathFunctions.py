import unittest
import MathFunctions

class KnownValues(unittest.TestCase):
    def test_areaCircle_for_10radius(self):
        #Capture the result of the function:
        result = MathFunctions.areaCircle(10)

        #Check for expected output:
        expected = 314.1592653589793
        self.assertEqual(expected, result)

    def test_areaCircle_for_2radius(self):
        result = MathFunctions.areaCircle(2)
        expected = 12.566370614359172
        self.assertEqual(expected, result)

    def test_areaCircle_for_500radius(self):
        result = MathFunctions.areaCircle(500)
        expected = 785398.1633974483
        self.assertEqual(expected, result)

# Run the tests
if __name__ == '__main__':
    unittest.main()

# $ python TestMathFunctions.py
# ...
# ----------------------------------------------------------------------
# Ran 3 tests in 0.000s
#
# OK
