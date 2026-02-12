### **3. Red Team Markdown**

```markdown
# Red Team Variant - Attack Campaign Risk Calculator (Grok)

**Author:** Grok (xAI)  
**Context:** Offensive Security (Red Team)  
**Learning Objective:** Apply basic conditional logic to model risk in offensive operations using varied operators.

### Cybersecurity Context
This script estimates the total risk score of a Red Team campaign.  
"Promotions" represent optimizations (better timing, proxy rotation, batching) that reduce the additional risk of extra actions when volume is high.

- PasswordSpraying = 2.74 risk units  
- SSH_Bruteforce = 1.37 risk units  
- Web_Exploits = 0.99 risk units  

Optimization rules (varied operators):
- PasswordSpraying: > 4 actions → 1 optimized ("free")
- SSH_Bruteforce: >= 6 actions → 1 optimized
- Web_Exploits: > 6 actions → 2 optimized (different arithmetic style)

```python
# Red Team: Attack Campaign Risk Calculator (restricted Python only)
# Shows variety in comparison and arithmetic operators

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
Count = int(CountActions)

if ChosenAttack == PasswordSpraying and Count > 4:
    TotalRisk = (ChosenAttack * Count) - (ChosenAttack * 1)
    print(TotalRisk)
elif ChosenAttack == SSH_Bruteforce and Count >= 6:
    TotalRisk = ChosenAttack * (Count - 1)          # varied arithmetic
    print(TotalRisk)
elif ChosenAttack == Web_Exploits and Count > 6:
    TotalRisk = ChosenAttack * (Count - 2)          # different expression style
    print(TotalRisk)
else:
    TotalRisk = ChosenAttack * Count
    print(TotalRisk)
