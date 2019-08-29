import unittest     # Import the Python unit testing framework
import maths        # Our code to test


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add(self):
        ''' Tests the add function. '''
        self.assertEqual(maths.add(1,3), 4, "The answer is wrong!")
    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''
        self.assertEqual(maths.fibonacci(5), 5, "The answer is wrong!")
    def test_convert_base(self):
        self.assertEqual(maths.convert_base(10, 16),'A', "The answer is wrong!")
    def test_convert_nbase(self):
        self.assertEqual(maths.convert_base(10, 2),'1010', "The answer is wrong!")        
    def test_new_add(self):
        self.assertEqual(maths.add(5, 3, 2),1000,"The answer is wrong!")
        self.assertEqual(maths.add(5, 3, 10),8,"The answer is wrong!")


# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
