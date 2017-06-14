#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Shaun Finglas'
SITENAME = 'Shaun Finglas'
SITESUBTITLE = 'Agile software development &amp; programming - one lesson at a time.'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'English'

DISPLAY_CATEGORIES_ON_MENU = False

USE_FOLDER_AS_CATEGORY = True

DEFAULT_PAGINATION = 30

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/posts/default.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

# Themes
THEME = 'themes/notmyidea'

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/ShaunFinglas'),
          ('Github', 'https://github.com/Finglas'),
          ('LinkedIn', 'https://www.linkedin.com/in/shaunfinglas/'),
          ('StackOverflow', 'https://stackoverflow.com/users/102482/finglas'))