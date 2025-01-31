import pyshark

# Set explicit path to TShark and fix the file path format
cap = pyshark.FileCapture(r"D:\example.pcapnp.pcapng", tshark_path="D:/Wireshark/tshark.exe", display_filter="http")

# Iterate over packets and extract relevant information
for packet in cap:
    try:
        if hasattr(packet, 'http'):
            # Extract HTTP request method (GET/POST)
            method = getattr(packet.http, 'request_method', 'N/A')

            # Extract Host and URI (URL) from the packet
            host = getattr(packet.http, 'host', 'N/A')
            uri = getattr(packet.http, 'request_uri', 'N/A')

            # Extract GET request URL (includes parameters)
            full_url = getattr(packet.http, 'request_full_uri', 'N/A')

            # Extract POST request data if available
            post_data = getattr(packet.http, 'file_data', 'N/A') if method == "POST" else "N/A"

            # Print extracted information
            print(f"Method: {method}, Host: {host}, URL: {uri}")
            print(f"Full URL: {full_url}")
            print(f"POST Data: {post_data}\n")

            # Detect insecure HTTP traffic
            if packet.highest_layer == "HTTP":
                print(f"⚠️ WARNING: Unsecured HTTP Traffic Detected -> {full_url}")

    except AttributeError:
        continue  # Skip packets without HTTP data
