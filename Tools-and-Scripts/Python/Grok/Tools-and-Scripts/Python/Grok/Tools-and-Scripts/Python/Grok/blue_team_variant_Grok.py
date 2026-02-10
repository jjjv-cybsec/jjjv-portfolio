# Blue Team Variant - Incident Response Effort Calculator (Grok)

**Blue Team Context:**
This code simulates the calculation of the **manual effort** (in hours) required by an analyst to investigate security alerts. The "promotions" represent automation rules (scripts, SOAR playbooks, or SIEM filters) that automatically resolve some alerts when the volume is high.

- **HighSeverityAlerts** = 2.74 hours per alert
- **MediumSeverityAlerts** = 1.37 hours
- **LowSeverityAlerts** = 0.99 hours

**Promotions (automation):**
- More than 4 High alerts → 1 is automatically resolved
- More than 5 Medium alerts → 1 is automatically resolved
- More than 6 Low alerts → 2 are automatically resolved

```python
# Blue Team: Incident Response Effort Calculator (restricted Python)
# Only uses: str, int, float, variables, if/elif/else, arithmetic operators

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
Count = float(CountAlerts)

if ChosenAlert == HighSeverityAlerts and Count > 4:
    TotalEffort = (ChosenAlert * Count) - (HighSeverityAlerts * 1)
    print(TotalEffort)
elif ChosenAlert == MediumSeverityAlerts and Count > 5:
    TotalEffort = (ChosenAlert * Count) - (MediumSeverityAlerts * 1)
    print(TotalEffort)
elif ChosenAlert == LowSeverityAlerts and Count > 6:
    TotalEffort = (ChosenAlert * Count) - (LowSeverityAlerts * 2)
    print(TotalEffort)
else:
    TotalEffort = ChosenAlert * Count
    print(TotalEffort)
