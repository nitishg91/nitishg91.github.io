# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1469903883.622955
_enable_loop = True
_template_filename = '/Users/nitishg/nikola/lib/python3.4/site-packages/nikola/data/themes/base/templates/base_helper.tmpl'
_template_uri = 'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_translations', 'html_headstart', 'html_stylesheets', 'html_feedlinks', 'late_load_js']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        sorted = context.get('sorted', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <ul class="translations">\n')
        for langname in sorted(translations):
            if langname != lang:
                __M_writer('            <li><a href="')
                __M_writer(str(abs_link(_link("root", None, langname))))
                __M_writer('" rel="alternate" hreflang="')
                __M_writer(str(langname))
                __M_writer('">')
                __M_writer(str(messages("LANGUAGE", langname)))
                __M_writer('</a></li>\n')
        __M_writer('    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        title = context.get('title', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        use_base_tag = context.get('use_base_tag', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        twitter_card = context.get('twitter_card', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        theme_color = context.get('theme_color', UNDEFINED)
        description = context.get('description', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html ')
        __M_writer("prefix='")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer('og: http://ogp.me/ns# article: http://ogp.me/ns/article# ')
        if comment_system == 'facebook':
            __M_writer('fb: http://ogp.me/ns/fb#\n')
        __M_writer("' ")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer('vocab="http://ogp.me/ns" ')
        if is_rtl:
            __M_writer('dir="rtl" ')
        __M_writer('lang="')
        __M_writer(str(lang))
        __M_writer('">\n<head>\n    <meta charset="utf-8">\n')
        if use_base_tag:
            __M_writer('    <base href="')
            __M_writer(str(abs_link(permalink)))
            __M_writer('">\n')
        if description:
            __M_writer('    <meta name="description" content="')
            __M_writer(filters.html_escape(str(description)))
            __M_writer('">\n')
        __M_writer('    <meta name="viewport" content="width=device-width">\n')
        if title == blog_title:
            __M_writer('        <title>')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</title>\n')
        else:
            __M_writer('        <title>')
            __M_writer(filters.html_escape(str(title)))
            __M_writer(' | ')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</title>\n')
        __M_writer('\n    ')
        __M_writer(str(html_stylesheets()))
        __M_writer('\n    <meta content="')
        __M_writer(str(theme_color))
        __M_writer('" name="theme-color">\n    ')
        __M_writer(str(html_feedlinks()))
        __M_writer('\n    <link rel="canonical" href="')
        __M_writer(str(abs_link(permalink)))
        __M_writer('">\n\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer('            <link rel="')
                __M_writer(str(name))
                __M_writer('" href="')
                __M_writer(str(file))
                __M_writer('" sizes="')
                __M_writer(str(size))
                __M_writer('"/>\n')
        __M_writer('\n')
        if comment_system == 'facebook':
            __M_writer('        <meta property="fb:app_id" content="')
            __M_writer(str(comment_system_id))
            __M_writer('">\n')
        __M_writer('\n')
        if prevlink:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(prevlink))
            __M_writer('" type="text/html">\n')
        if nextlink:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(nextlink))
            __M_writer('" type="text/html">\n')
        __M_writer('\n    ')
        __M_writer(str(mathjax_config))
        __M_writer('\n')
        if use_cdn:
            __M_writer('        <!--[if lt IE 9]><script src="https://html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer('        <!--[if lt IE 9]><script src="')
            __M_writer(str(url_replacer(permalink, '/assets/js/html5.js', lang)))
            __M_writer('"></script><![endif]-->\n')
        __M_writer('\n    ')
        __M_writer(str(extra_head_data))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        needs_ipython_css = context.get('needs_ipython_css', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            if use_cdn:
                __M_writer('            <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
            else:
                __M_writer('            <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n')
        else:
            __M_writer('        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/theme.css" rel="stylesheet" type="text/css">\n')
            if has_custom_css:
                __M_writer('            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        if needs_ipython_css:
            __M_writer('        <link href="/assets/css/ipython.min.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/nikola_ipython.css" rel="stylesheet" type="text/css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        generate_rss = context.get('generate_rss', UNDEFINED)
        len = context.get('len', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if rss_link:
            __M_writer('        ')
            __M_writer(str(rss_link))
            __M_writer('\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('rss', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(str(_link('rss', None)))
                __M_writer('">\n')
        if generate_atom:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer('                <link rel="alternate" type="application/atom+xml" title="Atom (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('index_atom', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/atom+xml" title="Atom" href="')
                __M_writer(str(_link('index_atom', None)))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        social_buttons_code = context.get('social_buttons_code', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(social_buttons_code))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"16": 0, "21": 2, "22": 67, "23": 71, "24": 92, "25": 115, "26": 125, "32": 117, "42": 117, "43": 119, "44": 120, "45": 121, "46": 121, "47": 121, "48": 121, "49": 121, "50": 121, "51": 121, "52": 124, "58": 3, "86": 3, "87": 6, "88": 7, "89": 8, "90": 10, "91": 11, "92": 13, "93": 14, "94": 15, "95": 17, "96": 18, "97": 21, "98": 21, "99": 21, "100": 24, "101": 25, "102": 25, "103": 25, "104": 27, "105": 28, "106": 28, "107": 28, "108": 30, "109": 31, "110": 32, "111": 32, "112": 32, "113": 33, "114": 34, "115": 34, "116": 34, "117": 34, "118": 34, "119": 36, "120": 37, "121": 37, "122": 38, "123": 38, "124": 39, "125": 39, "126": 40, "127": 40, "128": 42, "129": 43, "130": 44, "131": 44, "132": 44, "133": 44, "134": 44, "135": 44, "136": 44, "137": 47, "138": 48, "139": 49, "140": 49, "141": 49, "142": 51, "143": 52, "144": 53, "145": 53, "146": 53, "147": 55, "148": 56, "149": 56, "150": 56, "151": 58, "152": 59, "153": 59, "154": 60, "155": 61, "156": 62, "157": 63, "158": 63, "159": 63, "160": 65, "161": 66, "162": 66, "168": 73, "176": 73, "177": 74, "178": 75, "179": 76, "180": 77, "181": 78, "182": 80, "183": 81, "184": 84, "185": 85, "186": 88, "187": 89, "193": 94, "204": 94, "205": 95, "206": 96, "207": 96, "208": 96, "209": 97, "210": 98, "211": 99, "212": 100, "213": 100, "214": 100, "215": 100, "216": 100, "217": 102, "218": 103, "219": 103, "220": 103, "221": 106, "222": 107, "223": 108, "224": 109, "225": 109, "226": 109, "227": 109, "228": 109, "229": 111, "230": 112, "231": 112, "232": 112, "238": 69, "243": 69, "244": 70, "245": 70, "251": 245}, "filename": "/Users/nitishg/nikola/lib/python3.4/site-packages/nikola/data/themes/base/templates/base_helper.tmpl", "uri": "base_helper.tmpl", "source_encoding": "utf-8"}
__M_END_METADATA
"""
