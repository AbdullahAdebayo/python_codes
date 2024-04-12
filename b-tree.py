# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        print('inputs are not treenode')
        if (p.val != q.val) or ([p.left, p.right] != [q.left, q.right]):
            return False
        return True



p = TreeNode(val=1,left=TreeNode(val=3), right=TreeNode(val=2))
q = TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=2))

print(p)

print(Solution().isSameTree(p,q))
