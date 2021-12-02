import unittest

from solution import get_increased_count


class TestDay1Algorithm(unittest.TestCase):
    def test_algorithm(self):
        inp1 = [1, 1, 1, 1, 1]
        self.assertEqual(0, get_increased_count(inp1))

        inp2 = [1, 1, 1, 1, 1, 3]
        self.assertEqual(1, get_increased_count(inp2))

        inp3 = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        self.assertEqual(7, get_increased_count(inp3))

        inp4 = [5, 4, 3, 2, 1]
        self.assertEqual(0, get_increased_count(inp4))


if __name__ == "__main__":
    unittest.main()
