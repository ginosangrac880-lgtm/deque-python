import unittest

from sorting import bubble_sort, quick_sort


class TestSorting(unittest.TestCase):

    def test_bubble_sort(self):
        arr = [5, 2, 8, 1, 3]

        result = bubble_sort(arr)

        self.assertEqual(result, [1, 2, 3, 5, 8])

    def test_quick_sort(self):
        arr = [5, 2, 8, 1, 3]

        result = quick_sort(arr)

        self.assertEqual(result, [1, 2, 3, 5, 8])

    def test_empty_list(self):
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(quick_sort([]), [])

    def test_single_element(self):
        self.assertEqual(bubble_sort([10]), [10])
        self.assertEqual(quick_sort([10]), [10])

    def test_duplicates(self):
        arr = [3, 1, 3, 2, 1]

        self.assertEqual(
            bubble_sort(arr.copy()),
            [1, 1, 2, 3, 3]
        )

        self.assertEqual(
            quick_sort(arr),
            [1, 1, 2, 3, 3]
        )


if __name__ == "__main__":
    unittest.main()
