#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Shaun Finglas'
SITENAME = 'Shaun Finglas'
SITESUBTITLE = 'Programming & Software Development Blog'
SITEURL = 'https://blog.shaunfinglas.co.uk'

YEAR = '2019'

RELATIVE_URLS = True

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'English'

DISPLAY_CATEGORIES_ON_MENU = False

USE_FOLDER_AS_CATEGORY = True

DEFAULT_PAGINATION = 12

# Single author, do not generate author pages.
AUTHOR_SAVE_AS = ''

YEAR_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/index.html'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/posts/default.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

# Themes
THEME = 'simple'

# Style
CSS_FILE = 'main.css'

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/ShaunFinglas'),
          ('Github', 'https://github.com/Finglas'),
          ('LinkedIn', 'https://www.linkedin.com/in/shaunfinglas/'),
          ('StackOverflow', 'https://stackoverflow.com/users/102482/finglas'))

GOOGLE_ANALYTICS = 'UA-68423049-2'