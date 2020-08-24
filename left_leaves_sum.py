# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None: 
            return 0
        q=[]
        q.append(root)
        s=0
        while(len(q)>0):
            node=q.pop(0)
            if(node.left is not None):
                q.append(node.left)
                temp=node.left
                if(temp.left is None):
                    if(temp.right is None):
                        s+=node.left.val
            if(node.right is not None):
                q.append(node.right)
                
                
        return s