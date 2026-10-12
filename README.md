
# OSINT Domain Information Scanner

## About
A beginner-friendly Python tool for collecting
publicly available domain information.

## Features
- WHOIS registration information
- Domain creation, update and expiry dates
- IPv4 and IPv6 address resolution
- DNS A, AAAA, MX, NS, TXT and CAA records
- Approximate IP geolocation

## Requirements
- Python 3
- python-whois
- dnspython
- requests

## Installation
```bash
python3 -m venv venv
source venv/bin/activate
pip install python-whois dnspython requests
```

## Usage
```bash
python3 osint_scanner.py
```

Enter a domain when prompted, for example:
`example.com`

## Limitations
Results may be incomplete due to WHOIS privacy,
DNS configuration, or API availability.
Geolocation is approximate.

## Responsible Use
Use this tool for authorized learning and
legitimate information gathering.
