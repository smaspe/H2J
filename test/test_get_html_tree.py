from unittest import TestCase

import requests_mock

from test import file_to_string
from html_to_json.fetch_html import get_html_tree


class TestGetHtmlTree(TestCase):
    def test_get_html_tree(self):
        with requests_mock.Mocker() as m:
            m.get('https://slashdot.org', text=file_to_string('fixtures/index.html'))
            element = get_html_tree('https://slashdot.org')
            self.assertEqual(2, len(element.getchildren()), 'Should have head and body')
            self.assertEqual('en', element.get('lang'), 'lang should be en')
            self.assertEqual('html', element.tag, 'tag should be html')
