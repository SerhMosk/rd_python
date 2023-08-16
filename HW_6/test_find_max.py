import unittest

from task_3_find_max import get_max


class TestFindMax(unittest.TestCase):
    def test_find_max(self):
        self.assertEqual(get_max([-1, 5, 100, 0, -10]), 100)
        self.assertEqual(get_max([-1, -5, -100, 0, -10]), 0)


if __name__ == '__main__':
    unittest.main()
