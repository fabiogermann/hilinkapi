# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from datetime import datetime

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'HiLinkAPI'
copyright = f'{datetime.now().year}, HiLinkAPI Contributors'
author = 'HiLinkAPI Contributors'

# The version info for the project
try:
    # Try to get version from the package
    import HiLinkAPI
    version = HiLinkAPI.__version__
except (ImportError, AttributeError):
    # Fallback to reading from setup.py or use default
    version = '0.1.0'

release = version

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.githubpages',
    'sphinx_autodoc_typehints',
    'sphinx_copybutton',
    'myst_parser',
    'sphinxcontrib.mermaid',
]

# Add support for Markdown files
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []

# Napoleon settings for Google and NumPy style docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_type_aliases = None

# Autodoc settings
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__',
    'show-inheritance': True,
}

# Intersphinx mapping
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'aiohttp': ('https://docs.aiohttp.org/en/stable/', None),
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Theme options
html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'style_nav_header_background': '#2980B9',
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
}

# Add custom CSS if needed
html_css_files = [
    'custom.css',
]

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = '_static/logo.png'

# The name of an image file (relative to this directory) to use as a favicon
# html_favicon = '_static/favicon.ico'

# -- Options for LaTeX/PDF output ---------------------------------------------

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'preamble': r'''
\usepackage{charter}
\usepackage[defaultsans]{lato}
\usepackage{inconsolata}
''',
}

# Grouping the document tree into LaTeX files
latex_documents = [
    ('index', 'HiLinkAPI.tex', 'HiLinkAPI Documentation',
     'HiLinkAPI Contributors', 'manual'),
]

# -- Options for manual page output -------------------------------------------

man_pages = [
    ('index', 'hilinkapi', 'HiLinkAPI Documentation',
     ['HiLinkAPI Contributors'], 1)
]

# -- Options for Texinfo output -----------------------------------------------

texinfo_documents = [
    ('index', 'HiLinkAPI', 'HiLinkAPI Documentation',
     'HiLinkAPI Contributors', 'HiLinkAPI', 
     'Python API for Huawei HiLink modems',
     'Miscellaneous'),
]

# -- Options for Epub output --------------------------------------------------

epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# -- Extension configuration ---------------------------------------------------

# Copy button configuration
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True

# Mermaid configuration for diagrams
mermaid_version = "10.6.1"
