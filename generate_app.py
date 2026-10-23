import os
import base64

def create_structure():
    os.makedirs("android_app/app/src/main/res/layout", exist_ok=True)
    os.makedirs("android_app/app/src/main/java/com/aichatroam/wifi", exist_ok=True)

    manifest_b64 = "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPG1hbmlmZXN0IHhtbG5zOmFuZHJvaWQ9Imh0dHA6Ly9zY2hlbWFzLmFuZHJvaWQuY29tL2Fway9yZXMvYW5kcm9pZCI+CiAgICA8dXNlcy1wZXJtaXNzaW9uIGFuZHJvaWQ6bmFtZT0iYW5kcm9pZC5wZXJtaXNzaW9uLkFDQ0VTU19XSUZJX1NUQVRFIiAvPgogICAgPHVzZXMtcGVybWlzc2lvbiBhbmRyb2lkOm5hbWU9ImFuZHJvaWQucGVybWlzc2lvbi5DSEFOR0VfV0lGSV9TVEFURSIgLz4KICAgIDx1c2VzLXBlcm1pc3Npb24gYW5kcm9pZDpuYW1lPSJhbmRyb2lkLnBlcm1pc3Npb24uQUNDRVNTX0ZJTkVfTE9DQVRJT04iICz4KICAgIDx1c2VzLXBlcm1pc3Npb24gYW5kcm9pZDpuYW1lPSJhbmRyb2lkLnBlcm1pc3Npb24uQUNDRVNTX0NPQVJTRV9MT0NBVElPTiIgLz4KICAgIDx1c2VzLXBlcm1pc3Npb24gYW5kcm9pZDpuYW1lPSJhbmRyb2lkLnBlcm1pc3Npb24uSUVSTkVUIiAvPgogICAgPHVzZXMtcGVybWlzc2lvbiBhbmRyb2lkOm5hbWU9ImFuZHJvaWQucGVybWlzc2lvbi5BQ0NFU1NfTkVUV09SS19TVEFURSIgLz4KICAgIDxhcHBsaWNhdGlvbiBhbmRyb2lkOmFsbG93QmFja3VwPSJ0cnVlIiBhbmRyb2lkOmxhYmVsPSJBaUNoYXRSb2FtIFdpRmkgVG9vbGtpdCIgYW5kcm9pZDpzdXBwb3J0c1J0bD0idHJ1ZSIgYW5kcm9pZDp0aGVtZT0iQHN0eWxlL1RoZW1lLkFwcENvbXBhdC5MaWdodC5EYXJrQWN0aWJhciI+CiAgICAgICAgPGFjdGl2aXR5IGFuZHJvaWQ6bmFtZT0iLk1haW5BY3Rpdml0eSIgYW5kcm9pZDpleHBvcnRlZD0idHJ1ZSI+CiAgICAgICAgICAgIDxpbnRlbnQtZmlsdGVyPgogICAgICAgICAgICAgICAgPGFjdGlvbiBhbmRyb2lkOm5hbWU9ImFuZHJvaWQuaW50ZW50LmFjdGlvbi5NQUlOIiAvPgogICAgICAgICAgICAgICAgPGNhdGVnb3J5IGFuZHJvaWQ6bmFtZT0iYW5kcm9pZC5pbnRlbnQuY2F0ZWdvcnkuTGFVTkCERSIgLz4KICAgICAgICAgICAgPC9pbnRlbnQtZmlsdGVyPgogICAgICAgIDwvYWN0aXZpdHk+CiAgICA8L2FwcGxpY2F0aW9uPgo8L21hbmlmZXN0Pg=="

    settings_content = '''rootProject.name = "AiChatRoamWiFi"
include ':app'
'''

    layout_b64 = "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPGxpbmVhcmxheW91dCB4bWxuczphbmRyb2lkPSJodHRwOi8vc2NoZW1hcy5hbmRyb2lkLmNvbS9hcGsvcmVzL2FuZHJvaWQiIGFuZHJvaWQ6bGF5b3V0X3dpZHRoPSJtYXRjaF9wYXJlbnQiIGFuZHJvaWQ6bGF5b3V0X2hlaWdodD0ibWF0Y2hfcGFyZW50IiBhbmRyb2lkOm9yaWVudGF0aW9uPSJ2ZXJ0aWNhbCIgYW5kcm9pZDpwYWRkaW5nPSIxNnRwIiBhbmRyb2lkOmJhY2tncm91bmQ9IiMxMjEyMTIiPgogICAgPHRleHR2aWV3IGFuZHJvaWQ6bGF5b3V0X3dpZHRoPSJtYXRjaF9wYXJlbnQiIGFuZHJvaWQ6bGF5b3V0X2hlaWdodD0id3JhcF9jb250ZW50IiBhbmRyb2lkOnRleHQ9IkFpQ2hhdFJvYW0gV2lGaSBBdWRpdCAmYW1wOyBCeXBhc3MgVG9vbGtpdCIgYW5kcm9pZDp0ZXh0Q29sb3I9IiMwMEZGMDAiIGFuZHJvaWQ6dGV4dFNpemU9IjE4c3AiIGFuZHJvaWQ6dGV4dFN0eWxlPSJib2xkIiBhbmRyb2lkOmdyYXZpdHk9ImNlbnRlciIgYW5kcm9pZDpwYWRkaW5nQm90dG9tPSIxMmRwIiAvPgogICAgPGdyaWRsYXlvdXQgYW5kcm9pZDpsYXlvdXRfd2lkdGg9Im1hdGNoX3BhcmVudCIgYW5kcm9pZDpsYXlvdXRfaGVpZ2h0PSJ3cmFwX2NvbnRlbnQiIGFuZHJvaWQ6Y29sdW1uQ291bnQ9IjIiIGFuZHJvaWQ6YWxpZ25tZW50TW9kZT0iYWxpZ25NYXJnaW5zIj4KICAgICAgICA8YnV0dG9uIGFuZHJvaWQ6aWQ9IkBpZC9idG5TY2FuV2lmaSIgYW5kcm9pZDpsYXlvdXRfd2lkdGg9IjBkcCIgYW5kcm9pZDpsYXlvdXRfaGVpZ2h0PSJ3cmFwX2NvbnRlbnQiIGFuZHJvaWQ6bGF5b3V0X2luZGV4PSIwIiBhbmRyb2lkOmxheW91dF9jb2x1bW5XZWlnaHQ9IjEiIGFuZHJvaWQ6dGV4dD0iU2NhbiBBQ3MiIGFuZHJvaWQ6YmFja2dyb3VuZFRpbnQ9IiMzMzMzMzMiIGFuZHJvaWQ6dGV4dENvbG9yPSIjRkZGRkZGIiAvPgogICAgICAgIDxidXR0b24gYW5kcm9pZDppZD0iQGlkL2J0bkdhdGV3YXkiIGFuZHJvaWQ6bGF5b3V0X3dpZHRoPSIwZHAiIGFuZHJvaWQ6bGF5b3V0X2hlaWdodD0id3JhcF9jb250ZW50IiBhbmRyb2lkOmxheW91dF9jb2x1bW5XZWlnaHQ9IjEiIGFuZHJvaWQ6dGV4dD0iQ2hlY2sgR2F0ZXdheSIgYW5kcm9pZDpiYWNrZ3JvdW5kVGludD0iIzMzMzMzMyIgYW5kcm9pZDp0ZXh0Q29sb3I9IiNGRkZGRkYiIC8+CiAgICAgICAgPGJ1dHRvbiBhbmRyb2lkOmlkPSJAZWlkL2J0blBvcnRhbEJ5cGFzcyIgYW5kcm9pZDpsYXlvdXRfd2lkdGg9IjBkcCIgYW5kcm9pZDpsYXlvdXRfaGVpZ2h0PSJ3cmFwX2NvbnRlbnQiIGFuZHJvaWQ6bGF5b3V0X2NvbHVtbldlaWdodD0iMSIgYW5kcm9pZDp0ZXh0PSJQb3J0YWwgQnlwYXNzIiBhbmRyb2lkOmJhY2tncm91bmRUaW50PSIjMzMzMzMzIiBhbmRyb2lkOnRleHRDb2xvcj0iIkZGRkZGRiIgLz4KICAgICAgICA8YnV0dG9uIGFuZHJvaWQ6aWQ9IkBpZC9idG5aVEVQcm9iZSIgYW5kcm9pZDpsYXlvdXRfd2lkdGg9IjBkcCIgYW5kcm9pZDpsYXlvdXRfaGVpZ2h0PSJ3cmFwX2NvbnRlbnQiIGFuZHJvaWQ6bGF5b3V0X2NvbHVtbldlaWdodD0iMSIgYW5kcm9pZDp0ZXh0PSJaVEUgQXVkaXQiIGFuZHJvaWQ6YmFja2dyb3VuZFRpbnQ9IiMzMzMzMzMiIGFuZHJvaWQ6dGV4dENvbG9yPSIjRkZGRkZGIiAvPgog   PC9ncmlkbGF5b3V0PgogICAgPHRleHR2aWV3IGFuZHJvaWQ6bGF5b3V0X3dpZHRoPSJtYXRjaF9wYXJlbnQiIGFuZHJvaWQ6bGF5b3V0X2hlaWdodD0id3JhcF9jb250ZW50IiBhbmRyb2lkOnRleHQ9IkV4ZWN1dGlvbiBPdXRwdXQgQ29uc29sZToiIGFuZHJvaWQ6dGV4dENvbG9yPSIjQUFBQUFBIgogICAgICAgIGFuZHJvaWQ6dGV4dFNpemU9IjE0c3AiIGFuZHJvaWQ6cGFkZGluZ1RvcD0iMTJkcCIgYW5kcm9pZDpwYWRkaW5nQm90dG9tPSI0ZHAiIC8+CiAgICA8c2Nyb2xsdmlldyBhbmRyb2lkOmxheW91dF93aWR0aD0ibWF0Y2hfcGFyZW50IiBhbmRyb2lkOmxheW91dF9oZWlnaHQ9IjBkcCIgYW5kcm9pZDpsYXlvdXRfd2lkZ2h0PSIxIi backgroundColor=\"#000000\" android:padding=\"8dp\">\n        <TextView android:id=\"@+id/tvOutput\" android:layout_width=\"match_parent\" android:layout_height=\"wrap_content\" android:text=\"[System Ready...]\n\" android:textColor=\"#00FF00\" android:textSize=\"12sp\" android:fontFamily=\"monospace\"/>\n    </ScrollView>\n</LinearLayout>"

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
                    URL url = new URL("http://192.168.1.1/");
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
                Process process = Runtime.getRuntime().exec("ping -c 3 192.168.1.1");
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
                URL url = new URL("http://192.168.1.1/");
                HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                conn.setRequestProperty("User-Agent", "Mozilla/5.0");
                appendLog("[+] ZTE HTTP Status: " + conn.getResponseCode());
                appendLog("[+] Server Header: " + conn.getHeaderField("Server"));
            } catch (Exception e) {
                appendLog("[-] Audit error: " + e.getMessage());
            }
        }).start();
    }
}'''

    root_gradle = '''plugins {
    id 'com.android.application' version '8.2.0' apply false
}
'''

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
}'''

    with open("android_app/app/src/main/AndroidManifest.xml", "wb") as f:
        f.write(base64.b64decode(manifest_b64))

    with open("android_app/settings.gradle", "w") as f:
        f.write(settings_content)

    with open("android_app/app/src/main/res/layout/activity_main.xml", "wb") as f:
        f.write(base64.b64decode(layout_b64))

    with open("android_app/app/src/main/java/com/aichatroam/wifi/MainActivity.java", "w") as f:
        f.write(java_content)

    with open("android_app/build.gradle", "w") as f:
        f.write(root_gradle)

    with open("android_app/app/build.gradle", "w") as f:
        f.write(app_gradle)

    print("[+] Android app project fully updated with explicit namespace and base64 manifest!")

if __name__ == "__main__":
    create_structure()
