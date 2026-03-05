# xwinwrap + mpv Live Wallpaper (Linux Mint Cinnamon)

This document describes how to set up a **fully programmable desktop wallpaper**
on **Linux Mint Cinnamon (X11)** using:

- `xwinwrap` – pins a window behind desktop icons
- `mpv` – renders video or shader-based visuals
- Optional **GLSL shaders** for CRT / retro effects

This approach gives maximum control and works well with **Cursor** or **Cline**
for automation and iteration.

---

## Requirements

- Linux Mint Cinnamon (X11 session)
- GPU drivers installed (Mesa or vendor)
- Terminal access

---

## Install Dependencies

### Method 1: Using Package Manager (Recommended)

```bash
sudo apt update
sudo apt install -y xwinwrap mpv mesa-utils build-essential libx11-dev libxinerama-dev libxrender-dev
```

### Method 2: Build xwinwrap from Source (Alternative)

If xwinwrap is not available in your package manager, you can build it from source:

```bash
# Clone the repository
git clone https://github.com/ujjwal96/xwinwrap.git

# Build it
cd xwinwrap
make

# Install system-wide
sudo cp xwinwrap /usr/local/bin/
```

### Verify Installation

```bash
xwinwrap --help
mpv --version
```

---

## Directory Layout

```text
~/.local/wallpaper/
├── videos/
├── shaders/
└── scripts/
```

Create it:

```bash
mkdir -p ~/.local/wallpaper/{videos,shaders,scripts}
```

---

## Basic Video Wallpaper Test

Place a looping video:

```text
~/.local/wallpaper/videos/loop.mp4
```

Run:

```bash
xwinwrap -g 1920x1080 -ni -b -nf -- \
  mpv --loop --no-audio --wid=0 \
      --panscan=1.0 \
      ~/.local/wallpaper/videos/loop.mp4
```

**Note:** For newer versions of mpv (0.37+), use `--wid=0` instead of `--wid WID`. The `WID` placeholder syntax may not work with recent mpv versions.

Dynamic resolution:

```bash
$(xdpyinfo | awk '/dimensions/{print $2}')
```

---

## Stable Launcher Script

Create:

```bash
nano ~/.local/wallpaper/scripts/start-wallpaper.sh
```

```bash
#!/usr/bin/env bash

RES=$(xdpyinfo | awk '/dimensions/{print $2}')
VID="$HOME/.local/wallpaper/videos/loop.mp4"

pkill -f xwinwrap || true

xwinwrap -g "$RES" -ni -b -nf -- \
  mpv --loop --no-audio --wid=0 \
      --hwdec=auto-safe \
      --panscan=1.0 \
      --vo=gpu \
      "$VID"
```

Make executable:

```bash
chmod +x ~/.local/wallpaper/scripts/start-wallpaper.sh
```

Run:

```bash
~/.local/wallpaper/scripts/start-wallpaper.sh
```

---

## Autostart on Login (Cinnamon)

Create:

```bash
nano ~/.config/autostart/live-wallpaper.desktop
```

```ini
[Desktop Entry]
Type=Application
Name=Live Wallpaper
Exec=/home/YOURUSER/.local/wallpaper/scripts/start-wallpaper.sh
X-GNOME-Autostart-enabled=true
```

---

## GLSL Shader Wallpaper

Create shader:

```bash
nano ~/.local/wallpaper/shaders/crt-subtle.glsl
```

```glsl
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
```

Update mpv invocation:

```bash
mpv --loop --no-audio --wid=0 \
    --vo=gpu \
    --glsl-shader="$HOME/.local/wallpaper/shaders/crt-subtle.glsl" \
    "$VID"
```

---

## Cursor / Cline Automation Ideas

- Generate GLSL shaders automatically
- Time-of-day palette shifting
- Mode switching (`focus`, `chill`, `stream`)
- CLI controller (`wallpaper set crt`)
- CPU / audio reactive visuals

This setup behaves like a **desktop visual daemon**.

---

## Notes & Gotchas

- Best on **X11**
- Kill old instances before restarting
- Keep visuals subtle to avoid distraction
- Avoid mpv input capture

---

## Next Ideas

- TG16-style gradients
- CRT phosphor glow
- Stream-mode wallpaper switching
- Idle pixel snow
