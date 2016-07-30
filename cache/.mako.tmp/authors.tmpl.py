# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1469903132.57859
_enable_loop = True
_template_filename = '/Users/nitishg/nikola/lib/python3.4/site-packages/nikola/data/themes/base/templates/authors.tmpl'
_template_uri = 'authors.tmpl'
_source_encoding = 'utf-8'
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        items = context.get('items', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        messages = context.get('messages', UNDEFINED)
        hidden_authors = context.get('hidden_authors', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        items = context.get('items', UNDEFINED)
        def content():
            return render_content(context)
        messages = context.get('messages', UNDEFINED)
        hidden_authors = context.get('hidden_authors', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<article class="authorindex">\n')
        if items:
            __M_writer('        <h2>')
            __M_writer(str(messages("Authors")))
            __M_writer('</h2>\n        <ul class="postlist">\n')
            for text, link in items:
                if text not in hidden_authors:
                    __M_writer('                <li><a class="reference listtitle" href="')
                    __M_writer(str(link))
                    __M_writer('">')
                    __M_writer(filters.html_escape(str(text)))
                    __M_writer('</a></li>\n')
            __M_writer('        </ul>\n')
        __M_writer('</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 11, "65": 11, "66": 11, "27": 0, "68": 11, "37": 2, "70": 16, "42": 17, "76": 70, "48": 4, "67": 11, "69": 14, "57": 4, "58": 6, "59": 7, "60": 7, "61": 7, "62": 9, "63": 10}, "uri": "authors.tmpl", "filename": "/Users/nitishg/nikola/lib/python3.4/site-packages/nikola/data/themes/base/templates/authors.tmpl", "source_encoding": "utf-8"}
__M_END_METADATA
"""
