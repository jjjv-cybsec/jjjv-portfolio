# Red Team Exploitation Calculator - Attack Path Scoring

This Python script demonstrates basic conditional logic for a **Red Team** penetration testing scenario. It calculates the "impact value" of exploiting different vulnerability types during a security assessment.

## Scenario Context

A Red Team operator is conducting an authorized penetration test and has identified three types of exploitable vulnerabilities:
- **SQLInjection** - Database access vulnerabilities in web applications
- **RCE_Exploit** - Remote Code Execution flaws in network services
- **PrivEscalation** - Local privilege escalation vulnerabilities

Each vulnerability type has a base value representing how much access/control it provides to the attacker.

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

## Impact Scoring System

Each vulnerability type has a base impact value (1-10 scale):
- **SQLInjection**: 6.5 (Can extract database contents)
- **RCE_Exploit**: 8.0 (Remote command execution)
- **PrivEscalation**: 9.5 (Domain/root access)

### Chaining Bonuses (Privilege Multipliers)

In real penetration tests, exploiting multiple instances of the same vulnerability type creates "lateral movement" opportunities or "privilege escalation paths":

1. **SQLInjection**: If > 3 vulnerable endpoints found → chain 2 exploits for deeper database access (bonus: 2 × 6.5)
2. **RCE_Exploit**: If > 4 vulnerable services found → chain 3 exploits for multi-host control (bonus: 3 × 8.0)
3. **PrivEscalation**: If > 2 vulnerable systems found → chain 1 exploit for domain admin (bonus: 1 × 9.5)

The final score represents the total impact of the attack path after chaining exploits together.

---

## Python Code

```python
#This Python code calculates Red Team attack path impact for penetration testing.
#NOTE: The numerical values represent exploitation impact scores (1-10 scale).
#The base impact value for each vulnerability type is shown below:

SQLInjection = 6.5
RCE_Exploit = 8.0
PrivEscalation = 9.5

VulnType = input("Enter vulnerability type: ")
if VulnType == "SQLInjection":
    ChosenVuln = SQLInjection
elif VulnType == "RCE_Exploit":
    ChosenVuln = RCE_Exploit
elif VulnType == "PrivEscalation":
    ChosenVuln = PrivEscalation
else:
    ChosenVuln = 0.0
    print("Invalid vulnerability type")

#Here are the exploit chaining bonuses:
#Find more than 3 SQLInjection flaws → chain 2 exploits for database pivot.
#Find more than 4 RCE_Exploit flaws → chain 3 exploits for multi-host compromise.
#Find more than 2 PrivEscalation flaws → chain 1 exploit for domain admin access.

CountVulns = input("Enter number of vulnerable targets found: ")
CountVulnsFloat = float(CountVulns)
CountVulnsInt = int(CountVulns)

print("Analyzing " + CountVulns + " vulnerable targets")

if CountVulnsFloat <= 0:
    print("Error: Target count must be greater than zero")
    print(0.0)
elif ChosenVuln == 0.0:
    print("Cannot calculate impact - invalid vulnerability type")
    print(0.0)
elif ChosenVuln == SQLInjection and CountVulnsFloat > 3:
    ChainedImpact = (ChosenVuln * CountVulnsInt) - (SQLInjection * 2)
    print("EXPLOIT CHAIN AVAILABLE: Database pivot through 2 systems")
    print("Total attack path impact: " + str(ChainedImpact))
elif ChosenVuln == RCE_Exploit and CountVulnsFloat > 4:
    ChainedImpact = (ChosenVuln * CountVulnsInt) - (RCE_Exploit * 3)
    print("EXPLOIT CHAIN AVAILABLE: Multi-host compromise via 3 RCE exploits")
    print("Total attack path impact: " + str(ChainedImpact))
elif ChosenVuln == PrivEscalation and CountVulnsFloat > 2:
    ChainedImpact = (ChosenVuln * CountVulnsInt) - (PrivEscalation * 1)
    print("EXPLOIT CHAIN AVAILABLE: Domain admin via privilege escalation")
    print("Total attack path impact: " + str(ChainedImpact))
else:
    SingleExploitImpact = ChosenVuln * CountVulnsInt
    print("Single exploitation - no chaining possible")
    print("Total attack path impact: " + str(SingleExploitImpact))
```

