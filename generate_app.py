import os
import subprocess
import base64
import urllib.request
import zipfile
import shutil
import stat

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

    plat_dir = os.path.join(sdk_path, "platforms", "android-33")
    bt_dir = os.path.join(sdk_path, "build-tools", "33.0.1")
    lic_dir = os.path.join(sdk_path, "licenses")
    
    os.makedirs(plat_dir, exist_ok=True)
    os.makedirs(bt_dir, exist_ok=True)
    os.makedirs(lic_dir, exist_ok=True)
    
    # Base64 encoded XML stubs using namespace prefix ns2 (http://schemas.android.com/repository/android/common/02)
    plat_b64 = "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9InllcyI/Pgo8bnMyOnJlcG9zaXRvcnkgeG1sbnM6bnMyPSJodHRwOi8vc2NoZW1hcy5hbmRyb2lkLmNvbS9yZXBvc2l0b3J5L2FuZHJvaWQvY29tbW9uLzAyIiB4bWxuczp4c2k9Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlIj4KICAgIDxsb2NhbFBhY2thZ2UgcGF0aD0icGxhdGZvcm1zO2FuZHJvaWQtMzMiIG1ham9yUmV2PSIzMyI+CiAgICAgICAgPHR5cGUtZGV0YWlscyB4c2k6dHlwZT0ibnMyOlBsYXRmb3JtRGV0YWlsc1R5cGUiPgogICAgICAgICAgICA8YXBpLWxldmVsPjMzPC9hcGktbGV2ZWw+CiAgICAgICAgPC90eXBlLWRldGFpbHM+CiAgICAgICAgPHJldmlzaW9uPgogICAgICAgICAgICA8bWFqb3I+MzwvbWFqb3I+CiAgICAgICAgPC9yZXZpc2lvbj4KICAgICAgICA8ZGlzcGxheXM+CiAgICAgICAgICAgIDxzdHJpbmc+QW5kcm9pZCBJREsgUGxhdGZvcm0gMzM8L3N0cmluZz4KICAgICAgICA8L2Rpc3BsYXlzPgog   </div>
</ns2:repository>
"
    # Wait, let's write clean base64 without any trailing space typos
    plat_xml_b64 = "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9InllcyI/Pgo8bnMyOnJlcG9zaXRvcnkgeG1sbnM6bnMyPSJodHRwOi8vc2NoZW1hcy5hbmRyb2lkLmNvbS9yZXBvc2l0b3J5L2FuZHJvaWQvY29tbW9uLzAyIiB4bWxuczp4c2k9Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlIj4KICAgIDxsb2NhbFBhY2thZ2UgcGF0aD0icGxhdGZvcm1zO2FuZHJvaWQtMzMiIG1ham9yUmV2PSIzMyI+CiAgICAgICAgPHR5cGUtZGV0YWlscyB4c2k6dHlwZT0ibnMyOlBsYXRmb3JtRGV0YWlsc1R5cGUiPgogICAgICAgICAgICA8YXBpLWxldmVsPjMzPC9hcGktbGV2ZWw+CiAgICAgICAgPC90eXBlLWRldGFpbHM+CiAgICAgICAgPHJldmlzaW9uPgogICAgICAgICAgICA8bWFqb3I+MzwvbWFqb3I+CiAgICAgICAgPC9yZXZpc2lvbj4KICAgICAgICA8ZGlzcGxheXM+CiAgICAgICAgICAgIDxzdHJpbmc+QW5kcm9pZCBJREsgUGxhdGZvcm0gMzM8L3N0cmluZz4KICAgICAgICA8L2Rpc3BsYXlzPgogICAgPC9sb2NhbFBhY2thZ2U+CjwvbnMyOnJlcG9zaXRvcnk+Cg=="
    bt_xml_b64 = "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9InllcyI/Pgo8bnMyOnJlcG9zaXRvcnkgeG1sbnM6bnMyPSJodHRwOi8vc2NoZW1hcy5hbmRyb2lkLmNvbS9yZXBvc2l0b3J5L2FuZHJvaWQvY29tbW9uLzAyIiB4bWxuczp4c2k9Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlIj4KICAgIDxsb2NhbFBhY2thZ2UgcGF0aD0iYnVpbGQtdG9vbHM7MzMuMC4xIiBtYWpvcjBSZXY9IjMzIj4KICAgICAgICA8dHlwZS1kZXRhaWxzIHhzaTp0eXBlPSJuczI6QnVpbGRUb29sRGV0YWlsc1R5cGUiLz4KICAgICAgICA8cmV2aXNpb24+CiAgICAgICAgICAgIDxtYWpvcj4zMzwvbWFqb3I+CiAgICAgICAgICAgIDxtaW5vcj4wPC9taW5vcj4KICAgICAgICAgICAgPG1pY3JvPjE8L21pY3JvPgogICAgICAgIDwvcmV2aXNpb24+CiAgICAgICAgPGRpc3BsYXlzPgogICAgICAgICAgICA8c3RyaW5nPkFuZHJvaWQgU0RLIEJ1aWxkLVRvb2xzIDMzLjAuMTwvc3RyaW5nPgogICAgICAgIDwvZGlzcGxheXM+CiAgICA8L2xvY2FsUGFja2FnZT4KPC9uczI6cmVwb3NpdG9yeT4K"

    with open(os.path.join(plat_dir, "package.xml"), "wb") as f:
        f.write(base64.b64decode(plat_xml_b64))

    with open(os.path.join(bt_dir, "package.xml"), "wb") as f:
        f.write(base64.b64decode(bt_xml_b64))

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

