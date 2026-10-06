import unittest

from avl_tree import AVLTree


class TestAVLTree(unittest.TestCase):

    def test_insert(self):
        tree = AVLTree()
        root = None

        root = tree.insert(root, 10)
        root = tree.insert(root, 20)
        root = tree.insert(root, 30)

        self.assertEqual(root.key, 20)

    def test_search(self):
        tree = AVLTree()
        root = None

        root = tree.insert(root, 20)
        root = tree.insert(root, 10)
        root = tree.insert(root, 30)

        self.assertTrue(tree.search(root, 10))
        self.assertTrue(tree.search(root, 30))
        self.assertFalse(tree.search(root, 100))

    def test_inorder(self):
        tree = AVLTree()
        root = None

        root = tree.insert(root, 30)
        root = tree.insert(root, 10)
        root = tree.insert(root, 20)
        root = tree.insert(root, 40)

        self.assertEqual(
            tree.inorder(root),
            [10, 20, 30, 40]
        )

    def test_balance(self):
        tree = AVLTree()
        root = None

        root = tree.insert(root, 30)
        root = tree.insert(root, 20)
        root = tree.insert(root, 10)

        self.assertEqual(root.key, 20)
        self.assertEqual(root.left.key, 10)
        self.assertEqual(root.right.key, 30)


if __name__ == "__main__":
    unittest.main()
