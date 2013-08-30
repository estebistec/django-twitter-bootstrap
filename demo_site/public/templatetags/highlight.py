# -*- coding: utf-8 -*-


from django import template
from django.template.base import TextNode
from django.utils import html
from django.utils.safestring import mark_safe


register = template.Library()


@register.tag
def highlight(parser, token):
    token_args = token.split_contents()     
    lang = token_args[1]

    nodelist = parser.parse(('endhighlight',))
    parser.delete_first_token()
    return HighlightNode(nodelist)


class HighlightNode(template.Node):
    
    def __init__(self, nodelist, **kwargs):
        self.nodelist = nodelist

    def render(self, context):
        output = self.nodelist.render(context)
        return mark_safe(u"""<pre>{}</pre>""".format(
            html.escape(output)
        ))
