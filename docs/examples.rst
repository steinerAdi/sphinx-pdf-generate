:pdf-title: Examples
:pdf-filename: examples
:pdf-revision: 0.0.1
:pdf-type: Example
:pdfgen-debug: True

Examples
========

.. example::
    :collapsible: 

    - Collapsible default admonition
    - Custom defined admonition

.. demo::
    :collapsible: open

    Demonstration of custom defined admonition in the ``conf.py`` file.

    .. code:: python

        sphinx_immaterial_custom_admonitions = [
            {
                "name": "demo",
                "color": (43, 155, 70),
                "icon": "fontawesome/solid/arrow-up-right-dots",
                "classes": ["demo"],
                "override": True
            }
        ]