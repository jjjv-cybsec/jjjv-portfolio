# Copilot Red Team recontextualization
# Synthetic event generator (safe, non-malicious)

srcIP1 = "198.51.100.23"
dstPort1 = 445
protocol1 = "TCP"
count1 = 60

srcIP2 = "198.51.100.23"
dstPort2 = 80
protocol2 = "TCP"
count2 = 200

srcIP3 = "203.0.113.5"
dstPort3 = 3389
protocol3 = "TCP"
count3 = 8

score1 = 0
if dstPort1 == 445:
    score1 = score1 + 2
if count1 > 50:
    score1 = score1 + 1

score2 = 0
if dstPort2 == 445:
    score2 = score2 + 2
if count2 > 150:
    score2 = score2 + 2

score3 = 0
if dstPort3 == 3389:
    score3 = score3 + 2
if count3 > 50:
    score3 = score3 + 1

print("EVENT1:", srcIP1, dstPort1, protocol1, count1, score1)
print("EVENT2:", srcIP2, dstPort2, protocol2, count2, score2)
print("EVENT3:", srcIP3, dstPort3, protocol3, count3, score3)
