"""
AiChatRoam - Robust Network Reconnaissance & Diagnostic Module
Engineered collaboratively by Gemini and ChatGPT for practical utility.
"""

import subprocess
import platform
import json

def get_local_interfaces():
    print("[*] Inspecting local network interfaces...")
    interfaces = []
    try:
        output = subprocess.check_output(['ip', 'addr'], universal_newlines=True)
        interfaces.append(output)
    except Exception:
        try:
            output = subprocess.check_output(['ifconfig'], universal_newlines=True)
            interfaces.append(output)
        except Exception as e:
            interfaces.append(f"Interface check error: {e}")
    return interfaces

def scan_gateway_and_routes():
    print("[*] Analyzing local gateway and active socket routes...")
    routes = []
    try:
        output = subprocess.check_output(['ip', 'route'], universal_newlines=True)
        routes = output.splitlines()
    except Exception:
        routes.append("Default route check unavailable via ip command.")
    return routes

def run_diagnostic():
    report = {
        "system": platform.system(),
        "node": platform.node(),
        "interfaces": get_local_interfaces(),
        "routes": scan_gateway_and_routes()
    }
    filename = "network_diagnostic_report.json"
    with open(filename, "w") as f:
        json.dump(report, f, indent=4)
    print(f"[+] Diagnostic report successfully saved to {filename}")

if __name__ == "__main__":
    print("=== AiChatRoam Practical Network Diagnostics & Recon Tool ===")
    run_diagnostic()
