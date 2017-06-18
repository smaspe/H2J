import json
from unittest import TestCase

from lxml import html

from html_to_json.html_to_json import map_element_to_json


class TestMapElementToJson(TestCase):
    def file_to_string(self, path):
        with open(path) as f:
            return f.read()

    def test_map_element_to_json(self):
        index = html.parse('fixtures/index.html')
        mapping = json.loads(self.file_to_string('fixtures/mapping.json'))
        result = map_element_to_json(index, mapping)
        self.assertEqual(15, len(result), 'Wrong result size')
        self.assertEqual(
            '//news.slashdot.org/story/17/06/17/1541247/venezuelans-flock-to-cryptocoins-amid-spiralling-inflation',
            result[0]['link']['href'], 'Wrong link')
        self.assertEqual(
            'Venezuelans Flock To Cryptocoins Amid Spiralling Inflation',
            result[0]['link']['title'], 'Wrong title')
        self.assertEqual(1180, len(result[0]['content']), 'Wrong content size')
        self.assertEqual(
            '//it.slashdot.org/story/17/06/16/2151221/firm-responsible-for-mirai-infected-webcams-hires-software-firm-to-make-its-products-more-secure',
            result[14]['link']['href'], 'Wrong link')
        self.assertEqual(
            'Firm Responsible For Mirai-Infected Webcams Hires Software Firm To Make Its Products More Secure',
            result[14]['link']['title'], 'Wrong title')
        self.assertEqual(1780, len(result[14]['content']), 'Wrong content size')
