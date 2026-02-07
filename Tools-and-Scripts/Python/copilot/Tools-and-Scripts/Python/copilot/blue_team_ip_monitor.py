# Copilot Blue Team recontextualization
# Simple anomaly detector using only allowed features

srcIP = input("Source IP: ")
dstPortStr = input("Destination port: ")
protocol = input("Protocol (TCP/UDP/ICMP): ")
connCountStr = input("Connections observed: ")

if dstPortStr == "":
    dstPort = 0
else:
    dstPort = int(float(dstPortStr))

if connCountStr == "":
    connCount = 0
else:
    connCount = int(float(connCountStr))

SuspiciousPortFlag = 0
if dstPort == 22:
    SuspiciousPortFlag = 1
elif dstPort == 3389:
    SuspiciousPortFlag = 1
elif dstPort == 445:
    SuspiciousPortFlag = 1

BlacklistedIPFlag = 0
if srcIP == "198.51.100.23":
    BlacklistedIPFlag = 1
elif srcIP == "203.0.113.5":
    BlacklistedIPFlag = 1

ProtocolAnomaly = 0
if protocol != "TCP" and protocol != "UDP":
    ProtocolAnomaly = 1

BurstFlag = 0
if connCount > 100:
    BurstFlag = 1

AnomalyScore = SuspiciousPortFlag + BlacklistedIPFlag + ProtocolAnomaly + BurstFlag

if AnomalyScore > 0:
    print("ALERT:", AnomalyScore)
else:
    print("OK:", AnomalyScore)
