import pytest

from ..maximum_depth_of_binary_tree import Solution, TreeNode


def test_max_depth_single_node() -> None:
    root = TreeNode(1)
    sol = Solution()
    assert sol.maxDepth(root) == 1


def test_max_depth_balanced_tree() -> None:
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    sol = Solution()
    assert sol.maxDepth(root) == 2


def test_max_depth_unbalanced_tree_left() -> None:
    root = TreeNode(1, TreeNode(2, TreeNode(3)), None)
    sol = Solution()
    assert sol.maxDepth(root) == 3


def test_max_depth_unbalanced_tree_right() -> None:
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    sol = Solution()
    assert sol.maxDepth(root) == 3


def test_max_depth_empty_tree() -> None:
    root = None
    sol = Solution()
    assert sol.maxDepth(root) == 0


def test_max_depth_complex_tree() -> None:
    root = TreeNode(
        1,
        TreeNode(2, TreeNode(4, TreeNode(7), None), TreeNode(5)),
        TreeNode(3, None, TreeNode(6)),
    )

    sol = Solution()
    assert sol.maxDepth(root) == 4


if __name__ == "__main__":
    pytest.main()
