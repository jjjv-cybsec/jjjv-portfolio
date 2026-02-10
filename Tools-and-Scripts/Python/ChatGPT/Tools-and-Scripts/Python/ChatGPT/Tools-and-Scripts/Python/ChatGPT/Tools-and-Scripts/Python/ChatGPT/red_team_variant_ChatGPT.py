# Recontextualization – Red Team Cybersecurity Scenario

## Scenario
This version simulates a **Red Team attack planning model**.

Instead of selling products:
- We model **attack techniques**
- We calculate **attack cost**
- We apply **efficiency bonuses**

The original structure and constraints are preserved.

---

## Concept Mapping

| Original Concept | Red Team Equivalent |
|-----------------|---------------------|
| Fruit Name | Attack Technique |
| Fruit Price | Resource Cost |
| Quantity | Number of Attempts |
| Free Items | Efficiency Gain |

---

## Recontextualized Code (Red Team)

```python
# Attack cost per attempt
BruteForce = 2.5
PhishingCampaign = 1.8
PortScanning = 0.9

AttackType = input("Enter attack technique: ")

if AttackType == "BruteForce":
    AttackCost = float(BruteForce)
elif AttackType == "Phishing":
    AttackCost = float(PhishingCampaign)
elif AttackType == "PortScan":
    AttackCost = float(PortScanning)

Attempts = input("Enter number of attempts:")
print(float(Attempts))

# Efficiency rules
# BruteForce > 4 attempts → 1 free attempt
# Phishing > 5 attempts → 1 free attempt
# PortScan > 6 attempts → 2 free attempts

if AttackCost == float(BruteForce) and float(Attempts) > 4:
    TotalCost = (AttackCost * int(Attempts)) - (BruteForce * 1)
    print(TotalCost)
elif AttackCost == float(PhishingCampaign) and float(Attempts) > 5:
    TotalCost = (AttackCost * int(Attempts)) - (PhishingCampaign * 1)
    print(TotalCost)
elif AttackCost == float(PortScanning) and float(Attempts) > 6:
    TotalCost = (AttackCost * int(Attempts)) - (PortScanning * 2)
    print(TotalCost)
else:
    TotalCost = AttackCost * int(Attempts)
    print(TotalCost)

---

# Red Team Value

This exercise models:
- Cost-efficiency trade-offs.
- Resource planning.
- Attack optimization logic.

Using only foundational Python skills, reinforcing algorithmic thinking critical for offensive security.
