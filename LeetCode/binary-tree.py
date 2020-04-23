"""
Prompt: 
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Variable Table: 
Input:  [1,2,3,null,5]
Output:  ["1->3","1->2->5"]
Expected:  ["1->2->5","1->3"]

answer: []
stack: [] 
left: 
right: 


"""
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
