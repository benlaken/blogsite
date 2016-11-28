##!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import os.path as op

AUTHOR = u'Benjamin Laken'
AUTHOR_EMAIL = 'benlaken@gmail.com'
SITENAME = 'benlaken.com'
SITEURL = 'http://benlaken.github.io/blogsite'
# SITEURL = 'http://localhost:8000'
TAGLINE = u'Earth science meanderings'
DISQUS_SITENAME = 'www.benlaken.com'

PATH = 'content'
STATIC_PATHS = ['theme/static/', './theme/static/images/favicon.ico']
EXTRA_PATH_METADATA = {'favicon.ico': {'path': 'theme/static/images/favicon.ico'}}
PROFILE_IMAGE_URL = "theme/images/prfpic250.png"
COVER_IMG_URL = "theme/images/tenerife.jpg"

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = 'en'

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['gravatar', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', "tag_cloud", "simple_footnotes",
           'share_post']

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = None
# CATEGORY_FEED_ATOM = None
# TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None
FEED_ALL_ATOM = u'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = u'feeds/%s.atom.xml'
# TRANSLATION_FEED_ATOM = None

FEED_ALL_RSS = u'feeds/all.rss.xml'
CATEGORY_FEED_RSS = u'feeds/%s.rss.xml'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
         ('github-square', 'https://github.com/benlakentw'),
         ('twitter-square', 'https://twitter.com/benlaken'),
         ('linkedin-square', 'https://www.linkedin.com/in/benjamin-laken-a3089087'),
         ('book', 'https://impactstory.org/u/0000-0003-2021-6258/publications'),
)

DEFAULT_PAGINATION = 5

# Tag cloud settings
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100
TAG_CLOUD_SORTING = 'random'
TAG_CLOUD_BADGE = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "theme"

OUTPUT_PATH = 'output'
