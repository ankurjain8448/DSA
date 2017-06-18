class Node(object):
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self):
        self.root = None
        self.path = []

    def findNode(node):
        root = self.root
        return findParentNode(node, root)
    
    def findParentNode(self, node, root):
        if root is None:
            return None
        elif root.val == node.val:
            return root
        nodeFound = findParentNode(node, root.left)
        if nodeFound is None:
            nodeFound = findParentNode(node, root.right)
        return nodeFound

    def getnodepath(self, n, root):
        if root is not Node:
            if root.val == n:
                return True
            if getnodepath(root.left):
                self.path.append('L')
            if getnodepath(root.right):
                self.path.append('R')

    def insert(self, node, pos, parent):
        if self.root is None:
            self.root = node
        else:
            par = findNode(parent)
            if pos == 'L':
                par.left = node
            else:
                par.right = node

    @staticmethod
    def makeNode(val):
        return Node(val)
                
n , q = map(int, raw_input().strip().split())
tree = Tree()
par, child, pos = raw_input().strip().split()
par, child = map(tree.makeNode , [par, child])
tree.insert(par)
tree.insert(child, pos, par)
for i in xrange(1, n):
    par, child, pos = raw_input().strip().split()
    par, child = map(tree.makeNode , [par, child])
    tree.insert(child, pos, par)

for _ in xrange(q):
    n = input()
    temp_root = tree.root
    tree.path = []
    tree.getnodepath(n, temp_root)
    tree.path[::-1]
    temp_root = tree.root
    for i in tree.path:
        if i == 'L' and temp_root.left:
            temp_root = temp_root.left
        elif i == 'R' and temp_root.right:
            temp_root = temp_root.right
        else:
            print -1
            break
    else:
        print temp_root.val
