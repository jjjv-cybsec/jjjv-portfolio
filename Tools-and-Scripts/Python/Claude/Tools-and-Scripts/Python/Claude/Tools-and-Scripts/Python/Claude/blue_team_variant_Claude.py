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
