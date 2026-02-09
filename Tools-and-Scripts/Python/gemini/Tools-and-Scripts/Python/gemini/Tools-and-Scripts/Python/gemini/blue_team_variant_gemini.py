# Blue Team Scenario: Network Traffic Threshold Monitor

**Author:** Gemini (AI).
**Context:** Recontextualization of the "Grocery Store" logic for Cyber Defense.
**Goal:** To monitor network traffic protocols. If the packet count exceeds a safe baseline, the script calculates a "Risk Score" or applies a "Throttling Factor" (simulated here as a reduction in allowed bandwidth).

## The Analogy
* **Fruit** -> **Network Protocol** (SSH, HTTP, FTP).
* **Price** -> **Risk Weight** (SSH is riskier than HTTP).
* **Quantity** -> **Packet Count** detected in a burst.
* **Promotion** -> **Traffic Shaping/Alerting** (Reducing the calculated throughput score to indicate mitigation).

## The Code

```python
# --- Threat Intelligence Configuration ---
# Risk Weight per protocol (Higher number = Higher sensitivity)
# SSH is critical (Port 22)
Protocol_SSH = 10.5 
# FTP is insecure (Port 21)
Protocol_FTP = 8.2
# HTTP is standard (Port 80)
Protocol_HTTP = 1.5

# Input: Traffic Analysis
TargetProtocol = input("Enter Protocol detected (SSH, FTP, HTTP): ")

# Determine Risk Factor based on Protocol
CurrentRiskFactor = 0.0
ValidProtocol = 1

if TargetProtocol == "SSH":
    CurrentRiskFactor = float(Protocol_SSH)
elif TargetProtocol == "FTP":
    CurrentRiskFactor = float(Protocol_FTP)
elif TargetProtocol == "HTTP":
    CurrentRiskFactor = float(Protocol_HTTP)
else:
    print("Unknown Protocol. Logged for manual review.")
    ValidProtocol = 0

if ValidProtocol == 1:
    PacketInput = input("Enter number of packets in burst (1-1000): ")
    PacketCount = int(PacketInput)
    
    # --- Firewall Logic Engine ---
    # We calculate a 'Severity Score'. 
    # If packets exceed threshold, we subtract from the score (Simulating a throttle/drop action)
    
    FinalSeverityScore = 0.0

    # Logic: IF SSH packets > 50, Alert and mitigate (reduce score impact to show dropped packets)
    if TargetProtocol == "SSH" and PacketCount > 50:
        print("ALERT: Brute Force Suspected on SSH.")
        # Mitigate: effectively ignoring 20 packets of the load
        FinalSeverityScore = (CurrentRiskFactor * PacketCount) - (CurrentRiskFactor * 20)
        print("Mitigation: Traffic Throttled.")

    # Logic: IF FTP packets > 100, Warn
    elif TargetProtocol == "FTP" and PacketCount > 100:
        print("WARNING: Large FTP Data Transfer.")
        # Mitigate: ignoring 10 packets
        FinalSeverityScore = (CurrentRiskFactor * PacketCount) - (CurrentRiskFactor * 10)
        
    # Logic: HTTP usually allows high traffic
    elif TargetProtocol == "HTTP" and PacketCount > 500:
        print("INFO: High Web Traffic.")
        # Minimal mitigation
        FinalSeverityScore = (CurrentRiskFactor * PacketCount) - (CurrentRiskFactor * 5)
        
    else:
        print("Traffic is within normal baselines.")
        FinalSeverityScore = CurrentRiskFactor * PacketCount

    print("Calculated Incident Severity Score:")
    print(FinalSeverityScore)
