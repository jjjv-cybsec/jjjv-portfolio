# Walk‑Through XSS Injection VL: 1.0
**Project:** SOC en Casa  
**Author:** Jonás Joya  
**Date:** 2026-07-04

---

## SECTION I Home SOC Introduction
The Wazuh Dashboard was displayed on the Ubuntu Host device, introducing the simulated XSS Injection attack within the SOC en Casa laboratory.

---

## SECTION II The Attack
The perspective shifted to the Kali Linux VM, with the browser displaying the DVWA "XSS (Reflected)" page.  
A basic XSS payload, `<script>alert('XSS')</script>`, was injected into the text box. A pop‑up appeared on the screen, proving the browser executed the malicious script.

> **Evidencia textual del documento original:** “A basic XSS payload, `<script>alert('XSS')</script>`, was injected into the text box. Consequently, a pop‑up appeared on the screen, proving that the browser successfully executed the malicious script.”

---

## SECTION III Forensic Evidence
On the victim Windows Server the XAMPP `access.log` was opened. The incoming GET request containing the XSS payload was recorded in plain text by the web server.

---

## SECTION IV Wazuh Detection
A Level 6 security alert triggered in Wazuh by **rule.id = 31106**, confirming detection of the special characters used in the attack. The author created a Wazuh filter to streamline data gathering for the 5W report.

---

## SECTION V Conclusions
Understanding XSS detection is a core SOC skill. Next activity: Command Injection analysis.

---

## Appendix
- **Video demo:** `https://youtu.be/gHAcLL1Mz_0?si=VDwyOYwFgW8pKf0r`  
- **Logs:** `C:\xampp\apache\logs\access.log` (attach sanitized screenshots in PR)
