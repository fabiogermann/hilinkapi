.. HiLinkAPI documentation master file

Welcome to HiLinkAPI Documentation
===================================

.. image:: https://img.shields.io/pypi/v/hilinkapi.svg
   :target: https://pypi.org/project/hilinkapi/
   :alt: PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/hilinkapi.svg
   :target: https://pypi.org/project/hilinkapi/
   :alt: Python Versions

.. image:: https://readthedocs.org/projects/hilinkapi/badge/?version=latest
   :target: https://hilinkapi.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://img.shields.io/github/license/fabiogermann/hilinkapi.svg
   :target: https://github.com/fabiogermann/hilinkapi/blob/main/LICENSE
   :alt: License

**HiLinkAPI** is a Python library for interacting with Huawei HiLink modems and routers. It provides a clean, async-ready interface for managing and monitoring your HiLink devices.

Features
--------

* 🚀 **Async Support**: Built with modern async/await patterns for efficient operations
* 🔐 **Secure Authentication**: Handles HiLink's authentication mechanisms including SCRAM
* 📊 **Comprehensive Monitoring**: Access signal strength, data usage, SMS, and more
* 🔄 **Connection Management**: Control mobile data connections and network modes
* 📱 **SMS Operations**: Send, receive, and manage SMS messages
* 🌐 **Network Control**: Switch between 2G/3G/4G/5G modes
* 🛡️ **Type Safety**: Full type hints for better IDE support
* ⚡ **Performance**: Optimized for minimal resource usage

Quick Start
-----------

Installation
^^^^^^^^^^^^

Install HiLinkAPI using pip:

.. code-block:: bash

   pip install hilinkapi

Basic Usage
^^^^^^^^^^^

.. code-block:: python

   import asyncio
   from hilinkapi import HiLinkAPI

   async def main():
       # Initialize the API
       api = HiLinkAPI("192.168.8.1", username="admin", password="admin")
       
       # Connect and authenticate
       await api.connect()
       
       # Get device information
       info = await api.get_device_info()
       print(f"Device: {info['DeviceName']}")
       print(f"IMEI: {info['Imei']}")
       
       # Get signal information
       signal = await api.get_signal_info()
       print(f"Signal Strength: {signal['rssi']} dBm")
       
       # Get connection status
       status = await api.get_connection_status()
       print(f"Connected: {status['ConnectionStatus'] == '901'}")
       
       # Disconnect
       await api.disconnect()

   asyncio.run(main())

Supported Devices
-----------------

HiLinkAPI has been tested with the following devices:

* Huawei E3372h-153
* Huawei E3372h-320
* Huawei E8372h-155
* Huawei E8372h-320
* Most other HiLink-compatible modems

Documentation Contents
----------------------

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   installation
   quickstart
   authentication
   api-example

.. toctree::
   :maxdepth: 2
   :caption: API Reference

   HiLinkAPI
   modules

.. toctree::
   :maxdepth: 1
   :caption: Development

   contributing
   changelog
   license

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Getting Help
------------

* **GitHub Issues**: `Report bugs or request features <https://github.com/fabiogermann/hilinkapi/issues>`_
* **Discussions**: `Ask questions and share ideas <https://github.com/fabiogermann/hilinkapi/discussions>`_
* **Source Code**: `View on GitHub <https://github.com/fabiogermann/hilinkapi>`_

License
-------

HiLinkAPI is released under the MIT License. See the LICENSE file for more details.
