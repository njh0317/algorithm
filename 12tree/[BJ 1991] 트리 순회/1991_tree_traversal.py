class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def inorder(node):
    traverse = ""
    if node.left != '.':
        traverse += inorder(tree[node.left])
    traverse+=node.data
    if node.right != '.':
        traverse += inorder(tree[node.right])
    return traverse
def preorder(node):
    traverse = ""
    traverse+=node.data
    if node.left != '.':
        traverse += preorder(tree[node.left])
    if node.right != '.':
        traverse += preorder(tree[node.right])
    return traverse
def postorder(node):
    traverse = ""
    if node.left != '.':
        traverse += postorder(tree[node.left])
    if node.right != '.':
        traverse += postorder(tree[node.right])
    traverse+=node.data
    return traverse
if __name__ == "__main__":
    N = int(input())
    tree = {}

    for _ in range(N):
        node, left, right = map(str, input().split())
        tree[node] = Node(node, left, right)
    print(preorder(tree['A']))
    print(inorder(tree['A']))
    print(postorder(tree['A']))