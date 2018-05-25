import unittest #This module is in the standard library so no need to install anything.
import calculator #Now we also need to import the module that we want to test.

class TestCalculator(unittest.TestCase): #TestCalculator class inherits from unittest.TestCase which gives access to a lot of different testing capabilities within that class.
    def test_add(self):
        result = calculator.add(10, 5)
        self.assertEqual(result, 15)

        self.assertEqual(calculator.add(51, 49), 100)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-1, -1), -2)

    def test_subtract(self):
        result = calculator.subtract(10, 5)
        self.assertEqual(result, 5)

        self.assertEqual(calculator.subtract(-1, 1), -2)
        self.assertEqual(calculator.subtract(-1, -1), 0)


    def test_multiply(self):
        result = calculator.multiply(10, 5)
        self.assertEqual(result, 50)

        self.assertEqual(calculator.multiply(-1, 1), -1)
        self.assertEqual(calculator.multiply(-1, -1), 1)

    def test_divide(self):
        result = calculator.divide(10, 5)
        self.assertEqual(result, 2)

        self.assertEqual(calculator.divide(-1, 1), -1)
        self.assertEqual(calculator.divide(-1, -1), 1)

        self.assertRaises(ValueError, calculator.divide, 10, 0) #first way to test for raising errorss.
        #self.assertRaises(Exception that we expect, the function we want to run don't pass arguments to the fucntion, arguement1 pass to the function, arguement2 pass to the function)
        #The reason we don't pass the arguments directly to the funciton is because
        #our function will actuall throw that value error and out test will think that somthing failed.
        #But we will look at a way we pass in arguments directly like we normally do in the second way to test for errors.

        with self.assertRaises(ValueError): #second way to test for raising errors
            calculator.divide(10, 0)
        #This way is testing the exceptions using a context manager, this will allow us to handle and check the exception
        #properly and also call the funciton normally as in pass the arguments directly to the function.

# $ python -m unittest test_calculator
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
# OK

#It will be nice if we can run the test like $ pyton test_calculator.py rather then the above way.
# To do this we need to add in:
if __name__ == '__main__':
    unittest.main()

#If you don't understand what it's doing, well its actually not related to unit testing at all.
#There is a seperate video you can watch whihc speicically explains what its all abouot. https://www.youtube.com/watch?v=sugvnHA7ElY
#Basically its saying if we run this module direclty then run the code within the conditional and that code within
#our conditional is unittest.main() and unittest.main() will run all of our tests. So now we can run the test in the
#terminal like so:

# $ python test_calculator.py
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
# OK
