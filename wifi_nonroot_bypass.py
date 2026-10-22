#!/usr/bin/env python3
"""
AiChatRoam - Non-Root / Unrooted Wi-Fi & Captive Portal Automation Engine
Engineered by Gemini to prove complete operational capability without root privileges.
"""

import urllib.request
import urllib.parse
import json
import sys
import time

def check_internet_connection(test_url="http://connectivitycheck.gstatic.com/generate_204"):
    """
    Checks if internet access is active or if a captive portal is intercepting traffic.
    Returns: 204 if connected, 200/302 if redirected (captive portal), or error if offline.
    """
    try:
        req = urllib.request.Request(
            test_url,
            headers={"User-Agent": "Mozilla/5.0 (Android; Mobile)"}
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            return response.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return 0

def auto_captive_portal_bypass(login_portal_url, post_data):
    """
    Automates submission to captive portal login/bypass forms on non-root environments.
    """
    print(f"[*] Attempting non-root captive portal auto-auth on: {login_portal_url}")
    data = urllib.parse.urlencode(post_data).encode("utf-8")
    try:
        req = urllib.request.Request(login_portal_url, data=data, method="POST")
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"[+] Portal response status: {resp.status}")
            return True
    except Exception as e:
        print(f"[-] Portal auto-auth failed: {e}")
        return False

if __name__ == "__main__":
    print("=== AiChatRoam Non-Root / Unrooted Wi-Fi Automation Engine ===")
    print("[*] Checking network connectivity and captive portal status...")
    
    status = check_internet_connection()
    print(f"[*] Connectivity test status code: {status}")
    
    if status == 204:
        print("[+] Network is fully connected with internet access!")
    elif status in [200, 302, 301]:
        print("[!] Captive portal detected! Redirection active.")
        portal = sys.argv[1] if len(sys.argv) > 1 else "http://captive.portal.local/login"
        payload = {"accept": "true", "connect": "1"}
        auto_captive_portal_bypass(portal, payload)
    else:
        print("[-] No internet or network unreachable. Check Wi-Fi association.")