---

## Example Usage

### Test Case 1: SQL Injection Chain Attack
```
Enter vulnerability type: SQLInjection
Enter number of vulnerable targets found: 5
Analyzing 5 vulnerable targets
EXPLOIT CHAIN AVAILABLE: Database pivot through 2 systems
Total attack path impact: 19.5
```

**Explanation:** 5 SQL injection points × 6.5 impact = 32.5 total. Chaining through 2 systems costs 13.0 "effort", leaving net impact of 19.5 for the attack path.

---

### Test Case 2: Limited RCE Findings
```
Enter vulnerability type: RCE_Exploit
Enter number of vulnerable targets found: 3
Analyzing 3 vulnerable targets
Single exploitation - no chaining possible
Total attack path impact: 24.0
```

**Explanation:** Only 3 RCE vulnerabilities found (threshold is > 4), so 3 × 8.0 = 24.0 impact but no chaining bonus available.

---

### Test Case 3: Privilege Escalation to Domain Admin
```
Enter vulnerability type: PrivEscalation
Enter number of vulnerable targets found: 3
Analyzing 3 vulnerable targets
EXPLOIT CHAIN AVAILABLE: Domain admin via privilege escalation
Total attack path impact: 19.0
```

**Explanation:** 3 privilege escalation paths × 9.5 = 28.5 total. Using 1 in the chain (9.5 cost) achieves domain admin, with 19.0 net impact remaining.

---

## Red Team Learning Objectives

This exercise demonstrates:

1. **Attack path planning** - Choosing which vulnerabilities to exploit based on impact
2. **Resource allocation** - Some exploits are "spent" to enable bigger wins (chaining)
3. **Lateral movement concepts** - Using multiple footholds to achieve objectives
4. **Risk vs. reward** - Higher-count findings enable more sophisticated attacks

---

## Real-World Red Team Methodology

In actual penetration tests, this logic mirrors:
- **MITRE ATT&CK tactics** - Initial access → privilege escalation → lateral movement
- **Kill chain analysis** - Multi-stage attack progression
- **Exploit framework decision trees** - Metasploit, Cobalt Strike, Empire
- **Engagement reporting** - Impact scoring for executive summaries

---

## Ethical Context

⚠️ **IMPORTANT:** This code is for **authorized security testing only**. Red Team activities must:
- Have written permission from asset owners
- Follow rules of engagement (scope, timing, methods)
- Operate under legal contracts and NDAs
- Report findings to improve security, not cause harm

Unauthorized hacking is illegal and unethical.

---

## Technical Improvements for Production

Real Red Team tools would include:
- Automated vulnerability scanning integration (Nessus, Burp Suite)
- Exploit payload generation (shellcode, reverse shells)
- C2 (Command & Control) infrastructure
- OPSEC (Operational Security) evasion techniques
- Post-exploitation frameworks

However, those capabilities violate our learning constraints - the goal is understanding fundamental conditional logic for attack decision-making.

---

## Defensive Takeaways

For Blue Team defenders reading this:
- Monitor for **repeated exploit attempts** against the same vulnerability class
- Detect **lateral movement patterns** (multiple systems compromised in sequence)
- Implement **least privilege** to limit privilege escalation impact
- Use **network segmentation** to prevent exploit chaining across environments

Understanding Red Team thinking makes you a better Blue Team defender.

---

**Variant created by:** Claude AI (Anthropic)  
**Original concept by:** jjjv-cybsec  
**Red Team focus:** Offensive security and penetration testing methodology
