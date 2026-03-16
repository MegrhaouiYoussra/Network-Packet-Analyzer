# Network Packet Analyzer

A simple network packet analyzer built in Python using Scapy.  
The tool captures live network traffic and analyzes packet headers to extract useful networking information such as IP addresses, protocols, ports, and packet length.

This project demonstrates fundamental networking concepts and how network packets can be inspected in real time.

---

## Features

- Capture live network traffic
- Analyze IP packets
- Detect TCP, UDP, and ICMP protocols
- Display source and destination IP addresses
- Show source and destination ports
- Display packet length
- Real-time packet monitoring

---

## Technologies Used

- Python
- Scapy
- Networking protocols (TCP/IP)

---

## Project Structure

```
network-packet-analyzer
│
├── packet_analyzer.py
└── README.md
```

---

## Requirements

- Python 3
- Scapy
- Npcap (required on Windows for packet capture)

---

## Installation

Install Scapy:

```
pip install scapy
```

Install Npcap for Windows:

https://npcap.com/#download

Npcap allows Python and Scapy to capture packets from the network interface.

---

## How to Run

Run the analyzer using:

```
python packet_analyzer.py
```

The program will start capturing network packets in real time.

Press **Ctrl + C** to stop the capture.

---

## Example Output

```
Source IP: 192.168.1.15
Destination IP: 142.250.191.78
Protocol: TCP
Source Port: 51432
Destination Port: 443
Packet Length: 60 bytes
```

Example for UDP:

```
Source IP: 192.168.1.15
Destination IP: 8.8.8.8
Protocol: UDP
Source Port: 5353
Destination Port: 53
Packet Length: 74 bytes
```

---

## Purpose of the Project

The goal of this project is to better understand how network communication works by capturing and analyzing packets traveling through the network.

This project helped strengthen knowledge of:

- network packet structure
- TCP/IP protocols
- real-time traffic monitoring
- packet inspection and analysis

---

## Learning Outcomes

Through this project I gained practical experience with:

- network traffic analysis
- packet inspection
- Python networking tools
- real-time data processing

---

## Author

Youssra Meghraoui
