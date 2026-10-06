import unittest

from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_append(self):
        linked_list = LinkedList()

        linked_list.append(10)
        linked_list.append(20)

        self.assertEqual(linked_list.get(0), 10)
        self.assertEqual(linked_list.get(1), 20)

    def test_prepend(self):
        linked_list = LinkedList()

        linked_list.append(20)
        linked_list.prepend(10)

        self.assertEqual(linked_list.get(0), 10)
        self.assertEqual(linked_list.get(1), 20)

    def test_remove(self):
        linked_list = LinkedList()

        linked_list.append(10)
        linked_list.append(20)
        linked_list.append(30)

        linked_list.remove(1)

        self.assertEqual(linked_list.get(0), 10)
        self.assertEqual(linked_list.get(1), 30)
        self.assertEqual(len(linked_list), 2)

    def test_wrong_index(self):
        linked_list = LinkedList()

        linked_list.append(10)

        with self.assertRaises(IndexError):
            linked_list.get(5)


if __name__ == "__main__":
    unittest.main()
