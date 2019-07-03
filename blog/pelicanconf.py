#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ha.Minh'
SITENAME = u"Ha.Minh's Blog"
SITEURL = 'http://minhhh.github.io'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

PLUGINS = [
    'pelican_git'
]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          )

# Social widget
# SOCIAL = (
#           # ('Twitter', 'https://twitter.com/utsace'),
#           )
SOCIAL =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          )

GITHUB_URL = 'https://github.com/minhhh'
TWITTER_URL = ''
FACEBOOK_URL = ''
GOOGLEPLUS_URL = ''

# Pages
DEFAULT_PAGINATION = 10
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
DEFAULT_CATEGORY = ('Programming')
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}
MARKUP = ('rst', 'md')
ARTICLE_EXCLUDES = ('pages',)

# Url
# ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
# ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{slug}-{lang}.html'
ARTICLE_URL = 'posts/{slug}'
ARTICLE_LANG_URL = 'posts/{slug}-{lang}'
PAGE_URL = 'pages/{slug}'
PAGE_LANG_URL = '{pages/{slug}-{lang}'
# ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
# ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{slug}-{lang}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'
ARTICLE_LANG_SAVE_AS = 'posts/{slug}-{lang}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
PAGE_LANG_SAVE_AS = 'pages/{slug}-{lang}.html'

# Archive
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Themes
THEME = "pelican-themes/gum"
STATIC_PATHS = ['images', 'js', 'css']

# Analytics
GOOGLE_ANALYTICS = 'UA-50796592-2'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DELETE_OUTPUT_DIRECTORY = False
