import sys

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.parent = None
        self.left = left
        self.right = right

def preorder(node):
    if node is not None:
        print(node.data, end = "")
        if node.left != ".":
            preorder(tree[node.left])
        if node.right != ".":
            preorder(tree[node.right])
        
def inorder(node):
    if node.data is not None:
        if node.left != ".":
            inorder(tree[node.left])
        print(node.data, end = "")
        if node.right != ".":
            inorder(tree[node.right])

def postorder(node):
    if node is not None:
        if node.left != ".":
            postorder(tree[node.left])
        if node.right != ".":
            postorder(tree[node.right])
        print(node.data, end ="")



input = sys.stdin.readline
n = int(input())
tree = {}

for _ in range(n):
    node, left, right = map(str, input().split())
    tree[node] = Node(data = node, left = left, right = right)

preorder(tree["A"])
print()
inorder(tree["A"])
print()
postorder(tree["A"])