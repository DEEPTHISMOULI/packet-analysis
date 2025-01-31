import pyshark

# Corrected File Path (Ensure the correct filename)
pcap_file = r"D:\example.pcapng"

# Set the correct TShark path
tshark_path = r"D:\Wireshark\tshark.exe"

# Load the capture file with a display filter for HTTP
cap = pyshark.FileCapture(pcap_file, tshark_path=tshark_path, display_filter="http")

# Iterate over packets and extract relevant information
for packet in cap:
    try:
        if hasattr(packet, 'http'):
            # Extract HTTP request method (GET/POST)
            method = getattr(packet.http, 'request_method', 'N/A')

            # Extract Host and URI (URL) from the packet
            host = getattr(packet.http, 'host', 'N/A')
            uri = getattr(packet.http, 'request_uri', 'N/A')

            # Extract full URL if available
            full_url = getattr(packet.http, 'request_full_uri', 'N/A')

            # Extract POST request data if available
            post_data = getattr(packet.http, 'file_data', 'N/A') if method == "POST" else "N/A"

            # Print extracted information
            print(f"Method: {method}, Host: {host}, URL: {uri}")
            print(f"Full URL: {full_url}")
            print(f"POST Data: {post_data}\n")

            # Detect unsecured HTTP traffic
            if "http://" in full_url.lower():
                print(f"⚠️ WARNING: Unsecured HTTP Traffic Detected -> {full_url}\n")

    except Exception as e:
        print(f"Error processing packet: {e}")
        continue  # Skip packets with errors

# Close the capture file after reading
cap.close()
