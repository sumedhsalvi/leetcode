# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative approach 1
#         if root is None:
#             return []
        
#         stack, output, curr = [], [], root
        
#         while curr or stack:
#             while curr is not None:
#                 stack.append(curr)
#                 curr = curr.left
                
#             curr = stack.pop()
#             output.append(curr.val)
#             curr = curr.right
#         return output
                    
        # Iterative approach 2          
        if not root: return None
        
        orderStack = []
        res = []
        
        orderStack.append((root,0))
        while orderStack:
            #check top
            curr, state = orderStack.pop()
        
            if curr and state == 0:
                orderStack.append((curr, state+1))
                orderStack.append((curr.left, 0))
                
            elif curr and state == 1:
                orderStack.append((curr, state+1))
                res.append(curr.val)

                
            elif curr and state == 2:
                orderStack.append((curr, state+1))
                orderStack.append((curr.right, 0))
                
        return res