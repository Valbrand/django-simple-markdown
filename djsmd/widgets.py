# ~ le encoding: utf-8 ~

from django.forms import widgets, util
from django import template

class MarkdownWidget(widgets.Widget):
	def __init__(self, default_style=False, attrs=None):
		self.default_style = default_style
		super(MarkdownWidget, self).__init__(attrs)

	def render(self, name, value, attrs=None):
		if value is None:
			value = ''
		default_attrs = {
			'rows' : '10',
			'cols' : '40'
		}
		if attrs:
			default_attrs.update(attrs)
		tmpl = template.loader.get_template('djsmd_input.html')
		return tmpl.render(template.Context({
				'djsmd_custom_style' : not self.default_style,
				'djsmd_input_name' : name,
				'djsmd_initial_value' : value,
				'djsmd_form_attrs' : util.flatatt(default_attrs)
			}))
