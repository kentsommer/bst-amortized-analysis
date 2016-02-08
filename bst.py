import random
from tabulate import tabulate


class Node:
    # Parent pointer used for easier in-order traversal function
    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent


class BST:
    def __init__(self):
        self.root = None

    # Standard BST insert implementation
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        current = self.root
        while current:
            if value == current.value:
                return
            elif value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(value, current)
                    return
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(value, current)
                    return

    # Select random number N between 50:100 for use as tree size.
    # Sample N unique random numbers between 0:10,000
    # For each i'th unique number insert value into tree.
    def gen_random_tree(self):
        num_nodes = random.randint(50, 100)
        unique_list = random.sample(range(0,10000), num_nodes)
        for i in range(0, num_nodes):
            self.insert(unique_list[i])


# If current node has left child
# Set current to left child
# Continue until no more left children
def findmostleft(node, stepcount=0):
    stepcount = stepcount
    current = node
    while True:
        if current.left != None:
            current = current.left
            stepcount += 1
            continue
        break
    return current, stepcount


# If the current node has a right child, return leftmost child of right child.
# Else, continue going up parent pointers until parent.left equals current
# Return parent
def findnext(node):
    stepcount = 0
    if node.right != None:
        return findmostleft(node.right, 1)
    else:
        parent = node.parent
        stepcount += 1
        while parent != None:
            if parent.left == node:
                break
            node = parent
            parent = node.parent
            stepcount += 1
        return parent, stepcount


# Get first node by calling findmostleft on root
# Loop N-1 times (where N is the size of the tree) and make N-1 calls to findnext
def inorder(node):
    stepcount = 0
    first = findmostleft(node)
    stepcount += first[1]
    current = first[0]
    for x in range(1, bst_size(node)):
        next = findnext(current)
        stepcount += next[1]
        current = next[0]
    return stepcount


def bst_size(root, count=0):
    if root is None:
        return count
    return bst_size(root.left, bst_size(root.right, count + 1))


if __name__ == '__main__':
    table = []
    for i in range(1, 51):
        cTree = BST()
        cTree.gen_random_tree()
        count = inorder(cTree.root)
        size = bst_size(cTree.root)
        table.append(["Tree " + str(i), str(size), str(count), str(2 * (size-1))])
    print tabulate(table, headers=["Tree Number", "Number of Nodes", "Number of Steps", "2(N-1)"])
