# SQL Injection Attack & SIEM Detection — 5W Report (VL: 1.0)
**Project:** SOC en Casa  
**Date:** 2026-06-21  
**Author:** Jonás Joya

---

## Summary
This report documents a controlled SQL Injection simulation executed in the **SOC en Casa** home lab. The objective was to run two SQL injection payloads against a DVWA instance hosted on a Windows target and observe detection events in the Wazuh SIEM. The environment consisted of three VMs (Kali attacker, Windows target with DVWA, and Wazuh manager) running on an Ubuntu host with VirtualBox.

---

## Tools and environment
- Host: **Ubuntu 24.04.4 LTS** (Laptop host)  
- Virtualization: **Oracle VirtualBox 7.2.4**  
- Attacker VM: **Kali Linux (Kali-linux-2025.3)** — source IP: `192.168.56.11`  
- Target VM: **Windows 11 (Win11_Target-v2)** — agent IP recorded: `10.0.2.15`  
- SIEM / Manager: **Wazuh v4.14.1** (OVA)  
- Web app: **DVWA** (security level: *low*)  
- Logs inspected: `C:\xampp\apache\logs\access.log` (Windows target)

---

## The 5 W's

### Who caused the incident?
- The incident was simulated by the author using the Kali Linux attacker VM (source IP: **192.168.56.11**).

### What happened?
- Two SQL injection payloads were executed against the DVWA application:
  1. **Payload A (simple OR):** `%' OR '1' = '1` — this payload reached the server and was recorded in `access.log` but **did not** trigger Wazuh default rules.
  2. **Payload B (UNION SELECT):** `1' UNION SELECT null, concat(user,0x3a,password) FROM users-- -` — this payload reached the server, extracted credentials, and **triggered** a Wazuh alert.
- The second payload produced a Level 6 alert in Wazuh (rule id observed).

### When did the incident occur?
- **Payload A timestamp:** `Jun 21, 2026 23:23:09` (recorded in access.log).  
- **Payload B timestamp:** `Jun 21, 2026 23:23:19` (recorded in access.log).  
- **Wazuh alert logged at:** `Jun 21, 2026 23:23:20.999` (Wazuh Dashboard).  
- **TODO:** confirm timezone normalization for published timestamps (these are host-local times; convert to UTC if you want global consistency).

### Where did the incident happen?
- The attack targeted the DVWA web application on the Windows VM.  
- Apache access log path: `C:\xampp\apache\logs\access.log`.  
- Wazuh agent IP for the Windows target: **10.0.2.15**.

### Why did the incident happen?
- This was a **controlled simulation** to validate detection coverage in Wazuh.  
- Contributing factors intentionally set for the lab:
  - DVWA security level set to **low**.
  - Windows firewall on the target was **disabled** to ensure traffic reached the web server.
- The first payload bypassed default Wazuh rules due to its simple form; the second, more explicit UNION payload matched Wazuh signatures and triggered detection.

---

## Detection details
- **Wazuh rule IDs observed:** `31103` (no alert for payload A) and `31106` (alert for payload B).  
- **Alert level observed:** Level 6 for the UNION SELECT detection.  
- **Evidence:** Apache `access.log` contains both payloads in plain text; Wazuh Dashboard shows the alert for payload B.

---

## Impact and notes
- **Impact (lab):** Credentials were exposed in the DVWA output (simulated data). No real user data was involved.  
- **Operational note:** Default Wazuh rules may miss simple SQL injection patterns; consider tuning rules or adding custom detection for basic payloads.

---

## Recommendations
1. **Rule tuning:** Add or tune Wazuh rules to detect simple SQL injection patterns (e.g., common OR-based payloads).  
2. **Log forwarding:** Ensure Apache logs are fully ingested and parsed by Wazuh to increase detection coverage.  
3. **Harden DVWA/targets:** For production-like testing, enable host firewall and increase DVWA difficulty to test detection under more realistic conditions.

---

## Appendix / Evidence references
- Access log path: `C:\xampp\apache\logs\access.log` (contains both payloads).  
- Wazuh alert example: rule id `31106` (UNION SELECT detection).  
- **TODO:** attach or link screenshots of access.log and Wazuh alert. 
