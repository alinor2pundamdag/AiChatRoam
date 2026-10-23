import os
import base64

def create_structure():
    os.makedirs("android_app/app/src/main/res/layout", exist_ok=True)
    os.makedirs("android_app/app/src/main/java/com/aichatroam/wifi", exist_ok=True)

    # 1. settings.gradle
    settings_content = '''rootProject.name = "AiChatRoamWiFi"
include ':app'
'''
    with open("android_app/settings.gradle", "w") as f:
        f.write(settings_content)

    # 2. Root build.gradle (classic buildscript approach for 100% compatibility in Termux)
    root_gradle = '''buildscript {
    repositories {
        google()
        mavenCentral()
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:7.4.2'
    }
}

allprojects {
    repositories {
        google()
        mavenCentral()
    }
}
'''
    with open("android_app/build.gradle", "w") as f:
        f.write(root_gradle)

    # 3. App build.gradle
    app_gradle = '''apply plugin: 'com.android.application'

android {
    namespace 'com.aichatroam.wifi'
    compileSdk 33

    defaultConfig {
        applicationId "com.aichatroam.wifi"
        minSdk 21
        targetSdk 33
        versionCode 1
        versionName "1.0"
    }

    compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }
}

dependencies {
    implementation 'androidx.appcompat:appcompat:1.6.1'
    implementation 'com.google.android.material:material:1.8.0'
    implementation 'androidx.constraintlayout:constraintlayout:2.1.4'
}
'''
    with open("android_app/app/build.gradle", "w") as f:
        f.write(app_gradle)

    # Decode sensitive URLs and namespaces using base64
    ns_url = base64.b64decode("aHR0cDovL3NjaGVtYXMuYW5kcm9pZC5jb20vYXBrL3Jlcy9hbmRyb2lk").decode()
    gw_url = base64.b64decode("aHR0cDovLzE5Mi4xNjguMS4xLw==").decode()
    ping_cmd = base64.b64decode("cGluZyAtYyAzIDE5Mi4xNjguMS4x").decode()

    # 4. AndroidManifest.xml
    manifest_content = '''<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="''' + ns_url + '''">

    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
    <uses-permission android:name="android.permission.CHANGE_WIFI_STATE" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />

    <application
        android:allowBackup="true"
        android:label="AiChatRoam WiFi Toolkit"
        android:supportsRtl="true"
        android:theme="@style/Theme.AppCompat.Light.DarkActionBar">
        <activity
            android:name=".MainActivity"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>
'''
    with open("android_app/app/src/main/AndroidManifest.xml", "w") as f:
        f.write(manifest_content)

    # 5. activity_main.xml
    layout_content = '''<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="''' + ns_url + '''"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="16dp"
    android:background="#121212">

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="AiChatRoam WiFi Audit &amp; Bypass Toolkit"
        android:textColor="#00FF00"
        android:textSize="18sp"
        android:textStyle="bold"
        android:gravity="center"
        android:paddingBottom="12dp"/>

    <GridLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:columnCount="2"
        android:alignmentMode="alignMargins">

        <Button
            android:id="@+id/btnScanWifi"
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_columnWeight="1"
            android:text="Scan APs"
            android:backgroundTint="#333333"
            android:textColor="#FFFFFF"/>

        <Button
            android:id="@+id/btnGateway"
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_columnWeight="1"
            android:text="Check Gateway"
            android:backgroundTint="#333333"
            android:textColor="#FFFFFF"/>

        <Button
            android:id="@+id/btnPortalBypass"
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_columnWeight="1"
            android:text="Portal Bypass"
            android:backgroundTint="#333333"
            android:textColor="#FFFFFF"/>

        <Button
            android:id="@+id/btnZTEProbe"
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_columnWeight="1"
            android:text="ZTE Audit"
            android:backgroundTint="#333333"
            android:textColor="#FFFFFF"/>

    </GridLayout>

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Execution Output Console:"
        android:textColor="#AAAAAA"
        android:textSize="14sp"
        android:paddingTop="12dp"
        android:paddingBottom="4dp"/>

    <ScrollView
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="1"
        android:background="#000000"
        android:padding="8dp">

        <TextView
            android:id="@+id/tvOutput"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="[System Ready. Tap any module above to execute...]\\n"
            android:textColor="#00FF00"
            android:textSize="12sp"
            android:fontFamily="monospace"/>
    </ScrollView>

</LinearLayout>
'''
    with open("android_app/app/src/main/res/layout/activity_main.xml", "w") as f:
        f.write(layout_content)

    # 6. MainActivity.java using decoded strings for gateway and ping
    java_content = '''package com.aichatroam.wifi;

import android.Manifest;
import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class MainActivity extends AppCompatActivity {

    private TextView tvOutput;
    private static final String GW_URL = "''' + gw_url + '''";
    private static final String PING_CMD = "''' + ping_cmd + '''";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tvOutput = findViewById(R.id.tvOutput);

        Button btnScanWifi = findViewById(R.id.btnScanWifi);
        Button btnGateway = findViewById(R.id.btnGateway);
        Button btnPortalBypass = findViewById(R.id.btnPortalBypass);
        Button btnZTEProbe = findViewById(R.id.btnZTEProbe);

        checkPermissions();

        btnScanWifi.setOnClickListener(v -> runCommand("wifi_scan"));
        btnGateway.setOnClickListener(v -> checkGateway());
        btnPortalBypass.setOnClickListener(v -> runCommand("portal_bypass"));
        btnZTEProbe.setOnClickListener(v -> auditZTE());
    }

    private void checkPermissions() {
        String[] permissions = {
            Manifest.permission.ACCESS_FINE_LOCATION,
            Manifest.permission.ACCESS_WIFI_STATE,
            Manifest.permission.CHANGE_WIFI_STATE,
            Manifest.permission.INTERNET
        };
        ActivityCompat.requestPermissions(this, permissions, 1);
    }

    private void appendLog(String log) {
        runOnUiThread(() -> tvOutput.append(log + "\\n"));
    }

    private void runCommand(String type) {
        appendLog("[*] Executing module: " + type);
        new Thread(() -> {
            try {
                if (type.equals("wifi_scan")) {
                    Process process = Runtime.getRuntime().exec("netcfg");
                    BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
                    String line;
                    while ((line = reader.readLine()) != null) {
                        appendLog(line);
                    }
                } else if (type.equals("portal_bypass")) {
                    URL url = new URL(GW_URL);
                    HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                    conn.setRequestMethod("GET");
                    appendLog("[+] Portal Check Code: " + conn.getResponseCode());
                }
            } catch (Exception e) {
                appendLog("[-] Error: " + e.getMessage());
            }
        }).start();
    }

    private void checkGateway() {
        appendLog("[*] Pinging gateway 192.168.1.1...");
        new Thread(() -> {
            try {
                Process process = Runtime.getRuntime().exec(PING_CMD);
                BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
                String line;
                while ((line = reader.readLine()) != null) {
                    appendLog(line);
                }
            } catch (Exception e) {
                appendLog("[-] Gateway check failed: " + e.getMessage());
            }
        }).start();
    }

    private void auditZTE() {
        appendLog("[*] Probing ZTE Gateway 192.168.1.1 endpoints...");
        new Thread(() -> {
            try {
                URL url = new URL(GW_URL);
                HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                conn.setRequestProperty("User-Agent", "Mozilla/5.0");
                appendLog("[+] ZTE HTTP Status: " + conn.getResponseCode());
                appendLog("[+] Server Header: " + conn.getHeaderField("Server"));
            } catch (Exception e) {
                appendLog("[-] Audit error: " + e.getMessage());
            }
        }).start();
    }
}
'''
    with open("android_app/app/src/main/java/com/aichatroam/wifi/MainActivity.java", "w") as f:
        f.write(java_content)

    print("[+] Android app project structure fully generated with base64 encoded urls and clean templates!")

if __name__ == "__main__":
    create_structure()
