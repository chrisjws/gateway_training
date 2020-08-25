import unittest
from ..unit_tests_example_page import add_stuff, get_permutations


class WorkflowUnitTests(unittest.TestCase):

    def test_add_stuff(self):
        self.assertEqual(add_stuff(1, 2), 3)
        self.assertEqual(add_stuff(2, 2), 4)
        self.assertEqual(add_stuff(-7, 2), -5)

    def test_get_permutations(self):
        # for exact
        expected = [(1, 2), (2, 1)]
        self.assertEqual(get_permutations(1, 2), expected)

        # for approximately the same, note the different test
        expected = [(1, 2, 3), (1, 3, 2), (2, 3, 1), (2, 1, 3), (3, 1, 2), (3, 2, 1)]
        self.assertCountEqual(get_permutations(1, 2, 3), expected)
        try:
            self.assertEqual(get_permutations(1, 2, 3), expected)
        except Exception as e:
            print("Expected failure is expected")


if __name__ == '__main__':
    unittest.main()
