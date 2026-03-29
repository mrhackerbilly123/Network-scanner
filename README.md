# 🔎 Python Port Scanner

A simple Python-based port scanner that checks common ports on a target IP address and identifies whether they are open or closed.

---

## 📌 Overview

This project uses Python’s built-in `socket` library to attempt TCP connections to well-known ports.  
You use this to learn how network scanning works and build real cybersecurity skills.

---

## ⚙️ Features

- Scan common ports quickly
- Detect open and closed ports
- Map ports to known services
- Use timeouts for faster results
- Clean and readable code

---

## 🧠 Ports and Services

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

- You enter a target IP
- The script loops through each port
- A TCP connection attempt is made using `connect_ex()`
- Result:
  - `0` → Port is open
  - Other → Port is closed
- Output shows port status and service name

---

## ▶️ Usage

### 1. Clone the repository
```bash
git clone https://github.com/mrhackerbilly123/port-scanner.git
cd port-scanner
