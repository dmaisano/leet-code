from unittest.mock import patch

import pytest
import requests

from ..counting_movies import getNumberOfMovies


def test_getNumberOfMovies_success() -> None:
    # Mock response data
    mock_data = {
        "page": "1",
        "per_page": 10,
        "total": "15",
        "total_pages": 2,
        "data": [
            {"Title": "Movie1", "Year": 2000, "imdbID": "tt0000001"},
            # ... other movie entries
        ],
    }

    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = mock_data

        # Test with a mock query
        result: int = getNumberOfMovies("Movie")
        assert result == 15


def test_getNumberOfMovies_no_results() -> None:
    # Mock response data for no results
    mock_data = {
        "page": "1",
        "per_page": 10,
        "total": "0",
        "total_pages": 1,
        "data": [],
    }

    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = mock_data

        # Test with a mock query
        result: int = getNumberOfMovies("NonExistentMovie")
        assert result == 0


def test_getNumberOfMovies_api_error() -> None:
    with patch("requests.get") as mock_get:
        # Mock an API error response
        mock_get.side_effect = requests.exceptions.RequestException

        with pytest.raises(requests.exceptions.RequestException):
            getNumberOfMovies("Movie")


if __name__ == "__main__":
    pytest.main()
