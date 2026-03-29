# 🔎 Python Port Scanner

A simple Python-based port scanner that checks common ports on a target IP address and identifies whether they are open or closed.

---

## 📌 Overview

This project uses Python’s built-in `socket` library to attempt TCP connections to a set of well-known ports.  
It helps you understand how basic network scanning works and builds a foundation for cybersecurity tasks like enumeration and reconnaissance.

---

## ⚙️ Features

- Scans multiple common ports
- Identifies open and closed ports
- Maps ports to known services
- Uses timeout to speed up scanning
- Simple and readable code

---

## 🧠 Ports and Services

The scanner checks the following ports:

| Port | Service |
|------|--------|
| 21   | FTP    |
| 22   | SSH    |
| 23   | TELNET |
| 80   | HTTP   |
| 443  | HTTPS  |
| 445  | SMB    |
| 3389 | RDP    |

---

## 🛠️ How It Works

- You enter a target IP address
- The script loops through predefined ports
- For each port:
  - A socket is created
  - A connection attempt is made using `connect_ex()`
  - If the result is `0`, the port is open
  - Otherwise, the port is closed
- The result is printed with the service name

---

## ▶️ Usage

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/port-scanner.git
cd port-scanner
