# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# Example: sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Set Up VIZIO Smart TV'
copyright = '2025, VIZIO'
author = 'VIZIO'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML output settings ----------------------------------------------------

# Title shown in the browser tab and top of HTML pages
html_title = "How to Set Up VIZIO Smart TV via vizio.com/setup – Step-by-Step Guide"

# Optional short title (e.g., for nav bar)
html_short_title = "Set Up VIZIO Smart TV"

# Favicon (place 'favicon.ico' in the root or _static folder)
html_favicon = 'favicon.ico'

# Uncomment to use Read the Docs theme
# html_theme = 'sphinx_rtd_theme'

# Hide “View page source”
html_show_sourcelink = False

# Allow raw HTML blocks in .rst files
html_allow_unsafe = True

# Theme customization options
html_theme_options = {
    'show_powered_by': False,
}

raw_enabled = True

# Static paths (CSS, JS, images, etc.)
# Uncomment if using custom assets
# html_static_path = ['_static']
