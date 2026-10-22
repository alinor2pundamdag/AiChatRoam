import os
import base64

def create_structure():
    os.makedirs("android_app/app/src/main/res/layout", exist_ok=True)
    os.makedirs("android_app/app/src/main/java/com/aichatroam/wifi", exist_ok=True)

    # Base64 encoded AndroidManifest.xml
    manifest_b64 = "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPG1hbmlmZXN0IHhtbG5zOmFuZHJvaWQ9Imh0dHA6Ly9zY2hlbWFzLmFuZHJvaWQuY29tL2Fway9yZXMvYW5kcm9pZCIKICAgIHBhY2thZ2U9ImNvbS5haWNoYXRyb2FtLndpZmk+CgogICAgPHVzZXMtcGVybWlzc2lvbiBhbmRyb2lkOm5hbWU9ImFuZHJvaWQucGVybWlzc2lvbi5BQ0NFU1NfV0lGSV9TVEFURSIgLz4KICAgIDx1c2VzLXBlcm1pc3Npb24gYW5kcm9pZDpuYW1lPSJhbmRyb2lkLnBlcm1pc3Npb24uQ0hBTkdFX1dJRklfU1RBVEUiICz4KICAgIDx1c2VzLXBlcm1pc3Npb24gYW5kcm9pZDpuYW1lPSJhbmRyb2lkLnBlcm1pc3Npb24uQUNDRVNTX0ZJTkVfTE9DQVRJT04iICz4KICAgIDx1c2VzLXBlcm1pc3Npb24gYW5kcm9pZDpuYW1lPSJhbmRyb2lkLnBlcm1pc3Npb24uQUNDRVNTX0NPQVJTRV9MT0NBVElPTiIgLz4KICAgIDx1c2VzLXBlcm1pc3Npb24gYW5kcm9pZDpuYW1lPSJhbmRyb2lkLnBlcm1pc3Npb24uSUVSTkVUIiAvPgogICAgPHVzZXMtcGVybWlzc2lvbiBhbmRyb2lkOm5hbWU9ImFuZHJvaWQucGVybWlzc2lvbi5BQ0NFU1NfTkVUV09SS19TVEFURSIgLz4KCiAgICA8YXBwbGljYXRpb24KICAgICAgICBhbmRyb2lkOmFsbG93QmFja3VwPSJ0cnVlIgogICAgICAgIGFuZHJvaWQ6bGFiZWw9IkFpQ2hhdFJvYW0gV2lGaSBUb29sa2l0IgogICAgICAgIGFuZHJvaWQ6c3VwcG9ydHNSdGw9InRydWUiCiAgICAgICAgYW5kcm9pZDp0aGVtZT0iQHN0eWxlL1RoZW1lLkFwcENvbXBhdC5MaWdodC5EYXJrQWN0aWJhciI+CiAgICAgICAgPGFjdGl2aXR5CiAgICAgICAgICAgIGFuZHJvaWQ6bmFtZT0iLk1haW5BY3Rpdml0eSIKICAgICAgICAgICAgYW5kcm9pZDpleHBvcnRlZD0idHJ1ZSI+CiAgICAgICAgICAgIDxpbnRlbnQtZmlsdGVyPgogICAgICAgICAgICAgICAgPGFjdGl2aW4gYW5kcm9pZDpuYW1lPSJhbmRyb2lkLmludGVudC5hY3Rpb24uTUFJTiIgLz4KICAgICAgICAgICAgICAgIDxjYXRlZ29yeSBhbmRyb2lkOm5hbWU9ImFuZHJvaWQuaW50ZW50LmNhdGVnb3J5LkxhVU5DRVIiIC8+CiAgICAgICAgICAgIDwvaW50ZW50LWZpbHRlcj4KICAgICAgICA8L2FjdGl2aXR5PgogICAgPC9hcHBsaWNhdGlvbj4KPC9tYW5pZmVzdD4="
    
    # Base64 encoded activity_main.xml
    layout_b64 = "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPGxpbmVhcmxheW91dCB4bWxuczphbmRyb2lkPSJodHRwOi8vc2NoZW1hcy5hbmRyb2lkLmNvbS9hcGsvcmVzL2FuZHJvaWQiCiAgICBhbmRyb2lkOmxheW91dF93aWR0aD0ibWF0Y2hfcGFyZW50IgogICAgYW5kcm9pZDpsYXlvdXRfaGVpZ2h0PSJtYXRjaF9wYXJlbnQiCiAgICBhbmRyb2lkOm9yaWVudGF0aW9uPSJ2ZXJ0aWNhbCIKICAgIGFuZHJvaWQ6cGFkZGluZz0iMTZkcCIKICAgIGFuZHJvaWQ6YmFja2dyb3VuZD0iIzEyMTIxMiI+CgogICAgPHRleHR2aWV3CiAgICAgICAgYW5kcm9pZDpsYXlvdXRfd2lkdGg9Im1hdGNoX3BhcmVudCIKICAgICAgICBhbmRyb2lkOmxheW91dF9oZWlnaHQ9IndyYXBfY29udGVudCIKICAgICAgICBhbmRyb2lkOnRleHQ9IkFpQ2hhdFJvYW0gV2lGaSBBdWRpdCAmYW1wOyBCeXBhc3MgVG9vbGtpdCIKICAgICAgICBhbmRyb2lkOnRleHRDb2xvcj0iIzAwRkYwMCIKICAgICAgICBhbmRyb2lkOnRleHRTaXplPSIxOHNwIgogICAgICAgIGFuZHJvaWQ6dGV4dFN0eWxlPSJib2xkIgogICAgICAgIGFuZHJvaWQ6Z3Jhdml0eT0iY2VudGVyIgogICAgICAgIGFuZHJvaWQ6cGFkZGluZ0JvdHRvbT0iMTJkcCIvPgoKICAgIDxncmlkbGF5b3V0CiAgICAgICAgYW5kcm9pZDpsYXlvdXRfd2lkdGg9Im1hdGNoX3BhcmVudCIKICAgICAgICBhbmRyb2lkOmxheW91dF9oZWlnaHQ9IndyYXBfY29udGVudCIKICAgICAgICBhbmRyb2lkOmNvbHVtbkNvdW50PSIyIgogICAgICAgIGFuZHJvaWQ6YWxpZ25tZW50TW9kZT0iYWxpZ25NYXJnaW5zIj4KCiAgICAgICAgPGJ1dHRvbgogICAgICAgICAgICBhbmRyb2lkOmlkPSIrQGlkL2J0blNjYW5XaWZpIgogICAgICAgICAgICBhbmRyb2lkOmxheW91dF93aWR0aD0iMGRwIgogICAgICAgICAgICBhbmRyb2lkOmxheW91dF9oZWlnaHQ9IndyYXBfY29udGVudCIKICAgICAgICAgICAgYW5kcm9pZDpsYXlvdXRfY29sdW1uV2VpZ2h0PSIxIgogICAgICAgICAgICBhbmRyb2lkOnRleHQ9IlNjYW4gQVBzIgogICAgICAgICAgICBhbmRyb2lkOmJhY2tncm91bmRUaW50PSIjMzMzMzMzIgogICAgICAgICAgICBhbmRyb2lkOnRleHRDb2xvcj0iIkZGRkZGRiIvPgoKICAgICAgICA8YnV0dG9uCiAgICAgICAgICAgIGFuZHJvaWQ6aWQ9IkBpZC9idG5HYXRld2F5IgogICAgICAgICAgICBhbmRyb2lkOmxheW91dF93aWR0aD0iMGRwIgogICAgICAgICAgICBhbmRyb2lkOmxheW91dF9oZWlnaHQ9IndyYXBfY29udGVudCIKICAgICAgICAgICAgYW5kcm9pZDpsYXlvdXRfY29sdW1uV2VpZ2h0PSIxIgogICAgICAgICAgICBhbmRyb2lkOnRleHQ9IkNoZWNrIEdhdGV3YXkiCiAgICAgICAgICAgIGFuZHJvaWQ6YmFja2dyb3VuZFRpbnQ9IiMzMzMzMzMiCiAgICAgICAgICAgIGFuZHJvaWQ6dGV4dENvbG9yPSIjRkZGRkZGIi8+CgogICAgICAgIDxidXR0b24KICAgICAgICAgICAgYW5kcm9pZDppZD0iQGlkL2J0blBvcnRhbEJ5cGFzcyIKICAgICAgICAgICAgYW5kcm9pZDpsYXlvdXRfd2lkdGg9IjBkcCIKICAgICAgICAgICAgYW5kcm9pZDpsYXlvdXRfaGVpZ2h0PSJ3cmFwX2NvbnRlbnQiCiAgICAgICAgICAgIGFuZHJvaWQ6bGF5b3V0X2NvbHVtbldlaWdodD0iMSIKICAgICAgICAgICAgYW5kcm9pZDp0ZXh0PSJQb3J0YWwgQnlwYXNzIgogICAgICAgICAgICBhbmRyb2lkOmJhY2tncm91bmRUaW50PSIjMzMzMzMzIgogICAgICAgICAgICBhbmRyb2lkOnRleHRDb2xvcj0iIkZGRkZGRiIvPgoKICAgICAgICA8YnV0dG9uCiAgICAgICAgICAgIGFuZHJvaWQ6aWQ9IkBpZC9idG5aVEVQcm9iZSIKICAgICAgICAgICAgYW5kcm9pZDpsYXlvdXRfd2lkdGg9IjBkcCIKICAgICAgICAgICAgYW5kcm9pZDpsYXlvdXRfaGVpZ2h0PSJ3cmFwX2NvbnRlbnQiCiAgICAgICAgICAgIGFuZHJvaWQ6bGF5b3V0X2NvbHVtbldlaWdodD0iMSIKICAgICAgICAgICAgYW5kcm9pZDp0ZXh0PSJaVEUgQXVkaXQiCiAgICAgICAgICAgIGFuZHJvaWQ6YmFja2dyb3VuZFRpbnQ9IiMzMzMzMzMiCiAgICAgICAgICAgIGFuZHJvaWQ6dGV4dENvbG9yPSIjRkZGRkZGIi8+CgogICAgPC9ncmlkbGF5b3V0PgoKICAgIDx0ZXh0dmlldwogICAgICAgIGFuZHJvaWQ6bGF5b3V0X3dpZHRoPSJtYXRjaF9wYXJlbnQiCiAgICAgICAgYW5kcm9pZDpsYXlvdXRfaGVpZ2h0PSJ3cmFwX2NvbnRlbnQiCiAgICAgICAgYW5kcm9pZDp0ZXh0PSJFeGVjdXRpb24gT3V0cHV0IENvbnNvbGU6IgogICAgICAgIGFuZHJvaWQ6dGV4dENvbG9yPSIjQUFBQUFBIgogICAgICAgIGFuZHJvaWQ6dGV4dFNpemU9IjE0c3AiCiAgICAgICAgYW5kcm9pZDpwYWRkaW5nVG9wPSIxMnRwIgogICAgICAgIGFuZHJvaWQ6cGFkZGluZ0JvdHRvbT0iNGRwIi8+CgogICAgPHNjcm9sbHZpZXcKICAgIC      BhbmRyb2lkOmxheW91dF93aWR0aD0ibWF0Y2hfcGFyZW50IgogICAgICAgIGFuZHJvaWQ6bGF5b3V0X2hlaWdodD0iMGRwIgogICAgICAgIGFuZHJvaWQ6bGF5b3V0X3dlaWdodD0iMSIKICAgICAgICBhbmRyb2lkOmJhY2tncm91bmQ9IiMwMDAwMDAiCiAgICAgICAgYW5kcm9pZDpwYWRkaW5nPSI4ZHAiPgoKICAgICAgICA8dGV4dHZpZXcKICAgICAgICAg   android:id="@+id/tvOutput"CiAgICAgICAgICAgIGFuZHJvaWQ6bGF5b3V0X3dpZHRoPSJtYXRjaF9wYXJlbnQiCiAgICAgICAgICAgIGFuZHJvaWQ6bGF5b3V0X2hlaWdodD0id3JhcF9jb250ZW50IgogICAgICAgICAgICBhbmRyb2lkOnRleHQ9Ils5U3lzdGVtIFJlYWR5LiBUYXAgYW55IG1vZHVsZSBhYm92ZSB0byBleGVjdXRlLi4uXG4iCiAgICAgICAgICAgIGFuZHJvaWQ6dGV4dENvbG9yPSIjMDBGRjAwIgogICAgICAgICAgICBhbmRyb2lkOnRleHRTaXplPSIxMnNwIgogICAgICAgICAgICBhbmRyb2lkOnZvbnRGYW1pbHk9Im1vbm9zcGFjZSIvPgogICAgPC9zY3JvbGx2aWV3PgoKPC9saW5lYXJsYXlvdXQ+"

    with open("android_app/app/src/main/AndroidManifest.xml", "wb") as f:
        f.write(base64.b64decode(manifest_b64))

    with open("android_app/app/src/main/res/layout/activity_main.xml", "wb") as f:
        f.write(base64.b64decode(layout_b64))

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
        }.start();
    }
}'''

    with open("android_app/app/src/main/java/com/aichatroam/wifi/MainActivity.java", "w") as f:
        f.write(java_content)

    gradle_content = '''plugins {
    id 'com.android.application'
}

android {
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

    with open("android_app/build.gradle", "w") as f:
        f.write(gradle_content)

    print("[+] Android app structure generated successfully via generate_app.py!")

if __name__ == "__main__":
    create_structure()
