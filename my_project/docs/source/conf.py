# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'My C++ Doxygen+Breathe+Sphinx Project'
copyright = '2025, Ahsan Yusob'
author = 'Ahsan Yusob'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["breathe"]

# Path to Doxygen XML
breathe_projects = {
    "MyProject": "../build/xml"
}
breathe_default_project = "MyProject"

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Use the Read the Docs theme
html_theme = "sphinx_rtd_theme"
html_baseurl = "https://ahsanyusob.github.io/cpp_sphinx_test/"

# Optional: theme-specific options
html_theme_options = {
    'collapse_navigation': False,  # keep sidebar sections expanded
    'navigation_depth': 4,         # how many levels in the sidebar
    "canonical_url": "https://ahsanyusob.github.io/cpp_sphinx_test/",
    "display_version": True,
}
html_static_path = ['_static']
