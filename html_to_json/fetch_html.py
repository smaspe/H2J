from lxml import html

import requests


def get_html_tree(url):
    r = requests.get(url).content
    return html.fromstring(r)
