# Live Wallpaper GUI Application

## Overview

The `wallpaper-gui.py` is a Tkinter-based desktop application that provides a user-friendly interface for managing your xwinwrap + mpv live wallpaper system. It eliminates the need to use command line scripts and provides an intuitive graphical interface.

## Features

### 🎬 Video Management
- **File Browser**: Browse and select video files with native file picker
- **Supported Formats**: MP4, AVI, MKV, WebM, MOV, and more
- **Default Video**: Automatically detects and loads the default test video

### 🎨 Shader Support
- **Optional Shader Selection**: Browse and select GLSL shader files
- **Shader Toggle**: Enable/disable shader effects with checkbox
- **Sample Shader**: Includes CRT effect shader for testing

### 🎛️ Control Interface
- **Start/Stop/Restart**: One-click control buttons
- **Status Display**: Real-time status indicator (Running/Not Running)
- **Visual Feedback**: Color-coded status (Green=Running, Red=Not Running)

### ⚙️ Settings
- **Autostart Toggle**: Enable/disable automatic startup on login
- **Persistent Settings**: Remembers your preferences

### 📋 Information Panel
- **Usage Instructions**: Built-in help and instructions
- **Status Updates**: Real-time feedback on operations

## Usage

### Quick Start
```bash
# Run the GUI application
python3 wallpaper-gui.py

# Or make it executable and run directly
chmod +x wallpaper-gui.py
./wallpaper-gui.py
```

### Basic Workflow
1. **Select Video**: Click "Browse" to choose your video file
2. **Optional Shader**: Check "Use Shader" and browse for GLSL shader
3. **Start Wallpaper**: Click "Start Wallpaper" to begin
4. **Monitor Status**: Watch the status indicator for real-time feedback
5. **Control**: Use Stop/Restart buttons as needed

### Advanced Features

#### Shader Effects
- Enable the "Use Shader" checkbox
- Browse to select a `.glsl` file
- Start the wallpaper to see shader effects applied
- Try the included `crt-subtle.glsl` for a retro CRT effect

#### Autostart Management
- Check "Autostart on Login" to enable automatic startup
- The system will automatically configure desktop environment integration
- Works with Linux Mint Cinnamon's autostart system

#### File Management
- The GUI integrates with the existing file structure:
  - Videos: `~/.local/wallpaper/videos/`
  - Shaders: `~/.local/wallpaper/shaders/`
  - Scripts: `~/.local/wallpaper/scripts/`

## Requirements

### Python Dependencies
- **Tkinter**: Built into Python (no installation needed)
- **subprocess**: Built into Python
- **os, sys, threading, time, pathlib**: Built into Python

### System Dependencies
- **xwinwrap**: Installed by setup script
- **mpv**: Installed by setup script
- **Linux Mint Cinnamon**: Primary target environment

## Installation

### Prerequisites
1. Run the main setup script first:
   ```bash
   ./setup-live-wallpaper.sh
   ```

2. The GUI will automatically detect if setup is complete and prompt you if needed.

### Manual Installation
If you want to install the GUI separately:
```bash
# Make executable
chmod +x wallpaper-gui.py

# Run (will prompt for setup if needed)
./wallpaper-gui.py
```

## File Structure

```
/home/lancer1977/vaults/polyhydra/20_Projects/linux-desktop-themes/
├── wallpaper-gui.py              # Main GUI application
├── setup-live-wallpaper.sh       # Setup script (required)
├── xwinwrap + mpv Live Wallpaper (Linux Mint Cinnamon).md
└── SETUP_SUMMARY.md
```

## GUI Layout

