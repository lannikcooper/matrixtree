#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Cooper'
SITENAME = u'Matrix Tree'
SITEURL = 'http://tree.cooper.me'

TIMEZONE = 'Asia/Chongqing'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
)

# Social widget
SOCIAL = (
    ('新浪微博', 'http://weibo.com/gsavl'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DEFAULT_DATE_FORMAT = '周%a %B%d %Y'
DELETE_OUTPUT_DIRECTORY = True
MARKUP = ('md')

THEME = 'themes/default'

MD_EXTENSIONS = ([
    'codehilite(css_class=highlight)',
    'headerid',
    'extra',
    # 'toc'
])

PLUGIN_PATH = '../pelican-plugins'
PLUGINS = [
    # 'extract_toc'
]
