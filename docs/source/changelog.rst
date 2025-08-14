Changelog
=========

All notable changes to HiLinkAPI will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_,
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

[Unreleased]
------------

Added
^^^^^
- ReadTheDocs documentation
- Comprehensive authentication guide
- Quick start guide
- Installation instructions

[0.1.0] - 2024-01-15
--------------------

Added
^^^^^
- Initial release of HiLinkAPI
- Support for Huawei HiLink modems
- Basic authentication (username/password)
- SCRAM-SHA-256 authentication support
- Token-based session management
- Core API methods:
  
  - Device information retrieval
  - Signal strength monitoring
  - Connection status checking
  - SMS sending and receiving
  - Network mode control
  - Data usage statistics
  
- Async/await support
- Type hints throughout
- Comprehensive error handling
- Automatic token refresh
- Session persistence

Changed
^^^^^^^
- Migrated from old API structure to modern async design
- Improved error messages and exceptions
- Enhanced documentation

Fixed
^^^^^
- Token expiration handling
- SCRAM authentication for newer modems
- Connection timeout issues
- SMS encoding problems

[0.0.9] - 2023-12-01
--------------------

Added
^^^^^
- Support for E8372h-320 modem
- Network band selection
- Roaming control

Changed
^^^^^^^
- Improved connection stability
- Better error recovery

Fixed
^^^^^
- Authentication loop bug
- Memory leak in long-running sessions

[0.0.8] - 2023-10-15
--------------------

Added
^^^^^
- Support for 5G modems
- Advanced signal metrics (RSRP, RSRQ, SINR)
- Connection history tracking

Changed
^^^^^^^
- Refactored authentication module
- Updated dependencies

Fixed
^^^^^
- Compatibility with firmware v2.0+
- Unicode handling in SMS

[0.0.7] - 2023-08-20
--------------------

Added
^^^^^
- Context manager support
- Automatic reconnection
- Rate limiting

Changed
^^^^^^^
- Simplified API interface
- Improved documentation

Fixed
^^^^^
- Thread safety issues
- Session cleanup

Migration Guide
---------------

From 0.0.x to 0.1.0
^^^^^^^^^^^^^^^^^^^

The 0.1.0 release includes breaking changes. See the migration guide:

**Old API (0.0.x):**

.. code-block:: python

   from hilink import HiLink
   
   modem = HiLink("192.168.8.1")
   modem.login("admin", "password")
   info = modem.device_info()

**New API (0.1.0):**

.. code-block:: python

   from HiLinkAPI import HiLinkAPI
   
   api = HiLinkAPI("192.168.8.1", "admin", "password")
   api.connect()
   info = api.get_device_info()

Key Changes:

1. Module renamed from ``hilink`` to ``HiLinkAPI``
2. Class renamed from ``HiLink`` to ``HiLinkAPI``
3. Methods now use ``get_`` prefix for clarity
4. Async support added (optional)
5. Automatic authentication in ``connect()``

Deprecation Notices
-------------------

The following features are deprecated and will be removed in future versions:

- ``login()`` method - use ``connect()`` instead
- ``device_info()`` - use ``get_device_info()``
- ``signal()`` - use ``get_signal_info()``

Future Plans
------------

Planned features for upcoming releases:

- **0.0.2**
  
  - Web UI for modem management
  - Backup/restore configuration
  - Firmware update support
  
- **0.0.3**
  
  - Multi-modem support
  - Load balancing
  - Failover capabilities
  
- **0.1.0**
  
  - Stable API
  - Full test coverage
  - Production ready

Contributing
------------

See :doc:`contributing` for information on how to contribute to this project.

Support
-------

For questions and support:

- GitHub Issues: https://github.com/yourusername/hilinkapi/issues
- Discussions: https://github.com/yourusername/hilinkapi/discussions