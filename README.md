Full VAPT Cycle Project

Project Title: Vulnerability Assessment and Penetration Testing

### Objective

The objective of this project is to simulate a real-world penetration testing engagement by performing a complete VAPT cycle. 
This includes identifying vulnerabilities, exploiting them in a controlled environment, analyzing their impact, and providing actionable remediation steps.

### Tools Used

Kali Linux – Primary OS for penetration testing
Metasploit – Exploitation framework
Nikto - Web scanning 
Nmap - Service Enumeration 

### Methodology

### 1.Reconnaissance

* Gathered information about the target system
* Identified IP addresses, open ports, and technologies used
* Tools/Techniques: Nmap, Whois, DNS Enumeration

### 2.Scanning

* Performed vulnerability scanning to identify potential weaknesses
* Conducted both authenticated and unauthenticated scans
* Tools Used: OpenVAS, Nmap

### 3.Exploitation

* Exploited identified vulnerabilities in a controlled environment
* Example: SQL Injection using sqlmap
* Used Metasploit for gaining initial access

### 4.Post-Exploitation

* Checked for privilege escalation
* Extracted sensitive data (if applicable)
* Maintained access and analyzed system impact

### 5.Reporting

* Documented all findings with severity levels
* Included CVSS scores where applicable
* Provided remediation steps for each vulnerability


## 🚨 Key Findings

| Vulnerability            | Severity | Description                                          | Impact                      | Remediation                  |
| ------------------------ | -------- | ---------------------------------------------------- | --------------------------- | ---------------------------- |
| Remote Code Execution    |Critical  | Execution of system commands on server               |Full system compromise       | Validate input, patch system | 
| SQL Injection             | High     | Unsanitized user input in login form                 | Data leakage, DB compromise | Use prepared statements      |
| DOM XSS                  | Medium   | Client-side script injection via unsafe DOM handling | Session hijack, data theft  | Sanitize input, use CSP      |
| Open Ports               | Medium   | Unnecessary services exposed                         | Attack surface increase     | Close unused ports           |

## Conclusion

This project demonstrates a complete VAPT lifecycle, highlighting how vulnerabilities can be discovered, exploited, and mitigated. It emphasizes the importance of proactive security measures and continuous monitoring.

