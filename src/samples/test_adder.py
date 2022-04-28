import unittest

class SampleCase(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(2 + 2, 4)

if __name__ == '__main__':
    unittest.main()