### **2. Blue Team Markdown**

```markdown
# Blue Team Variant - Incident Response Effort Calculator (Grok)

**Author:** Grok (xAI)  
**Context:** Defensive Security (SOC Analyst / Blue Team)  
**Learning Objective:** Demonstrate conditional logic for automation rules in alert triage using only basic Python features.

### Cybersecurity Context
This script models the manual investigation effort (in hours) required by a SOC analyst.  
"Promotions" represent automation (SOAR playbooks, SIEM rules, or scripts) that resolve some alerts automatically when volume thresholds are reached.

- HighSeverityAlerts = 2.74 hours per alert  
- MediumSeverityAlerts = 1.37 hours per alert  
- LowSeverityAlerts = 0.99 hours per alert  

Automation rules (varied operators used):
- High severity: > 4 alerts → 1 handled automatically  
- Medium severity: >= 6 alerts → 1 handled automatically (varied comparison)  
- Low severity: > 6 alerts OR very high volume → 2 handled automatically (used OR)

```python
# Blue Team: Incident Response Effort Calculator (restricted Python only)
# Demonstrates varied logical and arithmetic operators

HighSeverityAlerts = 2.74
MediumSeverityAlerts = 1.37
LowSeverityAlerts = 0.99

AlertType = input("Enter alert type (HighSeverityAlerts, MediumSeverityAlerts, LowSeverityAlerts): ")

if AlertType == "HighSeverityAlerts":
    ChosenAlert = HighSeverityAlerts
elif AlertType == "MediumSeverityAlerts":
    ChosenAlert = MediumSeverityAlerts
elif AlertType == "LowSeverityAlerts":
    ChosenAlert = LowSeverityAlerts
else:
    ChosenAlert = 0.0
    print("Alert type not recognized")

CountAlerts = input("Enter the quantity of alerts:")
Count = int(CountAlerts)

if ChosenAlert == HighSeverityAlerts and Count > 4:
    TotalEffort = ChosenAlert * (Count - 1)          # varied arithmetic expression
    print(TotalEffort)
elif ChosenAlert == MediumSeverityAlerts and Count >= 6:
    TotalEffort = (ChosenAlert * Count) - (ChosenAlert * 1)
    print(TotalEffort)
elif ChosenAlert == LowSeverityAlerts or Count > 10:   # used OR for broad automation
    TotalEffort = ChosenAlert * (Count - 2)          # varied arithmetic expression
    print(TotalEffort)
else:
    TotalEffort = ChosenAlert * Count
    print(TotalEffort)
