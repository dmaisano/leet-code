import pytest

from .flipping_an_image import Solution


@pytest.fixture
def soln() -> Solution:
    return Solution()


def test_flip_and_invert_image(soln: Solution) -> None:
    sol = Solution()

    image1 = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    expected1 = [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
    assert sol.flipAndInvertImage(image1) == expected1

    image2 = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    expected2 = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]
    assert sol.flipAndInvertImage(image2) == expected2

    image3 = [[1, 0], [0, 1]]
    expected3 = [[1, 0], [0, 1]]
    assert sol.flipAndInvertImage(image3) == expected3

    image4 = [[0]]
    expected4 = [[1]]
    assert sol.flipAndInvertImage(image4) == expected4

    image5 = [[1]]
    expected5 = [[0]]
    assert sol.flipAndInvertImage(image5) == expected5


if __name__ == "__main__":
    pytest.main()
