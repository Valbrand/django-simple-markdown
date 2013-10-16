# ~ le encoding: utf-8 ~

from distutils.core import setup

setup(
	name = 'django_simple_markdown',
	version = '1.0.1',
	description = 'Django package for markdown editing within forms. Uses simple-markdown.js',
	packages = ['djsmd', 'djsmd/static/djsmd/js', 'djsmd/templates', 'djsmd/templatetags'],
	requires = ['Markdown'],
	author = 'Daniel Oliveira',
	author_email = 'daniel@dvalbrand.com',
	url = 'https://github.com/Valbrand/django-simple-markdown',
)