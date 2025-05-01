# packet-Sniffing-
a packet sniffer where you can know the the capturing the packets and how the data moves on network 
📘 Synopsis:
This project demonstrates how to build a simple network packet sniffer using Python and the Scapy library in a Kali Linux environment. The packet sniffer captures live packets from the network interface, analyzes them, and displays key details such as protocol types, IP addresses, ports, and DNS queries. This project helps beginners understand how network communication works at the packet level and lays the foundation for more advanced cybersecurity tools like intrusion detection systems (IDS) or traffic analyzers.

🎯 Objective:
To capture and analyze live network traffic using Python, providing visibility into how data is transmitted across the network.

⚙️ Tools and Technologies:
Operating System: Kali Linux

Programming Language: Python 3
Library Used: Scapy

Privileges Required: Root access (for packet capturing)

🔧 Steps You Followed:
✅ 1. Install Required Tools
Ensure Python 3 and Scapy are installed:sudo apt update
sudo apt install python3 python3-pip
pip3 install scapy

✅ 2. Create the Sniffer Script
Filename: sniffer.py

python
✅ 3. Run the Sniffer with Root Privileges
bash

sudo python3 sniffer.py

🧪 Testing Tips:
Open a browser or run ping google.com while sniffing to generate traffic.

Capture a few packets and then analyze them using Wireshark.


📚 What You Learned:
Basics of Scapy and packet sniffing

Common network protocols: IP, TCP, UDP, DNS

How to run Python scripts with root permissions in Kali

How to save and inspect captured packets using Wireshark
