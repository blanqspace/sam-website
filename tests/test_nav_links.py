import os
import unittest
from html.parser import HTMLParser


class NavLinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_nav = False
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        if tag == 'nav':
            self.in_nav = True
        elif self.in_nav and tag == 'a':
            for name, value in attrs:
                if name == 'href':
                    self.hrefs.append(value)

    def handle_endtag(self, tag):
        if tag == 'nav':
            self.in_nav = False


class TestNavLinks(unittest.TestCase):
    def test_nav_links(self):
        required = {'index.html', 'about.html', 'contact.html'}
        html_files = ['index.html', 'about.html', 'contact.html']
        for file in html_files:
            with open(file, encoding='utf-8') as f:
                parser = NavLinkParser()
                parser.feed(f.read())
                with self.subTest(file=file):
                    self.assertTrue(
                        required.issubset(set(parser.hrefs)),
                        msg=f"Missing nav links in {file}"
                    )


if __name__ == '__main__':
    unittest.main()
