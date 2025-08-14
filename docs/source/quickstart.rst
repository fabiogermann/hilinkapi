Quick Start Guide
=================

This guide will help you get started with HiLinkAPI in just a few minutes.

Basic Connection
----------------

The simplest way to connect to your HiLink modem:

.. code-block:: python

   from HiLinkAPI import HiLinkAPI
   
   # Create API instance
   api = HiLinkAPI("192.168.8.1")
   
   # Connect (authentication handled automatically)
   api.connect()
   
   # Get device information
   info = api.get_device_info()
   print(f"Device: {info['DeviceName']}")
   
   # Disconnect when done
   api.disconnect()

With Authentication
-------------------

If your modem requires authentication:

.. code-block:: python

   from HiLinkAPI import HiLinkAPI
   
   api = HiLinkAPI(
       host="192.168.8.1",
       username="admin",
       password="your_password"
   )
   
   api.connect()
   # Your code here
   api.disconnect()

Async Usage
-----------

For async applications:

.. code-block:: python

   import asyncio
   from HiLinkAPI import HiLinkAPI
   
   async def main():
       api = HiLinkAPI("192.168.8.1", username="admin", password="admin")
       
       await api.connect()
       
       # Get multiple data points concurrently
       info, signal, status = await asyncio.gather(
           api.get_device_info(),
           api.get_signal_info(),
           api.get_connection_status()
       )
       
       print(f"Device: {info['DeviceName']}")
       print(f"Signal: {signal['rssi']} dBm")
       print(f"Connected: {status['ConnectionStatus'] == '901'}")
       
       await api.disconnect()
   
   asyncio.run(main())

Common Operations
-----------------

Getting Signal Information
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   signal = api.get_signal_info()
   print(f"Signal Strength: {signal['rssi']} dBm")
   print(f"RSRP: {signal['rsrp']} dBm")
   print(f"RSRQ: {signal['rsrq']} dB")
   print(f"SINR: {signal['sinr']} dB")

Checking Data Usage
^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   stats = api.get_month_statistics()
   print(f"Monthly Download: {stats['CurrentMonthDownload']} bytes")
   print(f"Monthly Upload: {stats['CurrentMonthUpload']} bytes")
   print(f"Total Used: {stats['CurrentMonthTotal']} bytes")

Managing Connection
^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Check connection status
   status = api.get_connection_status()
   is_connected = status['ConnectionStatus'] == '901'
   
   # Connect to mobile network
   if not is_connected:
       api.connect_mobile()
   
   # Disconnect from mobile network
   api.disconnect_mobile()

Sending SMS
^^^^^^^^^^^

.. code-block:: python

   # Send SMS
   result = api.send_sms(
       phone_number="+1234567890",
       message="Hello from HiLinkAPI!"
   )
   
   if result['success']:
       print("SMS sent successfully")

Reading SMS
^^^^^^^^^^^

.. code-block:: python

   # Get inbox messages
   messages = api.get_sms_list(box_type=1)  # 1 = Inbox
   
   for msg in messages['Messages']['Message']:
       print(f"From: {msg['Phone']}")
       print(f"Date: {msg['Date']}")
       print(f"Content: {msg['Content']}")
       print("---")

Network Mode Control
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get current network mode
   mode = api.get_network_mode()
   print(f"Current mode: {mode['NetworkMode']}")
   
   # Set to 4G only
   api.set_network_mode(mode="03")  # 03 = 4G only
   
   # Set to automatic
   api.set_network_mode(mode="00")  # 00 = Auto

Error Handling
--------------

Always handle potential errors:

.. code-block:: python

   from HiLinkAPI import HiLinkAPI, HiLinkException
   
   try:
       api = HiLinkAPI("192.168.8.1")
       api.connect()
       
       info = api.get_device_info()
       print(f"Device: {info['DeviceName']}")
       
   except HiLinkException as e:
       print(f"HiLink error: {e}")
   except Exception as e:
       print(f"Unexpected error: {e}")
   finally:
       api.disconnect()

Context Manager
---------------

Use context manager for automatic cleanup:

.. code-block:: python

   from HiLinkAPI import HiLinkAPI
   
   with HiLinkAPI("192.168.8.1", "admin", "password") as api:
       info = api.get_device_info()
       print(f"Device: {info['DeviceName']}")
       # Connection automatically closed when exiting the context

Best Practices
--------------

1. **Always disconnect**: Close connections when done to free resources
2. **Handle errors**: Network operations can fail, always use try/except
3. **Use async for multiple operations**: Improves performance when fetching multiple data points
4. **Cache tokens**: The library handles token caching automatically
5. **Respect rate limits**: Don't poll too frequently (recommended: 5-10 second intervals)

Next Steps
----------

* Read the :doc:`authentication` guide for advanced authentication
* Explore the :doc:`HiLinkAPI` API reference
* Check :doc:`api-example` for more examples