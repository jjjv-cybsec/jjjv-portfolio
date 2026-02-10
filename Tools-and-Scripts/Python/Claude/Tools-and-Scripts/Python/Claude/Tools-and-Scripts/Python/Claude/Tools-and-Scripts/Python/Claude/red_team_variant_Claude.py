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
