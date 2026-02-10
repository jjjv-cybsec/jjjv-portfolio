# Red Team Variant - Risk Calculator for Offensive Campaigns (Grok)

**Red Team Context:**
This code simulates the **cumulative risk** (or exposure) of an attack campaign. The "promotions" represent technical optimizations (better timing, proxy rotation, batching, etc.) that allow some additional actions to have a lower detection cost when the volume is high.

- **PasswordSpraying** = 2.74 risk units
- **SSH_Bruteforce** = 1.37 risk units
- **Web_Exploits** = 0.99 risk units

**Promotions (offensive optimization):**
- More than 4 PasswordSpraying attacks → 1 "free" action (lower detection cost)
- More than 5 SSH_Bruteforce attacks → 1 "free" action
- More than 6 Web_Exploits → 2 "free" actions

```python
# Red Team: Attack Campaign Risk Calculator (restricted Python)
# Only uses: str, int, float, variables, if/elif/else, arithmetic operators

PasswordSpraying = 2.74
SSH_Bruteforce = 1.37
Web_Exploits = 0.99

AttackType = input("Enter attack type (PasswordSpraying, SSH_Bruteforce, Web_Exploits): ")

if AttackType == "PasswordSpraying":
    ChosenAttack = PasswordSpraying
elif AttackType == "SSH_Bruteforce":
    ChosenAttack = SSH_Bruteforce
elif AttackType == "Web_Exploits":
    ChosenAttack = Web_Exploits
else:
    ChosenAttack = 0.0
    print("Attack type not recognized")

CountActions = input("Enter the quantity of actions:")
Count = float(CountActions)

if ChosenAttack == PasswordSpraying and Count > 4:
    TotalRisk = (ChosenAttack * Count) - (PasswordSpraying * 1)
    print(TotalRisk)
elif ChosenAttack == SSH_Bruteforce and Count > 5:
    TotalRisk = (ChosenAttack * Count) - (SSH_Bruteforce * 1)
    print(TotalRisk)
elif ChosenAttack == Web_Exploits and Count > 6:
    TotalRisk = (ChosenAttack * Count) - (Web_Exploits * 2)
    print(TotalRisk)
else:
    TotalRisk = ChosenAttack * Count
    print(TotalRisk)
