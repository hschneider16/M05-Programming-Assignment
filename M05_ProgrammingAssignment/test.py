import unittest

from my_sum import sum
from fractions import Fraction

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()

# What do the test results mean?:
# In this case, there were two tests ran which failed and output a failure message. 
# Failures = 1 shows that there was one failure in the file
# and it also displays where the failure was, which was at line 21.
# the fractions were added up to 9/10, and did not equal 1, so it failed the test.