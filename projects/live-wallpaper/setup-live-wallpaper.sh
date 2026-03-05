#!/bin/bash

# Live Wallpaper Setup Script for Linux Mint Cinnamon
# This script automates the entire setup process for xwinwrap + mpv live wallpaper

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
WALLPAPER_DIR="$HOME/.local/wallpaper"
SCRIPT_DIR="$WALLPAPER_DIR/scripts"
SHADERS_DIR="$WALLPAPER_DIR/shaders"
VIDEOS_DIR="$WALLPAPER_DIR/videos"
AUTOSTART_DIR="$HOME/.config/autostart"

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to install dependencies
install_dependencies() {
    print_status "Installing dependencies..."
    
    # Check if we're on a Debian-based system
    if command_exists apt; then
        print_status "Detected Debian/Ubuntu system"
        
        # Method 1: Build xwinwrap from source (primary method)
        print_status "Building xwinwrap from source..."
        
        # Create temporary directory
        TEMP_DIR=$(mktemp -d)
        cd "$TEMP_DIR"
        
        # Clone and build
        git clone https://github.com/ujjwal96/xwinwrap.git
        cd xwinwrap
        make
        
        # Install
        if sudo cp xwinwrap /usr/local/bin/; then
            print_success "xwinwrap built and installed from source"
        else
            print_error "Failed to install xwinwrap from source"
            return 1
        fi
        
        # Clean up
        cd /
        rm -rf "$TEMP_DIR"
        
        # Method 2: Install other dependencies via package manager
        print_status "Installing other dependencies via package manager..."
        if sudo apt update && sudo apt install -y mpv mesa-utils build-essential libx11-dev libxinerama-dev libxrender-dev; then
            print_success "Other dependencies installed successfully"
        else
            print_error "Failed to install some dependencies via package manager"
            print_warning "Continuing with available dependencies..."
        fi
        
    else
        print_error "Unsupported package manager. Please install dependencies manually:"
        print_error "  - xwinwrap (build from source: https://github.com/ujjwal96/xwinwrap)"
        print_error "  - mpv"
        print_error "  - mesa-utils"
        print_error "  - build-essential"
        print_error "  - libx11-dev"
        print_error "  - libxinerama-dev"
        print_error "  - libxrender-dev"
        return 1
    fi
}

# Function to verify installation
verify_installation() {
    print_status "Verifying installation..."
    
    if ! command_exists xwinwrap; then
        print_error "xwinwrap not found. Please check installation."
        return 1
    fi
    
    if ! command_exists mpv; then
        print_error "mpv not found. Please check installation."
        return 1
    fi
    
    print_success "All dependencies verified"
}

# Function to create directory structure
create_directories() {
    print_status "Creating directory structure..."
    
    mkdir -p "$WALLPAPER_DIR"
    mkdir -p "$SCRIPT_DIR"
    mkdir -p "$SHADERS_DIR"
    mkdir -p "$VIDEOS_DIR"
    mkdir -p "$AUTOSTART_DIR"
    
    print_success "Directory structure created at $WALLPAPER_DIR"
}

# Function to create the main wallpaper script
create_wallpaper_script() {
    print_status "Creating main wallpaper script..."
    
    cat > "$SCRIPT_DIR/start-wallpaper.sh" << 'EOF'
#!/usr/bin/env bash

# Live Wallpaper Script for Linux Mint Cinnamon
# Uses xwinwrap + mpv for desktop background

# Get screen resolution
RES=$(xdpyinfo | awk '/dimensions/{print $2}')

# Video file path
VID="$HOME/.local/wallpaper/videos/loop.mp4"

# Kill any existing xwinwrap instances
pkill -f xwinwrap || true

# Start xwinwrap with mpv
xwinwrap -g "$RES" -ni -b -nf -fdt -ov -- \
  mpv --loop --no-audio --wid=0 \
      --hwdec=auto-safe \
      --panscan=1.0 \
      --vo=gpu \
      "$VID"
EOF

    chmod +x "$SCRIPT_DIR/start-wallpaper.sh"
    print_success "Wallpaper script created at $SCRIPT_DIR/start-wallpaper.sh"
}

# Function to create autostart configuration
create_autostart() {
    print_status "Creating autostart configuration..."
    
    cat > "$AUTOSTART_DIR/live-wallpaper.desktop" << EOF
[Desktop Entry]
Type=Application
Name=Live Wallpaper
Exec=$SCRIPT_DIR/start-wallpaper.sh
X-GNOME-Autostart-enabled=true
Hidden=false
NoDisplay=false
X-GNOME-Autostart-Delay=10
EOF

    print_success "Autostart configuration created at $AUTOSTART_DIR/live-wallpaper.desktop"
}

