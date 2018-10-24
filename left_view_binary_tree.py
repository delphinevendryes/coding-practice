'''
Given a Binary Tree, print Left view of it.
Left view of a Binary Tree is set of nodes visible when tree is visited from Left side.
'''

class Node():
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

    def insertLeft(self, val):
        assert not self.left
        self.left = Node(val)

    def insertRight(self, val):
        assert not self.right
        self.right = Node(val)

class BinaryTree():
    def __init__(self, root):
        self.root = Node(root)

    def __repr__(self):
        s = str()
        root = self.root
        stack = [root]
        while len(stack) > 0:
            c = stack.pop()
            s += ' ' + str(c.value)
            if c.left:
                stack.append(c.left)
                s += ' L --> ' + str(c.left.value)
            if c.right:
                stack.append(c.right)
                s += ' R --> ' + str(c.right.value)
        return s

    def insertLeft(self, element, node = None):
        if node:
            c = self.root
            stack = [c]
            while len(stack) > 0:
                c = stack.pop()
                if c.value == node:
                    break
                if c.left:
                    stack.append(c.left)
                if c.right:
                    stack.append(c.right)
            if (len(stack) == 0) & (c.value != node):
                print('No such node')
                return
            c.insertLeft(element)
        else:
            self.root.insertLeft(element)

    def print_left_path(self):
        c = self.root
        s = str(c.value)
        while c.left:
            c = c.left
            s += ' --> ' + str(c.value)
        print(s)


    def insertRight(self, element, node = None):
        if node:
            c = self.root
            stack = [c]
            while len(stack) > 0:
                c = stack.pop()
                if c.value == node:
                    break
                if c.left:
                    stack.append(c.left)
                if c.right:
                    stack.append(c.right)
            if (len(stack) == 0) & (c.value != node):
                print('No such node')
                return
            c.insertRight(element)
        else:
            self.root.insertRight(element)

bt = BinaryTree(2)
bt.insertLeft(3)
bt.insertRight(5)
bt.insertLeft(4, 3)
bt.insertLeft(6, 4)

bt.print_left_path()     # Should print: 2 --> 3 --> 4 --> 6