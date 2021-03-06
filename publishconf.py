#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://benlaken.com'
# SITEURL = 'https://benlaken.github.io/blogsite'
RELATIVE_URLS = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

EXTRA_PATH_METADATA = {'extra/travis.yml': {'path': '.travis.yml'}}


# Following items are often useful when publishing

DISQUS_SITENAME = "www-benlaken-com"
GOOGLE_ANALYTICS = "UA-10815370-4"
