# Command Injection Attack & SIEM Detection — 5W Report (VL:1.0)
**Project:** SOC en Casa  
**Date:** 2026-07-07  
**Author:** Jonás Joya

---

## Summary
This report documents a controlled Command Injection simulation executed in the **SOC en Casa** home lab. The objective was to execute command injection payloads (GET and POST) against DVWA, confirm command execution on the target, and validate Wazuh SIEM detection via a custom rule.

> From original report: "A dual-action Command Injection attack was performed. First, the crafted URL ... was executed to force a GET request. Then, the payload ... was submitted via the DVWA text box. In consequence, the server executed the command and revealed the current system user."

---

## Tools and environment
- **Host:** Ubuntu 24.04.4 LTS (Laptop host)  
- **Virtualization:** Oracle VirtualBox 7.2.4  
- **Attacker VM:** Kali Linux (source IP: `192.168.56.11`)  
- **Target VM:** Windows 11 (Win11_Target-v2) — agent IP: `10.0.2.15`  
- **SIEM / Manager:** Wazuh v4.14.1 (OVA)  
- **Web app:** DVWA (security level: *low*)  
- **Logs inspected:** `C:\xampp\apache\logs\access.log`

---

## The 5 W's

### Who caused the incident?
- Simulated by the author using the Kali Linux attacker VM (source IP **192.168.56.11**).

### What happened?
- **Step 1 (GET):** A crafted URL containing `& whoami` was executed to force command execution via a GET request.  
- **Step 2 (POST):** The payload `192.168.56.12 & whoami` was submitted via the DVWA text box; the server executed the command and returned the system user.  
- Both actions were recorded in Apache `access.log` and correlated by Wazuh using a custom detection rule.

### When did the incident occur?
- **GET alert (Wazuh Dashboard):** `Jul 7, 2026 09:39:45.543` (dashboard).  
- **GET raw log timestamp:** `Jul 7, 2026 09:39:44` (access.log).  
- **POST alert (Wazuh Dashboard):** `Jul 7, 2026 09:40:01.863` (dashboard).  
- **POST raw log timestamp:** `Jul 7, 2026 09:39:57` (access.log).  
- **TODO:** verify and normalize timestamps (host timezone vs UTC) before publishing.

### Where did the incident happen?
- Target web server on Windows VM; Apache access log path: `C:\xampp\apache\logs\access.log`.  
- Wazuh agent IP: **10.0.2.15**.

### Why did the incident happen?
- Controlled simulation to validate detection. DVWA set to **low** and Windows firewall intentionally disabled to ensure traffic reached the server and was logged.

---

## Detection details
- **Custom Wazuh rule used:** `rule.id = 100011` (engineered for this simulation).  
- **Evidence:** Apache `access.log` contains both GET and POST payloads in plain text; Wazuh Dashboard shows correlated alerts for both actions.

---

## Impact, recommendations, and next steps
- **Impact (lab):** Command execution confirmed; demonstrates need for strict input validation and monitoring.  
- **Recommendations:**  
  - Harden web application input handling and disable dangerous system calls.  
  - Maintain and test custom Wazuh rules; ensure rule coverage for both GET and POST injection vectors.  
  - Repeat tests with increased DVWA difficulty and host firewall enabled to validate detection under realistic constraints.

---

## Appendix
- Access log path: `C:\xampp\apache\logs\access.log`.  
- **Video demo:** `https://youtu.be/AAWvh8Z2OBc?si=COwakovJyxjwvwvv` (appendix / optional demo).  
- **TODO:** attach screenshots of access.log and Wazuh alerts; confirm timestamps/timezone; include raw log excerpts if you want to publish them.
