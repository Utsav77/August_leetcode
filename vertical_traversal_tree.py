# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:     
        xs = collections.defaultdict(list)
        def dfs(node,x=0,y=0):
            if not node:return None
            xs[x].append([y,node.val])
            dfs(node.left  ,x-1,y+1)
            dfs(node.right ,x+1,y+1)

        dfs(root)
        res = []
        items = list(xs.items())
        items.sort()
        for k,v in items:
            v.sort()
            item = [x[1] for x in v]
            res.append(item)
        return res