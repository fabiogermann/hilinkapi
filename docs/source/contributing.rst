Contributing Guide
==================

We welcome contributions to HiLinkAPI! This guide will help you get started.

Getting Started
---------------

1. **Fork the Repository**
   
   Fork the project on GitHub and clone your fork locally:
   
   .. code-block:: bash
   
      git clone https://github.com/yourusername/hilinkapi.git
      cd hilinkapi

2. **Set Up Development Environment**
   
   .. code-block:: bash
   
      # Create virtual environment
      python -m venv venv
      source venv/bin/activate  # On Windows: venv\Scripts\activate
      
      # Install in development mode with all dependencies
      pip install -e .[dev,docs]

3. **Create a Branch**
   
   .. code-block:: bash
   
      git checkout -b feature/your-feature-name

Development Workflow
--------------------

Code Style
^^^^^^^^^^

We use Black for code formatting and follow PEP 8:

.. code-block:: bash

   # Format code
   black HiLinkAPI.py
   
   # Check style
   flake8 HiLinkAPI.py
   
   # Type checking
   mypy HiLinkAPI.py

Testing
^^^^^^^

All contributions must include tests:

.. code-block:: bash

   # Run tests
   pytest tests/
   
   # Run with coverage
   pytest --cov=HiLinkAPI tests/

Writing Tests
^^^^^^^^^^^^^

.. code-block:: python

   import pytest
   from HiLinkAPI import HiLinkAPI
   
   def test_connection():
       api = HiLinkAPI("192.168.8.1")
       # Your test code here
       assert api.host == "192.168.8.1"

Documentation
^^^^^^^^^^^^^

Update documentation for new features:

.. code-block:: bash

   # Build documentation locally
   cd docs
   sphinx-build -b html source _build/html
   
   # View in browser
   open _build/html/index.html

Pull Request Process
--------------------

1. **Ensure Quality**
   
   - All tests pass
   - Code is formatted with Black
   - Documentation is updated
   - Commit messages are clear

2. **Submit PR**
   
   - Provide clear description
   - Reference any related issues
   - Include examples if applicable

3. **Code Review**
   
   - Address reviewer feedback
   - Keep PR updated with main branch
   - Be patient and respectful

Contribution Ideas
------------------

Looking for ways to contribute? Consider:

- **Bug Fixes**: Check the issue tracker
- **New Features**: Modem support, API methods
- **Documentation**: Improve guides, add examples
- **Testing**: Increase test coverage
- **Performance**: Optimize existing code

Code of Conduct
---------------

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive criticism
- Help others learn and grow

Getting Help
------------

- Open an issue for bugs
- Start a discussion for ideas
- Join our community chat
- Read existing documentation

Thank you for contributing to HiLinkAPI!