import os
import sys

sys.path.insert(0, os.path.abspath('../../src/switchai'))

project = 'SwitchAI'

html_theme = 'furo'

html_title = "SwitchAI Docs"

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    # Adds a convenient copy button to code blocks.
    "sphinx_copybutton",
    # Automagically adds Open Graph meta tags.
    "sphinxext.opengraph"
]

# Show only class names.
add_module_names = False
