# ~le encoding: utf-8 ~

from django import forms
from widgets import MarkdownWidget
import markdown

class MarkdownField(forms.Field):
	widget = MarkdownWidget

	def to_python(self, value):
		if value is None:
			value = ''

		return markdown.markdown(value)