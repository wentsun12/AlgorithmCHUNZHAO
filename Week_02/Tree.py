# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#94: 二叉树，中序，递归
class Solution:
    def inorderTraversal(self, root):
        res = []
        self.helper(root, res)
        return res
    
    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)
#94: 二叉树，中序，栈
class Solution:
    def inorderTraversal(self, root):
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right

#144:二叉树，前序，递归
class Solution:
    def preorderTraversal(self, root):
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root:
            res.append(root.val)
            self.helper(root.left, res)
            self.helper(root.right, res)
#144:二叉树，前序，栈
class Solution:
    def preorderTraversal(self, root):
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res


#590:N叉树，后序，递归
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root):
        res = []
        if root== None: return res
        self.helper(root, res)
        return res

    def helper(self, root, res):
        for child in root.children:
            self.helper(child, res)
        res.append(root.val)

#590:N叉树，后序，栈 (根据前序来写的，前序：根左右 交换顺序，根右左，然后反序变为左右根，即为后序)
class Solution:
    def postorder(self, root):
        res = []
        if root == None: return res

        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children)

        return res[::-1]

#589:N叉树，前序，递归
class Solution:
    def preorder(self, root):
        res = []
        if root == None: return res	
        self.helper(root, res)		
        return res

    def helper(self,root,res):
        res.append(root.val)
        for child in root.children:
            self.helper(child,res)


#589:N叉树，前序，栈
class Solution:
    def preorder(self, root):
        res = []
        if root==None: return res	        
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(reversed(node.children))
        return res

#589:N叉树，层序 (没怎么搞明白)

