import string, random

class URLShortener:
    def __init__(self):
        self.url_map = {}
        self.reverse_map = {}

    def shorten_url(self, long_url):
        if long_url in self.reverse_map:
            return self.reverse_map[long_url]
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        self.url_map[code] = long_url
        self.reverse_map[long_url] = code
        return code

    def get_url(self, code):
        return self.url_map.get(code)
