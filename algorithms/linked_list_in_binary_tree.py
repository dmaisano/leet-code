from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


# ? Helper function to check if there's a path starting from current tree node that matches the linked list
def dfs(tree_node: Optional[TreeNode], list_node: Optional[ListNode]) -> bool:
    if not list_node:  # We've matched the entire linked list
        return True
    if not tree_node:  # Reached the end of the tree path without fully matching
        return False
    if tree_node.val != list_node.val:  # Current values do not match
        return False
    # Continue the search in both left and right subtrees
    return dfs(tree_node.left, list_node.next) or dfs(tree_node.right, list_node.next)


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # Main function to traverse the tree and check from each node
        if not root:
            return False
        if dfs(root, head):
            return True
        # Check recursively in both left and right subtrees
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
