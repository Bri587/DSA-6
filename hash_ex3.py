 # CHAPTER 6 EXERCISE 3

import hashlib

class URLShortener:
    """
    Mini URL shortener.

    Store:
    - code_to_url   : short_code -> long_url
    - url_to_code   : long_url -> short_code
    - click_counts  : short_code -> int
    """

    def __init__(self):
        # initialize dictionaries
        self.code_to_url = {}
        self.url_to_code = {}
        self.click_counts = {}

    def _make_code(self, url, extra=""):
        """
        Create short code using md5 hash.
        """
        digest = hashlib.md5((url + extra).encode()).hexdigest()
        return digest[:6]

    def shorten(self, url):
        """
        Return short code for URL.
        """
        # If URL already shortened
        if url in self.url_to_code:
            return self.url_to_code[url]

        extra = ""
        code = self._make_code(url, extra)

        # Resolve collisions
        counter = 1
        while code in self.code_to_url and self.code_to_url[code] != url:
            extra = str(counter)
            code = self._make_code(url, extra)
            counter += 1

        # Save mappings
        self.code_to_url[code] = url
        self.url_to_code[url] = code
        self.click_counts[code] = 0

        return code

    def open_url(self, code):
        """
        Return original URL and increase click count.
        """
        if code not in self.code_to_url:
            return None

        self.click_counts[code] += 1
        return self.code_to_url[code]

    def get_stats(self, code):
        """
        Return code statistics.
        """
        if code not in self.code_to_url:
            return None

        return {
            "code": code,
            "url": self.code_to_url[code],
            "clicks": self.click_counts[code]
        }


# FOR TESTING

shortener = URLShortener()

url1 = "https://example.com/products/usb-cable"
url2 = "https://example.com/about"
url3 = "https://example.com/products/usb-cable"

code1 = shortener.shorten(url1)
code2 = shortener.shorten(url2)
code3 = shortener.shorten(url3)

print("Codes:", code1, code2, code3)

print("Open code1:", shortener.open_url(code1))
print("Open code1 again:", shortener.open_url(code1))

print("Stats code1:", shortener.get_stats(code1))