#!/usr/bin/env python3

import os
import sys
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('CinnamonDesktop', '3.0')
gi.require_version('Cinnamon', '0.0')

from gi.repository import Gtk, Gdk, CinnamonDesktop, Cinnamon
from ui.main_window import TronTextDisplay, EditWindow
from settings import SettingsManager

class LinuxHeaderApplet(Gtk.EventBox):
    def __init__(self):
        super().__init__()
        
        # Get applet directory
        self.applet_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Initialize settings
        self.settings_manager = SettingsManager(self.applet_dir)
        self.current_settings = self.settings_manager.get_current_settings()
        
        # Create UI
        self.text_display = TronTextDisplay()
        self.add(self.text_display)
        
        # Apply current settings
        self.apply_settings()
        
        # Connect signals
        self.connect("button-press-event", self.on_click)
        self.connect("popup-menu", self.on_right_click)
        
        # Show all widgets
        self.show_all()
        
    def apply_settings(self):
        """Apply current settings to the text display"""
        text = self.current_settings.get("text", "Linux Header")
        color = self.current_settings.get("color", "blue")
        alignment = self.current_settings.get("alignment", "center")
        
        self.text_display.set_text(text)
        self.text_display.set_font_color(color)
        self.text_display.set_alignment(alignment)
        
    def on_click(self, widget, event):
        """Handle click events"""
        if event.button == 1:  # Left click
            self.open_edit_window()
        return True
        
    def on_right_click(self, widget, event):
        """Handle right-click menu"""
        menu = Gtk.Menu()
        
        # Edit option
        edit_item = Gtk.MenuItem(label="Edit Text")
        edit_item.connect("activate", self.on_edit_menu_clicked)
        menu.append(edit_item)
        
        # Separator
        separator = Gtk.SeparatorMenuItem()
        menu.append(separator)
        
        # Reset option
        reset_item = Gtk.MenuItem(label="Reset to Default")
        reset_item.connect("activate", self.on_reset_menu_clicked)
        menu.append(reset_item)
        
        menu.show_all()
        menu.popup_at_pointer(event)
        return True
        
    def on_edit_menu_clicked(self, menu_item):
        """Handle edit menu click"""
        self.open_edit_window()
        
    def on_reset_menu_clicked(self, menu_item):
        """Handle reset menu click"""
        self.current_settings = self.settings_manager.default_settings.copy()
        self.settings_manager.save_settings(self.current_settings)
        self.apply_settings()
        
    def open_edit_window(self):
        """Open the edit window"""
        edit_window = EditWindow(self)
        edit_window.set_current_values(
            self.current_settings.get("text", "Linux Header"),
            self.current_settings.get("color", "blue"),
            self.current_settings.get("alignment", "center")
        )
        edit_window.show_all()
        
    def update_text(self, text, color, alignment):
        """Update text and settings from edit window"""
        self.current_settings = self.settings_manager.update_text(text, color, alignment)
        self.apply_settings()

def main():
    """Main function to run the applet"""
    applet = LinuxHeaderApplet()
    
    # Create a simple window to host the applet for testing
    window = Gtk.Window()
    window.set_title("Linux Header Applet Test")
    window.set_default_size(300, 50)
    window.connect("destroy", Gtk.main_quit)
    
    # Add applet to window
    window.add(applet)
    window.show_all()
    
    Gtk.main()

if __name__ == "__main__":
    main()