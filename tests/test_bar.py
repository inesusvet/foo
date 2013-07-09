from unittest import TestCase

from foo.bar.views import hello


class BarTestCase(TestCase):

    def test_bar(self):
        self.assertEqual(hello(), 'Hello, %username%!', "Wrong `bar()`")

