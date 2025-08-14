Authentication Guide
====================

HiLinkAPI supports multiple authentication methods used by different HiLink modem models. This guide explains how authentication works and how to handle different scenarios.

Authentication Methods
----------------------

Basic Authentication
^^^^^^^^^^^^^^^^^^^^

Most older HiLink modems use basic authentication:

.. code-block:: python

   from HiLinkAPI import HiLinkAPI
   
   api = HiLinkAPI(
       host="192.168.8.1",
       username="admin",
       password="admin"
   )
   api.connect()

SCRAM Authentication
^^^^^^^^^^^^^^^^^^^^

Newer modems (firmware versions 2019+) use SCRAM-SHA-256:

.. code-block:: python

   # The library automatically detects and handles SCRAM
   api = HiLinkAPI(
       host="192.168.8.1",
       username="admin",
       password="your_password"
   )
   api.connect()  # SCRAM negotiation happens automatically

Token-Based Authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^

All HiLink modems use session tokens for API requests:

.. code-block:: python

   # Tokens are managed automatically
   api = HiLinkAPI("192.168.8.1")
   api.connect()
   
   # The library handles:
   # - Requesting session tokens
   # - Including tokens in headers
   # - Refreshing expired tokens

Authentication Flow
-------------------

The authentication process follows these steps:

1. **Initial Connection**
   
   .. code-block:: python
   
      api = HiLinkAPI(host, username, password)

2. **Session Initialization**
   
   The library requests a session token from ``/api/webserver/SesTokInfo``

3. **Authentication Check**
   
   Determines if authentication is required by checking ``/api/user/state-login``

4. **Login Process**
   
   - For basic auth: Sends credentials to ``/api/user/login``
   - For SCRAM: Performs SCRAM-SHA-256 handshake

5. **Token Management**
   
   Stores and manages session tokens for subsequent requests

Handling Authentication Errors
-------------------------------

Common Errors
^^^^^^^^^^^^^

.. code-block:: python

   from HiLinkAPI import HiLinkAPI, AuthenticationError
   
   try:
       api = HiLinkAPI("192.168.8.1", "admin", "wrong_password")
       api.connect()
   except AuthenticationError as e:
       print(f"Authentication failed: {e}")
       # Handle error: wrong password, locked account, etc.

Error Codes
^^^^^^^^^^^

Common authentication error codes:

* ``108003``: User already logged in
* ``108006``: Wrong username or password
* ``108007``: Too many login attempts
* ``125002``: Token expired
* ``125003``: Invalid token

Automatic Re-authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The library automatically handles token expiration:

.. code-block:: python

   # Long-running application
   api = HiLinkAPI("192.168.8.1", "admin", "password")
   api.connect()
   
   while True:
       # Token refresh happens automatically if expired
       signal = api.get_signal_info()
       print(f"Signal: {signal['rssi']} dBm")
       time.sleep(10)

Advanced Configuration
----------------------

Custom Headers
^^^^^^^^^^^^^^

Add custom headers for specific modem models:

.. code-block:: python

   api = HiLinkAPI(
       host="192.168.8.1",
       username="admin",
       password="password",
       headers={
           "User-Agent": "Mozilla/5.0",
           "Accept-Language": "en-US"
       }
   )

Timeout Configuration
^^^^^^^^^^^^^^^^^^^^^

Configure connection and read timeouts:

.. code-block:: python

   api = HiLinkAPI(
       host="192.168.8.1",
       timeout=(5, 30)  # (connection_timeout, read_timeout)
   )

SSL/TLS Support
^^^^^^^^^^^^^^^

For modems with HTTPS support:

.. code-block:: python

   api = HiLinkAPI(
       host="192.168.8.1",
       use_https=True,
       verify_ssl=False  # Set to True if you have valid certificates
   )

Session Management
------------------

Manual Session Control
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   api = HiLinkAPI("192.168.8.1", "admin", "password")
   
   # Manual login
   api.login()
   
   # Check if logged in
   if api.is_logged_in():
       print("Successfully logged in")
   
   # Manual logout
   api.logout()

Session Persistence
^^^^^^^^^^^^^^^^^^^

Save and restore sessions:

.. code-block:: python

   # Save session
   api.connect()
   session_data = api.get_session_data()
   
   # Later, restore session
   new_api = HiLinkAPI("192.168.8.1")
   new_api.restore_session(session_data)

Multi-User Scenarios
---------------------

Handling Multiple Users
^^^^^^^^^^^^^^^^^^^^^^^^

Some modems support multiple concurrent users:

.. code-block:: python

   # User 1
   api1 = HiLinkAPI("192.168.8.1", "admin", "password")
   api1.connect()
   
   # User 2 (if supported)
   api2 = HiLinkAPI("192.168.8.1", "user", "user_password")
   api2.connect()

Force Login
^^^^^^^^^^^

Force login even if another user is connected:

.. code-block:: python

   api = HiLinkAPI(
       host="192.168.8.1",
       username="admin",
       password="password",
       force_login=True  # Kicks out other users
   )
   api.connect()

Security Best Practices
-----------------------

1. **Never hardcode credentials**
   
   .. code-block:: python
   
      import os
      
      api = HiLinkAPI(
          host=os.getenv("HILINK_HOST", "192.168.8.1"),
          username=os.getenv("HILINK_USER"),
          password=os.getenv("HILINK_PASS")
      )

2. **Use secure password storage**
   
   .. code-block:: python
   
      import keyring
      
      password = keyring.get_password("hilink", "admin")
      api = HiLinkAPI("192.168.8.1", "admin", password)

3. **Implement rate limiting**
   
   .. code-block:: python
   
      import time
      
      last_request = 0
      MIN_INTERVAL = 1.0  # seconds
      
      def rate_limited_request(api, method, *args):
          global last_request
          elapsed = time.time() - last_request
          if elapsed < MIN_INTERVAL:
              time.sleep(MIN_INTERVAL - elapsed)
          result = getattr(api, method)(*args)
          last_request = time.time()
          return result

4. **Handle session timeouts gracefully**
   
   .. code-block:: python
   
      def safe_api_call(api, method, *args, **kwargs):
          try:
              return getattr(api, method)(*args, **kwargs)
          except AuthenticationError:
              api.connect()  # Re-authenticate
              return getattr(api, method)(*args, **kwargs)

Troubleshooting
---------------

Debug Logging
^^^^^^^^^^^^^

Enable debug logging to troubleshoot authentication:

.. code-block:: python

   import logging
   
   logging.basicConfig(level=logging.DEBUG)
   
   api = HiLinkAPI("192.168.8.1", "admin", "password")
   api.connect()  # Detailed logs will show authentication flow

Common Issues
^^^^^^^^^^^^^

**"Already logged in" error**

Another user or session is active. Solutions:

- Wait for the session to timeout
- Use ``force_login=True``
- Restart the modem

**"Too many attempts" error**

Too many failed login attempts. Solutions:

- Wait 30 minutes for lockout to expire
- Restart the modem
- Check if the password has been changed

**Token expiration during long operations**

The library handles this automatically, but you can manually refresh:

.. code-block:: python

   api.refresh_token()