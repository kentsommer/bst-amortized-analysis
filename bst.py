import random
from tabulate import tabulate


class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent


class BST:
    def __init__(self):
        self.root = None

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

    def gen_random_tree(self):
        num_nodes = random.randint(50, 100)
        unique_list = random.sample(range(0,10000), num_nodes)
        for i in range(0, num_nodes):
            self.insert(unique_list[i])


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
        table.append(["table " + str(i), str(size), str(count), str(2 * (size-1))])
    print tabulate(table, headers=["Table Number", "Number of Nodes", "Number of Steps", "2(N-1)"])
