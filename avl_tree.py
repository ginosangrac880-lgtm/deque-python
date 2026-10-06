class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, y):
        x = y.left
        t2 = x.right

        x.right = y
        y.left = t2

        y.height = 1 + max(
            self.get_height(y.left),
            self.get_height(y.right)
        )

        x.height = 1 + max(
            self.get_height(x.left),
            self.get_height(x.right)
        )

        return x

    def rotate_left(self, x):
        y = x.right
        t2 = y.left

        y.left = x
        x.right = t2

        x.height = 1 + max(
            self.get_height(x.left),
            self.get_height(x.right)
        )

        y.height = 1 + max(
            self.get_height(y.left),
            self.get_height(y.right)
        )

        return y

    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root

        root.height = 1 + max(
            self.get_height(root.left),
            self.get_height(root.right)
        )

        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def search(self, root, key):
        if root is None:
            return False

        if root.key == key:
            return True

        if key < root.key:
            return self.search(root.left, key)

        return self.search(root.right, key)

    def inorder(self, root):
        result = []

        if root is not None:
            result += self.inorder(root.left)
            result.append(root.key)
            result += self.inorder(root.right)

        return result
