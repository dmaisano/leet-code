import requests


def getNumberOfMovies(substr: str) -> int:
    response = requests.get(
        f"https://jsonmock.hackerrank.com/api/moviesdata/search/?Title={substr}"
    )
    data = response.json()
    return int(data["total"])
