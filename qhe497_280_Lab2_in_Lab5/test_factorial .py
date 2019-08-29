import unittest     # Import the Python unit testing framework
import maths        # Our code to test


class MathsTest(unittest.TestCase):
    
    def test_factorial(self):
        self.assertEqual(maths.factorial(2), 2, "The answer is wrong!")
        self.assertEqual(maths.factorial(1), 1, "The answer is wrong!")





# This allows running the unit tests from the command line (python test_maths.py)



if __name__ == '__main__':
    unittest.main()
