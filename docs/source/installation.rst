Installation Guide
==================

Requirements
------------

* Python 3.8 or higher
* pip package manager
* Internet connection for downloading dependencies

Installing from PyPI
--------------------

The easiest way to install HiLinkAPI is using pip:

.. code-block:: bash

   pip install hilinkapi

To install with all optional dependencies:

.. code-block:: bash

   pip install hilinkapi[dev,docs]

Installing from Source
----------------------

Clone the repository and install in development mode:

.. code-block:: bash

   git clone https://github.com/yourusername/hilinkapi.git
   cd hilinkapi
   pip install -e .

For development with all dependencies:

.. code-block:: bash

   pip install -e .[dev,docs]

Verifying Installation
----------------------

You can verify the installation by importing the library:

.. code-block:: python

   import HiLinkAPI
   print(HiLinkAPI.__version__)

Dependencies
------------

Core Dependencies
^^^^^^^^^^^^^^^^^

* **requests**: HTTP library for API communication
* **xmltodict**: XML parsing for API responses
* **beautifulsoup4**: HTML parsing for web interface
* **urllib3**: URL handling and connection pooling

Optional Dependencies
^^^^^^^^^^^^^^^^^^^^^

Development dependencies (``hilinkapi[dev]``):

* **pytest**: Testing framework
* **pytest-cov**: Coverage reporting
* **black**: Code formatting
* **flake8**: Linting
* **mypy**: Type checking

Documentation dependencies (``hilinkapi[docs]``):

* **sphinx**: Documentation generator
* **sphinx-rtd-theme**: ReadTheDocs theme
* **sphinx-autodoc-typehints**: Type hints in documentation
* **sphinx-copybutton**: Copy button for code blocks
* **myst-parser**: Markdown support
* **sphinxcontrib-mermaid**: Diagram support

Troubleshooting
---------------

Common Issues
^^^^^^^^^^^^^

**ImportError: No module named 'HiLinkAPI'**

Make sure you've installed the package correctly:

.. code-block:: bash

   pip install --upgrade hilinkapi

**Connection timeout errors**

Ensure your modem is accessible at the correct IP address (default: 192.168.8.1)

**Authentication failures**

Verify your username and password. Default credentials are usually:

* Username: ``admin``
* Password: ``admin`` or printed on the device

Getting Help
^^^^^^^^^^^^

If you encounter issues:

1. Check the `GitHub Issues <https://github.com/yourusername/hilinkapi/issues>`_
2. Review the `FAQ section <https://hilinkapi.readthedocs.io/en/latest/faq.html>`_
3. Ask in the `Discussions forum <https://github.com/yourusername/hilinkapi/discussions>`_