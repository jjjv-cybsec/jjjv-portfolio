# Walk-Through: SQL Injection Simulation (VL: 1.0)
**Project:** SOC en Casa  
**Date:** 2026-06-21  
**Author:** Jonás Joya

---

## Section I — Lab overview
This walk-through documents the execution and observation of a SQL Injection simulation in the **SOC en Casa** environment. The lab uses three VirtualBox VMs: Kali Linux (attacker), Windows 11 (target with DVWA), and Wazuh manager (SIEM). The Wazuh Dashboard was used to monitor alerts and verify detection.

---

## Section II — Environment setup (brief)
- Host: Ubuntu 24.04.4 LTS running VirtualBox.  
- VMs: Kali (attacker), Windows 11 (DVWA target), Wazuh manager (SIEM).  
- DVWA security level: **low**.  
- Windows firewall: **disabled** for the simulation to ensure traffic reaches the web server.

---

## Section III — The attack (step-by-step)
1. **Attacker (Kali) preparation:** Open browser to DVWA on the Windows target.  
2. **Payload A (simple OR):** Enter `%' OR '1' = '1` into the vulnerable input and submit. The DVWA page returned results (credentials displayed).  
   - **Observation:** Apache `access.log` recorded the payload in plain text. Wazuh did **not** generate an alert for this payload under default rules.
3. **Payload B (UNION SELECT):** Enter `1' UNION SELECT null, concat(user,0x3a,password) FROM users-- -` and submit. The DVWA page displayed concatenated user:password strings.  
   - **Observation:** Apache `access.log` recorded the payload; Wazuh generated a Level 6 alert (rule id `31106`).

---

## Section IV — Forensic evidence
- **Access logs:** `C:\xampp\apache\logs\access.log` contains both payloads in plain text.  
- **Wazuh Dashboard:** shows an alert triggered by the UNION SELECT payload (rule id `31106`). The simpler OR payload was present in logs but not flagged by default Wazuh rules.

---

## Section V — Wazuh detection notes
- **Detected rule:** `31106` — matched the UNION SELECT pattern and raised a Level 6 alert.  
- **Missed detection:** `31103` (or other default rules) did not flag the simple OR payload. This indicates a gap in default signature coverage for basic SQL injection patterns.

---

## Section VI — Conclusions and next steps
- The lab successfully demonstrated the attack lifecycle: injection → server log entry → SIEM detection (for the UNION payload).  
- **Next activities:**  
  - Create custom Wazuh rules to detect simple SQL injection patterns.  
  - Repeat the simulation with DVWA set to higher difficulty and with host firewall enabled to test detection under constrained conditions.  
  - Document Cross-Site Scripting (XSS) and Command Injection simulations using the same workflow.

---

## Appendix
- For exact timestamps, IPs, and rule IDs, see the 5W report: `SOC-en-Casa/5W/SQL-Injection-VL1-5W.md`.  
- **TODO:** attach video link and optional screenshots. Video: `https://youtu.be/BrpuaGWiyas?si=USJe0TpbrBt0oYa8`
