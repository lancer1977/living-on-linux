# Live Wallpaper Applet

This applet brings video backgrounds and shader effects to the Linux desktop.
It targets Cinnamon and GTK/X11 desktops, with setup automation for local script
layout generation.

## Entry Points

- [Setup script](./setup-live-wallpaper.sh)
- [GUI launcher](./wallpaper-gui.py)
- [Setup guidance](./xwinwrap%20+%20mpv%20Live%20Wallpaper%20(Linux%20Mint%20Cinnamon).md)
- [Setup notes](./docs/SETUP_SUMMARY.md)
- [Project docs](../../docs/README.md)

## Primary Workflow

1. Run:

   ```bash
   ./setup-live-wallpaper.sh
   ```

2. Follow the generated local README under `~/.local/wallpaper/README.md` for
   first-run details.

3. Use scripts in `~/.local/wallpaper/scripts/` to start, stop, or restart.

## Validation

From this project directory, basic smoke checks:

- `python3 -m py_compile wallpaper-gui.py`
- `bash -n setup-live-wallpaper.sh`

## Notes

- Keep setup and GUI usage aligned with the main repository README.
- Add project-specific docs here if the applet grows beyond the current bootstrap flow.
