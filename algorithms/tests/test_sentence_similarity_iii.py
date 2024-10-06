import pytest

from algorithms.sentence_similarity_iii import Solution


@pytest.fixture
def solution() -> Solution:
    return Solution()


def test_sentences_are_similar(solution: Solution) -> None:
    assert solution.areSentencesSimilar("My name is John", "My name is") == True
    assert solution.areSentencesSimilar("Hello world", "Hello") == True
    assert (
        solution.areSentencesSimilar("I love programming", "love programming") == True
    )
    assert solution.areSentencesSimilar("Python is great", "Python is great") == True


def test_sentences_are_not_similar(solution: Solution) -> None:
    assert (
        solution.areSentencesSimilar("My name is John", "name is not Patrick Bateman")
        == False
    )
    assert solution.areSentencesSimilar("Hello world", "world Hello") == False
    assert (
        solution.areSentencesSimilar("I love programming", "programming love I")
        == False
    )
    assert solution.areSentencesSimilar("Python is great", "great is Python") == False


def test_edge_cases(solution: Solution) -> None:
    assert solution.areSentencesSimilar("", "") == True
    assert solution.areSentencesSimilar("a", "a") == True
    assert solution.areSentencesSimilar("a", "") == True
    assert solution.areSentencesSimilar("", "a") == True
    assert solution.areSentencesSimilar("a b c", "a c d e f") == False


if __name__ == "__main__":
    pytest.main()