# Function to create sample shader
create_sample_shader() {
    print_status "Creating sample CRT shader..."
    
    cat > "$SHADERS_DIR/crt-subtle.glsl" << 'EOF'
//!HOOK MAIN
//!BIND HOOKED
//!DESC Subtle CRT Drift

vec4 hook() {
    vec2 uv = HOOKED_pos;
    float scan = sin(uv.y * 800.0) * 0.02;
    vec3 col = HOOKED_tex(uv).rgb;
    col -= scan;
    return vec4(col, 1.0);
}
EOF

    print_success "Sample shader created at $SHADERS_DIR/crt-subtle.glsl"
}

# Function to create enhanced wallpaper script with shader support
create_enhanced_script() {
    print_status "Creating enhanced wallpaper script with shader support..."
    
    cat > "$SCRIPT_DIR/start-wallpaper-shader.sh" << 'EOF'
#!/usr/bin/env bash

# Enhanced Live Wallpaper Script with Shader Support
# Uses xwinwrap + mpv with GLSL shaders

# Get screen resolution
RES=$(xdpyinfo | awk '/dimensions/{print $2}')

# Configuration
VID="$HOME/.local/wallpaper/videos/loop.mp4"
SHADER="$HOME/.local/wallpaper/shaders/crt-subtle.glsl"

# Kill any existing xwinwrap instances
pkill -f xwinwrap || true

# Check if shader exists
if [ -f "$SHADER" ]; then
    print_status "Using shader: $SHADER"
    SHADER_ARG="--glsl-shader=$SHADER"
else
    print_status "No shader found, using plain video"
    SHADER_ARG=""
fi

# Start xwinwrap with mpv and optional shader
xwinwrap -g "$RES" -ni -b -nf -fdt -ov -- \
  mpv --loop --no-audio --wid=0 \
      --hwdec=auto-safe \
      --panscan=1.0 \
      --vo=gpu \
      $SHADER_ARG \
      "$VID"
EOF

    chmod +x "$SCRIPT_DIR/start-wallpaper-shader.sh"
    print_success "Enhanced wallpaper script created at $SCRIPT_DIR/start-wallpaper-shader.sh"
}

# Function to create test video
create_test_video() {
    print_status "Creating test video..."
    
    if command_exists ffmpeg; then
        print_status "Generating 30-second test video..."
        ffmpeg -f lavfi -i testsrc=duration=30:size=1920x1080:rate=30 \
               -c:v libx264 -preset veryfast -crf 18 \
               "$VIDEOS_DIR/loop.mp4" >/dev/null 2>&1
        print_success "Test video created at $VIDEOS_DIR/loop.mp4"
    else
        print_warning "ffmpeg not found. Please create your own video file at $VIDEOS_DIR/loop.mp4"
        print_warning "Or install ffmpeg: sudo apt install ffmpeg"
    fi
}

