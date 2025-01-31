Packet-analysis

This project analyzes HTTP traffic from a .pcapng file using PyShark. 
It extracts HTTP request details such as methods, URLs and POST data. It even detects unsecured HTTP traffic.
Features:
1. Extracts HTTP request method(GET,POST)
2. Displays host, request URI and full URL
3. Detects unsecured HTTP traffic (non-HTTPS)
4. Supports .pcapng files captured from Wireshark

Requirements:
1. Python 3.10+
2. Wireshark with tshark installed
3. Install PyShark (pip install pyshark)

Expected Output:
You need to view the HTTP requests and security warning in the console

Output received by the script:
D:\>python example.py
Method: GET, Host: ocsp.entrust.net, URL: /MFEwTzBNMEswSTAJBgUrDgMCGgUABBRr2bwARTxMtEy9aspRAZg5QFhagQQUgrrWPZfOn89x6JI3r%2F2ztWk1V88CEHHvVXSvNVTDWixp9m9La80%3D
Full URL: http://ocsp.entrust.net/MFEwTzBNMEswSTAJBgUrDgMCGgUABBRr2bwARTxMtEy9aspRAZg5QFhagQQUgrrWPZfOn89x6JI3r%2F2ztWk1V88CEHHvVXSvNVTDWixp9m9La80%3D
POST Data: N/A

⚠️ WARNING: Unsecured HTTP Traffic Detected -> http://ocsp.entrust.net/MFEwTzBNMEswSTAJBgUrDgMCGgUABBRr2bwARTxMtEy9aspRAZg5QFhagQQUgrrWPZfOn89x6JI3r%2F2ztWk1V88CEHHvVXSvNVTDWixp9m9La80%3D

Method: N/A, Host: N/A, URL: /MFEwTzBNMEswSTAJBgUrDgMCGgUABBRr2bwARTxMtEy9aspRAZg5QFhagQQUgrrWPZfOn89x6JI3r%2F2ztWk1V88CEHHvVXSvNVTDWixp9m9La80%3D
Full URL: http://ocsp.entrust.net/MFEwTzBNMEswSTAJBgUrDgMCGgUABBRr2bwARTxMtEy9aspRAZg5QFhagQQUgrrWPZfOn89x6JI3r%2F2ztWk1V88CEHHvVXSvNVTDWixp9m9La80%3D
POST Data: N/A

⚠️ WARNING: Unsecured HTTP Traffic Detected -> http://ocsp.entrust.net/MFEwTzBNMEswSTAJBgUrDgMCGgUABBRr2bwARTxMtEy9aspRAZg5QFhagQQUgrrWPZfOn89x6JI3r%2F2ztWk1V88CEHHvVXSvNVTDWixp9m9La80%3D

Method: GET, Host: ocsp.entrust.net, URL: /MFEwTzBNMEswSTAJBgUrDgMCGgUABBRr2bwARTxMtEy9aspRAZg5QFhagQQUgrrWPZfOn89x6JI3r%2F2ztWk1V88CEDWvt3udNB9q%2FI%2BERqsxNSs%3D
Full URL: http://ocsp.entrust.net/MFEwTzBNMEswSTAJBgUrDgMCGgUABBRr2bwARTxMtEy9aspRAZg5QFhagQQUgrrWPZfOn89x6JI3r%2F2ztWk1V88CEDWvt3udNB9q%2FI%2BERqsxNSs%3D
POST Data: N/A

⚠️ WARNING: Unsecured HTTP Traffic Detected -> http://ocsp.entrust.net/MFEwTzBNMEswSTAJBgUrDgMCGgUABBRr2bwARTxMtEy9aspRAZg5QFhagQQUgrrWPZfOn89x6JI3r%2F2ztWk1V88CEDWvt3udNB9q%2FI%2BERqsxNSs%3D

Method: N/A, Host: N/A, URL: /MFEwTzBNMEswSTAJBgUrDgMCGgUABBRr2bwARTxMtEy9aspRAZg5QFhagQQUgrrWPZfOn89x6JI3r%2F2ztWk1V88CEDWvt3udNB9q%2FI%2BERqsxNSs%3D
Full URL: http://ocsp.entrust.net/MFEwTzBNMEswSTAJBgUrDgMCGgUABBRr2bwARTxMtEy9aspRAZg5QFhagQQUgrrWPZfOn89x6JI3r%2F2ztWk1V88CEDWvt3udNB9q%2FI%2BERqsxNSs%3D
POST Data: N/A

⚠️ WARNING: Unsecured HTTP Traffic Detected -> http://ocsp.entrust.net/MFEwTzBNMEswSTAJBgUrDgMCGgUABBRr2bwARTxMtEy9aspRAZg5QFhagQQUgrrWPZfOn89x6JI3r%2F2ztWk1V88CEDWvt3udNB9q%2FI%2BERqsxNSs%3D

Method: GET, Host: ctldl.windowsupdate.com, URL: /msdownload/update/v3/static/trustedr/en/authrootstl.cab?bd0fc98c3f88ee1d
Full URL: http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en/authrootstl.cab?bd0fc98c3f88ee1d
POST Data: N/A

⚠️ WARNING: Unsecured HTTP Traffic Detected -> http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en/authrootstl.cab?bd0fc98c3f88ee1d

Method: N/A, Host: N/A, URL: /msdownload/update/v3/static/trustedr/en/authrootstl.cab?bd0fc98c3f88ee1d
Full URL: http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en/authrootstl.cab?bd0fc98c3f88ee1d
POST Data: N/A

⚠️ WARNING: Unsecured HTTP Traffic Detected -> http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en/authrootstl.cab?bd0fc98c3f88ee1d
