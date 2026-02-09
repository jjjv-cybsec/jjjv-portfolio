# Red Team Scenario: Payload Delivery Optimizer

**Author:** Gemini (AI) & [Tu Nombre/Usuario]
**Context:** Recontextualization of the "Grocery Store" made by "Jonás Joya" (GitHub user name: "jjjv-cybsec") logic for Cyber Offense.
**Goal:** To calculate the estimated "Time to Compromise" based on the target OS and the number of payloads sent. "Promotions" represent time saved by using automated exploit scripts when sending bulk payloads.

## The Analogy
* **Fruit** -> **Target OS** (Windows, Linux, MacOS).
* **Price** -> **Execution Time** (Seconds per payload manually).
* **Quantity** -> **Number of Payloads** to inject.
* **Promotion** -> **Automation Bonus** (Time deducted/saved because we script the attack when volume is high).

## The Code

```python
# --- Attack Configuration ---
# Base execution time per payload in seconds
Target_Windows = 5.5
Target_Linux = 3.2
Target_MacOS = 4.8

TargetOS = input("Select Target OS (Windows, Linux, MacOS): ")

BaseTime = 0.0
ReadyToAttack = 1

if TargetOS == "Windows":
    BaseTime = float(Target_Windows)
elif TargetOS == "Linux":
    BaseTime = float(Target_Linux)
elif TargetOS == "MacOS":
    BaseTime = float(Target_MacOS)
else:
    print("Error: Exploit kit not available for this OS.")
    ReadyToAttack = 0

if ReadyToAttack == 1:
    PayloadsInput = input("Enter number of payloads to inject: ")
    PayloadCount = int(PayloadsInput)
    
    EstimatedDuration = 0.0

    # Logic: 
    # If we send many payloads, we switch to 'Batch Mode' (The Promotion), saving time.
    
    if TargetOS == "Windows" and PayloadCount > 10:
        print("Mode: Mass-Deployment (PowerShell Script).")
        # Save time equivalent to 3 manual executions
        EstimatedDuration = (BaseTime * PayloadCount) - (BaseTime * 3)
        
    elif TargetOS == "Linux" and PayloadCount > 20:
        print("Mode: Bash Automation Loop.")
        # Save time equivalent to 5 manual executions
        EstimatedDuration = (BaseTime * PayloadCount) - (BaseTime * 5)
        
    elif TargetOS == "MacOS" and PayloadCount > 5:
        print("Mode: AppleScript Injection.")
        # Save time equivalent to 1 manual execution
        EstimatedDuration = (BaseTime * PayloadCount) - (BaseTime * 1)
        
    else:
        print("Mode: Manual Injection (One by one).")
        # No time savings
        EstimatedDuration = BaseTime * PayloadCount

    print("Estimated Attack Duration (Seconds):")
    print(EstimatedDuration)
