class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def create(self, root, x):
        if root is None:
            return Node(x)
        elif x < root.data:
            root.left = self.create(root.left, x)
        else:
            root.right = self.create(root.right, x)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    def search(self, root, x):
        if root is None or root.data == x:
            return root
        if x < root.data:
            return self.search(root.left, x)
        return self.search(root.right, x)

    def height(self, root):
        if root is None:
            return -1
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return max(left_height, right_height) + 1

    def depth(self, root, x, current_depth=0):
        if root is None:
            return -1
        if root.data == x:
            return current_depth
        if x < root.data:
            return self.depth(root.left, x, current_depth + 1)
        return self.depth(root.right, x, current_depth + 1)

    def sum_all(self, root):
        if root is None:
            return 0
        return root.data + self.sum_all(root.left) + self.sum_all(root.right)

    def sum_even(self, root):
        if root is None:
            return 0
        sum_left = self.sum_even(root.left)
        sum_right = self.sum_even(root.right)
        return (root.data if root.data % 2 == 0 else 0) + sum_left + sum_right

    def sum_odd(self, root):
        if root is None:
            return 0
        sum_left = self.sum_odd(root.left)
        sum_right = self.sum_odd(root.right)
        return (root.data if root.data % 2 != 0 else 0) + sum_left + sum_right

# Example usage:
t1 = Tree()
t1.root = t1.create(t1.root, 10)
t1.root = t1.create(t1.root, 5)
t1.root = t1.create(t1.root, 20)
t1.root = t1.create(t1.root, 7)

print("Inorder traversal:")
t1.inorder(t1.root)
print("\nPreorder traversal:")
t1.preorder(t1.root)
print("\nPostorder traversal:")
t1.postorder(t1.root)


print("\nSearching for 7 in the tree:", t1.search(t1.root, 7) is not None)


print("Height of the tree:", t1.height(t1.root))


print("Depth of node with value 7:", t1.depth(t1.root, 7))


print("Sum of all nodes:", t1.sum_all(t1.root))


print("Sum of even nodes:", t1.sum_even(t1.root))


print("Sum of odd nodes:", t1.sum_odd(t1.root))
