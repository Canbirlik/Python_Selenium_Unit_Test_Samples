import unittest
from mathematics import Mathematics

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.math = Mathematics()

    def test_sum(self):
        result = self.math.sumTwoNumbers(10, 5)
        self.assertEqual(15, result)

    def test_multiply(self):
        result = self.math.multiplyTwoNumbers(10, 5)
        self.assertEqual(50, result)

    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    unittest.main()
