# -*- coding: utf-8 -*-
__title__ = 'pelican-git'
__version__ = '0.1.0'
__author__ = 'Ha Minh'
__license__ = 'MIT'
__copyright__ = 'Copyright 2014'

from pelican_git.plugin import register

import jinja2 as jinja2_
jinja2 = jinja2_.Environment( loader=jinja2_.FileSystemLoader( 'templates' ) )
