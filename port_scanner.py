import socket

user_ip = input("Please enter an IP: ")

port_names = {
    21 : "FTP",
    22 : "SSH",
    23 : "TELNET",
    80 : "HTTP",
    443 : "HTTPS",
    445 : "SMB",
    3389 : "RDP"
    
    }
for port in port_names:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    status = s.connect_ex((user_ip, port))

    if status == 0:
        print(f"{port} IS OPEN. SERVICE: {port_names[port]}")
    else:
        print(f"{port} IS CLOSED. SERVICE: {port_names[port]}")
