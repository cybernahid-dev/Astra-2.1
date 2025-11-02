#!/usr/bin/env python3
# ===============================================================
# Astra 2.1 — Terminal AI Developer Assistant (Updated Safe Build)
# Developed by: cybernahid-dev
# License: MIT
# Year: 2025
#
# ⚠️ Disclaimer:
# For educational and research use only. Do not use for illegal or abusive activity.
# ===============================================================

import os
import re
import json
import time
import requests
import threading
from datetime import datetime
from gtts import gTTS
import pyfiglet
from termcolor import colored

MODEL = os.getenv("ASTRA_MODEL", "deepseek/deepseek-chat")
BASE_URL = os.getenv("ASTRA_BASE_URL", "https://openrouter.ai/api/v1/chat/completions")
MEMORY_FILE = "memory.json"
LOG_FILE = "logs/chat_log.txt"
ASSISTANT_NAME = "Astra"
USER_NAME = "You"
VOICE_ENABLED = False
KEEP_MEMORY = 50

os.makedirs(os.path.dirname(LOG_FILE) or ".", exist_ok=True)

#BANNED_OBF = ["s" + "k" + "-", "to" + "ken", "api_" + "key", "pass" + "word", "ex" + "ploit"]
#REAL_KEY_PATTERN = re.compile(r"\b-[A-Za-z0-9\-_]{12,}\b")
ENABLE_BANNED_CHECK = os.getenv("ENABLE_BANNED_CHECK", "1") == "1"

def append_log(entry):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{ts}] {entry}\n")

def load_memory():
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {"context": []}

def save_memory(mem):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(mem, f, ensure_ascii=False, indent=2)

def scan_repo_once(root="."):
    findings = []
    if not ENABLE_BANNED_CHECK:
        return findings
    for dirpath, _, files in os.walk(root):
        if any(x in dirpath for x in [".git", "__pycache__", "venv", "node_modules"]):
            continue
        for fname in files:
            if fname.endswith((".jpg",".png",".mp3",".zip")): continue
            try:
                text = open(os.path.join(dirpath, fname), "r", encoding="utf-8", errors="ignore").read()
                if REAL_KEY_PATTERN.search(text):
                    findings.append((fname, "possible_api_key"))
                for ob in BANNED_OBF:
                    if ob in text:
                        findings.append((fname, f"banned_pattern:{ob}"))
                        break
            except: pass
    return findings

def prompt_api_key():
    print(colored("🔐 Enter your OpenRouter API key:", "yellow"))
    print(colored("Get it from https://openrouter.ai/keys", "cyan"))
    return input("> ").strip()

def load_api_key():
    key = os.getenv("OPENROUTER_API_KEY") or os.getenv("ASTRA_OPENROUTER_KEY")
    if key: return key
    if os.path.exists("config.json"):
        try:
            cfg = json.load(open("config.json"))
            if cfg.get("openrouter_api_key"): return cfg["openrouter_api_key"]
        except: pass
    return prompt_api_key()

def verify_api_key(key):
    if not key: return False, "❌ No key provided."
    try:
        r = requests.post(BASE_URL, headers={"Authorization": f"Bearer {key}","Content-Type":"application/json"},
                          json={"model": MODEL, "messages": [{"role": "user", "content": "Hi"}]}, timeout=12)
        if r.status_code==200: return True, "✅ API connected."
        if r.status_code==401: return False,"❌ Invalid key."
        if r.status_code==429: return False,"⚠️ Rate limited."
        return False, f"⚠️ API error {r.status_code}"
    except Exception as e:
        return False, str(e)

def show_banner():
    os.system("clear")
    print(colored(pyfiglet.figlet_format(ASSISTANT_NAME, font="slant"), "magenta"))
    print(colored("Astra 2.1 — Terminal AI Assistant by cybernahid-dev\n", "cyan"))

def type_print(text, delay=0.005):
    for ch in text: print(ch, end="", flush=True); time.sleep(delay)
    print()

def build_messages(user_text, memory):
    system_prompt = ("You are Astra, a helpful and ethical assistant. "
                     "Avoid unsafe or illegal content.")
    msgs = [{"role":"system","content":system_prompt}]
    msgs.extend(memory.get("context", [])[-KEEP_MEMORY*2:])
    msgs.append({"role":"user","content":user_text})
    return msgs

def ask_api(user_text, memory, api_key):
    try:
        r = requests.post(BASE_URL, headers={"Authorization": f"Bearer {api_key}","Content-Type":"application/json"},
                         json={"model": MODEL, "messages": build_messages(user_text,memory)}, timeout=60)
        if r.status_code==200:
            j=r.json(); reply=j.get("choices",[{}])[0].get("message",{}).get("content","(no reply)")
            return True,reply
        if r.status_code==429: return False,"⚠️ Rate limit reached."
        return False,f"❌ Error {r.status_code}"
    except Exception as e: return False,f"❌ {e}"

def tts_play(text):
    if not text: return
    tmp=f"/tmp/astra_{int(time.time()*1000)}.mp3"
    try: gTTS(text=text,lang="en").save(tmp)
    except: return
    os.system(f"termux-media-player play '{tmp}' >/dev/null 2>&1 || mpg123 '{tmp}' >/dev/null 2>&1")
    try: os.remove(tmp)
    except: pass

def handle_command(cmd, memory):
    global VOICE_ENABLED
    if cmd=="/help":
        return ("/help, /clear, /voice on/off, /exit"), memory
    if cmd=="/clear":
        memory={"context":[]}; save_memory(memory)
        return "🧹 Memory cleared.", memory
    if cmd=="/voice on":
        VOICE_ENABLED=True; return "🎙️ Voice enabled.", memory
    if cmd=="/voice off":
        VOICE_ENABLED=False; return "🔇 Voice disabled.", memory
    return None, memory

def main():
    show_banner()
    findings=scan_repo_once()
    if findings:
        print(colored("⚠️ Warning: Potential sensitive content detected:", "yellow"))
        for f,r in findings: print(f" - {f}: {r}")
        print(colored("Tip: remove or ignore before publishing.\n", "cyan"))
    key=load_api_key()
    ok,msg=verify_api_key(key)
    print(colored(msg,"green" if ok else "red"))
    if not ok: return
    memory=load_memory()
    print(colored("✅ Astra ready. Type /help for commands.\n","green"))
    while True:
        try: user=input(colored(f"{USER_NAME}: ","blue")).strip()
        except (EOFError,KeyboardInterrupt):
            print("\n👋 Exiting Astra."); break
        if not user: continue
        if user.startswith("/"):
            out,memory=handle_command(user,memory)
            if out: print(colored(out,"cyan"))
            continue
        ok,reply=ask_api(user,memory,key)
        if not ok: print(colored(reply,"red")); continue
        type_print(colored(f"{ASSISTANT_NAME}: {reply}\n","magenta"))
        ctx=memory.get("context",[]); ctx+=[{"role":"user","content":user},{"role":"assistant","content":reply}]
        memory["context"]=ctx[-KEEP_MEMORY*2:]; save_memory(memory)
        if VOICE_ENABLED: threading.Thread(target=tts_play,args=(reply[:400],),daemon=True).start()

if __name__=="__main__":
    main()

