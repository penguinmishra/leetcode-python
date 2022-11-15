# https://leetcode.com/problems/count-complete-tree-nodes/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def height(self, node):
            if not node:
                return 0
            return 1 + self.height(node.left)

    
    
    def countNodes(self, root) -> int:
        if not root:
            return 0
        
        leftLeftHeight = self.height(root.left)
        rightLeftHeight = self.height(root.right)

        if leftLeftHeight == rightLeftHeight:
            return (1 << leftLeftHeight) + self.countNodes(root.right)
        else:
            return (1 << rightLeftHeight) + self.countNodes(root.left)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    solution = Solution()
    print(solution.countNodes(root))