# TEST OF CHARACTER FREQUENCY COUNTER EXCERCISE

import unittest
from excercise_3_sql_handler import get_pizza

# AUTOMATED TEST, DO NOT MODIFIED
class TestStringMethods(unittest.TestCase):
    def test_basic_test_cases(self):
        self.assertEqual(get_pizza(), [(1, 'Margerita', 1050), (2, 'Frutti di Mare', 1350), (3, 'Hawaii', 850)])


if __name__ == '__main__':
    unittest.main()
