# coding=utf-8

import os
import sys
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

sys.path.append(
    os.path.join(os.path.dirname(__file__), "..", "src")
)

from hecate import __version__


autodoc_member_order = 'bysource'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']

source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Hecate'
copyright = u'2015, David R. MacIver'
author = u'David R. MacIver'

version = __version__
release = __version__

language = None

exclude_patterns = ['_build']

pygments_style = 'sphinx'

todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_static_path = ['_static']

htmlhelp_basename = 'Hecatedoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
}

latex_documents = [
    (master_doc, 'Hecate.tex', u'Hecate Documentation',
     u'David R. MacIver', 'manual'),
]

man_pages = [
    (master_doc, 'hypothesis', u'Hecate Documentation',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'Hecate', u'Hecate Documentation',
     author, 'Hecate', 'Testing library for console applications.',
     'Miscellaneous'),
]