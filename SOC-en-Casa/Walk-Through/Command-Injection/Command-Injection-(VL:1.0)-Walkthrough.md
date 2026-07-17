# Walk‑Through Command Injection VL: 1.0
**Project:** SOC en Casa  
**Author:** Jonás Joya  
**Date:** 2026-07-07

---

## SECTION I Home SOC Introduction
The Wazuh Dashboard on the Ubuntu Host introduced a simulated Command Injection attack and its detection via a custom Wazuh rule.

---

## SECTION II The Attack
First, the crafted URL `http://192.168.56.12/dvwa/vulnerabilities/exec/?ip=192.168.56.12+%26+whoami&Submit=Submit` was used to force a GET request.  
Second, the payload `192.168.56.12 & whoami` was submitted via the DVWA text box. The page displayed the executed command output revealing the current system user.

> **Evidencia textual del documento original:** “First, the crafted URL ... was pasted into the DVWA server browser to force a GET request. Second, the payload ‘192.168.56.12 & whoami’ was typed directly into the DVWA text box. Consequently, the bottom of the page displayed the output of the executed command, revealing the current system user.”

---

## SECTION III Forensic Evidence
On the Windows Server the XAMPP `access.log` recorded the GET request with the injected command and the POST payload in plain text.

---

## SECTION IV Wazuh Detection
A Level 7 security alert triggered in Wazuh by **rule.id = 100011**, confirming the custom SIEM rule detected the command injection.

---

## SECTION V Conclusions
Detecting command injection and authoring custom SIEM rules are essential SOC competencies.

---

## Appendix
- **Video demo:** `https://youtu.be/AAWvh8Z2OBc?si=COwakovJyxjwvwvv`  
- **Logs:** `C:\xampp\apache\logs\access.log` (attach sanitized screenshots in PR)

