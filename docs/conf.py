import os
import sys
sys.path.insert(0, os.path.abspath('..'))  # リポジトリ直下をimport可能にする

project = 'SystemDevelopment6thTest'
author = 'Zanekichi'
extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = []
html_theme = 'alabaster'
html_static_path = ['_static']
