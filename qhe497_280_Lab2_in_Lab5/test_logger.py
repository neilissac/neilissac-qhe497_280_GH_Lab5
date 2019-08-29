import unittest     
import logger       
from unittest.mock import patch
from unittest import main


class LoggerTest(unittest.TestCase):
    
    def test_info(self):
        Test_correct = logger.Logger()
        
        with patch('builtins.print') as mocked_print:
            Test_correct.info("test")
            mocked_print.assert_called_with("[INFO] test")
        
    
    def test_error(self):
        Test_correct = logger.Logger()
        
        with patch('builtins.print') as mocked_print:
            Test_correct.error("second test")
            mocked_print.assert_called_with("[WARNING] second test")