import unittest

from main import elem_sum


class MyTestCase(unittest.TestCase):
    def test_elem_sum(self):
        a, b = 2, 3
        output = elem_sum(a, b)
        self.assertEqual(output, 1)

    def test(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
