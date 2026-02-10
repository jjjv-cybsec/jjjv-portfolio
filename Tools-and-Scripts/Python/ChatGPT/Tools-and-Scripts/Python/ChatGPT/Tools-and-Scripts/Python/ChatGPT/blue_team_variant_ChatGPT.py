# Recontextualization – Blue Team Cybersecurity Scenario

## Scenario
This algorithm is recontextualized to simulate a **SOC analyst alert-handling scenario**.

Instead of fruits and promotions:
- We process **security alerts**
- We apply **escalation rules**
- We calculate **final alert severity**

The structure and constraints of the original code remain unchanged.

---

## Concept Mapping

| Original Concept | Blue Team Equivalent |
|-----------------|----------------------|
| Fruit Name | Alert Type |
| Fruit Price | Base Severity Score |
| Quantity | Number of Alert Occurrences |
| Free Items | Severity Reduction (False Positives) |

---

## Recontextualized Code (Blue Team)

```python
# Base severity scores
MalwareAlert = 7.5
PhishingAlert = 5.0
PortScanAlert = 3.0

AlertType = input("Enter alert type: ")

if AlertType == "Malware":
    BaseSeverity = float(MalwareAlert)
elif AlertType == "Phishing":
    BaseSeverity = float(PhishingAlert)
elif AlertType == "PortScan":
    BaseSeverity = float(PortScanAlert)

AlertCount = input("Enter number of alert occurrences:")
print(float(AlertCount))

# Escalation rules
# Malware > 4 alerts → reduce severity by 1 (false positive correlation)
# Phishing > 5 alerts → reduce severity by 1
# PortScan > 6 alerts → reduce severity by 2

if BaseSeverity == float(MalwareAlert) and float(AlertCount) > 4:
    FinalSeverity = (BaseSeverity * int(AlertCount)) - (MalwareAlert * 1)
    print(FinalSeverity)
elif BaseSeverity == float(PhishingAlert) and float(AlertCount) > 5:
    FinalSeverity = (BaseSeverity * int(AlertCount)) - (PhishingAlert * 1)
    print(FinalSeverity)
elif BaseSeverity == float(PortScanAlert) and float(AlertCount) > 6:
    FinalSeverity = (BaseSeverity * int(AlertCount)) - (PortScanAlert * 2)
    print(FinalSeverity)
else:
    FinalSeverity = BaseSeverity * int(AlertCount)
    print(FinalSeverity)
