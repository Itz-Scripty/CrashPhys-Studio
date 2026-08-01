# 🚗💥 CrashPhys Studio

![Status](https://img.shields.io/badge/status-Development-orange)
![License](https://img.shields.io/badge/license-MIT-green)

## 🛠️ Open-Source Vehicle Physics & Development Toolkit for Garry's Mod

CrashPhys Studio is an open-source project focused on creating advanced vehicle simulation tools and systems for **Garry's Mod**.

The goal of CrashPhys is to move beyond basic vehicle spawning and create a framework focused on:

* 💥 Realistic crash simulation
* 🔧 Vehicle damage systems
* 🚗 Custom vehicle creation
* 📦 Workshop addon support
* 🧩 Developer-friendly expansion
* 🌎 Community-driven development

⚠️ **CrashPhys Studio is currently in Alpha development.**

Features are actively being created, tested, and improved.

---

# 📖 About CrashPhys

CrashPhys started with a simple idea:

> "What if Garry's Mod vehicles could have deeper damage, failure, and crash systems?"

🚗💥 From that idea, CrashPhys became a project focused on creating tools for developers who want more control over vehicles.

The long-term vision:

* Import vehicle addons
* Analyze vehicle models
* Create vehicle profiles
* Build custom damage systems
* Expand crash simulation
* Give creators more control

---

# ✨ Current Features

## 📦 Workshop Integration

CrashPhys Studio currently supports:

✅ Garry's Mod Workshop addon importing
✅ `.gma` extraction
✅ Addon folder scanning
✅ Model detection

---

## 🧱 Model System

CrashPhys can:

✅ Find `.mdl` files
✅ Browse extracted addon models
✅ Organize discovered models
✅ Support different addon structures

Example:

```text
models/example/car.mdl
```

---

# 🚘 Vehicle Builder

Create vehicle profiles using extracted models.

Current support:

✅ Vehicle naming
✅ Vehicle model assignment
✅ JSON profile exporting
✅ Engine data storage

Example profile:

```json
{
    "name": "Example Vehicle",
    "type": "single",
    "body": {
        "model": "models/example/car.mdl"
    },
    "engine_health": 100
}
```

---

# 🚙 Supported Vehicle Types

## 🟢 Single Model Vehicles

Many addons contain the entire vehicle as one model.

Example:

```text
models/example/car.mdl
```

CrashPhys can use the complete model directly.

---

## 🔵 Modular Vehicles

Some vehicles use separate parts:

```text
chassis.mdl
wheel_front_left.mdl
wheel_front_right.mdl
wheel_rear_left.mdl
wheel_rear_right.mdl
```

🚧 Modular vehicle support is actively being expanded.

---

# 🚧 Development Status

## 🏷️ Current Version

```
CrashPhys Studio v0.1 Alpha
```

Current development focus:

🔧 Better vehicle detection
🔧 Improved addon compatibility
🔧 Advanced vehicle systems
🔧 Damage simulation
🔧 Crash physics expansion

---

# 🗺️ Roadmap

## ✅ Completed

* [x] Workshop importing
* [x] GMA extraction
* [x] Model scanning
* [x] Vehicle profile exporting

---

## 🔨 In Development

* [ ] Single-model vehicle improvements
* [ ] Modular vehicle building
* [ ] Suspension damage
* [ ] Tire failures
* [ ] Engine failures
* [ ] Crash analysis tools
* [ ] More addon compatibility

---

# 🌎 Community Project

CrashPhys is built for developers, creators, and modders.

The goal is to create a project where people can:

💡 Share ideas
🛠️ Improve systems
🐛 Find bugs
🚀 Build new features
🤝 Help the community grow

Contributions are welcome!

---

# 📥 Installation

## Requirements

✔️ Python 3.x
✔️ Garry's Mod
✔️ Access to GMod `gmad.exe`

---

## Running CrashPhys Studio

Clone the repository:

```bash
git clone https://github.com/yourusername/CrashPhys-Studio.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch:

```bash
python main.py
```

---

# 🐛 Bug Reports

Found a problem?

Please include:

* 🖥️ CrashPhys version
* 📦 Addon name
* ❌ Error message
* 📝 Steps to reproduce
* 📸 Screenshots if possible

Good reports help us improve faster.

---

# 🤝 Contributing

Want to help?

You can contribute by:

✨ Creating features
🐛 Fixing bugs
📚 Improving documentation
🧪 Testing builds
💡 Suggesting ideas

Pull requests are welcome.

---

# 📜 License

CrashPhys Studio is released under the **MIT License**.

You are free to:

✅ Use the project
✅ Modify the project
✅ Fork the project
✅ Share improvements

See `LICENSE` for full details.

---

# ❤️ Thank You

CrashPhys Studio is an ongoing experiment built one system at a time.

Thank you to everyone who tests, contributes, gives feedback, and helps push the project forward.

🚗💥 The goal is simple:

**Build better vehicle simulation tools for Garry's Mod.**
