import pytest

from .encode_and_decode_tinyurl import Codec


@pytest.fixture
def codec() -> Codec:
    return Codec()


def test_codec(codec: Codec) -> None:
    url = "https://leetcode.com/problems/design-tinyurl"
    short_url = codec.encode(url)
    assert codec.decode(short_url) == url

    short_url_again = codec.encode(url)
    assert short_url == short_url_again
    assert codec.decode(short_url_again) == url

    url2 = "https://www.example.com"
    short_url2 = codec.encode(url2)
    assert short_url != short_url2
    assert codec.decode(short_url2) == url2

    non_existent_short_url = "http://tinyurl.com/nonexistent"
    assert codec.decode(non_existent_short_url) == ""

    urls = [
        "https://www.google.com",
        "https://www.facebook.com",
        "https://www.twitter.com",
        "https://www.linkedin.com",
    ]
    short_urls = [codec.encode(url) for url in urls]
    for short_url, url in zip(short_urls, urls):
        assert codec.decode(short_url) == url


if __name__ == "__main__":
    pytest.main()
