# 🚗 CrashPhys Studio

## Vehicle Physics Development Environment

![CrashPhys Studio](/screenshots/1.PNG)

---

# 🚀 About CrashPhys Studio

CrashPhys Studio is an experimental vehicle physics and simulation editor built around the idea of creating a dedicated workspace for designing, testing, and visualizing realistic vehicle systems.

The goal is to create a tool where developers can:

- 🚗 Build and inspect vehicles
- 🛞 Experiment with suspension systems
- 💥 Test crash behavior
- 🔧 Edit vehicle components
- 🎮 Preview physics systems in real time
- 🧩 Create tools for future vehicle simulation workflows

CrashPhys Studio is currently in **early beta development**.

This first release is not about having every feature finished.

It is about proving the foundation works.

---

# 🏁 Beta 0.1 Release

## The First Milestone

Beta 0.1 represents the first working version of the CrashPhys Studio vision.

The editor can now:

✅ Launch a dedicated 3D workspace  
✅ Render a real-time viewport  
✅ Spawn test vehicles  
✅ Delete selected vehicles  
✅ Display vehicle information  
✅ Browse project assets  
✅ Select assets through the browser  
✅ Display editor panels  
✅ Run a custom UI framework  
✅ Connect editor systems together  

This release proves the core architecture is possible.

---

# 📸 Screenshots

## 🖥️ Editor Workspace

![CrashPhys Studio Editor](/screenshots/1.PNG)

---

## 🚗 Vehicle Testing

![CrashPhys Studio Vehicle System](/screenshots/2.PNG)

---

# 🛠️ Current Systems

## 🌎 3D Viewport

The viewport is the foundation of CrashPhys Studio.

Current features:

- OpenGL rendering
- Camera system
- Grid environment
- Vehicle rendering
- Real-time editor scene

---

## 🚗 Vehicle System

CrashPhys Studio includes the beginning of a vehicle development pipeline.

Current vehicle features:

- Vehicle spawning
- Vehicle objects
- Vehicle inspection
- Basic vehicle data display

Future versions will expand this into:

- Suspension editing
- Damage zones
- Tire systems
- Engine simulation
- Crash testing

---

## 📁 Asset Browser

The project browser allows the editor to track supported assets.

Currently supports:

- Models
- Textures
- Data files

Supported formats:

```
.mdl
.obj
.fbx
.png
.jpg
.jpeg
.json
```

Future versions will expand the asset pipeline.

---

## 🔎 Inspector System

The inspector provides information about selected objects.

Currently displays:

- Object name
- Object type
- ID
- Transform data
- Engine information
- Wheel information
- Suspension information

---

# 🧱 Development Philosophy

CrashPhys Studio is being built around a few main ideas:

## 🔧 Tools First

A good simulation needs good tools.

The editor comes before advanced simulation features.

---

## 🧩 Modular Architecture

Systems are designed separately:

- Renderer
- Vehicles
- Physics
- UI
- Assets
- Editor tools

This allows CrashPhys Studio to grow without becoming one giant system.

---

## 🚀 Build The Foundation

The first goal is not perfection.

The first goal is creating a working platform where advanced systems can be built.

---

# 🗺️ Roadmap

For the full development roadmap:

➡️ See [ROADMAP.md](ROADMAP.md)

---

# 🔮 Future Goals

Planned systems include:

## 🚘 Vehicle Development

- Vehicle importer
- Vehicle editor
- Suspension tuning
- Tire configuration
- Engine tuning
- Vehicle components

---

## 💥 Crash Physics

Future crash systems:

- Damage zones
- Collision analysis
- Vehicle deformation simulation
- Crash playback
- Damage visualization

---

## 🎮 Simulation Tools

Future tools:

- Physics testing environments
- Scenario editor
- Vehicle comparisons
- Replay systems
- Automated testing

---

## 🛠️ Advanced Editor Features

Planned:

- Better camera controls
- Save/load projects
- Asset previews
- Material tools
- Animation tools
- Plugin support

---

# ⚠️ Current Limitations

Beta 0.1 is an early development release.

Known limitations:

- Camera controls are still being improved
- Save/load is not implemented yet
- Vehicle editing is limited
- Asset tools are still basic
- Physics simulation systems are still under development

---

# 💻 Installation

## Requirements

- Python 3.10+
- Modern GPU
- OpenGL 3.3+

---

## Running

Clone the repository:

```bash
git clone https://github.com/Itz-Scripty/CrashPhys-Studio.git
```

Enter the project:

```bash
cd CrashPhys-Studio
```

Install requirements:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

---

# 🤝 Contributing

CrashPhys Studio is currently an experimental solo development project.

As development continues, contributions and feedback may become possible.

---

# 📜 License

License information will be added as the project develops.

---

# 🚗 Final Note

CrashPhys Studio is the beginning of a bigger vision:

A complete vehicle physics development environment where creators can build, test, and explore realistic vehicle systems.

Beta 0.1 is the first step.

🚗💥 More coming soon.
