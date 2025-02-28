:pdf-title: Example
:pdf-filename: Example
:pdf-subtitle: Example of subtitle one | Separated subtitle
:pdf-revision: 0.0.1
:pdf-type: example

.. |pageLink| replace:: welcome page link 
.. _pageLink: index.html

.. role:: rst(code)
    :language: rst

.. role:: c(code)
    :language: c

.. _example:

Example
=======

This page is used to add some examples how to use sphinx codes and how it is rendered with this extension without additional fixures.
For more information about this extension, have a look to the |pageLink|_, `website link to google <https://www.google.com/>`_, `relative link to index page <index.html>`_ or `absolute link to options page </options.html>`_.

Admonitions
-----------

.. example::
    :collapsible: 

    - Collapsible default admonition
    - Custom defined admonition

.. demo::
    :collapsible: open

    Demonstration of custom defined admonition in the `conf.py` file.

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

Source Code
-----------
Source code can be included in the sentence like :c:`void` for C-code.

A paragraph for more lines is also possible:

.. code:: python

   number = 10
   numberName = "age"
   print(f'Number: {numberName} = {number}')

Formulas
--------

A ``formula`` can be inline like :rst:`:math:\`\\frac{3}{4}\text{m}\`` results in :math:`\frac{3}{4}\text{m}`.

A centered extended formula can be used with the math directive:

.. math::

   a^{2} + b^{2} = c^{2}

To render correctly math equations, use the math extension `sphinxcontrib.katex`.
The source is located at: `github <https://github.com/hagenw/sphinxcontrib-katex>`_ and use the same roles and directives as the sphinx math.
The difference to the base math is the configuration to prerender the math source and use them directly in the html file.
This must be set with:

.. code:: python

   katex_prerender = True



