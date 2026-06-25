# Asset Discovery & Intelligence

## Overview

This project is a simple Asset Discovery & Intelligence framework developed in Python. It automates the identification and analysis of web applications, APIs, endpoints, technologies, and domain information.

The project consists of four modules:

1. Web Application & API Discovery
2. Endpoint Mapping & Fingerprinting
3. Asset Classification Engine
4. Asset Enrichment Module

---

## Features

### Web Application & API Discovery

* Accepts a target URL from the user.
* Connects to the target website.
* Extracts links from the HTML source.
* Identifies potential API-related endpoints.

### Endpoint Mapping & Fingerprinting

* Retrieves HTTP response information.
* Detects server technologies.
* Displays HTTP headers and response metadata.

### Asset Classification Engine

* Categorizes assets based on naming patterns.
* Identifies APIs, Admin Portals, and Web Applications.

### Asset Enrichment Module

* Performs WHOIS lookups.
* Resolves IP addresses.
* Retrieves ownership and infrastructure information.
* Generates basic risk metadata.

---

## Requirements

Install the required dependencies:

```bash
pip install requests beautifulsoup4 python-whois dnspython
```

---

## Usage

### 1. Web Application & API Discovery

Run:

```bash
python discovery.py
```

Example:

```text
Enter URL (https://example.com): https://example.com
```

Output:

```text
[+] Web Application Found
[+] API Endpoint: /api/login
```

---

### 2. Endpoint Mapping & Fingerprinting

Run:

```bash
python fingerprint.py
```

Example:

```text
Enter URL (https://example.com): https://example.com
```

Output:

```text
Status Code: 200
Server: nginx
Technology: PHP
```

---

### 3. Asset Classification Engine

Run:

```bash
python classification.py
```

Example:

```text
Enter Asset (URL/Domain): api.example.com
```

Output:

```text
Category: API
```

---

### 4. Asset Enrichment Module

Run:

```bash
python enrichment.py
```

Example:

```text
Enter URL: https://example.com
```

Output:

```text
Domain: example.com
Owner: Example Registrar
IP Address: 93.184.216.34
Risk: Low
```

---

## Deliverables Mapping

| Deliverable                                                                   | Module            |
| ----------------------------------------------------------------------------- | ----------------- |
| Web Application & API Discovery                                               | discovery.py      |
| Endpoint Mapping & Fingerprinting                                             | fingerprint.py    |
| Asset Classification Engine                                                   | classification.py |
| Asset Enrichment with Ownership, Infrastructure, Technology and Risk Metadata | enrichment.py     |

---

## Limitations

* Basic technology fingerprinting using HTTP headers.
* Limited endpoint discovery from static HTML.
* Risk scoring is rule-based and simplified.
* WHOIS data availability depends on domain registrar support.

---

## Future Enhancements

* Subdomain discovery integration.
* JavaScript endpoint extraction.
* DNS record enumeration.
* Technology detection using Wappalyzer.
* Risk scoring based on security headers and exposure.

---

## Disclaimer

This project is intended for educational purposes and authorized security assessments only. Ensure that you have permission before scanning or analyzing any external systems.