```
┌─────────────────────────────────────────────────────────┐
│              Live Wallpaper Controller                  │
├─────────────────────────────────────────────────────────┤
│ Video File: [_______________________________] [Browse]  │
│                                                         │
│ Shader File (Optional):                                 │
│ [_______________________________] [Use Shader] [Browse] │
│                                                         │
│ ┌─────────────────Controls─────────────────┐            │
│ │ Status: Not Running                      │            │
│ │ [Start Wallpaper] [Stop Wallpaper] [Restart]         │
│ └──────────────────────────────────────────┘            │
│                                                         │
│ [✓] Autostart on Login                                  │
│                                                         │
│ ┌───────────────Information────────────────┐            │
│ │ Live Wallpaper Controller               │            │
│ │                                         │            │
│ │ • Select a video file to use as wallpaper│            │
│ │ • Optionally select a GLSL shader       │            │
│ │ • Use Start/Stop/Restart to control     │            │
│ │ • Enable autostart for automatic startup│            │
│ └──────────────────────────────────────────┘            │
└─────────────────────────────────────────────────────────┘
```

## Troubleshooting

### Common Issues

#### "Wallpaper scripts not found"
- **Solution**: Run `./setup-live-wallpaper.sh` first
- **Cause**: The GUI requires the setup script to create necessary directories and scripts

#### "Please select a video file first"
- **Solution**: Click "Browse" and select a video file
- **Cause**: No video file has been selected

#### "Selected video file does not exist"
- **Solution**: Ensure the video file path is correct and file exists
- **Cause**: File was moved or deleted after selection

#### "Failed to start wallpaper"
- **Solution**: Check terminal for error messages, ensure xwinwrap and mpv are installed
- **Cause**: Dependency issues or permission problems

### Debug Mode
For debugging, run the GUI from terminal to see error messages:
```bash
python3 wallpaper-gui.py
```

## Customization

### Adding Custom Videos
1. Place video files in `~/.local/wallpaper/videos/`
2. Use the GUI's "Browse" button to select them
3. Videos will be remembered for future use

### Adding Custom Shaders
1. Place `.glsl` files in `~/.local/wallpaper/shaders/`
2. Enable "Use Shader" and browse to select
3. Shaders will be applied when starting the wallpaper

### Modifying the GUI
The GUI is written in standard Python/Tkinter and can be modified:
- **File**: `wallpaper-gui.py`
- **Framework**: Tkinter (Python standard library)
- **Structure**: Object-oriented with clear separation of concerns

## Performance Notes

### Memory Usage
- **Minimal footprint**: Tkinter is lightweight
- **No background processes**: Only runs when GUI is open
- **Efficient threading**: Wallpaper runs in background thread

### Compatibility
- **Python 3.6+**: Requires modern Python
- **Linux focused**: Optimized for Linux Mint Cinnamon
- **Cross-platform**: Should work on other Linux distributions

## Integration

### With Existing Scripts
The GUI integrates seamlessly with the existing script-based system:
- Uses the same scripts (`start-wallpaper.sh`, `start-wallpaper-shader.sh`)
- Respects the same file structure
- Maintains compatibility with command-line usage

### Desktop Integration
- **Autostart**: Integrates with desktop environment autostart
- **File associations**: Uses native file pickers
- **System tray**: Could be extended for system tray integration

## Future Enhancements

Potential features that could be added:
- **Preview window**: Live preview of selected video/shader
- **Performance monitoring**: CPU/GPU usage display
- **Multiple profiles**: Save/load different configurations
- **Shader editor**: Built-in GLSL shader editor
- **System tray**: Minimize to system tray
- **Hotkeys**: Keyboard shortcuts for common operations

## Support

### Documentation
- **Main docs**: `xwinwrap + mpv Live Wallpaper (Linux Mint Cinnamon).md`
- **Setup guide**: `SETUP_SUMMARY.md`
- **This guide**: `GUI_GUIDE.md`

### Troubleshooting
- Check terminal output for error messages
- Ensure setup script has been run
- Verify file permissions on scripts
- Check that xwinwrap and mpv are installed

The GUI provides a complete, user-friendly interface for managing your live wallpaper system while maintaining full compatibility with the underlying script-based infrastructure.