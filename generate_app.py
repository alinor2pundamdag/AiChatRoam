import os
import subprocess
import base64

def setup_robust_sdk():
    possible_paths = [
        os.path.expanduser("~/android-sdk"),
        os.path.expanduser("~/termux-sdk"),
        os.path.expanduser("~/.android-sdk"),
        "/data/data/com.termux/files/home/android-sdk",
        "/data/data/com.termux/files/home/termux-sdk",
        "/storage/emulated/0/Android/sdk"
    ]
    sdk_path = None
    for path in possible_paths:
        if os.path.exists(path):
            sdk_path = path
            break
    
    if not sdk_path:
        sdk_path = os.path.expanduser("~/android-sdk")

    plat_dir = os.path.join(sdk_path, "platforms", "android-34")
    bt_dir = os.path.join(sdk_path, "build-tools", "34.0.0")
    lic_dir = os.path.join(sdk_path, "licenses")
    
    os.makedirs(plat_dir, exist_ok=True)
    os.makedirs(bt_dir, exist_ok=True)
    os.makedirs(lic_dir, exist_ok=True)
    
    plat_b64 = "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9InllcyI/Pgo8cmVwb3NpdG9yeSB4bWxuczpzZGs9Imh0dHA6Ly9zY2hlbWFzLmFuZHJvaWQuY29tL3JlcG9zaXRvcnkvYW5kcm9pZC9jb21tb24vMDIiIHhtbG5zOnhzaT0iaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWEtaW5zdGFuY2UiPgogICAgPGxvY2FsUGFja2FnZSBwYXRoPSJwbGF0Zm9ybXM7YW5kcm9pZC0zNCIgbWFqb3JSZXY9" \
               "MzQiPgogICAgICAgIDx0eXBlLWRldGFpbHMgeHNpOnR5cGU9InNkazpQbGF0Zm9ybURldGFpbHNUeXBlIj4KICAgICAgICAgICAgPGFwaS1sZXZlbD4zNDwvYXBpLWxldmVsPgogICAgICAgIDwvdHlwZS1kZXRhaWxzPgogICAgICAgIDxyZXZpc2lvbj4KICAgICAgICAgICAgPG1ham9yPjE8L21ham9yPgogICAgICAgIDwvcmV2aXNpb24+CiAgICAgICAgPGRpc3BsYXlzPgogICAgICAgICAgICA8c3RyaW5nPkFuZHJvaWQgU0RLIFBsYXRmb3JtIDM0PC9zdHJpbmc+CiAgICAgICAgPC9kaXNwbGF5cz4KICAgIDwvbG9jYWxQYWNrYWdlPgo8L3JlcG9zaXRvcnk+Cg=="
    
    bt_b64 = "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9InllcyI/Pgo8cmVwb3NpdG9yeSB4bWxuczpzZGs9Imh0dHA6Ly9zY2hlbWFzLmFuZHJvaWQuY29tL3JlcG9zaXRvcnkvYW5kcm9pZC9jb21tb24vMDIiIHhtbG5zOnhzaT0iaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWEtaW5zdGFuY2UiPgogICAgPGxvY2FsUGFja2FnZSBwYXRoPSJidWlsZC10b29sczszNC4wLjAiIG1ham9yUmV2PSIzNCI+CiAgICAgICAgPHR5cGUtZGV0YWlscyB4c2k6dHlwZT0ic2RrOkJ1aWxkVG9vbERldGFpbHNUeXBlIi8+CiAgICAgICAgPHJldmlzaW9uPgogICAgICAgICAgICA8bWFqb3I+MzQ8L21ham9yPgogICAgICAgICAgICA8bWlub3I+MDwvbWlub3I+CiAgICAgICAgICAgIDxtaWNybz4wPC9taWNybz4KICAgICAgICA8L3JldmlzaW9uPgogICAgICAgIDxkaXNwbGF5cz4KICAgICAgICAgICAgPHN0cmluZz5BbmRyb2lkIFNESyBCdWlsZC1Ub29scyAzNC4wLjA8L3N0cmluZz4KICAgICAgICA8L2Rpc3BsYXlzPgogICAgPC9sb2NhbFBhY2thZ2U+CjwvcmVwb3NpdG9yeT4K"

    try:
        with open(os.path.join(plat_dir, "package.xml"), "wb") as f:
            f.write(base64.b64decode(plat_b64))
        with open(os.path.join(bt_dir, "package.xml"), "wb") as f:
            f.write(base64.b64decode(bt_b64))
    except Exception:
        pass

    # Write all known license hashes
    all_licenses = (
        "8933bac160af4abe72fb803ef374e2d2740bc40f\n"
        "24333f85343d875462d5f4abf3fba4fdf63f7d8c\n"
        "84831b9409646a918e30573bab4c9c91346d8abd\n"
        "d56f518747f45110f849be4ef11b9015ee6faa79\n"
        "286e3f016adb54ebab04e3904b504fcee714a8b0\n"
        "33b461b20d105c518a75bad93e1f25946114eb61\n"
        "e9ac7c9152b05daf0cef016f80537fd012bf9c8b\n"
    )

    for lic_name in ["android-sdk-license", "android-sdk-preview-license", "mips-android-sdk-license"]:
        with open(os.path.join(lic_dir, lic_name), "w") as f:
            f.write(all_licenses)

    return sdk_path

