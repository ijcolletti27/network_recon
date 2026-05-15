# Network Reconnaissance Tool

This program performs basic network reconnaissance inside a terminal. It takes a host and a range of TCP ports and determines which ports are open/listening. The tool utilizes concurrent scans to speed up operations on large ranges.

## How to Deploy

### 1. Native Execution

#### Get the code

```bash
git clone https://github.com/ijcolletti27/network_recon.git
cd network_recon
```

#### Run the program

```bash
python main.py
```

#### Enter target host (either hostname or IPv4 address) and port range

```text
Enter target host: google.com
Enter starting port: 0
Enter ending port: 1024
```

#### Example Output

```text
=== Network recon tool ===

Enter target host: google.com
Enter starting port: 0
Enter ending port: 1024

Scan in progress...

=== Scan Complete in 11.089 seconds ===

Type 1 to only show open ports, 2 to show all scan results: 1

Port: 80 | Open: True
Port: 443 | Open: True
```

---

### 2. Using Docker

#### Get the code

```bash
git clone https://github.com/ijcolletti27/network_recon.git
cd network_recon
```

#### Build Docker image

```bash
docker build -t network_recon .
```

#### Run container

```bash
docker run --rm -it network_recon
```

#### Example Docker Scan

```text
=== Network recon tool ===

Enter target host: 127.0.0.1
Enter starting port: 0
Enter ending port: 65535

Scan in progress...

=== Scan Complete in 4.318 seconds ===

Type 1 to only show open ports, 2 to show all scan results: 1

Port: 33670 | Open: True
Port: 35686 | Open: True
```

## Limitations

- TCP only
- IPv4 only
- Large remote scans may require multiple KeyboardInterrupts due to Python thread cleanup behavior
- Large remote scans may take a very long time to complete, even with concurrent scans
  - Example: scan from ports 0 to 10000 on hostname `google.com` took 100.540 seconds
- Limited functionality: only displays whether ports are listening