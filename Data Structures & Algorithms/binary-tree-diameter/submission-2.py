# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            return 1 + max(left, right)

        if not root:
            return 0

        leftHeight = height(root.left)
        rightHeight = height(root.right)

        leftDiameter = self.diameterOfBinaryTree(root.left)
        rightDiameter = self.diameterOfBinaryTree(root.right)

        return max(leftHeight + rightHeight,
                leftDiameter,
                rightDiameter)



        