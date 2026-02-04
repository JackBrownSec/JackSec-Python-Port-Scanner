# JackSec-Python-Port-Scanner
JackSec-Python-Port-Scanner is a beginner friendly Python project that demonstrates how TCP port scanning works using sockets and multithreading. Created for learning networking and cybersecurity fundamentals.


The scanner follows these steps:

Domain Resolution
The user provides a target domain (for example, google.com). The program resolves this domain into an IP address using DNS via Python’s socket.gethostbyname() function.

Port Scanning via TCP Connections
Each port is scanned using a TCP socket. The scanner attempts to connect to the target IP and port using socket.connect_ex().
The return value from this function indicates the state of the port:

Open: A successful connection was made.

Closed: The target actively refused the connection.

Filtered: The connection timed out or was blocked by a firewall.

Multithreading for Speed
To improve performance, JackSec uses Python’s ThreadPoolExecutor to scan multiple ports simultaneously. This allows the scanner to test thousands of ports much faster than scanning them one by one.

Result Classification
Based on the response code returned by the socket connection, the tool classifies each port as open, closed, or filtered and prints the result to the terminal in real time.

This project focuses on understanding the mechanics of network scanning, not bypassing security. It does not exploit vulnerabilities or attempt unauthorized access.
