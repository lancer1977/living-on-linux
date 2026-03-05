# Living on Linux

A curated collection of microprojects and tools for enhancing the Linux desktop experience. This repository contains practical, well-documented solutions for common Linux desktop tasks and customization.

## 🎯 Project Philosophy

- **Microproject Focus**: Small, focused projects that solve specific problems
- **Documentation First**: Comprehensive guides and usage instructions
- **Production Ready**: Tested, reliable solutions for daily use
- **Minimal Dependencies**: Lightweight tools with minimal system impact
- **User Friendly**: Intuitive interfaces and clear error handling

## 📦 Applets

### 🎬 Live Wallpaper Applet
**Location**: `projects/live-wallpaper/`

A desktop applet that brings your wallpaper to life with video backgrounds and shader effects. Perfect for adding personality to your Linux desktop.

**Features**:
- ✅ **Desktop Integration**: Seamlessly integrates behind desktop icons
- ✅ **Minimal Footprint**: Lightweight design with zero extra dependencies
- ✅ **Shader Effects**: GLSL shader support for visual enhancements
- ✅ **Hardware Acceleration**: GPU-powered video playback
- ✅ **Easy Setup**: One-command installation and configuration
- ✅ **GUI Control**: Simple interface for daily management

**Quick Start**:
```bash
cd projects/live-wallpaper/
./setup-live-wallpaper.sh
./wallpaper-gui.py
```

**Documentation**: [Live Wallpaper Guide](projects/live-wallpaper/README.md)

---

## 📦 Projects

*Individual microprojects and tools for specific Linux tasks.*

---

## 🛠️ Development Guidelines

### Project Structure
```
living-on-linux/
├── README.md              # Main project documentation
├── CONTRIBUTING.md        # Contribution guidelines
├── LICENSE               # Project license
└── projects/             # Individual microprojects
    ├── project-name/
    │   ├── README.md     # Project-specific documentation
    │   ├── setup.sh      # Installation/setup script
    │   ├── main.py       # Main application/script
    │   ├── docs/         # Additional documentation
    │   └── assets/       # Project assets (icons, configs, etc.)
    └── another-project/
```

### Documentation Standards
Each project must include:
- **README.md**: Complete usage guide and troubleshooting
- **Setup script**: Automated installation and configuration
- **Code comments**: Clear explanations of complex logic
- **Error handling**: User-friendly error messages
- **Examples**: Practical usage examples

### Code Quality
- **Minimal dependencies**: Prefer built-in libraries
- **Error handling**: Comprehensive error checking
- **User feedback**: Clear status messages and progress indicators
- **Cross-platform**: Where possible, maintain compatibility
- **Security**: Safe handling of user input and system commands

## 🚀 Getting Started

### Prerequisites
- Linux system (Ubuntu/Debian family preferred)
- Python 3.6+
- Basic command line knowledge

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/username/living-on-linux.git
   cd living-on-linux
   ```

2. Explore available projects:
   ```bash
   ls projects/
   ```

3. Follow individual project documentation for setup and usage.

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Adding a New Project
1. Create project directory: `projects/your-project-name/`
2. Add comprehensive README with usage instructions
3. Include automated setup script
4. Add any necessary documentation
5. Update main README with project entry
6. Test on clean system if possible

## 📋 Project Ideas

- **System monitoring dashboard**
- **Desktop automation tools**
- **File organization utilities**
- **Network troubleshooting tools**
- **Development environment setup**
- **Backup and sync solutions**
- **Custom keyboard shortcuts**
- **Terminal enhancements**
- **Package management helpers**
- **Desktop customization tools**

## 🔧 Technical Stack

- **Primary Language**: Python 3
- **GUI Framework**: Tkinter (minimal footprint)
- **Shell Scripts**: Bash for system integration
- **Documentation**: Markdown with comprehensive guides
- **Version Control**: Git with clear commit messages

## 📚 Documentation

- [Live Wallpaper Setup](projects/live-wallpaper/README.md)
- [Setup Scripts Guide](docs/setup-scripts.md)
- [GUI Development](docs/gui-development.md)
- [Best Practices](docs/best-practices.md)

## 🐛 Bug Reports

Please use the GitHub issue tracker to report bugs. Include:
- System information (OS, version, dependencies)
- Steps to reproduce
- Expected vs. actual behavior
- Any error messages

## 💡 Feature Requests

We're always looking for new project ideas! Submit feature requests via GitHub issues with:
- Clear description of the problem being solved
- Use cases and target audience
- Implementation suggestions if applicable

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Linux community for continuous innovation
- Open source developers for amazing tools and libraries
- Users for feedback and suggestions

---

**Living on Linux** - Making Linux desktop life better, one microproject at a time.