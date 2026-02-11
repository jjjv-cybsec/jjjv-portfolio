# Blue Team Network Monitoring - Security Alert Threshold Calculator

This Python script demonstrates basic conditional logic for a **Blue Team** security operations scenario. It calculates alert priorities based on the number of security events detected from different source types.

## Scenario Context

A Security Operations Center (SOC) analyst monitors three types of security events:
- **SuspiciousLogins** - Failed authentication attempts from unusual locations
- **PortScans** - Network reconnaissance activities detected
- **MalwareSignatures** - Known malicious file hashes identified

The system has alert thresholds that trigger escalated responses when certain event counts are exceeded.

---

## Code Constraints

Following the original educational constraints from Python for Everybody (University of Michigan):
- ✅ String (str)
- ✅ Integer (int)
- ✅ Float (floating-point number)
- ✅ Variables
- ✅ Conditional statements (if, elif, else)
- ✅ Arithmetic operators (+, -, *, etc.)
- ❌ No mathematical functions (min, max, sum, etc.)
- ❌ No modules or libraries
- ❌ No other Python capabilities

---

## Alert Priority Scoring System

Each event type has a base severity score:
- **SuspiciousLogins**: 7.5 (High severity)
- **PortScans**: 5.0 (Medium severity)
- **MalwareSignatures**: 9.0 (Critical severity)

### Escalation Rules (Auto-Response Triggers)

When event counts exceed thresholds, automatic mitigation reduces the threat score:

1. **SuspiciousLogins**: If > 10 events detected → Auto-block 3 IPs (reduces score by 3 × 7.5)
2. **PortScans**: If > 15 events detected → Firewall blocks 2 sources (reduces score by 2 × 5.0)
3. **MalwareSignatures**: If > 5 events detected → Quarantine 4 files (reduces score by 4 × 9.0)

The final risk score shows what remains after automated defenses activate.

---

## Python Code

```python
#This Python code calculates security alert priorities for a Blue Team SOC environment.
#NOTE: The numerical values represent threat severity scores (0-10 scale).
#The base severity score for each event type is shown below:

SuspiciousLogins = 7.5
PortScans = 5.0
MalwareSignatures = 9.0

EventType = input("Enter event type: ")
if EventType == "SuspiciousLogins":
    ChosenEvent = SuspiciousLogins
elif EventType == "PortScans":
    ChosenEvent = PortScans
elif EventType == "MalwareSignatures":
    ChosenEvent = MalwareSignatures
else:
    ChosenEvent = 0.0
    print("Invalid event type")

#Here are the auto-response escalation thresholds:
#Detect more than 10 SuspiciousLogins → block 3 IPs automatically.
#Detect more than 15 PortScans → firewall blocks 2 sources automatically.
#Detect more than 5 MalwareSignatures → quarantine 4 files automatically.

CountEvents = input("Enter the number of events detected: ")
CountEventsFloat = float(CountEvents)
CountEventsInt = int(CountEvents)

print("Processing " + CountEvents + " events")

if CountEventsFloat <= 0:
    print("Error: Event count must be greater than zero")
    print(0.0)
elif ChosenEvent == 0.0:
    print("Cannot calculate risk - invalid event type")
    print(0.0)
elif ChosenEvent == SuspiciousLogins and CountEventsFloat > 10:
    RiskScoreAfterMitigation = (ChosenEvent * CountEventsInt) - (SuspiciousLogins * 3)
    print("AUTO-RESPONSE TRIGGERED: 3 IPs blocked")
    print("Remaining risk score: " + str(RiskScoreAfterMitigation))
elif ChosenEvent == PortScans and CountEventsFloat > 15:
    RiskScoreAfterMitigation = (ChosenEvent * CountEventsInt) - (PortScans * 2)
    print("AUTO-RESPONSE TRIGGERED: Firewall blocked 2 sources")
    print("Remaining risk score: " + str(RiskScoreAfterMitigation))
elif ChosenEvent == MalwareSignatures and CountEventsFloat > 5:
    RiskScoreAfterMitigation = (ChosenEvent * CountEventsInt) - (MalwareSignatures * 4)
    print("AUTO-RESPONSE TRIGGERED: 4 malware samples quarantined")
    print("Remaining risk score: " + str(RiskScoreAfterMitigation))
else:
    TotalRiskScore = ChosenEvent * CountEventsInt
    print("Standard monitoring - no auto-response needed")
    print("Total risk score: " + str(TotalRiskScore))
```

---

## Example Usage

### Test Case 1: High Volume Suspicious Logins
```
Enter event type: SuspiciousLogins
Enter the number of events detected: 12
Processing 12 events
AUTO-RESPONSE TRIGGERED: 3 IPs blocked
Remaining risk score: 67.5
```

**Explanation:** 12 login attempts × 7.5 severity = 90.0 total risk. Auto-blocking 3 IPs reduces by 22.5, leaving 67.5 residual risk for analyst review.

---

### Test Case 2: Below Threshold Port Scans
```
Enter event type: PortScans
Enter the number of events detected: 8
Processing 8 events
Standard monitoring - no auto-response needed
Total risk score: 40.0
```

**Explanation:** 8 scans × 5.0 severity = 40.0 risk. Below the 15-event threshold, so no automatic firewall rules deployed.

---

### Test Case 3: Critical Malware Detection
```
Enter event type: MalwareSignatures
Enter the number of events detected: 7
Processing 7 events
AUTO-RESPONSE TRIGGERED: 4 malware samples quarantined
Remaining risk score: 27.0
```

**Explanation:** 7 malware detections × 9.0 severity = 63.0 total risk. Quarantining 4 samples removes 36.0 risk, leaving 27.0 for forensic analysis.

---

## Blue Team Learning Objectives

This exercise demonstrates:

1. **Threshold-based automation** - Common in SIEM and SOAR platforms
2. **Event correlation** - Different event types have different severity weights
3. **Defensive prioritization** - Auto-responses reduce analyst workload on high-volume incidents
4. **Risk scoring** - Quantifying threats helps prioritize limited security resources

---

## Real-World Applications

In actual Blue Team operations, this logic appears in:
- **SIEM alert rules** (Splunk, QRadar, Sentinel)
- **IDS/IPS signatures** (Snort, Suricata)
- **EDR response playbooks** (CrowdStrike, SentinelOne)
- **WAF auto-blocking** (Cloudflare, AWS WAF)

---

## Improvements for Production

This educational code could be enhanced with:
- Database logging of events
- API integration with threat intelligence feeds
- Machine learning for anomaly detection
- Automated incident ticket creation
- Compliance reporting (NIST, ISO 27001)

However, those enhancements would violate our learning constraints - the goal is understanding fundamental conditional logic for security decision-making.

---

**Variant created by:** Claude AI (Anthropic)  
**Original concept by:** jjjv-cybsec  
**Blue Team focus:** Defensive security operations and incident response
