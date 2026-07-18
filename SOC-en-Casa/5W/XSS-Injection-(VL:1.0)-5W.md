# XSS Injection Attack & SIEM Detection — 5W Report (VL:1.0)
**Project:** SOC en Casa  
**Date:** 2026-07-04  
**Author:** Jonás Joya

---

## Summary
This report documents a controlled Cross‑Site Scripting (XSS) simulation executed in the **SOC en Casa** home lab. The objective was to inject a basic XSS payload into DVWA, confirm execution in the browser, and observe Wazuh SIEM detection and log correlation.

> From original report: "A basic XSS payload was injected into the 'DVWA' text box. The browser successfully executed the malicious script, triggering a pop-up message on the screen."  

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
- A basic XSS payload (`<script>alert('XSS')</script>`) was injected into DVWA and executed by the browser, producing a pop-up. The GET request containing the payload was recorded in Apache `access.log` and correlated in Wazuh.  
- **Detection:** Wazuh generated an alert (rule id `31106`) for the observed activity.

### When did the incident occur?
- **Access log timestamp:** `Jun 4, 2026 12:21:06` (web server).  
- **Wazuh alert timestamp:** `Jun 4, 2026 12:21:07.948` (Wazuh Dashboard).  
- **TODO:** confirm timezone normalization (host-local vs UTC) before publishing.

### Where did the incident happen?
- Target web server on Windows VM; Apache access log path: `C:\xampp\apache\logs\access.log`.  
- Wazuh agent IP: **10.0.2.15**.

### Why did the incident happen?
- Controlled simulation to validate detection. DVWA set to **low** and Windows firewall intentionally disabled to ensure traffic reached the server and was logged.

---

## Evidence and detection details
- **Wazuh rule triggered:** `31106`.  
- **Log evidence:** Apache `access.log` contains the GET request with the XSS payload in plain text.  
- **Video demo:** `https://youtu.be/gHAcLL1Mz_0?si=VDwyOYwFgW8pKf0r` (appendix / optional public demo).

---

## Impact, recommendations, and next steps
- **Impact (lab):** Demonstrated client-side script execution and successful SIEM correlation. No real user data involved.  
- **Recommendations:**  
  - Harden web input validation and output encoding.  
  - Ensure Wazuh rules cover common XSS patterns and that log parsing captures full request payloads.  
  - Repeat test with DVWA at higher difficulty and with host firewall enabled to validate detection under constrained conditions.

---

## Appendix
- Access log path: `C:\xampp\apache\logs\access.log`.  
- **TODO:** attach screenshots of access.log and Wazuh alert; confirm timestamps/timezone; optionally embed demo video thumbnail or link.
 
<!-- Prepared for PR: moved from main to soc-en-casa/5w-xss-existing on 2026-07-18 -->