# Function to create management scripts
create_management_scripts() {
    print_status "Creating management scripts..."
    
    # Stop script
    cat > "$SCRIPT_DIR/stop-wallpaper.sh" << 'EOF'
#!/usr/bin/env bash
pkill -f xwinwrap
echo "Live wallpaper stopped"
EOF

    # Restart script
    cat > "$SCRIPT_DIR/restart-wallpaper.sh" << 'EOF'
#!/usr/bin/env bash
"$HOME/.local/wallpaper/scripts/stop-wallpaper.sh"
sleep 2
"$HOME/.local/wallpaper/scripts/start-wallpaper.sh"
echo "Live wallpaper restarted"
EOF

    # Enable autostart
    cat > "$SCRIPT_DIR/enable-autostart.sh" << 'EOF'
#!/usr/bin/env bash
chmod +x "$HOME/.config/autostart/live-wallpaper.desktop"
echo "Autostart enabled"
EOF

    # Disable autostart
    cat > "$SCRIPT_DIR/disable-autostart.sh" << 'EOF'
#!/usr/bin/env bash
chmod -x "$HOME/.config/autostart/live-wallpaper.desktop"
echo "Autostart disabled"
EOF

    chmod +x "$SCRIPT_DIR"/*.sh
    print_success "Management scripts created"
}

# Function to create README
create_readme() {
    print_status "Creating README..."
    
    cat > "$WALLPAPER_DIR/README.md" << 'EOF'
# Live Wallpaper Setup

This directory contains a complete live wallpaper setup for Linux Mint Cinnamon using xwinwrap + mpv.

## Quick Start

1. Run the setup script: `./setup-live-wallpaper.sh`
2. Start the wallpaper: `~/.local/wallpaper/scripts/start-wallpaper.sh`
3. Enable autostart: `~/.local/wallpaper/scripts/enable-autostart.sh`

## Files Structure

```
~/.local/wallpaper/
├── README.md                    # This file
├── scripts/                     # Executable scripts
│   ├── start-wallpaper.sh       # Main wallpaper script
│   ├── start-wallpaper-shader.sh # With shader support
│   ├── stop-wallpaper.sh        # Stop wallpaper
│   ├── restart-wallpaper.sh     # Restart wallpaper
│   ├── enable-autostart.sh      # Enable autostart
│   └── disable-autostart.sh     # Disable autostart
├── shaders/                     # GLSL shaders
│   └── crt-subtle.glsl          # Sample CRT shader
└── videos/                      # Video files
    └── loop.mp4                 # Test video
```

## Usage

### Basic Usage
```bash
# Start wallpaper
~/.local/wallpaper/scripts/start-wallpaper.sh

# Stop wallpaper
~/.local/wallpaper/scripts/stop-wallpaper.sh

# Restart wallpaper
~/.local/wallpaper/scripts/restart-wallpaper.sh
```

### With Shaders
```bash
# Start with shader
~/.local/wallpaper/scripts/start-wallpaper-shader.sh
```

### Autostart
```bash
# Enable autostart on login
~/.local/wallpaper/scripts/enable-autostart.sh

# Disable autostart
~/.local/wallpaper/scripts/disable-autostart.sh
```

## Customization

### Adding Videos
Place your video files in `~/.local/wallpaper/videos/` and update the path in the scripts.

### Adding Shaders
Place GLSL shader files in `~/.local/wallpaper/shaders/` and update the shader path in the enhanced script.

### Configuration Options
Edit the scripts to customize:
- Video file path
- Shader file path
- mpv options
- xwinwrap options

## Troubleshooting

### Wallpaper not showing
- Check if xwinwrap and mpv are installed
- Verify video file exists
- Check terminal for error messages

### Performance issues
- Use hardware acceleration: `--hwdec=auto-safe`
- Reduce video resolution
- Use simpler shaders

### Desktop icons not visible
- Ensure `-fdt` flag is used in xwinwrap
- Check desktop environment settings

## Notes

- This setup works best on X11
- Keep videos short and optimized for performance
- Use subtle shaders to avoid distraction
- Test different video formats for compatibility
EOF

    print_success "README created at $WALLPAPER_DIR/README.md"
}

# Function to display final instructions
show_final_instructions() {
    print_success "Setup completed successfully!"
    echo ""
    print_status "Next steps:"
    echo "  1. Start the wallpaper: $SCRIPT_DIR/start-wallpaper.sh"
    echo "  2. Enable autostart: $SCRIPT_DIR/enable-autostart.sh"
    echo "  3. Customize videos in: $VIDEOS_DIR"
    echo "  4. Add shaders in: $SHADERS_DIR"
    echo ""
    print_status "Available commands:"
    echo "  • Start: $SCRIPT_DIR/start-wallpaper.sh"
    echo "  • Stop: $SCRIPT_DIR/stop-wallpaper.sh"
    echo "  • Restart: $SCRIPT_DIR/restart-wallpaper.sh"
    echo "  • With shader: $SCRIPT_DIR/start-wallpaper-shader.sh"
    echo ""
    print_status "Documentation: $WALLPAPER_DIR/README.md"
}

# Main execution
main() {
    echo "=================================="
    echo "  Live Wallpaper Setup Script"
    echo "=================================="
    echo ""
    
    # Check if running as root
    if [ "$EUID" -eq 0 ]; then
        print_warning "Please do not run this script as root"
        print_warning "It will request sudo privileges when needed"
        exit 1
    fi
    
    # Install dependencies
    install_dependencies
    
    # Verify installation
    verify_installation
    
    # Create directory structure
    create_directories
    
    # Create scripts
    create_wallpaper_script
    create_enhanced_script
    create_management_scripts
    
    # Create configuration
    create_autostart
    
    # Create assets
    create_sample_shader
    create_test_video
    
    # Create documentation
    create_readme
    
    # Show final instructions
    show_final_instructions
}

# Run main function
main "$@"