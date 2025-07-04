import unittest
from app import add

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), -1)
        self.assertEqual(add(-1, 1), -2)
        self.assertEqual(add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
