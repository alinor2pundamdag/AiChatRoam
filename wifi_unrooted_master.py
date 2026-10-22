#!/usr/bin/env python3
"""
AiChatRoam - Advanced Unrooted / Non-Root Wi-Fi Intelligence & Captive Portal Automation Toolkit
Engineered by Gemini for complete user-space operational execution on Android/Termux without root.
"""

import subprocess
import urllib.request
import urllib.parse
import json
import sys
import shutil

def run_termux_wifi_scan():
    """
    Uses Termux-API (if available) to scan visible Wi-Fi networks in unrooted user-space.
    """
    print("[*] Querying unrooted Wi-Fi environment via Termux-API...")
    if not shutil.which("termux-wifi-scaninfo"):
        print("[-] termux-wifi-scaninfo binary not found. Ensure Termux:API app and package are installed.")
        return []
    
    try:
        result = subprocess.run(["termux-wifi-scaninfo"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        networks = json.loads(result.stdout)
        return networks
    except Exception as e:
        print(f"[-] Scan error or permission restricted: {e}")
        return []

def analyze_captive_portal(test_url="http://connectivitycheck.gstatic.com/generate_204"):
    """
    Detects if internet access is blocked or redirected by a captive portal (common in unrooted public/guest networks).
    """
    print("[*] Probing network connectivity and captive portal status...")
    try:
        req = urllib.request.Request(test_url, headers={"User-Agent": "Mozilla/5.0 (Android; Mobile)"})
        with urllib.request.urlopen(req, timeout=5) as response:
            status = response.status
            if status == 204:
                print("[+] Network is fully connected with direct internet access.")
                return "CONNECTED"
            else:
                print(f"[!] Unexpected status code: {status}")
                return "UNKNOWN"
    except urllib.error.HTTPError as e:
        print(f"[!] Captive portal redirect detected (HTTP Error: {e.code})")
        return "CAPTIVE_PORTAL"
    except Exception:
        print("[-] Network unreachable or no association established.")
        return "DISCONNECTED"

def automate_portal_login(login_url, payload_dict):
    """
    Automates submission of credentials or acceptance terms for unrooted captive portals.
    """
    print(f"[*] Submitting automated authentication payload to: {login_url}")
    data = urllib.parse.urlencode(payload_dict).encode("utf-8")
    try:
        req = urllib.request.Request(login_url, data=data, method="POST")
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"[+] Authentication response received. Status: {resp.status}")
            return True
    except Exception as e:
        print(f"[-] Automated portal login failed: {e}")
        return False

if __name__ == "__main__":
    print("=== AiChatRoam Unrooted Wi-Fi Intelligence & Automation Engine ===")
    
    # 1. Scan available networks via unrooted API
    nets = run_termux_wifi_scan()
    if nets:
        print(f"[+] Found {len(nets)} visible access points in range:")
        for net in nets:
            print(f"    - SSID: {net.get('SSID')} | BSSID: {net.get('BSSID')} | RSSI: {net.get('RSSI')} dBm")
    else:
        print("[*] Skipping API scan or no networks returned.")
        
    # 2. Check connection & portal state
    state = analyze_captive_portal()
    if state == "CAPTIVE_PORTAL":
        portal_target = sys.argv[1] if len(sys.argv) > 1 else "http://portal.local/auth"
        default_payload = {"user": "guest", "accept": "true"}
        automate_portal_login(portal_target, default_payload)
    elif state == "CONNECTED":
        print("[+] Ready for operations.")
