class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


 
# Create instances of TreeNode
p = TreeNode(val=1, left=TreeNode(val=3), right=TreeNode(val=2))
q = TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3))

# Create an instance of Solution and call the method
solution = Solution()
print(solution.isSameTree(p, q))
