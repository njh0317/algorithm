class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1
    def depth(self):
        leftDepth = self.left.depth() if self.left else 0
        rightDepth = self.right.depth() if self.right else 0

        return leftDepth + 1 if leftDepth>rightDepth else rightDepth + 1
    def inorder(self):
        traverse = []
        if self.left:
            traverse += self.left.inorder()
        traverse.append(self.data)
        if self.right:
            traverse += self.right.inorder()
        return traverse
    def preorder(self):
        traverse = []
        traverse.append(self.data)
        if self.left:
            traverse += self.left.preorder()
        if self.right:
            traverse += self.right.preorder()
        return traverse
    def postorder(self):
        traverse = []
        if self.left:
            traverse += self.left.postorder()
        if self.right:
            traverse += self.right.postorder()
        traverse.append(self.data)
        return traverse
    def insert(self, data):
        if data<self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        elif data>self.data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)
        else:
            raise KeyError("data %d is already exist!"%data)
    def lookup(self, data, parent=None):
        if data<self.data:
            if self.left:
                return self.left.lookup(data, self)
            else:
                return None, None
        elif data > self.data:
            if self.right:
                return self.right.lookup(data, self)
            else:
                return None, None
        else:
            return self, parent
    def countChild(self):
        count = 0
        if self.left:count+=1
        if self.right:count+=1
        return count
class BinaryTree:
    def __init__(self, r):
        self.root = r
    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0
    def depth(self):
        if self.root:
            return self.root.depth()
        else:
            return 0
    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []
    def preorder(self):
        if self.root:
            return self.root.preorder()
        else:
            return []
    def postorder(self):
        if self.root:
            return self.root.postorder()
        else:
            return []
    def insert(self, data):
        if self.root:
            self.root.insert(data)
        else:
            self.root = Node(data)
    
    def lookup(self, data):
        if self.root: 
            return self.root.lookup(data)
        else:
            return None, None
    
    def remove(self, data):
        node, parent = self.lookup(data)
        if node:
            nChildren = node.countChild()
            #[Case1] : no children
            if nChildren == 0:
                # parent가 있을 경우
                # node가 왼쪽 자식인지 오른쪽 자식인지 판단해 
                # parent.left 혹은 parent.right를 None으로 하여
                # left node였던 자식을 트리에서 끊어낸다.
                if parent:
                    if parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None
                # parent가 없을 경우(==node가 root인 경우)
                # self.root를 None으로 한다.
                else:
                    self.root = None
            
            #[Case2] : only one child
            elif nChildren == 1:
                #하나 있는 자식이 왼쪽인지 오른쪽인지 판단
                # 그 자식을 어떤 변수가 가리키도록 한다.
                # 만약 parent가 있으면 node가 왼쪽인지 오른쪽인지 판단해
                # 위에서 가리킨 자식을 대신 node의 자리에 넣는다.
                if parent:
                    if node.left:#자식이 왼쪽 자식이라면 
                        if parent.left == node:
                            parent.left = node.left
                        else:
                            parent.right = node.left
                    else:
                        if parent.right == node:
                            parent.right = node
                        else:
                            parent.right = node.right
                #parent가 없으면(node가 root인 경우)
                #self.root에 위에서 가리킨 자식을 대신 넣는다.
                else:
                    if node.left:
                        self.root = node.left
                    else:
                        self.root = node.right
            #[Case 3] : both left and right children
            else:
                
                parent = node
                successor = node.right
                #오른쪽 자식 서브트리의 최소값을 찾아야 한다.
                # parent가 node를 가리키도록 하고,
                # successor는 node의 오른쪽 자식 서브트리의 root 노드를 가리키도록 한다.
                # successor로 부터 왼족 자식의 링크를 반복하여 따라감으로써
                # 순환문이 종료할 때 successor는 node의 오른쪽 자식 서브트리의 최소값을,
                # 그리고 parent는 그 노드의 부모 노드를 가리키도록 찾아낸다.
                
                while successor.left:
                    parent = successor
                    successor = successor.left
                
                #삭제하려는 노드인 node에 방금 찾은 successor의 key, data를 대입
                node.data = successor.data
                # 이제, successor 가 parent 의 왼쪽 자식인지 오른쪽 자식인지를 판단하여
                # 그에 따라 parent.left 또는 parent.right 를 successor 가 가지고 있던 (없을 수도 있지만) 자식을 가리키도록 합니다.

                if parent.left == successor:
                    if successor.left:
                        parent.left = successor
                    elif successor.right:
                        parent.left = successor.right
                    else:
                        parent.left = None
                else:
                    if successor.left:
                        parent.right = successor.left
                    elif successor.right:
                        parent.right = successor.right
                    else:
                        parent.right = None
            return True
        else:
            return False