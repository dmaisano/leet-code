import base64


class Codec:
    def __init__(self) -> None:
        self.url_to_code: dict[str, str] = {}
        self.code_to_url: dict[str, str] = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        if longUrl in self.url_to_code:
            return self.url_to_code[longUrl]

        encoded_bytes = base64.urlsafe_b64encode(longUrl.encode("utf-8"))
        short_code = encoded_bytes.decode("utf-8").rstrip("=")

        short_url = "http://tinyurl.com/" + short_code
        self.url_to_code[longUrl] = short_url
        self.code_to_url[short_code] = longUrl
        return short_url

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        if len(shortUrl) == 0:
            return ""
        short_code: str = shortUrl.split("/")[-1]
        if short_code not in self.code_to_url:
            return ""

        padded_code = short_code + "=" * (-len(short_code) % 4)
        decoded_bytes = base64.urlsafe_b64decode(padded_code)
        return decoded_bytes.decode("utf-8")
