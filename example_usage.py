#!/usr/bin/env python3
"""
Simple example demonstrating the modernized HiLink API usage
"""
import logging
import time
from HiLinkAPI_modern import HiLinkAPI, HiLinkException

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def monitor_connection(host="192.168.8.1", username="admin", password="admin"):
    """
    Monitor modem connection status and signal strength
    """
    # Create API instance
    api = HiLinkAPI(
        modem_name="HuaweiModem",
        host=host,
        username=username,
        password=password
    )
    
    try:
        # Initialize API
        print("Initializing HiLink API...")
        if not api.initialize():
            print("Failed to initialize API")
            return
        
        print(f"✓ Connected to modem (WebUI version {api.webui_version})")
        
        # Login if required
        if api.check_login_required():
            print("Authentication required...")
            if api.login():
                print("✓ Logged in successfully")
            else:
                print("✗ Login failed")
                return
        
        # Get device information
        print("\n=== Device Information ===")
        device_info = api.get_device_info()
        print(f"Model: {device_info.get('DeviceName', 'Unknown')}")
        print(f"IMEI: {device_info.get('Imei', 'Unknown')}")
        print(f"Software: {device_info.get('SoftwareVersion', 'Unknown')}")
        print(f"Hardware: {device_info.get('HardwareVersion', 'Unknown')}")
        
        # Monitor connection
        print("\n=== Connection Status ===")
        while True:
            # Get connection status
            conn_status = api.get_connection_status()
            wan_ip = api.get_wan_ip()
            signal_info = api.get_signal_info()
            network_info = api.get_network_info()
            
            # Display status
            print(f"\nTime: {time.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Network: {network_info.get('FullName', 'Unknown')}")
            print(f"WAN IP: {wan_ip or 'Not connected'}")
            print(f"Connection: {conn_status.get('ConnectionStatus', 'Unknown')}")
            
            # Display signal strength
            if signal_info:
                rssi = signal_info.get('rssi', 'N/A')
                rsrp = signal_info.get('rsrp', 'N/A')
                rsrq = signal_info.get('rsrq', 'N/A')
                sinr = signal_info.get('sinr', 'N/A')
                print(f"Signal: RSSI={rssi} dBm, RSRP={rsrp} dBm, RSRQ={rsrq} dB, SINR={sinr} dB")
            
            # Wait before next update
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\n\nMonitoring stopped by user")
    except HiLinkException as e:
        print(f"\nAPI Error: {e}")
    finally:
        # Logout if logged in
        if api.logged_in:
            print("\nLogging out...")
            api.logout()


def manage_connection(host="192.168.8.1", username="admin", password="admin"):
    """
    Example of managing modem connection settings
    """
    api = HiLinkAPI(
        modem_name="HuaweiModem",
        host=host,
        username=username,
        password=password
    )
    
    try:
        # Initialize and login
        if not api.initialize():
            print("Failed to initialize API")
            return
        
        if api.check_login_required() and not api.login():
            print("Login failed")
            return
        
        print("Connected to modem")
        
        # Configure data connection
        print("\nConfiguring data connection...")
        if api.configure_data_connection(roaming=True, max_idle_time=3600):
            print("✓ Data connection configured (roaming enabled, 1 hour idle timeout)")
        
        # Switch network mode
        print("\nSwitching network modes...")
        modes = ["LTE", "WCDMA", "AUTO"]
        for mode in modes:
            print(f"  Switching to {mode}...")
            if api.switch_network_mode(mode):
                print(f"  ✓ Switched to {mode}")
                time.sleep(2)
        
        # Toggle connection
        print("\nToggling data connection...")
        print("  Disabling...")
        if api.switch_connection(False):
            print("  ✓ Connection disabled")
            time.sleep(3)
        
        print("  Enabling...")
        if api.switch_connection(True):
            print("  ✓ Connection enabled")
        
        print("\nConnection management completed")
        
    except HiLinkException as e:
        print(f"API Error: {e}")
    finally:
        if api.logged_in:
            api.logout()


def check_sms(host="192.168.8.1", username="admin", password="admin"):
    """
    Check SMS messages on the modem
    """
    api = HiLinkAPI(
        modem_name="HuaweiModem",
        host=host,
        username=username,
        password=password
    )
    
    try:
        # Initialize and login
        if not api.initialize():
            print("Failed to initialize API")
            return
        
        if api.check_login_required() and not api.login():
            print("Login failed")
            return
        
        # Get SMS count
        sms_count = api.get_sms_count()
        
        print("=== SMS Status ===")
        print(f"Unread messages: {sms_count['unread']}")
        print(f"Total inbox: {sms_count['inbox']}")
        print(f"Outbox: {sms_count['outbox']}")
        print(f"Drafts: {sms_count['draft']}")
        
    except HiLinkException as e:
        print(f"API Error: {e}")
    finally:
        if api.logged_in:
            api.logout()


def quick_status(host="192.168.8.1"):
    """
    Quick status check without authentication
    """
    api = HiLinkAPI(
        modem_name="HuaweiModem",
        host=host
    )
    
    try:
        # Initialize API
        if not api.initialize():
            print("Failed to connect to modem")
            return
        
        print(f"Modem detected: WebUI version {api.webui_version}")
        
        # Check if login is required
        login_required = api.check_login_required()
        print(f"Authentication required: {'Yes' if login_required else 'No'}")
        
        if not login_required:
            # Can get some info without login
            device_info = api.get_device_info()
            if device_info:
                print(f"Device: {device_info.get('DeviceName', 'Unknown')}")
            
            wan_ip = api.get_wan_ip()
            if wan_ip:
                print(f"WAN IP: {wan_ip}")
        else:
            print("Login required for more information")
            
    except HiLinkException as e:
        print(f"Error: {e}")


def main():
    """
    Main function with menu
    """
    print("HiLink API Modern Implementation - Examples")
    print("=" * 50)
    print("1. Monitor connection (real-time)")
    print("2. Manage connection settings")
    print("3. Check SMS status")
    print("4. Quick status (no auth)")
    print("5. Exit")
    print("=" * 50)
    
    choice = input("Select option (1-5): ").strip()
    
    if choice == "1":
        print("\nStarting connection monitor (Press Ctrl+C to stop)...")
        monitor_connection()
    elif choice == "2":
        print("\nManaging connection settings...")
        manage_connection()
    elif choice == "3":
        print("\nChecking SMS status...")
        check_sms()
    elif choice == "4":
        print("\nPerforming quick status check...")
        quick_status()
    elif choice == "5":
        print("Goodbye!")
    else:
        print("Invalid option")


if __name__ == "__main__":
    main()