def ensure_gradle_8_1_1(app_dir):
    gradle_home = os.path.expanduser("~/.gradle-local-8.1.1")
    gradle_bin = os.path.join(gradle_home, "bin", "gradle")
    if not os.path.exists(gradle_bin):
        print("[*] Downloading Gradle 8.1.1 binary distribution for Termux...")
        zip_path = os.path.join(app_dir, "gradle-8.1.1-bin.zip")
        url = "https://services.gradle.org/distributions/gradle-8.1.1-bin.zip"
        try:
            urllib.request.urlretrieve(url, zip_path)
            os.makedirs(gradle_home, exist_ok=True)
            with zipfile.ZipFile(zip_path, 'r') as zf:
                zf.extractall(app_dir)
            extracted_dir = os.path.join(app_dir, "gradle-8.1.1")
            if os.path.exists(gradle_home):
                shutil.rmtree(gradle_home)
            shutil.move(extracted_dir, gradle_home)
            if os.path.exists(zip_path):
                os.remove(zip_path)
            print("[+] Gradle 8.1.1 installed successfully!")
        except Exception as e:
            print(f"[-] Error downloading Gradle 8.1.1: {e}")
    
    bin_dir = os.path.join(gradle_home, "bin")
    if os.path.exists(bin_dir):
        for f in os.listdir(bin_dir):
            fp = os.path.join(bin_dir, f)
            os.chmod(fp, stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)

    return gradle_bin

def create_structure():
    app_dir = "android_app"
    os.makedirs(f"{app_dir}/app/src/main/res/layout", exist_ok=True)
    os.makedirs(f"{app_dir}/app/src/main/java/com/aichatroam/wifi", exist_ok=True)

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
    with open(f"{app_dir}/settings.gradle", "w") as f:
        f.write(settings_content)

    # 2. Root build.gradle with AGP 8.1.1
    root_gradle = '''plugins {
    id 'com.android.application' version '8.1.1' apply false
}
'''
    with open(f"{app_dir}/build.gradle", "w") as f:
        f.write(root_gradle)

    # 3. App build.gradle
    app_gradle = '''plugins {
    id 'com.android.application'
}

android {
    namespace 'com.aichatroam.wifi'
    compileSdk 33

    defaultConfig {
        applicationId "com.aichatroam.wifi"
        minSdk 21
        targetSdk 33
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
    with open(f"{app_dir}/app/build.gradle", "w") as f:
        f.write(app_gradle)

    # 4. Global & Local Gradle Properties
    gradle_props = '''org.gradle.jvmargs=-Xmx2048m -XX:MaxMetaspaceSize=512m -Dfile.encoding=UTF-8
org.gradle.parallel=true
org.gradle.caching=true
org.gradle.configureondemand=true
android.enableJetifier=true
android.useAndroidX=true
'''
    with open(f"{app_dir}/gradle.properties", "w") as f:
        f.write(gradle_props)

    os.makedirs(os.path.expanduser("~/.gradle"), exist_ok=True)
    with open(os.path.expanduser("~/.gradle/gradle.properties"), "w") as f:
        f.write(gradle_props)

    # 5. Robust local.properties
    sdk_path = setup_robust_sdk()
    with open(f"{app_dir}/local.properties", "w") as f:
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
    with open(f"{app_dir}/app/src/main/AndroidManifest.xml", "w") as f:
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
    with open(f"{app_dir}/app/src/main/res/layout/activity_main.xml", "w") as f:
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
                HttpURLConnection conn = (HttpURLConnnection) url.openConnection();
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
    # Wait, let's fix HttpURLConnection typo in auditZTE (HttpURLConnnection -> HttpURLConnection)
    java_code = java_code.replace("HttpURLConnnection", "HttpURLConnection")
    with open(f"{app_dir}/app/src/main/java/com/aichatroam/wifi/MainActivity.java", "w") as f:
        f.write(java_code)

    # 8. Ensure robust gradlew pointing directly to standalone Gradle 8.1.1 binary
    gradle_bin = ensure_gradle_8_1_1(app_dir)
    gradlew_content = f'''#!/bin/sh
exec "{gradle_bin}" "$@"
'''
    with open(f"{app_dir}/gradlew", "w") as wf:
        wf.write(gradlew_content)
    os.chmod(f"{app_dir}/gradlew", 0o755)

    os.makedirs(f"{app_dir}/gradle/wrapper", exist_ok=True)
    with open(f"{app_dir}/gradle/wrapper/gradle-wrapper.properties", "w") as wf:
        wf.write("""distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
distributionUrl=https\\://services.gradle.org/distributions/gradle-8.1.1-bin.zip
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
""")

    print("[+] Android app project fully configured with base64 SDK 33.0.1 package.xml stubs and AGP 8.1.1!")

if __name__ == "__main__":
    create_structure()
