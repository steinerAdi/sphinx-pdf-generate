# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

from sphinx_pdf_generate.version import __version__

sys.path.append(os.path.abspath("../"))

project = "Sphinx-Pdf-Generate"
copyright = "2023, Chipsee"
author = "Chipsee"
version = __version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_immaterial",
    "sphinx_pdf_generate",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "research.md"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_immaterial"
# html_sidebars = {
#     "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
# }
html_static_path = ["_static"]

rst_epilog = """

.. _github-issues: https://github.com/iSOLveIT/sphinx-pdf-generate/issues

.. |github-issues| replace:: GitHub issues

.. _weasyprint-linux: https://weasyprint.readthedocs.io/en/latest/install.html#linux

.. |weasyprint-linux| replace:: Linux

.. _weasyprint-macos: https://weasyprint.readthedocs.io/en/latest/install.html#os-x

.. |weasyprint-macos| replace:: MacOS

.. _weasyprint-windows: https://weasyprint.readthedocs.io/en/latest/install.html#windows

.. |weasyprint-windows| replace:: Windows

.. _sphinx-immaterial: https://github.com/jbms/sphinx-immaterial/

.. |sphinx-immaterial| replace:: Sphinx-Immaterial

.. _contributing: https://isolveit.github.io/sphinx-pdf-generate/contribute.html

.. |contributing| replace:: Contribution Guidelines

"""

# Sphinx-PDF-Generate configurations
pdfgen_verbose = False
pdfgen_site_url = "http://127.0.0.1:8000"
# pdfgen_debug = True
# pdfgen_debug_target = "index.rst"
pdfgen_author = "Chipsee"
pdfgen_author_logo = "_static/logo-chipsee-white.png"
pdfgen_copyright = copyright
pdfgen_disclaimer = "Disclaimer: Content can change at anytime and best to refer to website for latest information."
pdfgen_cover = True
# pdfgen_cover_title = ""
# pdfgen_cover_subtitle = ""
pdfgen_custom_template_path = ""
pdfgen_custom_css_path = ""
pdfgen_toc = True
pdfgen_toc_numbering = True
pdfgen_toc_title = "Contents"
pdfgen_toc_level = 6
pdfgen_cover_images = {}