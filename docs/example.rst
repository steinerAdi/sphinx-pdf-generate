:pdf-title: Example
:pdf-filename: Example
:pdf-revision: 0.0.1
:pdf-type: manual

.. |pageLink| replace:: welcome page link 
.. _pageLink: index.html


.. role:: rst(code)
    :language: rst

.. role:: c(code)
    :language: c


Example
=======

This page is used to add some examples how to use sphinx codes and how it is rendered with this extension [1]_.
For more information about this extension, have a look to the |pageLink|_.

Links
-----

Sphinx offers several link options with basic methods and additional roles.

`website link to google <https://www.google.com/>`_, `relative link to index page <index.html>`_ or `absolute link to options page </options.html>`_.
Link with :rst:`:doc:` role: :doc:`options`

Admonitions
-----------

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

Formulas
--------

A formula can be inline like: `:math:\`\frac{3}{4}\\,\\text{m}\`.` results in :math:`\frac{3}{4}\,\text{m}`.

A centered extended formula can be used with the math directive:

.. math::

    a^{2} + b^{2} = c^{2}


Lists
-----

List can be done as the basic

#. First element
#. Second element
#. Third element

After a list, a next can be started with the desired offset:

5. Element with offset of 5
#. Incremented element
#. Incremented element


.. [1]
   This is a basic footnote at the end of the document.
   Find more examples and customizations for the web page at `sphinx-immaterial documentation <https://jbms.github.io/sphinx-immaterial/>`_.