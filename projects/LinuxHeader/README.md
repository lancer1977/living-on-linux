# LinuxHeader Applet

This project is a Cinnamon applet that renders a configurable Tron-style text
widget on the panel.

## Project files

- `applet/applet.py`: applet bootstrap and interaction logic
- `applet/__init__.py`: Cinnamon metadata references and applet package entry
- `applet/applet.js`: Cinnamon UUID and manifest data
- `applet/settings.py`: settings persistence
- `applet/ui/main_window.py`: display and edit UI
- `applet/data/`: runtime data storage

## Running

From a Cinnamon environment, copy the `applet/` directory into the expected
user Cinnamon applet path and refresh the applet list.

## Validation

From repository root:

- `python3 -m py_compile projects/LinuxHeader/applet/*.py projects/LinuxHeader/applet/ui/*.py`
- `bash -n scripts/test.sh`