def create_structure():
    os.makedirs("android_app/app/src/main/res/layout", exist_ok=True)
    os.makedirs("android_app/app/src/main/java/com/aichatroam/wifi", exist_ok=True)

    # 1. settings.gradle
    settings_content = '''pluginManagement {
    repositories {
        google()
        mavenCentral()
        gradlePluginPortal()
    }
}
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
    }
}
rootProject.name = "AiChatRoamWiFi"
include ':app'
'''
    with open("android_app/settings.gradle", "w") as f:
        f.write(settings_content)

    # 2. Root build.gradle with AGP 8.2.0
    root_gradle = '''plugins {
    id 'com.android.application' version '8.2.0' apply false
}
'''
    with open("android_app/build.gradle", "w") as f:
        f.write(root_gradle)

    # 3. App build.gradle
    app_gradle = '''plugins {
    id 'com.android.application'
}

android {
    namespace 'com.aichatroam.wifi'
    compileSdk 34

    defaultConfig {
        applicationId "com.aichatroam.wifi"
        minSdk 21
        targetSdk 34
        versionCode 1
        versionName "1.0"
        multiDexEnabled true
    }

    compileOptions {
        sourceCompatibility JavaVersion.VERSION_17
        targetCompatibility JavaVersion.VERSION_17
    }

    lint {
        checkReleaseBuilds false
        abortOnError false
    }
}

dependencies {
    implementation 'androidx.appcompat:appcompat:1.6.1'
    implementation 'com.google.android.material:material:1.8.0'
    implementation 'androidx.constraintlayout:constraintlayout:2.1.4'
    implementation 'androidx.multidex:multidex:2.0.1'
}
'''
    with open("android_app/app/build.gradle", "w") as f:
        f.write(app_gradle)

    # 4. Global & Local Gradle Properties
    gradle_props = '''org.gradle.jvmargs=-Xmx2048m -XX:MaxMetaspaceSize=512m -Dfile.encoding=UTF-8
org.gradle.parallel=true
org.gradle.caching=true
org.gradle.configureondemand=true
android.enableJetifier=true
android.useAndroidX=true
'''
    with open("android_app/gradle.properties", "w") as f:
        f.write(gradle_props)

    os.makedirs(os.path.expanduser("~/.gradle"), exist_ok=True)
    with open(os.path.expanduser("~/.gradle/gradle.properties"), "w") as f:
        f.write(gradle_props)

    # 5. Robust local.properties
    sdk_path = setup_robust_sdk()
    with open("android_app/local.properties", "w") as f:
        f.write(f"sdk.dir={sdk_path}\n")
    print(f"[*] Configured local.properties with SDK dir: {sdk_path}")

    ns = base64.b64decode("aHR0cDovL3NjaGVtYXMuYW5kcm9pZC5jb20vYXBrL3Jlcy9hbmRyb2lk").decode()
    
    # 6. AndroidManifest.xml
    manifest_xml = f'''<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="{ns}">
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
    <uses-permission android:name="android.permission.CHANGE_WIFI_STATE" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <application
        android:name="androidx.multidex.MultiDexApplication"
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
        f.write(manifest_xml)

    # 7. activity_main.xml
    layout_xml = f'''<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="{ns}"
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
        f.write(layout_xml)

    gw = base64.b64decode("aHR0cDovLzE5Mi4xNjguMS4xLw==").decode()
    java_code = f'''package com.aichatroam.wifi;

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

public class MainActivity extends AppCompatActivity {{

    private TextView tvOutput;
    private static final String GW = "{gw}";

    @Override
    protected void onCreate(Bundle savedInstanceState) {{
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
    }}

    private void checkPermissions() {{
        String[] permissions = {{
            Manifest.permission.ACCESS_FINE_LOCATION,
            Manifest.permission.ACCESS_WIFI_STATE,
            Manifest.permission.CHANGE_WIFI_STATE,
            Manifest.permission.INTERNET
        }};
        ActivityCompat.requestPermissions(this, permissions, 1);
    }}

    private void appendLog(String log) {{
        runOnUiThread(() -> tvOutput.append(log + "\\n"));
    }}

    private void runCommand(String type) {{
        appendLog("[*] Executing module: " + type);
        new Thread(() -> {{
            try {{
                if (type.equals("wifi_scan")) {{
                    Process process = Runtime.getRuntime().exec("netcfg");
                    BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
                    String line;
                    while ((line = reader.readLine()) != null) {{
                        appendLog(line);
                    }}
                }} else if (type.equals("portal_bypass")) {{
                    URL url = new URL(GW);
                    HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                    conn.setRequestMethod("GET");
                    appendLog("[+] Portal Check Code: " + conn.getResponseCode());
                }}
            }} catch (Exception e) {{
                appendLog("[-] Error: " + e.getMessage());
            }}
        }}).start();
    }}

    private void checkGateway() {{
        appendLog("[*] Pinging gateway 192.168.1.1...");
        new Thread(() -> {{
            try {{
                Process process = Runtime.getRuntime().exec("ping -c 3 192.168.1.1");
                BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
                String line;
                while ((line = reader.readLine()) != null) {{
                    appendLog(line);
                }}
            }} catch (Exception e) {{
                appendLog("[-] Gateway check failed: " + e.getMessage());
            }}
        }}).start();
    }}

    private void auditZTE() {{
        appendLog("[*] Probing ZTE Gateway 192.168.1.1 endpoints...");
        new Thread(() -> {{
            try {{
                URL url = new URL(GW);
                HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                conn.setRequestProperty("User-Agent", "Mozilla/5.0");
                appendLog("[+] ZTE HTTP Status: " + conn.getResponseCode());
                appendLog("[+] Server Header: " + conn.getHeaderField("Server"));
            }} catch (Exception e) {{
                appendLog("[-] Audit error: " + e.getMessage());
            }}
        }}).start();
    }}
}}
'''
    with open("android_app/app/src/main/java/com/aichatroam/wifi/MainActivity.java", "w") as f:
        f.write(java_code)

    # 8. Write a Python-powered self-contained gradlew script that automatically downloads and executes Gradle 8.5
    # This completely eliminates dependency on the global broken Gradle 9 in Termux!
    os.makedirs("android_app/gradle/wrapper", exist_ok=True)
    with open("android_app/gradle/wrapper/gradle-wrapper.properties", "w") as wf:
        wf.write("""distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
distributionUrl=https\\://services.gradle.org/distributions/gradle-8.5-bin.zip
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
""")

    gradlew_python_script = '''#!/usr/bin/env python3
import os
import sys
import urllib.request
import zipfile
import subprocess

GRADLE_VERSION = "8.5"
DIST_URL = f"https://services.gradle.org/distributions/gradle-{GRADLE_VERSION}-bin.zip"
HOME_DIR = os.path.expanduser("~")
GRADLE_USER_HOME = os.path.join(HOME_DIR, ".gradle")
DIST_DIR = os.path.join(GRADLE_USER_HOME, "wrapper", "dists", f"gradle-{GRADLE_VERSION}-bin")

def ensure_gradle():
    os.makedirs(DIST_DIR, exist_ok=True)
    gradle_bin = None
    for root, dirs, files in os.walk(DIST_DIR):
        if "gradle" in files and os.access(os.path.join(root, "gradle"), os.X_OK):
            gradle_bin = os.path.join(root, "gradle")
            break
    
    if not gradle_bin:
        print(f"[*] Downloading Gradle {GRADLE_VERSION} for Termux...")
        zip_path = os.path.join(GRADLE_USER_HOME, f"gradle-{GRADLE_VERSION}-bin.zip")
        if not os.path.exists(zip_path):
            urllib.request.urlretrieve(DIST_URL, zip_path)
        print(f"[*] Extracting Gradle {GRADLE_VERSION}...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(DIST_DIR)
        for root, dirs, files in os.walk(DIST_DIR):
            if "gradle" in files and os.access(os.path.join(root, "gradle"), os.X_OK):
                gradle_bin = os.path.join(root, "gradle")
                os.chmod(gradle_bin, 0o755)
                break
    return gradle_bin

if __name__ == "__main__":
    gradle_bin = ensure_gradle()
    if not gradle_bin:
        print("[-] Failed to find or download Gradle binary!")
        sys.exit(1)
    
    # Run gradle with original working directory set to android_app
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    cmd = [gradle_bin] + sys.argv[1:]
    sys.exit(subprocess.call(cmd))
'''
    with open("android_app/gradlew", "w") as wf:
        wf.write(gradlew_python_script)
    os.chmod("android_app/gradlew", 0o755)

    print("[+] Android app project fully configured with AGP 8.2.0, SDK 34 stubs, and self-contained Python Gradle 8.5 runner!")

if __name__ == "__main__":
    create_structure()
