# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root==None:
            return None
        root.left, root.right=root.right, root.left
        self.invertTree(root.left) #Call the left substree
        self.invertTree(root.right)  #Call the right substree
        
        return root
