from typing import List

import pytest

from algorithms.linked_list_in_binary_tree import ListNode, Solution, TreeNode


# Helper function to create a linked list from a list of values
def create_linked_list(values: List[int]) -> ListNode:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


# Helper function to create a binary tree from a list of values (level order)
def create_binary_tree(values: List[int]) -> TreeNode:
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    children = nodes[::-1]
    root = children.pop()
    for node in nodes:
        if node:
            if children:
                node.left = children.pop()
            if children:
                node.right = children.pop()
    return root


def test_is_sub_path() -> None:
    solution = Solution()

    # Test case 1: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
    head = create_linked_list([4, 2, 8])
    root = create_binary_tree(
        [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3]
    )
    assert solution.isSubPath(head, root) == True

    # Test case 2: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
    head = create_linked_list([1, 4, 2, 6])
    root = create_binary_tree(
        [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3]
    )
    assert solution.isSubPath(head, root) == True

    # Test case 3: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
    head = create_linked_list([1, 4, 2, 6, 8])
    root = create_binary_tree(
        [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3]
    )
    assert solution.isSubPath(head, root) == False

    # Additional Test case: Single node list and single node tree
    head = create_linked_list([1])
    root = create_binary_tree([1])
    assert solution.isSubPath(head, root) == True

    # Additional Test case: List does not match tree path
    head = create_linked_list([5])
    root = create_binary_tree([1])
    assert solution.isSubPath(head, root) == False

    # Additional Test case: List matches root but no matching path
    head = create_linked_list([1, 4])
    root = create_binary_tree([1, 2])
    assert solution.isSubPath(head, root) == False


if __name__ == "__main__":
    pytest.main()
