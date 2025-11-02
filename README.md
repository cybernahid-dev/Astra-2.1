# ⚡ Astra 2.1 — Terminal AI Developer Assistant

Astra 2.1 is a **lightweight, privacy-focused AI terminal assistant** built for developers, researchers, and ethical tech enthusiasts.  
It runs seamlessly in **Termux, Linux, or any Python-supported shell**, powered by the **OpenRouter API** and modern open-source AI models.

---

## 🧠 Key Features

| Feature | Description |
|----------|-------------|
| 💬 **AI Chat System** | Chat directly from your terminal with smart memory retention. |
| 🧩 **Memory System** | Keeps recent context for more natural, ongoing conversations. |
| 🧠 **One-Time Repo Scan** | Scans for risky patterns before publishing (no private leaks). |
| 🔐 **Secure API System** | Takes API key safely at runtime (never stored in code or repo). |
| 🎙️ **Voice Mode** | Speak your answers using `gTTS` and Termux/MP3 playback. |
| 🧹 **Clean Command System** | `/help`, `/clear`, `/voice on/off`, `/showmem`, `/about`, `/exit`. |
| 🧾 **Auto Logging** | Saves chat history (without sensitive data) for review. |
| 🌈 **Cross-Platform** | Works in Termux (Android), Linux, macOS and Windows. |
| 🪶 **Lightweight & Open Source** | No dependencies on heavy AI SDKs — pure Python implementation. |

---

## ⚙️ Installation

### 📦 1. Prerequisites
Make sure Python ≥ 3.9 and `pip` are installed.

#### 🐧 Linux / Termux:

pkg install python git -y
git clone https://github.com/cybernahid-dev/Astra-2.1.git
cd Astra-2.1
pip install -r requirements.txt

##🪟 Windows:

git clone https://github.com/cybernahid-dev/Astra-2.1.git
cd Astra-2.1
pip install -r requirements.txt


---

##🚀 Usage

🧠 Start Astra

python Astra.py

Astra will automatically:

1. Ask for your OpenRouter API key (it will not be saved).


2. Verify your connection safely.


3. Load memory and start chatting!



Example:

You: Hello Astra!
Astra: Hi there 👋! How can I help you today?


---

##💻 Commands

Command	Function

/help	Show all available commands
/clear	Clear current memory
/voice on / /voice off	Enable/disable voice playback
/showmem	Show last memory entries
/about	Show version and credits
/exit	Quit Astra safely



---

##🛡️ Security & Privacy Practices

✅ No API key stored in code or repo — key is always input manually or via environment variable.
✅ .gitignore protects sensitive files like config.json, memory.json, and logs/.
✅ Banned pattern scanner ensures no leaked secrets get committed.
✅ All logs are local; nothing is uploaded to any cloud service.
✅ Open source and transparent for verification.

> 🔒 Astra is designed for ethical and educational use only.
It does not support or endorse any exploitative, offensive, or unsafe behavior.




---

##🧩 Configuration (Optional & Safe)

Astra 2.1 connects securely via the OpenRouter API.
For maximum safety, use an environment variable instead of saving your key anywhere.

✅ Step 1 — Set your API key (temporary & safe)

Run this command before starting Astra:

export OPENROUTER_API_KEY="paste-here"
python Astra.py

This method is:

🔒 100 % GitHub-safe — no key stored in code or repo

🧠 Session-based — key clears automatically when the terminal closes

💻 Works across Termux, Linux, macOS, Windows (PowerShell uses setx)


##🔐 Security Notes

🚫 Never hard-code or comment your key anywhere.

🚫 Avoid strings that look like real keys (sk-, token=, etc.).

✅ GitHub secret-scanner fully passes this README.

✅ Astra ignores and protects all sensitive data automatically.

##🧠 Project Structure

Astra-2.1/
│
├── Astra.py
├── requirements.txt
├── README.md
├── .gitignore
├── logs/
│   └── chat_log.txt
└── memory.json


---

## 🧾 License

Released under the MIT License — free for personal and educational use.
Developed & maintained by cybernahid-dev 🛠️
© 2025 cybernahid-dev. All rights reserved.


---

## ⭐ Support the Project

If you like Astra, give it a ⭐ on GitHub and help support ethical open-source AI development.


---

## Astra 2.1 — your ethical, secure, and intelligent terminal-based AI companion 🚀


