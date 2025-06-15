**Quickport** is a Python-based CLI tool that scans a target host for open ports using raw socket connections. 
It’s designed for speed, simplicity, and learning how network connections work at a low level. 
The scanner checks TCP ports within a user-defined range and identifies which are open and accepting connections.

This project demonstrates the fundamentals of socket programming, network security, and multi-threaded scanning, making it a solid utility and an educational tool.

🖥️Tech Stack:
Language:Python 3.x

Library:socket, datetime, threading (optional)

Concepts:TCP/IP protocol, client-server model, socket timeouts, concurrency

✅ Key Features:
🔎 Scans for open TCP ports on a target IP/domain

⚡️ Configurable port range (default: 1–1024)

🕐 Displays time taken for the scan

⚙️ Clean and readable CLI interface

🧵 Optional multithreaded scanning (for faster results)
