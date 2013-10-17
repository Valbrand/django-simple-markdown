# ~ le encoding: utf-8 ~

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

setup(
	name = 'django_simple_markdown',
	version = '1.0.5',
	description = 'Django package for markdown editing within forms. Uses simple-markdown.js',
	package_dir = {
		'django_simple_markdown' : 'djsmd'
	},
	packages = ['django_simple_markdown', 'django_simple_markdown.templatetags'],
	package_data = {
		'django_simple_markdown' : ['templates/*', 'static/djsmd/js/*']
	},
	requires = ['Markdown'],
	install_requires = ['Markdown'],
	author = 'Daniel Oliveira',
	author_email = 'daniel@dvalbrand.com',
	url = 'https://github.com/Valbrand/django-simple-markdown',
)