import unittest

from dynamic_array import DynamicArray


class TestDynamicArray(unittest.TestCase):

    def test_append(self):
        arr = DynamicArray()

        arr.append(10)
        arr.append(20)

        self.assertEqual(arr.get(0), 10)
        self.assertEqual(arr.get(1), 20)

    def test_set(self):
        arr = DynamicArray()

        arr.append(10)
        arr.set(0, 100)

        self.assertEqual(arr.get(0), 100)

    def test_remove(self):
        arr = DynamicArray()

        arr.append(10)
        arr.append(20)
        arr.append(30)

        arr.remove(1)

        self.assertEqual(arr.get(0), 10)
        self.assertEqual(arr.get(1), 30)
        self.assertEqual(len(arr), 2)

    def test_resize(self):
        arr = DynamicArray(2)

        arr.append(1)
        arr.append(2)
        arr.append(3)

        self.assertEqual(arr.get(2), 3)
        self.assertEqual(arr.capacity, 4)

    def test_wrong_index(self):
        arr = DynamicArray()

        arr.append(10)

        with self.assertRaises(IndexError):
            arr.get(10)


if __name__ == "__main__":
    unittest.main()
