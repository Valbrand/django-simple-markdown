# ~ le encoding: utf-8 ~

from django import template
import re

register = template.Library()

def remove_quotes(arg):
	"""
	This function returns two values:
	- The treated string (i.e., without surrounding quotes)
	- A boolean value informing whether it removed any quotes or not

	Note that it will only remove anything if the quotes at each end match.
	Therefore, strings like "foo' will be returned as they are
	"""
	quotes = ("'", '"')
	if arg[0] == arg[-1] and arg[0] in quotes:
		return (arg[1:-1], True)

	return (arg, False)

@register.tag
def mdinput(parser, token):
	args = token.split_contents()
	tag_name = args[0]

	args = args[1:]
	widget_id = '""'
	input_name = '"md-text"'
	custom_style = False

	for arg in args:
		key_value = re.search(r'(?P<key>.+)\s*=\s*(?P<value>.+)', arg)

		if key_value is not None:
			if key_value.group('key') == u'id':
				widget_id = key_value.group('value')
			elif key_value.group('key') == u'name':
				input_name = key_value.group('value')
			else:
				raise template.TemplateSyntaxError(u"{0}: Invalid argument '{1}'.".format(tag_name, key_value.group('key')))
		else:
			real_arg, had_quotes = remove_quotes(arg)
			if real_arg == 'custom_style':
				custom_style = True
			else:
				raise template.TemplateSyntaxError(u"{0}: Invalid argument '{1}'.".format(tag_name, real_arg))

	return MarkdownInputNode(widget_id, input_name, custom_style)

class MarkdownInputNode(template.Node):
	def __init__(self, widget_id, input_name, custom_style):
		self.widget_id = widget_id
		self.input_name = input_name
		self.custom_style = custom_style

	def render(self, context):
		def evaluate_argument(arg):
			treated_argument, arg_had_quotes = remove_quotes(arg)

			if arg_had_quotes:
				return treated_argument
			else:
				try:
					return template.Variable(treated_argument).resolve(context)
				except template.VariableDoesNotExist:
					return u''

		tmp = template.loader.get_template('djsmd_input.html')

		return tmp.render(template.Context({
				'djsmd_widget_id' : evaluate_argument(self.widget_id),
				'djsmd_input_name' : evaluate_argument(self.input_name),
				'djsmd_custom_style' : self.custom_style,
				'djsmd_form_attrs' : ' rows="10" cols="40"'
			}))
